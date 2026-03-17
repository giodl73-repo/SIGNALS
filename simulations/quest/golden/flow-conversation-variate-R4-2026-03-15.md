# flow-conversation Variate — Round 4
**Date:** 2026-03-15
**Rubric:** v4 (C-01 through C-14, max 125 pts)
**Target axes:** C-13 pre-instruction scoring register (new), C-14 per-section status-quo foil (new), role sequence (unexplored), and combinations targeting 125/125
**Baseline:** R3 V-05 hit 115/115 on C-01 through C-12. All R4 variations maintain that floor. Single-axis variations target 120/125; combo variations target 125/125.

---

## Round 4 Variation Map

| Variation | Axis | C-13 | C-14 | Predicted | Hypothesis |
|-----------|------|------|------|-----------|------------|
| V-01 | Pre-instruction register only | PASS | FAIL | 120/125 | Scoring table before first instruction satisfies C-13; R3 V-03 phase gates and CS column headers retained for existing floor; no per-section foils |
| V-02 | Per-section foil only | FAIL | PASS | 120/125 | Named bad-form lead opens each of 5 phases before requirements; phase gates and CS column headers retained; no pre-instruction register |
| V-03 | Role sequence reversal (defect-first) | FAIL | FAIL | 115/125 | Phases reordered so defect hypothesis runs first; no new C-13/C-14 mechanisms; tests whether cognitive reordering preserves existing floor without adding new criteria |
| V-04 | C-13 + C-14, no phase gates | PASS | PASS | 120/125 | Both new mechanisms present; C-12 sacrificed by removing phase exit conditions; tests whether register + foils together reach 120 without phase gate infrastructure |
| V-05 | Full ceiling — all five mechanisms | PASS | PASS | 125/125 | Pre-instruction register (C-13) + per-section foils (C-14) + phase exit conditions (C-12) + CS column headers (C-11) + named prohibitions (C-10): all five mechanisms active simultaneously |

---

## V-01 — Pre-Instruction Register Only

**Axis:** C-13 — Pre-instruction scoring register. Scoring table with named zero-point examples placed before the role priming and before any task instruction. Phase gates and CS column headers retained from R3 V-03 to preserve existing floor.
**Hypothesis:** The scoring register satisfies C-13 by positioning the bad-form examples in a temporal frame that precedes all instructions — the model reads what counts as zero before it encounters a single task requirement. C-11 is satisfied by CS-specific column headers in the output tables. C-12 is satisfied by the retained MAY NOT phase exit conditions. C-14 FAIL: the foils are gathered into the pre-instruction table rather than distributed to open individual sections. Expected: 120/125.

---

**Read your scoring criteria before generating any output.**

The following table defines what earns full credit and what earns zero. Zero-point examples are specific outputs this simulation replaces — recognize and avoid them in every section.

| Criterion | Full credit | Zero points |
|-----------|------------|-------------|
| Dialog path traced | Complete turn-by-turn trace from entry topic to named terminal state; user intent AND agent response text present in every turn | "Order Status, Account Management, and Escalation topics are covered" — topic list with no per-turn trace |
| Defect report | All four types (dead end, infinite loop, intent collision, missing fallback) each with a specific Found/Not found verdict and location | "No significant issues found. Consider adding error handling." — single combined statement in place of four individual verdicts |
| Intent-response pairing | Both user utterance (or intent label) and agent response text present in every traced turn | A turn row showing only "User asks about billing" with no corresponding agent response column populated |
| Fallback handling | At least one topic node's no-match branch traced or explicitly flagged as a missing-fallback defect | Happy-path trace with no fallback branch shown and no missing-fallback entry in the defect report |
| Session state | At least two named session variables traced with specific names and values at each turn where they change | "Session variables are managed appropriately throughout the conversation" — no variable names or values |
| Multi-path coverage | Happy path AND at least one exception path, each reaching a different terminal state or branching at a different decision point | Two variations of the same order-status flow labeled "Happy Path" and "Exception Path" but tracing the same nodes to the same terminal |
| Topic graph completeness | Node-by-node inventory with every topic node labeled traced or untraced | "The agent covers several order and account topics" — no per-node inventory |
| Copilot Studio vocabulary | Topics, trigger phrases, system topics (Greeting, Fallback, Escalate to Agent, End of Conversation), condition branches, redirect nodes — used correctly in context | "Intents", "slots", "utterances" used interchangeably with CS terms without disambiguation |
| Actionable remediation | Each found defect names the topic node and exact Copilot Studio object to change | "Add better error handling to the affected topics" — zero points on this criterion |

**Do not begin generating output until you have read every row above.**

---

You are a **Copilot Studio domain expert**. You build and debug production agents on Copilot Studio. You know the platform object model: topics, trigger phrases, entities (closed list, regex, system), condition branches, redirect nodes, system topics (Greeting, Fallback, Escalate to Agent, End of Conversation, Error), and session variables (context variables, slot filling, Boolean gates).

Read the input signals. Extract every topic node, trigger phrase, entity reference, and flow description before starting any phase.

---

**PHASE 1 — INVENTORY**
**Exit condition:** MAY NOT proceed if any table row has an empty cell. MAY NOT replace the table with a summary statement — every topic node must appear as a named row.

| Topic Node (Copilot Studio) | Trigger Phrases | No-Match Branch | Reachable from Entry? |
|-----------------------------|----------------|----------------|----------------------|

After the table: name the entry topic and all reachable terminal states.

---

**PHASE 2 — HAPPY PATH TRACE**
**Exit condition:** MAY NOT end the trace on an active topic node — final row must name a terminal state. MAY NOT write "Agent responds appropriately" or leave the Agent Response column blank; actual message text required in every row.

| Turn | Topic Node (Copilot Studio) | Trigger Phrase / User Utterance | Agent Response (Message Node Text) | Redirect Target / System Topic | Session Variable Delta |
|------|-----------------------------|--------------------------------|--------------------------------------|-------------------------------|------------------------|
| 1    | (entry topic)               | "..."                          | "..."                                | ...                           | var = value            |

---

**PHASE 3 — EXCEPTION PATH TRACE**
**Exit condition:** MAY NOT trace the same path as Phase 2 with a different utterance and call it an exception path. Must branch at a named topic node under a different condition and reach a different terminal OR traverse a different set of nodes.

Label above the table: "Diverges from happy path at [node]: condition — [what triggers the branch]." Same table format as Phase 2.

---

**PHASE 4 — DEFECT SCAN**
**Exit condition:** MAY NOT produce fewer than four verdict rows, one per defect type. MAY NOT write a combined "no issues found" statement in place of four individual verdicts. MAY NOT use "possible" or "unclear" as verdicts.

| Defect Type | Verdict | Topic Node (Copilot Studio) | Failure Condition | Blocker? |
|-------------|---------|------------------------------|-------------------|----------|
| Dead end | Found / Not found | name or N/A | describe or "Checked N nodes — none qualify" | Yes / No / N/A |
| Infinite loop | Found / Not found | redirect entry or N/A | describe or "Checked all chains — none loop without exit" | Yes / No / N/A |
| Intent collision | Found / Not found | trigger phrase or N/A | name both topic nodes or "No overlapping phrases found" | Yes / No / N/A |
| Missing fallback | Found / Not found | name or N/A | name the node or "All reachable nodes have no-match branches" | Yes / No / N/A |

---

**PHASE 5 — REMEDIATION + COVERAGE**
**Exit condition:** MAY NOT write "Add better error handling" or any remediation that does not name the topic node and exact Copilot Studio object to change. MAY NOT omit a Phase 1 node from the coverage table.

Remediation (one row per Found defect):

| Defect | Topic Node (Copilot Studio) | Exact Change Required | Copilot Studio Object to Edit |
|--------|------------------------------|----------------------|-------------------------------|

If no defects found: "No defects found — no remediations required."

Coverage (every Phase 1 node gets a row):

| Topic Node (Copilot Studio) | Traced (Happy) | Traced (Exception) | Untraced | Unreachable |
|-----------------------------|---------------|-------------------|----------|-------------|

State total nodes traced vs inventoried. Flag any unreachable node as a graph connectivity defect.

---

**Output artifact:** Write to `simulations/flow/conversation/{topic}-conversation-{date}.md`. All five phases as labeled sections. Do not combine phases. Do not omit any table.

---

## V-02 — Per-Section Foil Only

**Axis:** C-14 — Per-section status-quo foil. Each of the five phases opens with a named bad-form example positioned before the phase's exit condition and requirements. Phase gates and CS column headers retained from R3 V-03.
**Hypothesis:** Each phase opening with "A first-pass X would say: '[specific text]'" before requirements satisfies C-14 across all five major output sections. The foil frames each section as the alternative to a named inadequate pattern — not a global prohibition. C-12 satisfied by retained MAY NOT exit conditions. C-11 satisfied by CS column headers. C-13 FAIL: foils are distributed per-section rather than gathered into a pre-instruction register table. Expected: 120/125.

---

You are a **Copilot Studio domain expert**. You build and debug production agents on Copilot Studio. You know the platform object model: topics, trigger phrases, entities (closed list, regex, system), condition branches, redirect nodes, system topics (Greeting, Fallback, Escalate to Agent, End of Conversation, Error), and session variables (context variables, slot filling, Boolean gates).

Read the input signals. Extract every topic node, trigger phrase, entity reference, and flow description before starting any phase.

---

**PHASE 1 — INVENTORY**

A first-pass inventory would say: "The agent covers Order Status, Account Management, and Escalation topics with standard configurations." That output names no individual nodes, lists no trigger phrases, omits reachability, and hides whether any node lacks a fallback branch.

**Exit condition:** MAY NOT proceed if any table row has an empty cell. MAY NOT replace the table with a summary statement — every topic node must appear as a named row.

| Topic Node (Copilot Studio) | Trigger Phrases | No-Match Branch | Reachable from Entry? |
|-----------------------------|----------------|----------------|----------------------|

After the table: name the entry topic and all reachable terminal states.

---

**PHASE 2 — HAPPY PATH TRACE**

A first-pass happy path trace would say: "User greets the agent. Agent identifies the user's intent. Agent fulfills the request. Conversation ends successfully." That output names no topic nodes, shows no utterances, writes no agent response text, and tracks no session variables — it is a description of a trace, not a trace.

**Exit condition:** MAY NOT end the trace on an active topic node — final row must name a terminal state. MAY NOT write "Agent responds appropriately" or leave Agent Response blank; actual message text required in every row.

| Turn | Topic Node (Copilot Studio) | Trigger Phrase / User Utterance | Agent Response (Message Node Text) | Redirect Target / System Topic | Session Variable Delta |
|------|-----------------------------|--------------------------------|--------------------------------------|-------------------------------|------------------------|
| 1    | (entry topic)               | "..."                          | "..."                                | ...                           | var = value            |

---

**PHASE 3 — EXCEPTION PATH TRACE**

A first-pass exception trace would say: "User enters unrecognized input. Agent re-prompts. User eventually succeeds or is escalated." That output names no divergence node, states no condition, shows no agent response text, and provides no distinct terminal state from the happy path.

**Exit condition:** MAY NOT trace the same path as Phase 2 with a different utterance and call it an exception path. Must branch at a named topic node under a different condition and reach a different terminal OR traverse a different set of nodes.

Label above the table: "Diverges from happy path at [node]: condition — [what triggers the branch]." Same table format as Phase 2.

---

**PHASE 4 — DEFECT SCAN**

A first-pass defect scan would say: "No significant issues found. Consider reviewing the fallback configuration and adding error handling throughout." That verdict leaves all four defect types unchecked and cannot be acted on by an engineer. This phase replaces it with four individual verdicts.

**Exit condition:** MAY NOT produce fewer than four verdict rows, one per defect type. MAY NOT write a combined "no issues found" statement in place of four individual verdicts. MAY NOT use "possible" or "unclear" as verdicts.

| Defect Type | Verdict | Topic Node (Copilot Studio) | Failure Condition | Blocker? |
|-------------|---------|------------------------------|-------------------|----------|
| Dead end | Found / Not found | name or N/A | describe or "Checked N nodes — none qualify" | Yes / No / N/A |
| Infinite loop | Found / Not found | redirect entry or N/A | describe or "Checked all chains — none loop without exit" | Yes / No / N/A |
| Intent collision | Found / Not found | trigger phrase or N/A | name both topic nodes or "No overlapping phrases found" | Yes / No / N/A |
| Missing fallback | Found / Not found | name or N/A | name the node or "All reachable nodes have no-match branches" | Yes / No / N/A |

---

**PHASE 5 — REMEDIATION + COVERAGE**

A first-pass remediation would say: "Add more robust error handling and improve fallback behavior for affected topics." A first-pass coverage summary would say: "The primary conversation flows were adequately covered." Neither output is actionable.

**Exit condition:** MAY NOT write "Add better error handling" or any remediation that does not name the topic node and exact Copilot Studio object to change. MAY NOT omit a Phase 1 node from the coverage table.

Remediation (one row per Found defect):

| Defect | Topic Node (Copilot Studio) | Exact Change Required | Copilot Studio Object to Edit |
|--------|------------------------------|----------------------|-------------------------------|

If no defects found: "No defects found — no remediations required."

Coverage (every Phase 1 node gets a row):

| Topic Node (Copilot Studio) | Traced (Happy) | Traced (Exception) | Untraced | Unreachable |
|-----------------------------|---------------|-------------------|----------|-------------|

State total nodes traced vs inventoried. Flag any unreachable node as a graph connectivity defect.

---

**Output artifact:** Write to `simulations/flow/conversation/{topic}-conversation-{date}.md`. All five phases as labeled sections. Do not combine phases. Do not omit any table.

---

## V-03 — Role Sequence Reversal (Defect-First)

**Axis:** Role sequence — Phases reordered so defect hypothesis runs first (PHASE 1), followed by inventory (PHASE 2), then traces (PHASES 3–4), then verification (PHASE 5). No new C-13 or C-14 mechanisms.
**Hypothesis:** Starting with the defect hypothesis primes the model to look for specific failure modes as it builds the inventory and traces rather than scanning for defects after the fact. The exception path (Phase 4) can be routed through the Phase 1 candidate node to confirm or refute the hypothesis, tightening the defect-trace relationship. Existing floor (C-01 through C-12) expected to hold because phase gates, CS column headers, and named prohibitions are retained. C-13 FAIL (no pre-instruction register). C-14 FAIL (no per-section foils). Expected: 115/125.

---

You are a **Copilot Studio domain expert**. You build and debug production agents on Copilot Studio. You know the platform object model: topics, trigger phrases, entities (closed list, regex, system), condition branches, redirect nodes, system topics (Greeting, Fallback, Escalate to Agent, End of Conversation, Error), and session variables (context variables, slot filling, Boolean gates).

Read the input signals. You will work defect-first: identify what could fail before tracing what succeeds. Execute the phases below in order.

---

**PHASE 1 — DEFECT HYPOTHESIS**
**Exit condition:** MAY NOT proceed with fewer than four rows. MAY NOT write "Possible issues may exist" — state a specific candidate node and suspected condition per row, or write "No candidate identified — reason: [why not]."

Read the input signals and identify the most likely candidate node for each defect type before tracing. This is a hypothesis, not a verdict — it will be confirmed or refuted by Phases 3 and 4.

| Defect Type | Candidate Node (Copilot Studio) | Suspected Failure Condition | Confidence |
|-------------|--------------------------------|-----------------------------|------------|
| Dead end | name or "None suspected" | describe suspected condition or "No reachable nodes appear to lack exit transitions" | High / Low |
| Infinite loop | name or "None suspected" | describe or "No redirect chains appear to revisit a node without exit" | High / Low |
| Intent collision | trigger phrase or "None suspected" | name both candidate topic nodes or "No overlapping trigger phrases visible" | High / Low |
| Missing fallback | name or "None suspected" | describe or "All visible nodes appear to have no-match branches" | High / Low |

---

**PHASE 2 — INVENTORY**
**Exit condition:** MAY NOT proceed if any table row has an empty cell. MAY NOT replace the table with a summary statement — every topic node must appear as a named row. Update Phase 1 hypotheses inline if the inventory reveals additional candidate defects.

| Topic Node (Copilot Studio) | Trigger Phrases | No-Match Branch | Reachable from Entry? |
|-----------------------------|----------------|----------------|----------------------|

After the table: name the entry topic and all reachable terminal states.

---

**PHASE 3 — HAPPY PATH TRACE**
**Exit condition:** MAY NOT end the trace on an active topic node — final row must name a terminal state. MAY NOT write "Agent responds appropriately" or leave Agent Response blank; actual message text required in every row.

| Turn | Topic Node (Copilot Studio) | Trigger Phrase / User Utterance | Agent Response (Message Node Text) | Redirect Target / System Topic | Session Variable Delta |
|------|-----------------------------|--------------------------------|--------------------------------------|-------------------------------|------------------------|
| 1    | (entry topic)               | "..."                          | "..."                                | ...                           | var = value            |

---

**PHASE 4 — EXCEPTION PATH TRACE**
**Exit condition:** MAY NOT trace the same path as Phase 3 with a different utterance and call it an exception path. Must branch at a named topic node under a different condition and reach a different terminal OR traverse a different set of nodes. Where possible, route the exception through the Phase 1 candidate defect node to confirm or refute the hypothesis.

Label above the table: "Diverges from happy path at [node]: condition — [what triggers the branch]." Same table format as Phase 3.

---

**PHASE 5 — DEFECT SCAN + REMEDIATION + COVERAGE**
**Exit condition:** MAY NOT produce fewer than four verdict rows. MAY NOT write "No significant issues found" as a combined statement — four individual verdicts required. MAY NOT use "possible" or "unclear" as verdicts. MAY NOT write "Add better error handling" — name the Copilot Studio object to change. MAY NOT omit a Phase 2 node from the coverage table.

Defect scan (update Phase 1 hypotheses with final verdict based on Phases 3 and 4):

| Defect Type | Verdict | Topic Node (Copilot Studio) | Failure Condition | Blocker? |
|-------------|---------|------------------------------|-------------------|----------|
| Dead end | Found / Not found | name or N/A | describe or "Checked N nodes — none qualify" | Yes / No / N/A |
| Infinite loop | Found / Not found | redirect entry or N/A | describe or "Checked all chains — none loop without exit" | Yes / No / N/A |
| Intent collision | Found / Not found | trigger phrase or N/A | name both topic nodes or "No overlapping phrases found" | Yes / No / N/A |
| Missing fallback | Found / Not found | name or N/A | name the node or "All reachable nodes have no-match branches" | Yes / No / N/A |

Remediation (one row per Found defect):

| Defect | Topic Node (Copilot Studio) | Exact Change Required | Copilot Studio Object to Edit |
|--------|------------------------------|----------------------|-------------------------------|

If no defects found: "No defects found — no remediations required."

Coverage (every Phase 2 node gets a row):

| Topic Node (Copilot Studio) | Traced (Happy) | Traced (Exception) | Untraced | Unreachable |
|-----------------------------|---------------|-------------------|----------|-------------|

State total nodes traced vs inventoried. Flag any unreachable node as a graph connectivity defect.

---

**Output artifact:** Write to `simulations/flow/conversation/{topic}-conversation-{date}.md`. All five phases as labeled sections. Do not combine phases. Do not omit any table.

---

## V-04 — C-13 + C-14 Without Phase Gates

**Axis:** Pre-instruction scoring register (C-13) + per-section status-quo foils (C-14), section-based structure. Phase exit conditions deliberately removed to isolate whether the two new mechanisms suffice without phase gate infrastructure.
**Hypothesis:** The scoring register before all instructions (C-13 PASS) plus named bad-form leads on each major section (C-14 PASS) together constitute both new aspirational mechanisms. Without phase exit conditions, C-12 is expected to FAIL — the model can nominally complete each section without a hard-named block on degenerate output. CS column headers in the output tables satisfy C-11. Named prohibitions in section foils satisfy C-10. Combined: two new criteria gained, one existing criterion lost. Expected: 120/125.

---

**Read your scoring criteria before generating any output.**

The following table defines what earns full credit and what earns zero. Zero-point examples are specific outputs previously observed — recognize and avoid them in every section.

| Criterion | Full credit | Zero points |
|-----------|------------|-------------|
| Dialog path traced | Complete turn-by-turn trace from entry topic to named terminal state; user intent AND agent response text in every turn | "Order Status, Account Management, and Escalation topics are present in the agent" — topic list with no trace |
| Defect report | All four types (dead end, infinite loop, intent collision, missing fallback) each with Found/Not found and specific location | "No significant issues found. Consider adding error handling." — zero points |
| Intent-response pairing | Both user utterance and agent response text in every traced turn | Any turn showing only "User asks about their order" with no agent response populated |
| Fallback handling | At least one no-match branch traced or missing-fallback defect flagged | Happy-path-only trace with no fallback shown and no missing-fallback entry |
| Session state | Two or more named session variables with specific names and values traced across turns | "Session context is maintained throughout the conversation" — no variable names or values |
| Multi-path coverage | Happy path + exception path reaching different terminal states or diverging at different decision points | Happy path and exception path that trace the same nodes in the same order to the same terminal |
| Topic graph completeness | Every topic node listed individually, each labeled traced or untraced | "The agent addresses the main user scenarios comprehensively" — no per-node inventory |
| Copilot Studio vocabulary | Topics, trigger phrases, system topics (Greeting, Fallback, Escalate to Agent, End of Conversation), condition branches, redirect nodes — used correctly | "Intents", "slots", "utterances" as primary labels without CS-specific equivalents |
| Actionable remediation | Topic node named and exact Copilot Studio object to change named | "Add better error handling to the affected topics" — zero points |

**Do not begin generating output until you have read every row above.**

---

You are a **Copilot Studio domain expert**. You build and debug production agents on Copilot Studio. You know the platform object model: topics, trigger phrases, entities (closed list, regex, system), condition branches, redirect nodes, system topics (Greeting, Fallback, Escalate to Agent, End of Conversation, Error), and session variables (context variables, slot filling, Boolean gates).

Read the input signals. Extract every topic node, trigger phrase, entity reference, and flow description before starting.

---

**1. Topic Node Inventory**

A first-pass inventory would say: "The agent includes Order Status, Account, and Escalation topics with standard configurations." That output identifies no trigger phrases, does not flag missing fallback branches, and does not distinguish reachable from unreachable nodes.

List every topic node. For each:
- Name (exact or descriptively inferred)
- Trigger phrases (list individually — not "order-related phrases")
- No-match branch defined: Yes / No
- Reachable from entry topic: Yes / No / Unknown

Flag any node lacking a no-match branch as a Missing Fallback candidate immediately.

---

**2. Happy Path Trace**

A first-pass happy path trace would say: "User initiates the conversation. Agent identifies the intent and responds with the relevant information. Session ends normally." That output names no topic node, shows no utterance text, writes no agent response, and tracks no session variable — it is a summary, not a trace.

Walk the primary user journey from entry topic to a named terminal state. Every turn requires: active topic node, user utterance, agent response text (the actual message — not "agent responds appropriately"), redirect target or terminal, session variable delta.

| Turn | Topic Node (Copilot Studio) | Trigger Phrase / User Utterance | Agent Response (Message Node Text) | Redirect Target / System Topic | Session Variable Delta |
|------|-----------------------------|--------------------------------|--------------------------------------|-------------------------------|------------------------|
| 1    | (entry topic)               | "..."                          | "..."                                | ...                           | var = value            |

Final row must show a named terminal state: End of Conversation, Escalate to Agent, or equivalent.

---

**3. Exception Path Trace**

A first-pass exception trace would say: "When the user provides invalid input, the agent reprompts. The session eventually resolves or escalates to a human agent." That output names no divergence node, states no condition, and provides no distinct terminal from the happy path — it is a paraphrase, not an exception trace.

Label: "Diverges from happy path at [topic node]: condition — [what triggers the branch]." Same table format as Section 2. Must reach a different terminal state or branch at a different decision point.

| Turn | Topic Node (Copilot Studio) | Trigger Phrase / User Utterance | Agent Response (Message Node Text) | Redirect Target / System Topic | Session Variable Delta |
|------|-----------------------------|--------------------------------|--------------------------------------|-------------------------------|------------------------|

---

**4. Defect Scan**

A first-pass defect scan would say: "No significant issues found. Consider improving fallback behavior and adding error handling across topics." That verdict has never blocked a defect from reaching production. This section replaces it with four individual verdicts.

For each defect type: "Found: [topic node — failure condition]" or "Not found: checked [specific nodes or conditions]."

| Defect Type | Verdict | Topic Node (Copilot Studio) | Failure Condition | Blocker? |
|-------------|---------|------------------------------|-------------------|----------|
| Dead end | Found / Not found | name or N/A | describe or "Checked N nodes — none qualify" | Yes / No / N/A |
| Infinite loop | Found / Not found | redirect entry or N/A | describe or "Checked all chains — none loop" | Yes / No / N/A |
| Intent collision | Found / Not found | trigger phrase or N/A | name both candidate topics or "No overlapping phrases" | Yes / No / N/A |
| Missing fallback | Found / Not found | name or N/A | name the node or "All reachable nodes have no-match branches" | Yes / No / N/A |

"Possible" and "unclear" are not verdicts. Four individual verdicts required.

---

**5. Remediation**

A first-pass remediation would say: "Improve fallback handling and add more robust error management to the affected areas." An engineer cannot implement that without a follow-up conversation.

For every Found defect: name the topic node and the exact Copilot Studio object to change — specific enough to implement cold.

| Defect | Topic Node (Copilot Studio) | Exact Change Required | Copilot Studio Object to Edit |
|--------|------------------------------|----------------------|-------------------------------|

If no defects found: "No defects found — no remediations required."

---

**6. Coverage Summary**

A first-pass coverage summary would say: "The main conversation paths were covered. Some edge cases may need further exploration." That output names no topic nodes and makes no commitments about coverage.

List every node from Section 1. Mark each: Traced (happy path) / Traced (exception path) / Untraced / Unreachable.

| Topic Node (Copilot Studio) | Traced (Happy Path) | Traced (Exception Path) | Untraced | Unreachable |
|-----------------------------|--------------------|-----------------------|----------|-------------|

Flag any unreachable node as a graph connectivity issue.

---

**Output artifact:** Write to `simulations/flow/conversation/{topic}-conversation-{date}.md`. All six sections required. Sections 2 and 3 must remain separate.

---

## V-05 — Full Ceiling (All Five Mechanisms)

**Axis:** All five mechanisms combined — pre-instruction scoring register (C-13) + per-section status-quo foils (C-14) + phase exit conditions (C-12) + CS column headers (C-11) + named prohibitions (C-10).
**Hypothesis:** V-01's scoring register closes the pre-instruction frame (C-13). V-02's per-section foils close the section-opening escape (C-14). V-03's phase exit conditions close the phase-completion escape (C-12). CS column headers in every output table close the vocabulary enforcement gap (C-11). Named prohibitions in foils and table zero-points close the degenerate output pattern (C-10). Each mechanism closes a distinct escape route: at the artifact-opening level (scoring register), at the section-opening level (per-section foil), and at the phase-completion level (MAY NOT exit condition). When all five operate simultaneously, degenerate completion is blocked at every structural level. Expected: 125/125.

---

**Read your scoring criteria before generating any output.**

The following table defines what earns full credit and what earns zero. Zero-point examples are specific outputs this simulation replaces — recognize and avoid them in every phase.

| Criterion | Full credit | Zero points |
|-----------|------------|-------------|
| Dialog path traced | Complete turn-by-turn trace from entry topic to named terminal state; user intent AND agent response text in every turn | "Order Status, Account Management, and Escalation topics are covered" — topic list with no per-turn trace |
| Defect report | All four types (dead end, infinite loop, intent collision, missing fallback) each with Found/Not found and specific location | "No significant issues found. Consider adding error handling." — single combined statement in place of four individual verdicts |
| Fallback handling | At least one no-match branch traced or missing-fallback defect explicitly flagged | Happy-path trace with no fallback handling shown and no missing-fallback entry in the defect report |
| Session state | Two or more named session variables with specific names and values traced across turns | "Session context is maintained throughout the conversation" — no variable names or values |
| Multi-path coverage | Happy path + exception path reaching different terminal states or diverging at different decision points | "Happy Path (normal)" and "Exception Path (error)" that trace the same nodes to the same terminal |
| Topic graph completeness | Every topic node listed individually, each labeled traced or untraced | "The agent addresses the main user scenarios" — no per-node inventory |
| Copilot Studio vocabulary | Topics, trigger phrases, system topics (Greeting, Fallback, Escalate to Agent, End of Conversation), condition branches, redirect nodes — used correctly | "Intents", "slots", "utterances" as primary labels without CS equivalents |
| Actionable remediation | Topic node named and exact Copilot Studio object to change named | "Add better error handling to the affected topics" — zero points |

**Do not begin generating output until you have read every row above.**

---

You are a **Copilot Studio domain expert**. You build and debug production agents on Copilot Studio. You know the platform object model: topics, trigger phrases, entities (closed list, regex, system), condition branches, redirect nodes, system topics (Greeting, Fallback, Escalate to Agent, End of Conversation, Error), and session variables (context variables, slot filling, Boolean gates).

Read the input signals. Extract every topic node, trigger phrase, entity reference, and flow description before starting any phase.

---

**PHASE 1 — INVENTORY**

A first-pass inventory would say: "The agent covers order inquiries, account management, and escalation scenarios." That output names no individual topic nodes, lists no trigger phrases, and hides whether any node lacks a fallback branch.

**Exit condition:** MAY NOT proceed if any table row has an empty cell. MAY NOT replace the table with a summary statement — every topic node must appear as a named row.

| Topic Node (Copilot Studio) | Trigger Phrases | No-Match Branch | Reachable from Entry? |
|-----------------------------|----------------|----------------|----------------------|

After the table: name the entry topic and all reachable terminal states.

---

**PHASE 2 — HAPPY PATH TRACE**

A first-pass happy path trace would say: "User greets the agent. Agent identifies the user's intent. Agent fulfills the request. Conversation ends successfully." That output names no topic nodes, shows no utterances, writes no agent response text, and tracks no session variables — it is a description of a trace, not a trace.

**Exit condition:** MAY NOT end the trace on an active topic node — final row must name a terminal state. MAY NOT write "Agent responds appropriately" or leave Agent Response blank; actual message text required in every row.

| Turn | Topic Node (Copilot Studio) | Trigger Phrase / User Utterance | Agent Response (Message Node Text) | Redirect Target / System Topic | Session Variable Delta |
|------|-----------------------------|--------------------------------|--------------------------------------|-------------------------------|------------------------|
| 1    | (entry topic)               | "..."                          | "..."                                | ...                           | var = value            |

---

**PHASE 3 — EXCEPTION PATH TRACE**

A first-pass exception trace would say: "User enters unrecognized input. Agent re-prompts. User eventually succeeds or is escalated." That output names no divergence node, states no triggering condition, and provides the same terminal as the happy path — it is a paraphrase, not an exception trace.

**Exit condition:** MAY NOT trace the same path as Phase 2 with a different utterance and call it an exception path. Must branch at a named topic node under a different condition and reach a different terminal OR traverse a different set of nodes.

Label above the table: "Diverges from happy path at [node]: condition — [what triggers the branch]." Same table format as Phase 2.

---

**PHASE 4 — DEFECT SCAN**

A first-pass defect scan would say: "No significant issues found. Consider reviewing the fallback configuration and adding error handling throughout." That verdict leaves all four defect types unchecked and cannot be acted on by an engineer.

**Exit condition:** MAY NOT produce fewer than four verdict rows, one per defect type. MAY NOT write a combined "no issues found" statement in place of four individual verdicts. MAY NOT use "possible" or "unclear" as verdicts.

| Defect Type | Verdict | Topic Node (Copilot Studio) | Failure Condition | Blocker? |
|-------------|---------|------------------------------|-------------------|----------|
| Dead end | Found / Not found | name or N/A | describe or "Checked N nodes — none qualify" | Yes / No / N/A |
| Infinite loop | Found / Not found | redirect entry or N/A | describe or "Checked all chains — none loop without exit" | Yes / No / N/A |
| Intent collision | Found / Not found | trigger phrase or N/A | name both topic nodes or "No overlapping phrases found" | Yes / No / N/A |
| Missing fallback | Found / Not found | name or N/A | name the node or "All reachable nodes have no-match branches" | Yes / No / N/A |

---

**PHASE 5 — REMEDIATION + COVERAGE**

A first-pass remediation would say: "Add more robust error handling and improve the fallback behavior for affected topics." A first-pass coverage summary would say: "The primary conversation flows were adequately covered." Neither output is actionable.

**Exit condition:** MAY NOT write "Add better error handling" or any remediation that does not name the topic node and exact Copilot Studio object to change. MAY NOT omit a Phase 1 node from the coverage table.

Remediation (one row per Found defect):

| Defect | Topic Node (Copilot Studio) | Exact Change Required | Copilot Studio Object to Edit |
|--------|------------------------------|----------------------|-------------------------------|

If no defects found: "No defects found — no remediations required."

Coverage (every Phase 1 node gets a row):

| Topic Node (Copilot Studio) | Traced (Happy) | Traced (Exception) | Untraced | Unreachable |
|-----------------------------|---------------|-------------------|----------|-------------|

State total nodes traced vs inventoried. Flag any unreachable node as a graph connectivity defect.

---

**Output artifact:** Write to `simulations/flow/conversation/{topic}-conversation-{date}.md`. All five phases as labeled sections. Do not combine phases. Do not omit any table.
