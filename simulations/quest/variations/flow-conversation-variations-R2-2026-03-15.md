---

# flow-conversation Variate — Round 2

**Rubric:** v2 (C-01–C-12) | **Target:** C-10, C-11, C-12 | **Baseline:** R1 V-04/V-05 passed C-01–C-09

---

## Round 2 Variation Map

| Variation | Axis | C-10 | C-11 | C-12 | Hypothesis |
|-----------|------|------|------|------|------------|
| **V-01** | Phrasing register (named prohibitions) | PASS | FAIL | FAIL | Named prohibitions at each instruction site give model a local pattern-match signal; no CS column headers, no phase gates |
| **V-02** | Output format (CS-specific column headers) | FAIL | PASS | FAIL | CS column headers enforce vocabulary by schema; no named prohibitions, no phase gates |
| **V-03** | Lifecycle emphasis (phase exit conditions naming blocked failures) | FAIL | FAIL | PASS | Hard exit conditions naming the blocked failure prevent degenerate phase completion; no named prohibitions, no CS headers |
| **V-04** | Phrasing register + Output format (C-10 + C-11) | PASS | PASS | FAIL | Named prohibitions close prose escape routes; CS column headers close table-cell escape routes; phase collapse still possible without hard gates |
| **V-05** | All three combined (ceiling) | PASS | PASS | PASS | No discretionary space for collapse in prose, tables, or phase completion |

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

List every topic node you identified. For each: name (exact or inferred), trigger phrases, whether the no-match branch is defined, whether it is reachable from the entry point.

> **Do NOT write:** "The conversation covers several topics related to user needs."
> **Write:** Each topic node by name — e.g., "Order Status — triggers: 'where is my order', 'track my package'; no-match branch: undefined."

Flag any node lacking a no-match branch as a Missing Fallback candidate immediately.

---

**2. Happy Path Trace**

Trace the primary user journey. For EVERY turn: active topic node, user intent label + utterance, agent's exact response, topic transition or terminal state, session variable delta (name and value).

> **Do NOT write:** "Agent responds appropriately" or "Agent handles the request."
> **Write:** The actual message text — e.g., `"Your order #12345 is in transit and will arrive Thursday."`

The trace MUST end at a named terminal state.

---

**3. Exception Path Trace**

Trace one exception path — fallback branch, entity resolution failure, loop exit, or escalation trigger. Same turn structure as Section 2.

> **Do NOT write:** "The exception path follows a different route through the conversation."
> **Write:** The exact topic node where the path diverges and the condition — e.g., "diverges at Order Status, condition: entity `order_number` not resolved after two prompts."

---

**4. Defect Report**

For EACH of the four defect types, write: "Found: [topic node + failure condition]" or "Not found: checked [nodes examined]."

- Dead end | Infinite loop | Intent collision | Missing fallback

> **Do NOT write:** "No significant issues were found across the conversation."
> **Write** a verdict for each type — e.g., "Missing fallback — Found: topic Order Status has no no-match branch defined."

---

**5. Remediation**

For each "Found" defect: name the topic node to change, state exactly what to add/remove/modify.

> **Do NOT write:** "Add better error handling." or "Improve the fallback logic."
> **Write:** "In topic Order Status, add a condition branch on `no-match` that redirects to the Fallback system topic." That is the level of specificity required.

---

**6. Coverage Summary**

List every Section 1 node with status: traced (happy), traced (exception), untraced, or unreachable.

**Output artifact:** `simulations/flow/conversation/{topic}-conversation-{date}.md`

---

## V-02 — Output Format (CS-Specific Column Headers)

**Axis:** Output format — every output table uses Copilot Studio–specific column headers
**Hypothesis:** When a table column is named with a CS term, every cell in that column becomes a CS artifact by construction. A cell in "Copilot Studio Object to Edit" cannot contain "Fix the fallback" — the header demands a specific CS object path. A cell in "Redirect Target / System Topic" cannot say "next step" — it must name a topic node or system topic. Vocabulary enforcement at the schema level does not depend on role priming or general instructions to use correct terminology.

---

You are simulating the conversation flow for the topic provided in your inputs. Read the input signals to extract the conversation design, then produce the artifact below.

---

**Section 1 — Topic Node Inventory**

| Topic Node (Copilot Studio) | Trigger Phrases | No-Match Branch Defined? | Reachable from Entry Topic? |
|-----------------------------|-----------------|--------------------------|------------------------------|
| ... | ... | Yes / No | Yes / No / Unknown |

---

**Section 2 — Happy Path Trace**

| Turn | Active Topic Node | Trigger Phrase / User Utterance | Agent Response (Message Node Text) | Redirect Target / System Topic | Session Variable Delta |
|------|------------------|---------------------------------|--------------------------------------|-------------------------------|------------------------|
| 1 | ... | "..." | "..." | ... | var_name = value |

Final row MUST show a named terminal state.

---

**Section 3 — Exception Path Trace**

Same table format. Label divergence above table: "Diverges from happy path at Turn N, topic node [X]: [condition]."

| Turn | Active Topic Node | Trigger Phrase / User Utterance | Agent Response (Message Node Text) | Redirect Target / System Topic | Session Variable Delta |
|------|------------------|---------------------------------|--------------------------------------|-------------------------------|------------------------|

---

**Section 4 — Defect Scan**

All four defect types must appear. "Found" or "Not found" only — "possible" and "unclear" are not acceptable verdicts.

| Defect Type | Verdict | Topic Node (Copilot Studio) | Failure Condition | Blocker? |
|-------------|---------|------------------------------|-------------------|----------|
| Dead end | Found / Not found | topic node or "N/A" | Describe or "Checked all nodes — none qualify" | Yes / No / N/A |
| Infinite loop | Found / Not found | redirect chain entry or "N/A" | Describe or "Checked all redirect chains — none loop without exit" | Yes / No / N/A |
| Intent collision | Found / Not found | Trigger Phrase or "N/A" | Name both topic nodes or "No overlapping trigger phrases" | Yes / No / N/A |
| Missing fallback | Found / Not found | topic node or "N/A" | Name the node or "All reachable nodes have no-match branches" | Yes / No / N/A |

---

**Section 5 — Remediation**

| Defect | Topic Node (Copilot Studio) | Exact Change Required | Copilot Studio Object to Edit |
|--------|------------------------------|----------------------|-------------------------------|
| ... | [Node name] | Add a `no-match` condition branch redirecting to the Fallback system topic. | Topic editor > Add node > Condition > No Match |

If no defects: "No defects found — no remediations required."

---

**Section 6 — Coverage Summary**

| Topic Node (Copilot Studio) | Traced (Happy Path) | Traced (Exception Path) | Untraced | Unreachable |
|-----------------------------|--------------------|-----------------------|----------|-------------|

**Output artifact:** `simulations/flow/conversation/{topic}-conversation-{date}.md`

---

## V-03 — Lifecycle Emphasis (Phase Exit Conditions Naming Blocked Failures)

**Axis:** Lifecycle emphasis — phase exit conditions are hard constraints naming the specific blocked degenerate output by form
**Hypothesis:** An exit condition written as "MAY NOT proceed if [specific bad form is present]" forces the model to actively check for the named failure before transitioning. Generic exit conditions ("when complete") leave the decision to the model. By naming the exact failure form blocked — not describing the desired state — the exit condition creates a detectable negative. Two or more such gates prevent the two most common collapse patterns: single-line defect non-verdicts and truncated traces.

---

You are simulating the conversation flow for the topic provided in your inputs. Read the input signals before starting. Execute the following phases in order. Complete each phase before beginning the next. Do not skip any phase.

---

### PHASE 1 — TOPIC INVENTORY

**Entry condition:** Input signals read.
**Exit condition:** MAY NOT proceed if any row in the inventory has an empty cell. MAY NOT exit with a summary statement — every topic node must be named as an individual row.

| Node | Trigger Phrases | Fallback Defined? | Reachable? |
|------|----------------|-------------------|------------|

Do not leave this table empty. Infer topic nodes from described intents if not explicitly named.

---

### PHASE 2 — HAPPY PATH TRACE

**Entry condition:** Phase 1 complete — at least one topic node named.
**Exit condition:** MAY NOT end the trace on an active topic node — the final row MUST show a named terminal state. MAY NOT leave any agent response cell blank or with a placeholder.

Walk the primary user journey: active topic node, user intent + utterance, exact agent response, next topic or terminal, session variable delta.

---

### PHASE 3 — EXCEPTION PATH TRACE

**Entry condition:** Phase 2 complete with a named terminal state in the final row.
**Exit condition:** MAY NOT trace the same path as Phase 2 with a different utterance and label it an exception path. Path MUST branch at a named topic node under a different condition and MUST reach a different terminal state OR traverse a different set of nodes.

Label the divergence: "diverges from happy path at [topic node], condition: [what triggers the branch]."

---

### PHASE 4 — DEFECT SCAN

**Entry condition:** Phase 3 complete.
**Exit condition:** MAY NOT produce fewer than four verdict entries, one per defect type. MAY NOT use "possible", "unclear", or "may exist". MAY NOT write a single combined "no issues found" statement in place of four individual verdicts.

**Dead ends:** Verdict: "Found at [node]" or "Not found — checked [nodes examined]."
**Infinite loops:** Verdict: "Found at [redirect entry]" or "Not found — checked all redirect chains."
**Intent collisions:** Verdict: "Found — '[phrase]' collides between [A] and [B]" or "Not found — no overlapping trigger phrases."
**Missing fallbacks:** Verdict: "Found at [node]" or "Not found — all reachable nodes have no-match branches."

---

### PHASE 5 — REMEDIATION AND COVERAGE SUMMARY

**Entry condition:** Phase 4 complete — verdict on all four defect types.
**Exit condition:** MAY NOT write a remediation without naming the topic node to change. MAY NOT omit a coverage row for any Phase 1 node.

For each defect found: name the node, state the exact change (branch to add, trigger phrase to remove, redirect to wire).

Coverage table:

| Node | Traced (happy) | Traced (exception) | Untraced | Unreachable |
|------|---------------|-------------------|----------|-------------|

**Output artifact:** `simulations/flow/conversation/{topic}-conversation-{date}.md`

---

## V-04 — Named Prohibitions + CS Column Headers (C-10 + C-11)

**Axis:** Phrasing register + output format
**Hypothesis:** Named prohibitions and CS-specific column headers are complementary. Prohibitions close the generic-advice loophole in prose fields — the model has seen the exact bad string. CS column headers close the generic-vocabulary loophole in table cells — "Copilot Studio Object to Edit" makes "Fix the issue" an obvious violation of the column contract. Together they cover both prose and table form of degenerate completion without requiring phase gates.

*(Full prompt body: combines V-01 named prohibitions at each instruction site with V-02 CS-specific column headers on all tables. Role framing from V-01. All six sections present. Phase structure is section-based, not gated.)*

**[Full prompt body at `simulations/quest/golden/flow-conversation-variate-R2-2026-03-15.md` — V-04 section]**

---

## V-05 — Named Prohibitions + CS Column Headers + Phase Exit Conditions (Ceiling)

**Axis:** Phrasing register + output format + lifecycle emphasis
**Hypothesis:** Three mechanisms, three escape routes closed. Named prohibitions close the "reasonable-looking but generic prose" route. CS column headers close the "right column, wrong vocabulary" route. Phase exit conditions naming blocked failures close the "all phases present but completion was skimmed" route. No discretionary space remains in any output section.

*(Full prompt body at `simulations/quest/golden/flow-conversation-variate-R2-2026-03-15.md` — V-05 section)*

---

Written to `simulations/quest/golden/flow-conversation-variate-R2-2026-03-15.md`.

---

## Design decisions across Round 2

**Why FAIL not PARTIAL for single-axis misses:**
C-10/C-11/C-12 all have binary pass conditions ("at least one" type). If V-01 has no tables, there are zero CS-specific column headers — that is FAIL, not PARTIAL. No ambiguous middle state.

**Why V-03 does not accidentally pass C-10:**
The phase exit conditions in V-03 are structural constraints ("MAY NOT produce fewer than four verdict entries") not named-example prohibitions. C-10 requires the prompt to name a plausible bad output by instance. "MAY NOT write fewer than four verdicts" is a count constraint, not a named-form prohibition. V-03 keeps these structurally distinct.

**Why V-04 is not the ceiling:**
V-04 lacks phase gates with named blocked failures (C-12). Without hard exit conditions, the model retains discretion to transition phases after shallow completion — the table schemas enforce what each cell must contain but not that the phase produced enough cells. V-05 adds that gate.

**Key pattern from R1 → R2:**
R1 established that role priming (V-01) is soft — it enables CS vocabulary but does not require it row by row. R2 V-02 tests whether schema enforcement (column headers as CS terms) is the structural fix. R2 V-03 tests whether the phase-gate mechanism from R1 V-03/V-05 can be made even harder by naming the failure form rather than describing the desired state.
