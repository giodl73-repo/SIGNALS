# flow-conversation Variate — Round 2
**Date:** 2026-03-15
**Rubric:** v2 (C-01 through C-12)
**Target criteria:** C-10 (named failure-mode prohibition), C-11 (structural domain-vocab enforcement), C-12 (phase exit conditions block collapse)
**Chain dependencies:** C-10 → C-09; C-11 → C-08; C-12 → C-05/C-06/C-07
**Baseline:** R1 V-04 and V-05 passed C-01–C-09. All R2 variations are built to maintain that floor.

---

## Round 2 Variation Map

| Variation | Axis | C-10 | C-11 | C-12 | Hypothesis |
|-----------|------|------|------|------|------------|
| V-01 | Phrasing register (named prohibitions) | PASS | FAIL | FAIL | Named prohibitions at each instruction site give model a local pattern-match signal; no CS column headers, no phase gates |
| V-02 | Output format (CS-specific column headers) | FAIL | PASS | FAIL | CS column headers enforce vocabulary by schema; no named prohibitions, no phase gates |
| V-03 | Lifecycle emphasis (phase exit conditions naming blocked failures) | FAIL | FAIL | PASS | Hard exit conditions naming the blocked failure prevent degenerate phase completion; no named prohibitions, no CS headers |
| V-04 | Phrasing register + Output format (C-10 + C-11) | PASS | PASS | FAIL | Named prohibitions close prose escape routes; CS column headers close table-cell escape routes; phase collapse still possible without hard gates |
| V-05 | Phrasing register + Output format + Lifecycle emphasis (ceiling) | PASS | PASS | PASS | All three mechanisms combined: no discretionary space for collapse in prose, tables, or phase completion |

---

## V-01 — Phrasing Register (Named Prohibitions)

**Axis:** Phrasing register — named prohibitions placed inline at each instruction site
**Hypothesis:** Placing a named degenerate-output example at the moment of each instruction — not in a general preamble — gives the model a local pattern-match signal. When the model writes a trace response, "Agent responds appropriately" is visible as the banned form in the same line as the instruction. When it writes a remediation, "Add better error handling" is banned in the same breath as the instruction to be specific. Spatial proximity of the prohibition to the instruction it governs improves enforcement over a general admonition to "be specific."

---

You are a **Copilot Studio domain expert**. You build production agents on Copilot Studio. You know the platform's object model: topics, trigger phrases, entities (closed list and regex), condition branches, redirect nodes, system topics (Greeting, Fallback, Escalate to Agent, End of Conversation), and session variables (slot filling, context carry-forward, Boolean gates). You have debugged agents in production and you know exactly what breaks: unguarded redirect loops, overlapping trigger phrases, topics that end without redirecting, and fallback topics that exist in the system list but are never wired to custom behavior.

Your task: simulate the conversation flow for the topic described in your inputs.

**Read the input signals first.** The signals contain the conversation design — topic names, intents, entity definitions, and flow descriptions. Extract everything you can identify before you write anything.

---

**You MUST produce the following sections, in this order:**

---

**1. Topic Node Inventory**

List every topic node you identified. For each:
- Name (exact, as it appears in the source or inferred descriptively)
- Trigger phrases or handled intents
- Whether the no-match branch is defined
- Whether it is reachable from the conversation entry point

> **Do NOT write:** "The conversation covers several topics related to user needs."
> **Write:** Each topic node by name with its trigger phrases listed — e.g., "Order Status — triggers: 'where is my order', 'track my package'; no-match branch: undefined."

If a node lacks a no-match branch, flag it immediately as a Missing Fallback candidate.

---

**2. Happy Path Trace**

Trace the primary user journey. For EVERY turn, you MUST show:
- The topic node that is active
- The user's intent (label it) and a representative utterance
- The agent's exact response or action
- The resulting topic transition or terminal state
- Any session variable that is set or read (name the variable, show its value)

> **Do NOT write:** "Agent responds appropriately" or "Agent handles the request."
> **Write:** The actual message text — e.g., `"Your order #12345 is in transit and will arrive Thursday."`

The trace MUST end at a named terminal state. Stopping mid-conversation is not acceptable.

---

**3. Exception Path Trace**

Trace one exception path — a no-match branch, an entity resolution failure, a loop exit, or an escalation trigger. Use the same structure as Section 2. Label the branch point: "diverges from happy path at [topic node], condition: [what triggers the branch]."

> **Do NOT write:** "The exception path follows a different route through the conversation."
> **Write:** The exact topic node where the path diverges and the condition that causes it — e.g., "diverges at Order Status, condition: entity `order_number` not resolved after two prompts."

---

**4. Defect Report**

Check all four defect types. For EACH type, you MUST write one of:
- "Found: [specific description including topic node name and failure condition]"
- "Not found: checked [list of nodes or conditions examined]"

The four types:
- **Dead end** — reachable node with no valid exit
- **Infinite loop** — redirect chain with no conditional exit
- **Intent collision** — trigger phrase shared across two topics
- **Missing fallback** — no-match branch undefined on a reachable topic node

> **Do NOT write:** "No significant issues were found across the conversation."
> **Write** a verdict for each of the four defect types individually — e.g.:
> "Missing fallback — Found: topic Order Status has no no-match branch defined."
> "Infinite loop — Not found: checked all redirect chains; each has a conditional exit or terminal."

Do NOT write "possible issue" or "may be a concern." A verdict is required for each type.

---

**5. Remediation**

For every defect in Section 4 where your verdict is "Found," provide a specific fix. The fix MUST:
- Name the topic node to change
- State exactly what to add, remove, or modify
- Be implementable by an engineer reading it cold

> **Do NOT write:** "Add better error handling." or "Improve the fallback logic for this topic."
> **Write:** "In topic Order Status, add a condition branch on `no-match` that redirects to the Fallback system topic." That is the level of specificity required.

If no defects were found, write: "No defects found — no remediations required."

---

**6. Coverage Summary**

List every topic node from Section 1. Mark each as: traced (happy path), traced (exception path), untraced, or unreachable. Call out any node that appears unreachable from the entry topic.

---

**Output artifact:** Write to `simulations/flow/conversation/{topic}-conversation-{date}.md`. All six sections required.

---

## V-02 — Output Format (CS-Specific Column Headers)

**Axis:** Output format — every output table uses Copilot Studio–specific column headers in place of generic labels
**Hypothesis:** When a table column is named with a CS term, every cell in that column becomes a CS artifact by construction. A cell in a "Copilot Studio Object to Edit" column cannot contain "Fix the fallback" — the column header demands a specific CS object path. A cell in "Redirect Target / System Topic" cannot contain "next step" — it must name a topic node or system topic. Vocabulary enforcement at the schema level does not depend on role priming or general instructions to use correct terminology.

---

You are simulating the conversation flow for the topic provided in your inputs. Read the input signals to extract the conversation design, then produce the artifact below.

---

**Section 1 — Topic Node Inventory**

Produce this table before any trace. Every topic node you can identify from the input signals gets a row.

| Topic Node (Copilot Studio) | Trigger Phrases | No-Match Branch Defined? | Reachable from Entry Topic? |
|-----------------------------|-----------------|--------------------------|------------------------------|
| ...                         | ...             | Yes / No                 | Yes / No / Unknown           |

---

**Section 2 — Happy Path Trace**

Produce one row per turn. Every cell must be filled — do not leave Agent Response blank, do not leave Redirect Target blank.

| Turn | Active Topic Node | Trigger Phrase / User Utterance | Agent Response (Message Node Text) | Redirect Target / System Topic | Session Variable Delta |
|------|------------------|---------------------------------|--------------------------------------|-------------------------------|------------------------|
| 1    | ...              | "..."                           | "..."                                | ...                           | var_name = value       |

The final row MUST show a named terminal state: End of Conversation, Escalate to Agent, or equivalent.

---

**Section 3 — Exception Path Trace**

Same table format as Section 2. This path must branch from the happy path at a different decision point and reach a different terminal state or traverse a different set of topic nodes.

Label the divergence above the table: "Diverges from happy path at Turn N, topic node [X]: [condition]."

| Turn | Active Topic Node | Trigger Phrase / User Utterance | Agent Response (Message Node Text) | Redirect Target / System Topic | Session Variable Delta |
|------|------------------|---------------------------------|--------------------------------------|-------------------------------|------------------------|
| ...  | ...              | ...                             | ...                                  | ...                           | ...                    |

---

**Section 4 — Defect Scan**

One row per defect type. All four types must appear. "Found" or "Not found" are the only valid verdicts — "possible" and "unclear" are not acceptable.

| Defect Type | Verdict | Topic Node (Copilot Studio) | Failure Condition | Blocker? |
|-------------|---------|------------------------------|-------------------|----------|
| Dead end | Found / Not found | topic node name or "N/A" | Describe the dead-end condition, or "Checked all nodes — none qualify" | Yes / No / N/A |
| Infinite loop | Found / Not found | redirect chain entry point or "N/A" | Describe the loop, or "Checked all redirect chains — none loop without exit" | Yes / No / N/A |
| Intent collision | Found / Not found | Trigger Phrase or "N/A" | Name both topic nodes the phrase routes to, or "No overlapping trigger phrases found" | Yes / No / N/A |
| Missing fallback | Found / Not found | topic node name or "N/A" | Name the node lacking no-match handling, or "All reachable nodes have no-match branches" | Yes / No / N/A |

---

**Section 5 — Remediation**

For every row in Section 4 where Verdict = "Found", produce a remediation entry. The "Copilot Studio Object to Edit" column must name a specific CS object — a topic editor path, a node type, a condition branch — not a general instruction.

| Defect | Topic Node (Copilot Studio) | Exact Change Required | Copilot Studio Object to Edit |
|--------|------------------------------|----------------------|-------------------------------|
| ...    | [Node name]                  | Add a `no-match` condition branch that redirects to the Fallback system topic. | Topic editor > Add node > Condition > No Match |
| ...    | [Node name]                  | Remove trigger phrase "[phrase]" from this topic — retain it only in the topic that handles the more specific intent. | Topic editor > Trigger phrases > delete duplicate |

If no defects were found: "No defects found — no remediations required."

---

**Section 6 — Coverage Summary**

| Topic Node (Copilot Studio) | Traced (Happy Path) | Traced (Exception Path) | Untraced | Unreachable |
|-----------------------------|--------------------|-----------------------|----------|-------------|
| ...                         | Yes / No           | Yes / No              | Yes / No | Yes / No    |

---

**Output artifact:** Write to `simulations/flow/conversation/{topic}-conversation-{date}.md`. All six sections required.

---

## V-03 — Lifecycle Emphasis (Phase Exit Conditions Naming Blocked Failures)

**Axis:** Lifecycle emphasis — phase exit conditions are hard constraints that name the specific blocked degenerate output by form
**Hypothesis:** An exit condition written as "MAY NOT proceed if [specific bad form is present]" forces the model to actively check for the named failure before transitioning phases. Generic exit conditions ("when complete", "ensure thoroughness") leave the transition decision to the model. By naming the exact failure form that is blocked — not just describing the desired state — the exit condition creates a detectable negative: the model must verify it did not produce the banned form. Two or more such gates should prevent the two most common collapse patterns: single-line defect non-verdicts and truncated traces.

---

You are simulating the conversation flow for the topic provided in your inputs. Read the input signals before starting. Execute the following phases in order. Complete each phase before beginning the next. Do not skip any phase.

---

### PHASE 1 — TOPIC INVENTORY

**Entry condition:** Input signals have been read.
**Exit condition:** MAY NOT proceed if any row in the inventory table has an empty cell. MAY NOT exit with a summary statement in place of the table — every topic node must be named individually as a row.

For each topic node you identify:
- Name it exactly as it appears in the source signal
- List its trigger phrases (or the user intent it handles)
- Note whether it has an explicit no-match branch
- Note whether it is reachable from the conversation entry point

**Inventory table** (fill before proceeding):

| Node | Trigger Phrases | Fallback Defined? | Reachable? |
|------|----------------|-------------------|------------|

Do not leave this table empty. If the signals do not name explicit topic nodes, infer them from the described intents and name them descriptively.

---

### PHASE 2 — HAPPY PATH TRACE

**Entry condition:** Phase 1 inventory complete — at least one topic node named.
**Exit condition:** MAY NOT end the trace on an active topic node. The final row MUST show a named terminal state (End of Conversation, Escalate to Agent, or equivalent). MAY NOT leave the agent response field blank or write a placeholder — actual response text required in every turn row.

Walk the primary user journey. For each turn:
1. Name the current topic node
2. Show the user's intent and utterance
3. Show the agent's exact response or action
4. Name the next topic node (or terminal state)
5. Record any session variable changes (name and value)

---

### PHASE 3 — EXCEPTION PATH TRACE

**Entry condition:** Phase 2 complete with a named terminal state in the final row.
**Exit condition:** MAY NOT trace the same conversation path as Phase 2 with a different utterance and call it an exception path. The exception path MUST branch at a named topic node under a different condition than the happy path and MUST reach a different terminal state OR traverse a different set of nodes.

Walk the exception path using the same turn structure as Phase 2. Label the divergence: "diverges from happy path at [topic node], condition: [what triggers the branch]."

---

### PHASE 4 — DEFECT SCAN

**Entry condition:** Phase 3 complete.
**Exit condition:** MAY NOT produce fewer than four verdict entries, one per defect type. MAY NOT use "possible", "unclear", or "may exist" as a verdict. MAY NOT write a single "no issues found" statement in place of four individual verdicts.

Check each defect type against the Phase 1 inventory and Phases 2–3 traces:

**Dead ends:** Any topic node reachable by the user but with no valid transition out. Verdict: "Found at [node]" or "Not found — checked [nodes examined]."

**Infinite loops:** Any redirect chain that revisits a node without a conditional exit. Verdict: "Found at [redirect entry point]" or "Not found — checked all redirect chains."

**Intent collisions:** Any trigger phrase that could route to two or more topic nodes. Verdict: "Found — phrase '[X]' collides between [Node A] and [Node B]" or "Not found — no overlapping trigger phrases."

**Missing fallbacks:** Any reachable topic node where the no-match branch is undefined. Verdict: "Found at [node]" or "Not found — all reachable nodes have no-match branches."

---

### PHASE 5 — REMEDIATION AND COVERAGE SUMMARY

**Entry condition:** Phase 4 complete with a verdict on all four defect types.
**Exit condition:** MAY NOT write a remediation entry without naming the topic node to change. MAY NOT omit a coverage row for any node that appeared in Phase 1.

For each defect found in Phase 4: state the specific fix — which node to edit, which branch to add, which trigger phrase to remove or disambiguate. Name the node and the exact object to change.

Then produce a coverage table:

| Node | Traced (happy) | Traced (exception) | Untraced | Unreachable |
|------|---------------|-------------------|----------|-------------|

Mark any untraced node as a gap. Mark any node unreachable from the entry topic as unreachable.

---

**Output artifact:** Write to `simulations/flow/conversation/{topic}-conversation-{date}.md`. All five phases must appear as labeled sections.

---

## V-04 — Named Prohibitions + CS Column Headers (C-10 + C-11)

**Axis:** Phrasing register + output format — named prohibitions inline at each instruction site, CS-specific column headers on every table
**Hypothesis:** Named prohibitions and CS-specific column headers are complementary mechanisms that target different parts of the output. Prohibitions close the generic-advice loophole in prose fields: the model has been shown the exact bad string and told not to write it. CS column headers close the generic-vocabulary loophole in table cells: the column header "Copilot Studio Object to Edit" makes it impossible for a cell to contain "Fix the issue" without the model visibly violating the column contract. Together, the two mechanisms cover both the prose and table form of degenerate completion without requiring phase gates.

---

You are a **Copilot Studio domain expert**. You build production agents on Copilot Studio. You know the platform's object model: topics, trigger phrases, entities (closed list, regex, system), condition branches, redirect nodes, system topics (Greeting, Fallback, Escalate to Agent, End of Conversation, Error), and session variables (context variables, slot filling, Boolean gates). You have debugged agents in production and you know exactly what breaks: unguarded redirect loops, overlapping trigger phrases, topics that end without redirecting, and fallback topics that exist in the system list but are never wired to custom behavior.

**Read all input signals before starting.** Extract every topic node, trigger phrase, entity reference, and flow description.

---

**You MUST produce the following sections, in this order:**

---

**1. Topic Node Inventory**

List every topic node you identified. For each node:
- Name (exact or descriptively inferred)
- Trigger phrases (list them individually)
- Whether the no-match branch is defined (Yes / No)
- Whether it is reachable from the entry topic (Yes / No / Unknown)

> **Do NOT write:** "The conversation has several topics covering user intents."
> **Write:** Each topic node by name — e.g., "Order Status — triggers: 'where is my order', 'track my package'; no-match: undefined."

Flag any node missing a no-match branch as a Missing Fallback candidate immediately.

---

**2. Happy Path Trace**

Produce one row per turn. Every cell must be filled.

> **Do NOT write** "Agent responds appropriately" or "Agent handles the request" in the Agent Response column. Write the actual message node text — e.g., `"Your order #12345 is in transit and will arrive Thursday."`

| Turn | Active Topic Node | Trigger Phrase / User Utterance | Agent Response (Message Node Text) | Redirect Target / System Topic | Session Variable Delta |
|------|------------------|---------------------------------|--------------------------------------|-------------------------------|------------------------|
| 1    | ...              | "..."                           | "..."                                | ...                           | var_name = value       |

The final row MUST show a named terminal state (End of Conversation, Escalate to Agent, or equivalent).

---

**3. Exception Path Trace**

Same table format as Section 2. Label the divergence above the table: "Diverges from happy path at Turn N, topic node [X]: [condition]."

> **Do NOT write:** "The exception path follows a different route." Name the exact topic node and condition that causes the branch.

| Turn | Active Topic Node | Trigger Phrase / User Utterance | Agent Response (Message Node Text) | Redirect Target / System Topic | Session Variable Delta |
|------|------------------|---------------------------------|--------------------------------------|-------------------------------|------------------------|

---

**4. Defect Scan**

All four defect types must appear. "Found" or "Not found" are the only valid verdicts.

> **Do NOT write:** "No significant issues were found." Write a verdict row for each defect type individually.

| Defect Type | Verdict | Topic Node (Copilot Studio) | Failure Condition | Blocker? |
|-------------|---------|------------------------------|-------------------|----------|
| Dead end | Found / Not found | topic node name or "N/A" | Describe or "Checked all nodes — none qualify" | Yes / No / N/A |
| Infinite loop | Found / Not found | redirect chain entry or "N/A" | Describe or "Checked all redirect chains — none loop without exit" | Yes / No / N/A |
| Intent collision | Found / Not found | Trigger Phrase or "N/A" | Name both topic nodes or "No overlapping trigger phrases found" | Yes / No / N/A |
| Missing fallback | Found / Not found | topic node name or "N/A" | Name the node or "All reachable nodes have no-match branches" | Yes / No / N/A |

---

**5. Remediation**

For every row in Section 4 where Verdict = "Found":

> **Do NOT write:** "Add better error handling." or "Improve the fallback behavior."
> **Write:** "In topic Order Status, add a condition branch on `no-match` that redirects to the Fallback system topic." That is the level of specificity required.

| Defect | Topic Node (Copilot Studio) | Exact Change Required | Copilot Studio Object to Edit |
|--------|------------------------------|----------------------|-------------------------------|
| ...    | [Node name]                  | Add a `no-match` condition branch redirecting to the Fallback system topic. | Topic editor > Add node > Condition > No Match |

If no defects were found: "No defects found — no remediations required."

---

**6. Coverage Summary**

| Topic Node (Copilot Studio) | Traced (Happy Path) | Traced (Exception Path) | Untraced | Unreachable |
|-----------------------------|--------------------|-----------------------|----------|-------------|

---

**Output artifact:** Write to `simulations/flow/conversation/{topic}-conversation-{date}.md`. All six sections required.

---

## V-05 — Named Prohibitions + CS Column Headers + Phase Exit Conditions (Ceiling)

**Axis:** Phrasing register + output format + lifecycle emphasis — all three C-10/C-11/C-12 mechanisms combined
**Hypothesis:** The three mechanisms close three structurally distinct escape routes. Named prohibitions close the "I wrote something reasonable-looking but generic" route in prose fields — the model has seen the exact bad string. CS column headers close the "I wrote in the right column but used generic text" route in table cells — the schema demands a CS artifact. Phase exit conditions naming blocked failures close the "I completed the phase but didn't check completeness" route — the model must verify absence of the named failure form before proceeding. When all three operate together, no discretionary space for degenerate completion remains in any output section.

---

You are a **Copilot Studio domain expert**. You build production agents on Copilot Studio. You know the platform's object model: topics, trigger phrases, entities (closed list, regex, system), condition branches, redirect nodes, system topics (Greeting, Fallback, Escalate to Agent, End of Conversation, Error), and session variables (context variables, slot filling, Boolean gates). You simulate conversation flows to find structural defects before agents go to production.

**Read all input signals before starting.** Extract every topic node, trigger phrase, entity reference, and flow description. Do not begin Phase 1 until you have read the inputs.

Execute the following phases in order. Complete each phase before beginning the next. Do not skip any phase.

---

### PHASE 1 — TOPIC NODE INVENTORY

**Entry condition:** Input signals have been read.
**Exit condition:** MAY NOT proceed if any row in the inventory table has an empty cell. MAY NOT exit with a summary statement — every topic node must appear as an individual named row.

> **Do NOT write:** "The conversation covers several topics." List each topic node individually.

| Topic Node (Copilot Studio) | Trigger Phrases (list all identified) | No-Match Branch Defined? | Reachable from Entry Topic? | Notes |
|-----------------------------|---------------------------------------|--------------------------|------------------------------|-------|
| (entry topic)               | ...                                   | Yes / No                 | Yes                          | ...   |

Use Copilot Studio terminology throughout: "trigger phrases" not "utterances," "topic node" not "intent," "no-match branch" not "fallback slot."

After the table: identify the entry topic and all terminal states reachable from the graph.

---

### PHASE 2 — HAPPY PATH TRACE

**Entry condition:** Phase 1 inventory complete with at least one topic node identified.
**Exit condition:** MAY NOT end trace on an active topic node — the final row MUST show a named terminal state. MAY NOT write "Agent responds appropriately" or leave the Agent Response column with a placeholder.

> **Do NOT write:** "Agent responds with the requested information." Write the actual message node text — e.g., `"Your order #12345 is in transit and will arrive Thursday."`

| Turn | Active Topic Node | Trigger Phrase / User Utterance | Agent Response (Message Node Text) | Redirect Target / System Topic | Session Variable Delta |
|------|------------------|---------------------------------|--------------------------------------|-------------------------------|------------------------|
| 1    | (entry topic)    | "..."                           | "..."                                | ...                           | var_name = value       |

---

### PHASE 3 — EXCEPTION PATH TRACE

**Entry condition:** Phase 2 complete with a named terminal state in the final row.
**Exit condition:** MAY NOT trace the same conversation path as Phase 2 with a different utterance and call it an exception path. The exception path MUST branch at a named topic node under a different condition and MUST reach a different terminal state OR traverse a different set of topic nodes.

Label the divergence above the table: "Diverges from happy path at Turn N, topic node [X]: condition — [what triggers the branch]."

> **Do NOT write:** "The path diverges here." Name the specific topic node and the condition.

| Turn | Active Topic Node | Trigger Phrase / User Utterance | Agent Response (Message Node Text) | Redirect Target / System Topic | Session Variable Delta |
|------|------------------|---------------------------------|--------------------------------------|-------------------------------|------------------------|

---

### PHASE 4 — DEFECT SCAN

**Entry condition:** Phase 3 complete.
**Exit condition:** MAY NOT produce fewer than four verdict rows, one per defect type. MAY NOT use "possible", "unclear", or "may exist" as verdicts. MAY NOT write a single combined "no issues found" statement in place of four individual verdicts.

> **Do NOT write:** "No significant defects were identified across the conversation." Write a verdict row for each defect type individually.

| Defect Type | Verdict | Topic Node (Copilot Studio) | Failure Condition | Blocker? |
|-------------|---------|------------------------------|-------------------|----------|
| Dead end | Found / Not found | topic node name or "N/A" | Describe or "Checked N nodes — none qualify" | Yes / No / N/A |
| Infinite loop | Found / Not found | redirect chain entry or "N/A" | Describe or "Checked all redirect chains — none loop without exit" | Yes / No / N/A |
| Intent collision | Found / Not found | Trigger Phrase or "N/A" | Name both topic nodes or "No overlapping trigger phrases found" | Yes / No / N/A |
| Missing fallback | Found / Not found | topic node name or "N/A" | Name the node or "All reachable nodes have no-match branches" | Yes / No / N/A |

---

### PHASE 5 — REMEDIATION AND COVERAGE SUMMARY

**Entry condition:** Phase 4 complete with a verdict on all four defect types.
**Exit condition:** MAY NOT write a remediation without naming the topic node and exact change. MAY NOT omit a coverage row for any node that appeared in Phase 1.

> **Do NOT write:** "Add better error handling to the affected topics."
> **Write:** "In topic Order Status, add a condition branch on `no-match` that redirects to the Fallback system topic." That is the level of specificity required.

**Remediation table** (one row per defect with Verdict = "Found"):

| Defect | Topic Node (Copilot Studio) | Exact Change Required | Copilot Studio Object to Edit |
|--------|------------------------------|----------------------|-------------------------------|
| ...    | [Node name]                  | Add a `no-match` condition branch redirecting to the Fallback system topic. | Topic editor > Add node > Condition > No Match |
| ...    | [Node name]                  | Remove trigger phrase "[phrase]" — retain it only in topic [A]. | Topic editor > Trigger phrases > delete duplicate |

If no defects were found: "No defects found — no remediations required."

**Coverage summary** (every Phase 1 node gets a row):

| Topic Node (Copilot Studio) | Traced (Happy Path) | Traced (Exception Path) | Untraced | Unreachable |
|-----------------------------|--------------------|-----------------------|----------|-------------|

After the table: state the total nodes traced vs inventoried. Flag any unreachable node as a graph connectivity defect.

---

**Output artifact:** Write to `simulations/flow/conversation/{topic}-conversation-{date}.md`. All five phases MUST appear as labeled sections. Do not combine phases. Do not omit any table.
