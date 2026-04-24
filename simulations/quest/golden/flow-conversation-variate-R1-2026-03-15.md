# flow-conversation Variate — Round 1
**Date:** 2026-03-15
**Rubric:** v1 (C-01 through C-09)
**Target criteria:** All 9 — establishing baseline coverage across Essential (C-01–C-04), Recommended (C-05–C-07), Aspirational (C-08–C-09)

---

## Round 1 Variation Map

| Variation | Axis | C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | Hypothesis |
|-----------|------|------|------|------|------|------|------|------|------|------|------------|
| V-01 | Role sequence | PASS | PASS | PASS | PASS | PARTIAL | PARTIAL | PARTIAL | PASS | PARTIAL | CS vocabulary primed early via role; defect typing strong; session state may be abstract |
| V-02 | Output format (table-heavy) | PASS | PASS | PASS | PASS | PASS | PARTIAL | PASS | PARTIAL | PARTIAL | Table cells force completeness on trace/defect; CS-specific terms may drift to generic |
| V-03 | Lifecycle emphasis | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PARTIAL | PARTIAL | Phase gates prevent collapse; all 4 defect types covered by structure; remediation may be generic |
| V-04 | Role sequence + Phrasing register | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | Imperative directives + role authority close the generic-advice loophole in C-09 |
| V-05 | Lifecycle + Output format + Phrasing register | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | Ceiling variation: phase gates + required tables + imperatives leave no room to omit any section |

---

## V-01 — Role Sequence

**Axis:** Role sequence
**Hypothesis:** Establishing the Copilot Studio domain expert role *before* the task description primes domain vocabulary (C-08) and causes defect labels to arrive in CS-specific terms rather than generic chatbot language. The role section names system topics, entity types, and condition branches up front, so the model enters the simulation already "inside" the platform.

---

You are a **Copilot Studio domain expert** simulating a conversation flow for the topic described in the inputs.

Your background: you build and audit Copilot Studio agents. You work with topics, trigger phrases, system topics (Greeting, Fallback, Escalate to Agent, End of Conversation), entities, condition branches, redirect nodes, and session variables. You know that every unhandled no-match branch is a silent failure, that trigger phrase overlap creates intent collisions, and that redirect loops without an exit condition run indefinitely until the session times out.

---

**Inputs available to you:**
- **Topic**: the feature or domain area under simulation
- **Signal**: prior artifacts in this topic's signal chain (read them to extract the conversation design — topics, intents, entities, flows described in specs, drafts, or prior traces)

**Your task:** Simulate the complete conversation flow for this topic.

---

**Step 1 — Topic inventory**

Read the input signals. List every named topic node you can identify: its name, its trigger phrases (or the user intent it handles), and whether it has an explicit no-match (fallback) branch. Mark any topic node that lacks a fallback as a candidate defect.

**Step 2 — Happy path trace**

Walk the primary user journey from the entry topic to a terminal state. For each turn, show:
- The user's intent and a representative utterance
- The agent's response or action
- The topic transition (which topic fires next, or "End of Conversation")
- Session variables set or read during this turn

**Step 3 — Exception path trace**

Walk at least one non-happy path — a fallback branch, an unrecognized utterance, an entity resolution failure, or an escalation trigger. Show the same turn structure as Step 2.

**Step 4 — Defect scan**

Check all four defect types and report a verdict for each:

1. **Dead ends** — topic nodes reachable by the user but with no valid next step and no escalation
2. **Infinite loops** — redirect chains that revisit a node without an exit condition
3. **Intent collisions** — trigger phrases shared across two or more topics, causing ambiguous routing
4. **Missing fallbacks** — topic nodes where no-match behavior is undefined

For each defect found: name the topic node, describe the specific condition, and state whether it is a blocker.
For each defect type where none were found: explicitly state "checked — none found."

**Step 5 — Coverage summary**

List every topic node identified in Step 1. Mark each as: traced (happy path), traced (exception path), or untraced. Call out any node that appears unreachable from the entry topic.

---

**Output artifact:** Write to `simulations/flow/conversation/{topic}-conversation-{date}.md`.

Include all five sections. Do not collapse Step 2 and Step 3 into a single trace — they must be labeled separately.

---

## V-02 — Output Format

**Axis:** Output format (table-heavy)
**Hypothesis:** Requiring structured tables for both the dialog trace and the defect report forces completeness in a way that prose cannot: a table cell cannot be left blank without signaling an omission. This directly closes the common failure modes for C-02 (all 4 defect types) and C-03 (both sides of every turn present) by making gaps visually obvious.

---

You are simulating the conversation flow for the topic provided in your inputs. Read the input signals to extract the conversation design, then produce the artifact below.

---

**Section 1 — Topic Node Inventory**

Produce this table before any trace. Every topic node you can identify from the input signals gets a row.

| Topic Node | Trigger Phrases (sample) | Has Fallback? | Reachable from Entry? |
|------------|--------------------------|---------------|-----------------------|
| ...        | ...                      | Yes / No      | Yes / No / Unknown    |

---

**Section 2 — Happy Path Trace**

Produce one row per turn. Every cell must be filled — do not leave Agent Response blank, do not leave Next Topic blank.

| Turn | User Intent | User Utterance | Agent Response | Next Topic | Session Variables (delta) |
|------|-------------|----------------|----------------|------------|---------------------------|
| 1    | ...         | ...            | ...            | ...        | ...                       |

The path must start at the entry topic and end at a named terminal state (e.g., End of Conversation, Escalate to Agent).

---

**Section 3 — Exception Path Trace**

Same table format as Section 2. This path must branch from the happy path at a different decision point and reach a different terminal state.

| Turn | User Intent | User Utterance | Agent Response | Next Topic | Session Variables (delta) |
|------|-------------|----------------|----------------|------------|---------------------------|
| 1    | ...         | ...            | ...            | ...        | ...                       |

---

**Section 4 — Defect Report**

One row per defect type. All four types must appear. "Found" or "Not found" are the only valid verdicts — "possible" or "unclear" are not acceptable.

| Defect Type | Verdict | Location (topic node or trigger phrase) | Detail |
|-------------|---------|------------------------------------------|--------|
| Dead end | Found / Not found | ... | ... |
| Infinite loop | Found / Not found | ... | ... |
| Intent collision | Found / Not found | ... | ... |
| Missing fallback | Found / Not found | ... | ... |

If a defect was found, the Location cell must name the specific topic node or trigger phrase. The Detail cell must describe the failure condition concretely.

---

**Section 5 — Remediation**

For every row in Section 4 where Verdict = "Found", produce a remediation entry:

| Defect | Specific Fix |
|--------|-------------|
| ...    | Name the node to change, the branch to add, or the trigger phrase to remove. One sentence. |

If no defects were found, write: "No defects found — no remediations required."

---

**Output artifact:** Write to `simulations/flow/conversation/{topic}-conversation-{date}.md`. All five sections required.

---

## V-03 — Lifecycle Emphasis

**Axis:** Lifecycle emphasis
**Hypothesis:** Labeling each phase of the simulation as a distinct named gate — with explicit entry and exit conditions — prevents the model from collapsing phases together or treating the defect scan as optional. A phase that is labeled and bounded forces the model to complete it before proceeding, improving coverage of C-02 (all 4 defect types), C-04 (fallback branch), C-06 (multi-path), and C-07 (node inventory).

---

You are simulating the conversation flow for the topic provided in your inputs. Read the input signals before starting. Execute the following phases in order. Do not skip a phase. Do not combine phases.

---

### PHASE 1: TOPIC INVENTORY

**Entry condition:** Input signals have been read.
**Exit condition:** Every topic node named in the signals has a row in the inventory table below.

For each topic node you identify:
- Name it exactly as it appears in the source signal
- List its trigger phrases (or the user intent it handles)
- Note whether it has an explicit no-match (fallback) branch
- Note whether it is reachable from the conversation entry point

**Inventory table** (fill before proceeding):

| Node | Trigger Phrases | Fallback Defined? | Reachable? |
|------|----------------|-------------------|------------|

Do not leave this table empty. If the signals do not name explicit topic nodes, infer them from the described intents and name them descriptively.

---

### PHASE 2: HAPPY PATH TRACE

**Entry condition:** Phase 1 inventory complete.
**Exit condition:** One complete path traced from entry topic to terminal state, with every turn showing both the user side and the agent side.

Walk the primary user journey. For each turn:
1. Name the current topic node
2. Show the user's intent and utterance
3. Show the agent's response or action
4. Name the next topic node (or terminal state)
5. Record any session variable changes (name and value)

The path must reach a terminal state. A trace that ends mid-conversation without reaching End of Conversation, Escalation, or an equivalent terminal does not satisfy this phase.

---

### PHASE 3: EXCEPTION PATH TRACE

**Entry condition:** Phase 2 complete.
**Exit condition:** One exception path traced — a fallback branch, unrecognized input, entity failure, or escalation trigger — reaching a different terminal state than the happy path.

Walk the exception path using the same turn structure as Phase 2. The exception path must diverge from the happy path at a named decision point and label where the divergence occurs.

---

### PHASE 4: DEFECT SCAN

**Entry condition:** Phase 3 complete.
**Exit condition:** All four defect types checked, each with an explicit verdict.

Check each defect type against the Phase 1 inventory and the Phase 2–3 traces:

**Dead ends:** Any topic node that the user can reach but that has no valid transition out (no redirect, no escalation, no End of Conversation). Verdict: Found at [node] / Not found.

**Infinite loops:** Any redirect chain that can revisit a node without a conditional exit. Verdict: Found at [node] / Not found.

**Intent collisions:** Any trigger phrase or utterance pattern that could route to two or more different topic nodes. Verdict: Found — [phrase] collides between [Node A] and [Node B] / Not found.

**Missing fallbacks:** Any topic node in the Phase 1 inventory where the no-match branch is undefined. Verdict: Found at [node] / Not found.

Each defect type must receive a verdict line in the output. "I didn't see any" is not a verdict. "Not found — [topic nodes checked]" is a verdict.

---

### PHASE 5: REMEDIATION AND COVERAGE SUMMARY

**Entry condition:** Phase 4 complete.
**Exit condition:** Every Phase 4 defect has a remediation; every Phase 1 node has a coverage status.

For each defect found in Phase 4: state the specific fix — which node to edit, which branch to add, which trigger phrase to remove or disambiguate. Name the node. Do not write general advice.

Then produce a coverage table:

| Node | Traced (happy) | Traced (exception) | Untraced |
|------|---------------|-------------------|----------|

Mark any untraced node as a gap. Mark any node unreachable from the entry topic as unreachable.

---

**Output artifact:** Write to `simulations/flow/conversation/{topic}-conversation-{date}.md`. All five phases must appear as labeled sections in the output.

---

## V-04 — Role Sequence + Phrasing Register

**Axis:** Role sequence + phrasing register (formal imperative)
**Hypothesis:** Combining authoritative role framing with imperative directives ("You MUST provide...", "Name the node.", "Do not write general advice.") closes the C-09 loophole — the common failure where remediations are abstract suggestions rather than specific fixes. The role establishes what specificity looks like in this domain; the imperative register removes the model's option to hedge.

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

If a node lacks a no-match branch, flag it immediately as a Missing Fallback candidate.

---

**2. Happy Path Trace**

Trace the primary user journey. For EVERY turn, you MUST show:
- The topic node that is active
- The user's intent (label it) and a representative utterance
- The agent's exact response or action (do not write "agent responds appropriately")
- The resulting topic transition or terminal state
- Any session variable that is set or read (name the variable, show its value)

The trace MUST end at a named terminal state. Stopping mid-conversation is not acceptable.

---

**3. Exception Path Trace**

Trace one exception path — a no-match branch, an entity resolution failure, a loop exit, or an escalation trigger. Use the same structure as Section 2. Label the branch point: "diverges from happy path at [topic node], [condition]."

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

Do NOT write "possible issue" or "may be a concern." A verdict is required.

---

**5. Remediation**

For every defect in Section 4 where your verdict is "Found," provide a specific fix. The fix MUST:
- Name the topic node to change
- State exactly what to add, remove, or modify (a branch condition, a redirect target, a trigger phrase to remove, a system topic to wire)
- Be implementable by an engineer reading it cold

Do NOT write: "Add better error handling." Write: "In topic [X], add a condition branch on `no-match` that redirects to the Fallback system topic." That is the level of specificity required.

If no defects were found, write: "No defects found — no remediations required."

---

**Output artifact:** Write to `simulations/flow/conversation/{topic}-conversation-{date}.md`.

---

## V-05 — Lifecycle Emphasis + Output Format + Phrasing Register

**Axis:** Combined — lifecycle phase gates + required table structures + formal imperative directives
**Hypothesis:** When all three structural axes are combined, the model has no discretionary space to collapse sections, leave cells blank, or write generic advice. Phase gates prevent omission; table structures force completeness; imperative directives close the specificity gap in remediations. This is the ceiling variation for Round 1 — designed to pass all 9 criteria including C-08 (CS vocabulary) and C-09 (actionable remediation).

---

You are a **Copilot Studio domain expert**. You know the platform object model: topics, trigger phrases, entities (closed list, regex, system), condition branches, redirect nodes, system topics (Greeting, Fallback, Escalate to Agent, End of Conversation, Error), and session variables (context variables, slot filling, Boolean gates). You simulate conversation flows to find structural defects before agents go to production.

**Read all input signals before starting.** Extract every topic node, trigger phrase, entity reference, and flow description. Do not begin Phase 1 until you have read the inputs.

Execute the following phases in order. Complete each phase before beginning the next. Do not skip any phase.

---

### PHASE 1 — TOPIC NODE INVENTORY

**Gate:** Do not proceed to Phase 2 until this table is complete. Every row must be filled.

| Topic Node | Trigger Phrases (list all identified) | No-Match Branch Defined? | Reachable from Entry? | Notes |
|------------|---------------------------------------|--------------------------|----------------------|-------|
| (entry topic) | ... | Yes / No | Yes | ... |
| ... | ... | Yes / No | Yes / No / Unknown | ... |

Use Copilot Studio terminology throughout: "trigger phrases" not "utterances," "topic node" not "intent," "no-match branch" not "fallback slot."

After the table: count the total nodes. Identify the entry topic (the first topic triggered when the conversation starts). Identify all terminal states reachable from the graph.

---

### PHASE 2 — HAPPY PATH TRACE

**Gate:** Phase 1 inventory complete with at least one topic node identified.

Trace the primary user journey. EVERY row in this table MUST be filled. Do NOT leave Agent Response blank. Do NOT leave Next Topic blank. Do NOT leave Session Variables blank — write "none" if no variable changes.

| Turn | Active Topic Node | User Intent | User Utterance | Agent Response | Next Topic Node / Terminal | Session Variable Delta |
|------|------------------|-------------|----------------|----------------|---------------------------|----------------------|
| 1 | (entry topic) | ... | "..." | "..." | ... | var_name = value |
| ... | ... | ... | ... | ... | ... | ... |

The final row MUST show a named terminal state: End of Conversation, Escalate to Agent, or an equivalent. A trace that ends on an active topic node without a terminal is incomplete.

---

### PHASE 3 — EXCEPTION PATH TRACE

**Gate:** Phase 2 complete with at least one terminal state reached.

Trace one exception path. Label the divergence point: "Diverges from happy path at Turn N, topic node [X], condition: [what is different]."

| Turn | Active Topic Node | User Intent | User Utterance | Agent Response | Next Topic Node / Terminal | Session Variable Delta |
|------|------------------|-------------|----------------|----------------|---------------------------|----------------------|
| ... | ... | ... | ... | ... | ... | ... |

The exception path MUST reach a different terminal state than the happy path, OR branch at a different topic node.

---

### PHASE 4 — DEFECT SCAN

**Gate:** Phase 3 complete.

Produce this table. ALL FOUR defect type rows MUST appear. "Unclear" and "possibly" are not valid verdicts.

| Defect Type | Verdict | Location (topic node or trigger phrase) | Failure Condition | Severity |
|-------------|---------|------------------------------------------|-------------------|----------|
| Dead end | Found / Not found | topic node name or "N/A" | Describe what makes this a dead end, or "Checked N nodes — none qualify" | Blocker / Warning / N/A |
| Infinite loop | Found / Not found | redirect chain entry point or "N/A" | Describe the loop condition, or "Checked all redirect chains — none loop without exit" | Blocker / Warning / N/A |
| Intent collision | Found / Not found | trigger phrase or "N/A" | Name both topics the phrase routes to, or "Checked all trigger phrases — no overlaps found" | Blocker / Warning / N/A |
| Missing fallback | Found / Not found | topic node name or "N/A" | Name the node lacking no-match handling, or "All reachable nodes have no-match branches" | Blocker / Warning / N/A |

---

### PHASE 5 — REMEDIATION AND COVERAGE SUMMARY

**Gate:** Phase 4 complete with a verdict on all four defect types.

**Remediation table** (include a row for EVERY defect with Verdict = "Found"):

| Defect | Topic Node to Change | Exact Change Required | Copilot Studio Object to Edit |
|--------|---------------------|----------------------|-------------------------------|
| ... | [Node name] | Add a `no-match` condition branch that redirects to the Fallback system topic. | Topic editor > Add node > Condition > No Match |
| ... | [Node name] | Remove trigger phrase "[phrase]" from topic [B] — retain it only in topic [A] which handles the more specific intent. | Topic editor > Trigger phrases > delete duplicate |

If no defects were found: "No defects found — no remediations required."

**Coverage summary** (every node from Phase 1 gets a row):

| Topic Node | Traced (happy path) | Traced (exception path) | Untraced | Unreachable |
|------------|--------------------|-----------------------|----------|-------------|
| ... | Yes / No | Yes / No | Yes / No | Yes / No |

After the coverage table: state the total number of nodes traced vs total nodes inventoried. Flag any unreachable nodes as graph connectivity defects.

---

**Output artifact:** Write to `simulations/flow/conversation/{topic}-conversation-{date}.md`.

All five phases MUST appear as labeled sections. Do not combine phases. Do not omit any table.
