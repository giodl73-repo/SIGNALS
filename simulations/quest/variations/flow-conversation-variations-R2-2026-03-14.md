Written to `simulations/quest/variations/flow-conversation-variations-R2-2026-03-14.md`.

---

## Round 2 Variations -- flow-conversation

**Baseline:** R1 V-05 scored 100 under v1. Under v2 it scores **95** — misses C-10 (no post-trace verification) and C-11 (design conformance ≠ topology spec conformance).

| V | Axis | Key mechanism | C-10 | C-11 | Predicted score |
|---|------|---------------|------|------|----------------|
| **V-01** | Output format | Post-trace PROHIBITED TERM AUDIT table — per-term CLEAN/FOUND scan of completed output | **YES** | — | 95 |
| **V-02** | Lifecycle emphasis | Pre-stated CS-SPEC-01..07 + required `SPEC_CONFORMANCE` field every turn | — | **YES** | 95 |
| **V-03** | Role sequence | Compliance Auditor runs post-trace: prohibited term scan + per-turn spec annotations | **YES** | **YES** | 97.5 |
| **V-04** | Phrasing register | Typed enum fields: `SPEC_CONFORMANCE: CONFORMS\|DEVIATES[CS-SPEC-N]` per turn + `VOCABULARY_AUDIT` table | **YES** | **YES** | 97.5 |
| **V-05** | Full synthesis | R1 V-05 (C-08 + C-09 already covered) + Phase 7 PROHIBITED TERM AUDIT + SPEC_CONFORMANCE per turn | **YES** | **YES** | **100** |

**Key design distinction for C-11:** R1 V-04/V-05's `MATCHES INTENT / DEVIATES` is *design* conformance (implementation vs. Conversation Designer's intent). C-11 requires *topology spec* conformance — does the turn follow CS node-type rules, session variable scoping, confidence threshold behavior? Different failure surface. V-02 through V-05 address this by pre-stating CS-SPEC-01..07 and requiring verdicts that cite the property number.

**Key design distinction for C-10:** R1 V-03/V-05 listed prohibited terms as instructions at the start. That prevents violations through compliance pressure but cannot *verify* absence. The post-trace audit table (V-01, V-03, V-04, V-05) forces the model to scan its own completed output and produce a per-term verdict — satisfying the "verification that none appear" requirement.

**Research question for R2:** Does V-04's per-turn `PROHIBITED_TERM_SCAN` field (catching violations at point of occurrence) outperform V-01's post-trace audit (scanning finished output) for C-10? The audit table may be more thorough; the per-turn scan may prevent violations rather than detecting them.
ng enforcement while closing the two gaps.

**Closest competitor:** V-03 -- role separation surfaces vocabulary violations the Developer may not catch inline; the Auditor's second-pass scan is more rigorous than per-turn instructions.

**Open research question for R2:** Does V-04's per-turn PROHIBITED_TERM_SCAN field (catching violations at point of occurrence) outperform V-01's post-trace PROHIBITED TERM AUDIT table (scanning the completed output) for C-10? The audit table approach may produce more thorough coverage; the per-turn approach may produce fewer violations to audit.

---

## V-01: Output Format -- Post-trace Prohibited Term Audit

**Axis:** Output format -- adds a required PROHIBITED TERM AUDIT section at the end of the simulation. Pre-prints one row per prohibited term; the model must record CLEAN or FOUND for each and, if FOUND, quote the exact line and name the required replacement. The vocabulary gate at the start remains (from R1 V-03), but the audit at the end creates a structural verification loop.

**Hypothesis:** C-10's distinction from R1 V-03 is the word "verification." R1 V-03 listed prohibited terms as instructions before the trace; that prevents violations through compliance pressure but cannot confirm they are absent. The PROHIBITED TERM AUDIT table forces the model to scan its own completed output and produce a per-term verdict. The start-of-trace gate + end-of-trace audit is a before/after enforcement pair; neither alone satisfies C-10's "verification that none appear in the output" requirement.

```
You are running /flow:conversation for topic "{topic}".

Read: simulations/flow/conversation/{topic}-conversation-{date}.md if it exists.
Read: any signal artifacts in simulations/ relevant to "{topic}".

Role: Copilot Studio Domain Expert.

---

Copilot Studio topology vocabulary -- the only permitted vocabulary in this output:
  Topics               -- named conversation flows within the agent
  Trigger phrases      -- registered phrases that activate a topic when matched
  Conditions           -- logical branch nodes within a topic
  Fallback topics      -- topics that activate when no trigger phrase matches
  Escalation           -- node that routes from the agent to a human agent queue
  Session variables    -- named values stored during the conversation (topic-scoped or global)
  Topic redirects      -- nodes that transfer conversation flow to another topic
  Actions              -- nodes that call external flows, APIs, or connectors
  Generative answers   -- AI-generated responses sourced from a configured knowledge source
  Knowledge sources    -- SharePoint libraries, Dataverse tables, or uploaded files
  End of conversation  -- terminal node type that closes the session

PROHIBITED TERMS -- none of these words may appear anywhere in this output.
A PROHIBITED TERM AUDIT section at the end of this output will scan for each term.

  intent | dialog | slot | NLU | utterance (use "user input" or "trigger phrase") |
  chatbot (use "agent") | handoff (use "escalation") | context (use "session variables") |
  fallback intent (use "fallback topic") | bot (use "agent")

---

## VOCABULARY GATE

[Complete before simulation. Map the agent to Copilot Studio topology.]

Agent name: [Name or description]
Topics in graph: [List all topic names]
Trigger phrases (2-3 per topic):
  [Topic 1]: "[phrase]", "[phrase]"
  [Topic 2]: "[phrase]", "[phrase]"
Fallback topic: [Topic name / "System Fallback Topic" / "not configured"]
Escalation path: [Topic name containing escalation node, or "not configured"]
Session variables:
  [VarName]: scope=[topic-scoped / global], type=[Text/Number/Boolean]
Knowledge sources:
  [Name]: type=[SharePoint / Dataverse / file upload], content=[brief description]
  [or "none configured"]

VOCABULARY GATE confirmed. Copilot Studio topology mapped. Proceeding with permitted vocabulary only.

---

## CONVERSATION TRACE

Scenario: [User goal for this turn sequence]

Turn [N]:
  User input: "[what the user typed or said]"
  Trigger phrase matched: "[exact phrase]" in topic "[Topic name]"
  Topic activated: [Topic name] (confidence: [X.XX]) | Runner-up: "[Topic name]" ([X.XX])
  Node path: [chain of node types in execution order: Trigger phrase node > Message node >
    Question node > Condition node > Action node > Redirect node > End of conversation node]
  Action node (if any): [Action name] -> result: [return value] / "none"
  Condition evaluated (if any): [expression] -> branch taken: [label]
  Session variables after this turn:
    [VarName] = [value] (scope: topic-scoped / global, changed: yes/no)
    [VarName] = awaiting input (scope: ...)
    [VarName] = [carried from Turn N-1]
  Agent response: "[exact text shown to user]"

[Continue for each turn. Each turn block is mandatory. Do not collapse or skip turns.]

---

## DEFECT ANALYSIS

**Dead ends** -- topic's node path terminates with no redirect node, escalation node, or fallback topic configured:
Verdict: FOUND / CONFIRMED ABSENT
[FOUND: topic name, terminal node type, what the user experiences -- session hangs, generic error, silent exit.]
[CONFIRMED ABSENT: "All [N] topics traced exit via redirect node to [names], escalation node, or fallback topic. No topic terminates without a valid exit path."]

**Infinite loops** -- topic redirect node targets a topic that redirects back to the originating topic:
Verdict: FOUND / CONFIRMED ABSENT
[FOUND: full redirect path (Topic A redirect node -> Topic B redirect node -> Topic A) and triggering condition.]
[CONFIRMED ABSENT: "Redirect graph across [N] topics is acyclic. Redirect map: [A->B(terminal)], [C->D(terminal)]. No cycle detected."]

**Trigger phrase collisions** -- two or more topics register trigger phrases producing ambiguous confidence scores for the same user input:
Verdict: FOUND / CONFIRMED ABSENT
[FOUND: the user input, competing topics, confidence scores.
  Disambiguation strategy: [Entity enrichment -- add question node before topic activation to distinguish /
    Condition ordering -- add session variable condition to gate topic activation /
    Trigger phrase refactor -- remove overlapping phrases, replace with distinct ones]
  Rationale: [Why this resolves the collision in Copilot Studio's matching model.]
[CONFIRMED ABSENT: "All user inputs tested resolved to a single topic above 0.7 confidence with runner-up below 0.4."]

**Missing fallbacks** -- condition node defines specific branches but has no default/else branch:
Verdict: FOUND / CONFIRMED ABSENT
[FOUND: topic name, condition expression, the unhandled branch.]
[CONFIRMED ABSENT: "All condition nodes in [N] topics carry a default branch or redirect to fallback topic. Default branches confirmed: [list topics]."]

---

## FALLBACK CHAIN TRACE

[Trace one complete fallback path from unrecognized input to terminal state.
Walk every node. Do not stop at the first fallback topic activation.]

User input: "[phrase that matches no trigger phrase above confidence threshold]"
Step 1: Trigger phrase matching: [N] topics evaluated, 0 match above threshold
         -> System routes to: [Fallback topic / System Fallback Topic]
Step 2: [First node in fallback topic] -- [what it does]
Step 3: [Next node -- question node / generative answers / escalation offer / condition node]
...
Step N: Terminal state:
  [Escalation node activates -> human agent session opened /
   End of conversation node -> session closes with "[closing message]" /
   Redirect node -> returns to topic "[Topic name]"]

Fallback chain quality: COMPLETE (reaches terminal state) / LOOPS (redirect cycle, never terminates) / TRUNCATED (reaches generic error with no path forward)

---

## FINDINGS

P1 [session-breaking]: [Topic name], [node type], [what fails and what the user experiences]
P2 [significant degradation]: [Topic name], [node type], [what degrades]
P3 [minor]: [Topic name], [potential improvement]

## AMENDMENTS

[Name the topic and node type for every P1 and P2 finding. Reproduction steps required.]

1. Topic "[Topic name]", [node type]: [Specific Copilot Studio change --
   e.g., "add a redirect node after Question node targeting '[Fallback topic]'" /
   "add a default branch to Condition node on [expression]" /
   "refactor trigger phrases: remove '[phrase]' from '[Topic A]', add distinct phrase"]
   Trigger phrase sequence: "[phrase 1]" -> "[phrase 2]" -> [observable failure at this step]
   Observable failure: [What the user sees or experiences]

2. [Amendment]
   Trigger phrase sequence: [sequence] -> [failure]
   Observable failure: [What the user sees]

---

## PROHIBITED TERM AUDIT

[Scan the VOCABULARY GATE, CONVERSATION TRACE, DEFECT ANALYSIS, FALLBACK CHAIN TRACE,
FINDINGS, and AMENDMENTS sections above for each prohibited term.
Record CLEAN or FOUND for each. If FOUND, quote the exact line and name the required replacement.
This audit covers the full output -- not just the trace section.]

| Prohibited term | Status | Line (if FOUND) | Required replacement |
|-----------------|--------|-----------------|----------------------|
| intent          | CLEAN / FOUND | [quote or "—"] | "trigger phrase" or "topic activation" |
| dialog          | CLEAN / FOUND | [quote or "—"] | "conversation" or "topic sequence" |
| slot            | CLEAN / FOUND | [quote or "—"] | "session variable" or "question node input" |
| NLU             | CLEAN / FOUND | [quote or "—"] | "trigger phrase matching" |
| utterance       | CLEAN / FOUND | [quote or "—"] | "user input" or "trigger phrase" |
| chatbot         | CLEAN / FOUND | [quote or "—"] | "agent" |
| handoff         | CLEAN / FOUND | [quote or "—"] | "escalation" |
| context         | CLEAN / FOUND | [quote or "—"] | "session variables" |
| fallback intent | CLEAN / FOUND | [quote or "—"] | "fallback topic" |
| bot             | CLEAN / FOUND | [quote or "—"] | "agent" |

PROHIBITED TERM AUDIT result: CLEAN (all 10 terms absent from output) / VIOLATIONS FOUND ([N] terms require replacement -- see table)

---

Write artifact: simulations/flow/conversation/{topic}-conversation-{date}.md
Frontmatter: skill, topic, date, agent_name, topic_count, turns_simulated, defects_found (list),
fallback_quality, vocabulary_clean (CLEAN / VIOLATIONS FOUND [N]).
```

---

## V-02: Lifecycle Emphasis -- Per-turn Topology Spec Conformance

**Axis:** Lifecycle emphasis -- pre-states a topology spec (CS-SPEC-01 through CS-SPEC-07) before any simulation begins, then makes SPEC_CONFORMANCE a required gate field in every turn block. Each turn's verdict must reference the CS-SPEC property by number.

**Hypothesis:** C-11 requires CONFORMS/DEVIATES "against the expected topology spec," not against designer intent. R1 V-04/V-05's `MATCHES INTENT / DEVIATES` is a different signal -- it compares implementation to the Conversation Designer's intended flow. C-11 asks whether each turn follows the Copilot Studio topology rules (session variable scoping, confidence threshold behavior, condition node completeness). By pre-printing the spec properties as named clauses before the trace, the model has a concrete reference to cite in each SPEC_CONFORMANCE verdict. A verdict that says "DEVIATES: violates CS-SPEC-02 (topic-scoped variable carried past topic boundary)" is qualitatively more precise than "DEVIATES: not what the designer intended."

```
You are running /flow:conversation for topic "{topic}".

Read: simulations/flow/conversation/{topic}-conversation-{date}.md if it exists.
Read: any signal artifacts in simulations/ relevant to "{topic}".

Role: Copilot Studio Domain Expert.
Use Copilot Studio vocabulary: Topics, Trigger phrases, Conditions, Fallback topics, Escalation,
Session variables, Topic redirects, Actions, Generative answers, Knowledge sources, End of conversation.
Do not use: intent, dialog, slot, NLU, chatbot, handoff, context.

---

## TOPOLOGY SPEC

[These seven properties define correct Copilot Studio behavior.
Each turn's SPEC_CONFORMANCE verdict must reference the CS-SPEC property number if DEVIATES.]

CS-SPEC-01: Trigger phrase matching activates the highest-confidence topic above the matching threshold.
  If runner-up is within 0.2 confidence of the top match, the agent may prompt for clarification
  before activating. A topic activated with confidence below the threshold is a violation.

CS-SPEC-02: Session variables declared as topic-scoped are cleared when the topic ends (redirect node
  fires or End of conversation node executes). Topic-scoped variables must not persist across topic
  boundaries. Session variables declared as global persist for the session duration.

CS-SPEC-03: Condition nodes must evaluate all possible branch outcomes. A condition node that defines
  specific branches but lacks a default/else branch leaves unhandled cases that route silently to the
  fallback topic or produce no response. Every condition node requires a default branch or explicit
  fallback topic redirect.

CS-SPEC-04: Redirect nodes transfer conversation control to the target topic and do not carry
  topic-scoped variables from the source topic. Only global variables survive topic transitions.

CS-SPEC-05: End of conversation nodes terminate the session. No further user input is processed
  after this node executes. The session cannot be resumed.

CS-SPEC-06: Escalation nodes route to a human agent queue. The agent session remains open but the
  Copilot Studio agent stops responding. The human agent takes over the session.

CS-SPEC-07: The System Fallback Topic (or a configured custom fallback topic) activates when no
  trigger phrase in any topic exceeds the confidence threshold. The fallback topic handles
  unrecognized input. If no fallback topic is configured, the agent produces no response.

---

## AGENT PROFILE

Agent name: [Name or description]
Topics in graph: [N] -- [list all topic names]
Trigger phrases (2-3 per topic):
  [Topic name]: "[phrase]", "[phrase]"
Fallback topic: [Topic name / "System Fallback Topic" / "not configured"]
Escalation path: [Topic containing escalation node, or "not configured"]
Session variables:
  [VarName]: scope=[topic-scoped / global], type=[Text/Number/Boolean]
Knowledge sources: [Name, type, content / "none configured"]
Scenario: [User goal for this turn sequence]
Turn count: [N total turns]

---

## CONVERSATION TRACE

[Walk each turn in sequence. Fill in all fields for every turn.
SPEC_CONFORMANCE is a required field. Do not advance to the next turn without completing it.
If DEVIATES, name the CS-SPEC number violated and describe the violation precisely.]

### Turn [N] of [TOTAL]

User input: "[what the user typed or said]"
Topic activated: [Topic name]
  Trigger phrase matched: "[exact phrase]" (confidence: [X.XX])
  Runner-up topic: "[Topic name]" ([X.XX])
Node path: [Trigger phrase node] -> [Message node / Question node / Condition node /
  Action node / Redirect node / End of conversation node]
Action node (if any): [Action name] -> result: [return value or status] / "none"
Condition evaluated (if any): [expression] -> branch taken: [label] / default branch
Session variables after this turn:
  [VarName] = [value] (scope: topic-scoped / global, changed this turn: yes/no)
  [VarName] = awaiting input (scope: ...)
  [VarName] = [carried from Turn N-1]
  [VarName] = cleared (topic-scoped, topic ended this turn)
Agent response: "[exact text shown to user]"
SPEC_CONFORMANCE: CONFORMS / DEVIATES
  [CONFORMS: "Turn follows CS-SPEC-01 through CS-SPEC-07. Trigger phrase matching above threshold.
   Session variables handled per scope rules. Node sequencing valid."]
  [DEVIATES: "Violates CS-SPEC-[N]: [describe the specific violation --
    e.g., CS-SPEC-02: topic-scoped variable [VarName] carried past topic boundary when redirect
    node fired to [Topic name]; variable should have been cleared." /
    CS-SPEC-03: Condition node on [expression] has no default branch; unhandled case routes
    silently to System Fallback Topic instead of showing an agent response."]

### Turn [N+1] of [TOTAL]
[Same structure. SPEC_CONFORMANCE required. Do not skip it.]

[Continue for all turns.]

TRACE GATE: All [N] turns completed. SPEC_CONFORMANCE verdict present on every turn.
Session variables tracked and scoped correctly across all transitions.

---

## DEFECT ANALYSIS

**Dead ends**:
Verdict: FOUND / CONFIRMED ABSENT
[FOUND: topic name, terminal node type, user experience.]
[CONFIRMED ABSENT: "All [N] topics traced exit via redirect node, escalation node, or fallback topic.
  Exits confirmed: [list]. No topic terminates without a valid exit path."]

**Infinite loops**:
Verdict: FOUND / CONFIRMED ABSENT
[FOUND: full redirect path and triggering condition.]
[CONFIRMED ABSENT: "Redirect graph across [N] topics is acyclic. Redirect map: [A->B (terminal)],
  [C->D (terminal)]. No cycle detected."]

**Trigger phrase collisions**:
Verdict: FOUND / CONFIRMED ABSENT
[FOUND: user input, competing topics, confidence scores.
  Disambiguation strategy: [Entity enrichment / Condition ordering / Trigger phrase refactor]
  Rationale: [Why this resolves it in Copilot Studio's matching model.]]
[CONFIRMED ABSENT: "All user inputs tested resolved to a single topic above 0.7 confidence with
  runner-up below 0.4. No overlapping trigger phrases detected."]

**Missing fallbacks**:
Verdict: FOUND / CONFIRMED ABSENT
[FOUND: topic name, condition expression, unhandled branch. Note: this defect corresponds to a
  CS-SPEC-03 violation and should be cross-referenced with any DEVIATES turn above.]
[CONFIRMED ABSENT: "All condition nodes in [N] topics carry a default branch or explicit redirect
  to fallback topic. Default branches confirmed: [list topics and their default branch targets]."]

DEFECT GATE: All four classes have verdict + evidence.

---

## SPEC CONFORMANCE SUMMARY

[Drawn from DEVIATES turns in the trace. One row per DEVIATES verdict.]

| Turn | CS-SPEC violated | Violation | Linked defect class |
|------|------------------|-----------|---------------------|
| [N] | CS-SPEC-[N] | [Description of the violation] | [dead end / loop / collision / missing fallback / "no defect class — topology error only"] |

[Write "No topology spec deviations. All [N] turns CONFORMS." if all turns passed.]

---

## FALLBACK CHAIN TRACE

[Walk one complete fallback path from unrecognized input to terminal state.
Use CS-SPEC-07 as the reference for correct fallback activation behavior.]

User input: "[phrase that matches no trigger phrase above threshold]"
Step 1: Trigger phrase matching: [N] topics evaluated, 0 match above threshold
         -> CS-SPEC-07 activates: routes to [Fallback topic / System Fallback Topic]
Step 2: [First node in fallback topic] -- [what it does]
Step 3: [Next node]
...
Step N: Terminal state: [escalation / end of conversation / redirect to root topic]

Fallback chain quality: COMPLETE / LOOPS / TRUNCATED

---

## FINDINGS

P1 [session-breaking]: [Topic name], [node type], [what fails]
P2 [significant degradation]: [Topic name], [node type], [what degrades]
P3 [minor]: [Topic, improvement opportunity]

## AMENDMENTS

1. Topic "[Topic name]", [node type]: [Specific Copilot Studio change]
   Trigger phrase sequence: "[phrase 1]" -> "[phrase 2]" -> [observable failure at this step]
   Observable failure: [What the user sees or experiences]

2. [Amendment]
   Trigger phrase sequence: [sequence] -> [failure]
   Observable failure: [What the user sees]

---

Write artifact: simulations/flow/conversation/{topic}-conversation-{date}.md
Frontmatter: skill, topic, date, agent_name, topic_count, turns_simulated, defects_found (list),
fallback_quality, turns_spec_conformant ([N] CONFORMS of [TOTAL] total), spec_deviations (count).
```

---

## V-03: Role Sequence -- Copilot Studio Developer + Compliance Auditor

**Axes:** Role sequence (Compliance Auditor runs after Developer trace) + output format (two-phase output with compliance annotations as a second pass)

**Hypothesis:** Separating simulation from compliance auditing solves two problems simultaneously. First, during the Developer trace, the role is not interrupted by per-turn compliance checks — the Developer focuses on accurate simulation. Second, the Compliance Auditor reads the completed Developer output as a reader, not a writer, which is a stronger scan mode for prohibited term detection. The Auditor annotates each turn with its SPEC_CONFORMANCE verdict after the fact, drawing from a stated topology spec. This two-pass architecture means the Developer doesn't need to hold the prohibited terms list or the spec property numbers in working context while simulating — those concerns are cleanly delegated to the Auditor role. The expected gain: cleaner Developer output (fewer vocabulary violations, because the role isn't switching between simulation and compliance) and more rigorous Auditor findings (because the Auditor is reading finished text, not producing it).

```
You are running /flow:conversation for topic "{topic}".

Read: simulations/flow/conversation/{topic}-conversation-{date}.md if it exists.
Read: any signal artifacts in simulations/ relevant to "{topic}".

Two roles execute in sequence. Complete Phase 1 fully before Phase 2 begins.

---

# PHASE 1: COPILOT STUDIO DEVELOPER

[Copilot Studio Developer speaks. Simulate the conversation using Copilot Studio vocabulary.
Focus on accurate simulation: topic matching, node paths, session variable tracking, fallback chains.
Compliance verification is performed by the Compliance Auditor in Phase 2.]

## DEVELOPER: AGENT PROFILE

Agent name: [Name or description]
Topics in graph: [N] -- [list all topic names]
Trigger phrases (2-3 per topic):
  [Topic name 1]: "[phrase]", "[phrase]"
  [Topic name 2]: "[phrase]", "[phrase]"
Fallback topic: [Topic name / "System Fallback Topic" / "not configured"]
Escalation path: [Topic name containing escalation node, or "not configured"]
Session variables:
  [VarName]: scope=[topic-scoped / global], type=[Text/Number/Boolean]
Knowledge sources: [Name, type, content / "none configured"]
Scenario: [User goal for this turn sequence]
Turn count: [N total turns]

## DEVELOPER: CONVERSATION TRACE

Turn [N] of [TOTAL]:
  User input: "[what the user typed or said]"
  Trigger phrase matched: "[exact phrase]" in topic "[Topic name]"
  Topic activated: [Topic name] (confidence: [X.XX]) | Runner-up: "[Topic name]" ([X.XX])
  Node path: [Trigger phrase node] -> [Message / Question / Condition / Action / Redirect /
    End of conversation node]
  Action node (if any): [Action name] -> result: [return value] / "none"
  Condition evaluated (if any): [expression] -> branch: [label] / default branch
  Session variables after this turn:
    [VarName] = [value] (scope: topic-scoped / global, changed: yes/no)
    [VarName] = awaiting input
    [VarName] = [carried from Turn N-1]
  Agent response: "[exact text shown to user]"

[Repeat for every turn. Each turn block is mandatory.]

## DEVELOPER: DEFECT ANALYSIS

**Dead ends**:
Verdict: FOUND / CONFIRMED ABSENT
[Evidence or scope statement.]

**Infinite loops**:
Verdict: FOUND / CONFIRMED ABSENT
[Evidence or scope statement.]

**Trigger phrase collisions**:
Verdict: FOUND / CONFIRMED ABSENT
[Evidence. If FOUND: disambiguation strategy (entity enrichment / condition ordering / trigger phrase refactor) + rationale.]

**Missing fallbacks**:
Verdict: FOUND / CONFIRMED ABSENT
[Evidence or scope statement.]

## DEVELOPER: FALLBACK CHAIN TRACE

User input: "[phrase that matches no trigger phrase above threshold]"
Step 1: 0 topics match -> routes to [Fallback topic / System Fallback Topic]
Step 2: [First node] -- [what it does]
...
Step N: Terminal state: [escalation / end of conversation / redirect to root]

Fallback chain quality: COMPLETE / LOOPS / TRUNCATED

## DEVELOPER: FINDINGS AND AMENDMENTS

P1 [session-breaking]: [Topic name], [node type], [what breaks]
P2 [significant degradation]: [Topic name], [node type], [what degrades]
P3 [minor]: [Topic, improvement opportunity]

Amendments:
1. Topic "[Topic name]", [node type]: [Specific Copilot Studio change]
   Trigger phrase sequence: "[phrase 1]" -> "[phrase 2]" -> [observable failure]
   Observable failure: [What the user sees]

2. [Amendment]
   Trigger phrase sequence: [sequence] -> [failure]
   Observable failure: [What the user sees]

---

# PHASE 2: VOCABULARY AND SPEC COMPLIANCE AUDITOR

[Compliance Auditor speaks. Read the Developer output above and perform two compliance checks.
Do not re-simulate. Operate entirely from the Developer's completed output.]

## AUDITOR: TOPOLOGY SPEC REFERENCE

[The Auditor applies these conformance criteria to each turn in the Developer trace.]

CS-SPEC-01: Topic activation uses confidence-threshold matching. Topic-scoped trigger phrase activation
  below threshold is a violation.
CS-SPEC-02: Topic-scoped session variables are cleared when the topic ends. Carrying topic-scoped
  variables across a redirect node or End of conversation node is a violation.
CS-SPEC-03: Condition nodes must have a default branch. A condition node without a default branch
  that handles unmatched cases is a violation.
CS-SPEC-04: Redirect nodes do not carry topic-scoped variables to the target topic. Only global
  variables survive topic transitions.
CS-SPEC-05: End of conversation nodes terminate the session. No further input is processed after
  this node executes.
CS-SPEC-06: Escalation nodes open a human agent session. The Copilot Studio agent stops responding.
CS-SPEC-07: System Fallback Topic (or custom fallback topic) activates when no trigger phrase
  matches above threshold. No configured fallback topic means no response to unrecognized input.

## AUDITOR: PER-TURN SPEC CONFORMANCE ANNOTATIONS

[For every turn in the Developer trace, assign a SPEC_CONFORMANCE verdict.
Reference the turn number and cite the CS-SPEC property if DEVIATES.
Annotate all turns. Do not skip any.]

Turn [N]:
  SPEC_CONFORMANCE: CONFORMS / DEVIATES
  [CONFORMS: "Session variable scoping, trigger phrase matching, and node sequencing are consistent
    with CS-SPEC-01 through CS-SPEC-07."]
  [DEVIATES: "Violates CS-SPEC-[N]: [exact description of the violation found in the Developer output]"]

Turn [N+1]:
  SPEC_CONFORMANCE: CONFORMS / DEVIATES
  [...]

[Continue for all turns.]

Spec conformance summary: [N] CONFORMS, [N] DEVIATES of [TOTAL] turns.
DEVIATES turns: [list turn numbers] / "none"

## AUDITOR: PROHIBITED TERM AUDIT

[Scan the entire Developer output (AGENT PROFILE, CONVERSATION TRACE, DEFECT ANALYSIS,
FALLBACK CHAIN TRACE, FINDINGS, AMENDMENTS) for each prohibited term.
Record CLEAN or FOUND. If FOUND, quote the line and name the required replacement.]

Prohibited terms checked:
  intent | dialog | slot | NLU | utterance | chatbot | handoff | context | fallback intent | bot

| Term | Status | Location (if FOUND) | Required replacement |
|------|--------|---------------------|----------------------|
| intent | CLEAN / FOUND | [quote / "—"] | "trigger phrase" or "topic activation" |
| dialog | CLEAN / FOUND | [quote / "—"] | "conversation" or "topic sequence" |
| slot | CLEAN / FOUND | [quote / "—"] | "session variable" or "question node input" |
| NLU | CLEAN / FOUND | [quote / "—"] | "trigger phrase matching" |
| utterance | CLEAN / FOUND | [quote / "—"] | "user input" or "trigger phrase" |
| chatbot | CLEAN / FOUND | [quote / "—"] | "agent" |
| handoff | CLEAN / FOUND | [quote / "—"] | "escalation" |
| context | CLEAN / FOUND | [quote / "—"] | "session variables" |
| fallback intent | CLEAN / FOUND | [quote / "—"] | "fallback topic" |
| bot | CLEAN / FOUND | [quote / "—"] | "agent" |

Vocabulary audit result: CLEAN ([N] terms scanned, 0 violations) /
  VIOLATIONS FOUND ([N] terms found, replacement required before artifact is published)

---

Write artifact: simulations/flow/conversation/{topic}-conversation-{date}.md
Frontmatter: skill, topic, date, agent_name, topic_count, turns_simulated, defects_found (list),
fallback_quality, turns_spec_conformant ([N] CONFORMS of [TOTAL]),
spec_deviations (count), vocabulary_clean (CLEAN / VIOLATIONS [N]).
```

---

## V-04: Phrasing Register -- Machine-readable Typed Assertion Fields

**Axis:** Phrasing register -- formal/technical, machine-readable. All verdicts expressed as typed enum fields with constrained values. Per-turn blocks include `SPEC_CONFORMANCE: CONFORMS | DEVIATES[CS-SPEC-N: description]` and `PROHIBITED_TERM_SCAN: CLEAN | FOUND[term: line]`. Post-trace summary uses a structured audit table.

**Hypothesis:** When verdicts are constrained enum values rather than prose instructions, two improvements occur. First, consistency: the model cannot produce "largely conforms" or "mostly clean" when the field accepts only CONFORMS or DEVIATES. Second, parseability: the frontmatter and typed verdict fields make the artifact machine-readable for downstream scoring. The PROHIBITED_TERM_SCAN field catches violations at the point of occurrence (in the turn where the violation happened) rather than requiring a post-trace scan that may miss inline violations. The combined effect is that C-10 is enforced both per-turn (catching violations in the trace itself) and post-trace (auditing the full output), while C-11 verdicts are precise typed assertions rather than narrative judgments.

```
You are running /flow:conversation for topic "{topic}".

Read: simulations/flow/conversation/{topic}-conversation-{date}.md if it exists.
Read: any signal artifacts in simulations/ relevant to "{topic}".

Role: Copilot Studio Domain Expert.

Output format: typed assertion fields throughout. All verdicts are constrained enum values.
  Do not use prose where a typed field is provided. Fill every bracket.

---

## VOCABULARY_REGISTRY

[Pre-map the Copilot Studio topology terms used in this output.
This registry is the permitted vocabulary for all sections below.]

TERM[topics]: named conversation flows within the agent
TERM[trigger_phrases]: registered phrases that activate a topic when matched
TERM[conditions]: logical branch nodes within a topic
TERM[fallback_topic]: topic that activates when no trigger phrase matches
TERM[escalation]: node that routes from the agent to a human agent queue
TERM[session_variables]: named values stored during the conversation (topic-scoped or global)
TERM[topic_redirect]: node that transfers conversation flow to another topic
TERM[action_node]: node that calls an external flow, API, or connector
TERM[generative_answers]: AI-generated responses from a configured knowledge source
TERM[knowledge_source]: SharePoint library, Dataverse table, or uploaded file
TERM[end_of_conversation]: terminal node type that closes the session

PROHIBITED_TERM_LIST:
  [1] intent           -> use: "trigger phrase" or "topic activation"
  [2] dialog           -> use: "conversation" or "topic sequence"
  [3] slot             -> use: "session variable" or "question node input"
  [4] NLU              -> use: "trigger phrase matching"
  [5] utterance        -> use: "user input" or "trigger phrase"
  [6] chatbot          -> use: "agent"
  [7] handoff          -> use: "escalation"
  [8] context          -> use: "session variables"
  [9] fallback_intent  -> use: "fallback topic"
  [10] bot             -> use: "agent"

TOPOLOGY_SPEC:
  CS-SPEC-01: topic activation by confidence-threshold trigger phrase matching
  CS-SPEC-02: topic-scoped session variables cleared at topic boundary
  CS-SPEC-03: condition nodes require default/else branch
  CS-SPEC-04: redirect nodes do not carry topic-scoped variables
  CS-SPEC-05: end of conversation node terminates session
  CS-SPEC-06: escalation node routes to human agent; agent stops responding
  CS-SPEC-07: fallback topic activates when no trigger phrase exceeds threshold

---

## AGENT_PROFILE

AGENT_NAME: [Name or description]
TOPIC_COUNT: [N]
TOPICS: [[Topic 1], [Topic 2], [Topic 3], ...]
TRIGGER_PHRASES:
  [Topic 1]: ["[phrase]", "[phrase]"]
  [Topic 2]: ["[phrase]", "[phrase]"]
FALLBACK_TOPIC: [Topic name / "System Fallback Topic" / "not configured"]
ESCALATION_PATH: [Topic name / "not configured"]
SESSION_VARIABLES:
  [VarName]: {scope: "topic-scoped" | "global", type: "Text" | "Number" | "Boolean"}
KNOWLEDGE_SOURCES:
  [Name]: {type: "SharePoint" | "Dataverse" | "file", content: "[brief description]"}
  [or NONE]
SCENARIO: [User goal for this turn sequence]
TURN_COUNT: [N]

---

## CONVERSATION_TRACE

[Complete all fields for every turn. SPEC_CONFORMANCE and PROHIBITED_TERM_SCAN are required.]

### TURN[N] of TURN[TOTAL]

USER_INPUT: "[what the user typed or said]"
TOPIC_ACTIVATED: [Topic name]
TRIGGER_PHRASE_MATCHED: "[exact phrase]"
CONFIDENCE: [X.XX]
RUNNER_UP_TOPIC: "[Topic name]" ([X.XX])
NODE_PATH: [Trigger phrase node > Message node | Question node | Condition node | Action node | Redirect node | End of conversation node]
ACTION_NODE: [Action name, result: [value]] | NONE
CONDITION_EVALUATED: [expression -> branch: [label]] | NONE
SESSION_VARIABLES_DELTA:
  [VarName]: {value: [value], scope: "topic-scoped" | "global", changed: true | false}
  [VarName]: {value: "awaiting_input", scope: "..."}
  [VarName]: {value: [value], scope: "...", carried_from: "Turn [N-1]"}
  [VarName]: {value: "cleared", scope: "topic-scoped", reason: "topic ended this turn"}
AGENT_RESPONSE: "[exact text shown to user]"
SPEC_CONFORMANCE: CONFORMS | DEVIATES[CS-SPEC-[N]: [description of violation]]
PROHIBITED_TERM_SCAN: CLEAN | FOUND[[term]: "[exact line where term appears]"]

### TURN[N+1] of TURN[TOTAL]
[Same structure. SPEC_CONFORMANCE and PROHIBITED_TERM_SCAN required. Do not omit.]

[Continue for all turns.]

---

## DEFECT_MATRIX

[All four rows required. Verdict: FOUND | CONFIRMED_ABSENT. No other value.]

| DEFECT_CLASS | VERDICT | EVIDENCE |
|--------------|---------|----------|
| dead_ends | FOUND \| CONFIRMED_ABSENT | [FOUND: {turn: N, topic: "[name]", terminal_node: "[type]", user_experience: "[description]"}. CONFIRMED_ABSENT: "All [N] topic exits route to redirect node, escalation node, or fallback topic. Exits: [list]."] |
| infinite_loops | FOUND \| CONFIRMED_ABSENT | [FOUND: {path: "[A redirect -> B redirect -> A]", trigger: "[condition or trigger phrase]"}. CONFIRMED_ABSENT: "Redirect graph acyclic across [N] redirects. Map: [A->B(terminal)], [C->D(terminal)]."] |
| trigger_phrase_collisions | FOUND \| CONFIRMED_ABSENT | [FOUND: {user_input: "[phrase]", competing_topics: ["[A]([X.XX])", "[B]([X.XX])"], disambiguation_strategy: "entity_enrichment" \| "condition_ordering" \| "trigger_phrase_refactor", rationale: "[why this resolves it in CS]"}. CONFIRMED_ABSENT: "All [N] trigger phrases tested resolve to single topic >0.7 confidence, runner-up <0.4."] |
| missing_fallbacks | FOUND \| CONFIRMED_ABSENT | [FOUND: {topic: "[name]", condition_expression: "[expr]", unhandled_branch: "[description]"}. CONFIRMED_ABSENT: "All condition nodes in [N] topics carry default branch or fallback topic redirect. Default branches: [list]."] |

---

## FALLBACK_CHAIN_TRACE

UNRECOGNIZED_INPUT: "[phrase that matches no trigger phrase above threshold]"
STEP[1]: {action: "trigger phrase matching", topics_evaluated: [N], matches_above_threshold: 0, routes_to: "[Fallback topic / System Fallback Topic]"}
STEP[2]: {node: "[first node type]", behavior: "[what it does]"}
STEP[3]: {node: "[next node]", behavior: "[behavior]"}
...
STEP[N]: {terminal_state: "escalation" | "end_of_conversation" | "redirect_to_root", detail: "[closing message or target topic]"}

FALLBACK_CHAIN_QUALITY: COMPLETE | LOOPS | TRUNCATED

---

## VOCABULARY_AUDIT

[Post-trace scan of the full output. One row per prohibited term.
Covers AGENT_PROFILE, CONVERSATION_TRACE, DEFECT_MATRIX, FALLBACK_CHAIN_TRACE.]

| TERM_ID | TERM | STATUS | OCCURRENCE (if FOUND) |
|---------|------|--------|-----------------------|
| [1] | intent | CLEAN \| FOUND | [quote or "—"] |
| [2] | dialog | CLEAN \| FOUND | [quote or "—"] |
| [3] | slot | CLEAN \| FOUND | [quote or "—"] |
| [4] | NLU | CLEAN \| FOUND | [quote or "—"] |
| [5] | utterance | CLEAN \| FOUND | [quote or "—"] |
| [6] | chatbot | CLEAN \| FOUND | [quote or "—"] |
| [7] | handoff | CLEAN \| FOUND | [quote or "—"] |
| [8] | context | CLEAN \| FOUND | [quote or "—"] |
| [9] | fallback_intent | CLEAN \| FOUND | [quote or "—"] |
| [10] | bot | CLEAN \| FOUND | [quote or "—"] |

VOCABULARY_AUDIT_RESULT: CLEAN | VIOLATIONS_FOUND[N]

---

## FINDINGS

P1: [session-breaking] {topic: "[name]", node: "[type]", failure: "[description]", user_experience: "[description]"}
P2: [significant degradation] {topic: "[name]", node: "[type]", degradation: "[description]"}
P3: [minor] {topic: "[name]", improvement: "[description]"}

## AMENDMENTS

1. {topic: "[name]", node_type: "[type]", change: "[Specific Copilot Studio change]"}
   REPRODUCTION: {trigger_phrase_sequence: ["[phrase 1]", "[phrase 2]"], failure_point: "[where it breaks]"}
   OBSERVABLE_FAILURE: "[What the user sees or experiences]"

2. {topic: "[name]", node_type: "[type]", change: "[change]"}
   REPRODUCTION: {trigger_phrase_sequence: ["[phrase]"], failure_point: "[failure]"}
   OBSERVABLE_FAILURE: "[What the user sees]"

---

Write artifact: simulations/flow/conversation/{topic}-conversation-{date}.md
Frontmatter: skill, topic, date, agent_name, topic_count, turns_simulated,
turns_spec_conformant, spec_deviations, defects_found (list),
fallback_quality, vocabulary_audit_result.
```

---

## V-05: Full Synthesis -- R1 V-05 + C-10 Audit + C-11 Per-turn Verdict

**Axes:** All axes combined. Builds directly on R1 V-05 (which scored 100 under v1 rubric with 9/9 criteria) and adds the two new aspirational criteria as minimal structural additions. C-11 becomes a required field in every Phase 2 turn block. C-10 becomes a new Phase 7 (PROHIBITED TERM AUDIT) that verifies the completed output. Every other phase from R1 V-05 is preserved unchanged.

**Hypothesis:** R1 V-05's enforcement mechanisms for C-01 through C-09 are proven. The only score gap under v2 rubric is C-10 and C-11. C-10 was partially addressed in R1 V-05 (vocabulary gate + prohibited terms instruction) but lacked post-trace verification. C-11 was structurally absent -- R1 V-05's `MATCHES INTENT / DEVIATES` is design conformance, not topology spec conformance. The minimum change to achieve 100 under v2 is: (1) add SPEC_CONFORMANCE field to Phase 2 turn blocks referencing pre-stated topology spec properties, and (2) add Phase 7 as a post-trace prohibited term audit table. No existing phases are modified. This is the maximal coverage approach for v2.

```
You are running /flow:conversation for topic "{topic}".

Read: simulations/flow/conversation/{topic}-conversation-{date}.md if it exists.
Read: any signal artifacts in simulations/ relevant to "{topic}".

Roles execute in sequence: Conversation Designer (Phase 1), then Copilot Studio Developer (Phases 2-6),
then Compliance Auditor (Phase 7).
All phases are gates. Complete each phase fully before advancing.
Do not describe the topic graph abstractly -- walk it turn by turn in Phase 2.

Use Copilot Studio vocabulary exclusively throughout:
  Topics, Trigger phrases, Conditions, Fallback topics, Escalation, Session variables,
  Topic redirects, Actions, Generative answers, Knowledge sources, End of conversation nodes.
Do not use: intent, dialog, slot, NLU, chatbot, handoff, context.

---

## PHASE 1: SETUP + VOCABULARY GATE
[Conversation Designer speaks. Define agent topology, intended flow, and topology spec before any simulation begins.]

Agent name: [Name or description]
Topics in graph: [N] -- list all topic names
  [Topic name 1], [Topic name 2], [Topic name 3], ...
Trigger phrases (2-3 per topic):
  [Topic name 1]: "[phrase]", "[phrase]"
  [Topic name 2]: "[phrase]", "[phrase]"
  [or "inferred from description" if not provided]
Fallback topic: [Name / "System Fallback Topic" / "not configured"]
Escalation path: [Topic name containing escalation node, or "not configured"]
Session variables:
  [VarName]: scope=[topic-scoped / global], type=[Text/Number/Boolean], initial=[value or "unset"]
Knowledge sources:
  [Name]: type=[SharePoint / Dataverse table / file upload], content=[brief description]
  [or "none configured"]

Conversation Designer -- intended flow:
  User goal: [What the user is trying to accomplish]
  Intended topic sequence: [Topic A] -> [Topic B] -> [Topic C] -> [terminal: escalation / end / root]
  Intended turn count: [N]
  Intended fallback: [Designed behavior for off-script inputs]
  Anticipated design weaknesses: [Known gaps or "none identified"]

Coverage scope: [N] topics total in graph. This simulation will visit [N] topics ([N/total * 100]%).
Unvisited topics (acceptable gap or coverage concern?): [List or "none -- full coverage"]

Topology spec (for Phase 2 SPEC_CONFORMANCE verdicts):
  CS-SPEC-01: Trigger phrase matching activates topic above confidence threshold. Sub-threshold activation is a violation.
  CS-SPEC-02: Topic-scoped session variables cleared at topic boundary (redirect or end of conversation node). Cross-boundary carry is a violation.
  CS-SPEC-03: Condition nodes require a default branch. Missing default branch routes unhandled cases to fallback topic silently.
  CS-SPEC-04: Redirect nodes do not carry topic-scoped variables to the target topic.
  CS-SPEC-05: End of conversation nodes terminate the session. No further input is processed.
  CS-SPEC-06: Escalation nodes open human agent session; agent stops responding.
  CS-SPEC-07: Fallback topic activates when no trigger phrase exceeds threshold.

Prohibited terms (must not appear anywhere in Phases 2-6; verified in Phase 7):
  intent | dialog | slot | NLU | utterance (use "user input") | chatbot (use "agent") |
  handoff (use "escalation") | context (use "session variables") | fallback intent (use "fallback topic") | bot (use "agent")

SETUP GATE: Topic count confirmed. Turn sequence defined. Session variables enumerated. Coverage scope stated.
Topology spec stated. Prohibited terms listed. Advance to Phase 2.

## PHASE 2: CONVERSATION TRACE
[Copilot Studio Developer speaks. Walk every turn from the Phase 1 turn sequence.
No turns may be skipped or collapsed. Each turn requires its own block.
SPEC_CONFORMANCE is required on every turn -- reference the CS-SPEC number if DEVIATES.
Compare each turn to the Conversation Designer's intended flow (MATCHES INTENT / DEVIATES).]

Turn [N] of [TOTAL]:
  User: "[exact user input]"
  Trigger phrase matched: "[phrase]" in topic "[Topic name]"
  Confidence: [X.XX] | Runner-up topic: "[Topic name]" ([X.XX])
  Node path: [chain in execution order -- Trigger phrase node > Message node > Question node >
    Condition node > Action node > Redirect node > End of conversation node]
  Action node (if any): [Action name] -> result: [return value or status] / "none"
  Condition evaluated (if any): [expression] -> branch taken: [label] / default branch
  Session variables after this turn:
    [VarName] = [value] (scope: topic-scoped / global, changed: yes/no)
    [VarName] = awaiting_input (scope: ...)
    [VarName] = [carried unchanged from Turn N-1]
    [VarName] = cleared (topic-scoped, topic ended this turn)
  Response: "[agent response text shown to user]"
  SPEC_CONFORMANCE: CONFORMS / DEVIATES
    [CONFORMS: "Turn follows CS-SPEC-01 through CS-SPEC-07. Trigger phrase matching above threshold.
     Session variable scoping correct. Node sequencing valid."]
    [DEVIATES: "Violates CS-SPEC-[N]: [exact description of the violation]" -- severity: P1/P2/P3]
  Implementation vs. design: MATCHES INTENT / DEVIATES
    [If DEVIATES: describe what was intended (from Phase 1 Conversation Designer) vs. what happened.
     Severity: P1 / P2 / P3]

[Repeat for every turn. Each Turn block is mandatory. SPEC_CONFORMANCE required on every turn.]

TRACE GATE: All [N] turns completed. SPEC_CONFORMANCE present on every turn. Session state carried
across all transitions. All implementation deviations flagged. Advance to Phase 3.

## PHASE 3: DEFECT MATRIX
[Complete all four rows. FOUND or CONFIRMED ABSENT -- no other verdict is valid.
"CONFIRMED ABSENT" requires an explicit scope statement. If FOUND for trigger phrase collisions,
include a disambiguation strategy with rationale.]

| Defect class | Verdict | Evidence / Confirmation |
|--------------|---------|------------------------|
| Dead ends (topic exits with no valid next intent and no fallback topic redirect) | FOUND / CONFIRMED ABSENT | [FOUND: turn N, topic name, terminal node type, user experience. CONFIRMED ABSENT: "All [N] topic exits route to redirect node, escalation node, or fallback topic. Exit paths confirmed: [list]."] |
| Infinite loops (Topic A redirect node -> Topic B redirect node -> Topic A) | FOUND / CONFIRMED ABSENT | [FOUND: full loop path and triggering condition. CONFIRMED ABSENT: "Topic redirect graph is acyclic across [N] redirects traced. No cycle. Redirect map: [A->B (terminal)], [C->D (terminal)]."] |
| Trigger phrase collisions (trigger phrase in multiple topics produces ambiguous confidence scores) | FOUND / CONFIRMED ABSENT | [FOUND: the trigger phrase, competing topics, confidence scores. Disambiguation strategy: [entity enrichment -- add entity question node before topic activation / condition ordering -- add session variable condition before trigger matching / trigger phrase refactor -- remove overlapping phrases, replace with distinct ones] -- rationale: [why this resolves it in Copilot Studio's matching model]. CONFIRMED ABSENT: "All [N] trigger phrases tested resolve to single topic above 0.7, runner-up below 0.4."] |
| Missing fallbacks (condition node with no else/default branch) | FOUND / CONFIRMED ABSENT | [FOUND: topic name, condition expression, unhandled branch. Note: also a CS-SPEC-03 violation -- cross-reference Phase 2 SPEC_CONFORMANCE. CONFIRMED ABSENT: "All condition nodes in [N] topics carry default branch or fallback topic redirect. Default branches confirmed: [list topics]."] |

DEFECT GATE: All four classes have verdict + evidence. Advance to Phase 4.

## PHASE 4: FALLBACK CHAIN TRACE
[Walk one complete fallback path from unrecognized input to terminal state.
Every step is required. Do not stop at the first fallback topic activation.
Reference CS-SPEC-07 for correct fallback activation behavior.]

Unrecognized input: "[phrase that matches no trigger phrase list]"
Step 1: Trigger phrase matching: [N] topics evaluated, 0 match above confidence threshold
  -> CS-SPEC-07 activates: routes to [Fallback topic / System Fallback Topic]
Step 2: [Fallback topic first node type] -- [what it does]
Step 3: [Next node -- question node / generative answers / escalation offer / condition node]
...
Step N: Terminal state:
  [Escalation node activates -> human agent session opened /
   End of conversation node -> session closes with "[closing message]" /
   Redirect node -> returns user to topic "[Topic name]"]

Fallback chain quality: COMPLETE (reaches terminal state) / LOOPS (redirect cycle) / TRUNCATED (generic error, no path forward)

FALLBACK GATE: Fallback chain traced to terminal state. Quality verdict recorded. Advance to Phase 5.

## PHASE 5: ADVERSARIAL TURN INJECTION
[Inject one adversarial scenario: unexpected user input mid-flow, topic switch during session variable
collection, session variable loss, or session timeout. Walk the actual agent node path.]

Adversarial scenario type: [Topic switch mid-variable-collection / Unexpected off-topic input mid-flow / Session timeout clears session variables / Repeated same input triggering loop]
Injected at: Turn [N] of original scenario, before session variable [VarName] is collected
Adversarial input: "[the unexpected user input that breaks expected flow]"
Agent response (trace actual node path):
  -> Trigger phrase matching: [does a new topic activate, or does the current topic handle it?]
  -> Node path: [nodes executed in response to this adversarial input]
  -> Session variables: [VarName] = [carried / lost / reset] (scope: topic-scoped / global)
  -> Response shown to user: "[agent response]"
Outcome: [describe what the user experiences -- conversation recovers / loops / ends abruptly / loses session variables]
Assessment: GRACEFUL (agent handles deviation and continues) / BRITTLE (agent fails, loops, or gives confusing response) / SILENT FAILURE (agent produces no error but loses session state)

## PHASE 6: FINDINGS, COVERAGE, AND AMENDMENTS

Coverage report:
  Topics visited: [N] of [TOTAL] ([N/TOTAL * 100]%)
  Topics unvisited: [List, or "none -- full coverage achieved"]
  Trigger phrases exercised: [N] of approximately [estimated total] ([N/est * 100]%)
  Turns simulated: [N] (scenario) + 1 (adversarial) = [N+1] total
  Spec conformance: [N] CONFORMS, [N] DEVIATES of [N+1] total turns (including adversarial)

Findings [priority-ordered; reference topic names and node types]:
  P1 [session-breaking]: [Topic name], [node type], [what fails and user experience]
  P2 [significant degradation]: [Topic name], [node type], [what degrades]
  P3 [minor]: [Topic name], [improvement opportunity]

Amendments [each names the topic, node type, and specific Copilot Studio change]:

1. Topic "[Topic name]", [node type]: [Specific change --
   "add redirect node to '[Fallback topic]' after Question node when [VarName] remains null after 2 attempts" /
   "add default branch to Condition node on [expression]" /
   "refactor trigger phrases: remove '[phrase]' from '[Topic]', add entity question node"]
   Trigger phrase sequence: "[phrase 1]" -> "[phrase 2]" -> [observable failure at this step]
   Observable failure: [What the user sees or experiences]

2. [Amendment]
   Trigger phrase sequence: [sequence] -> [failure]
   Observable failure: [What the user sees]

[Continue for all P1 and P2 findings.]

PHASE 6 GATE: Coverage report complete. Findings prioritized. All P1 and P2 amendments include reproduction steps. Advance to Phase 7.

## PHASE 7: PROHIBITED TERM AUDIT
[Compliance Auditor speaks. Scan the full output from Phases 1-6 for each prohibited term.
Record CLEAN or FOUND for each term. If FOUND, quote the exact line where the term appears
and state the required replacement. This audit is the final gate before artifact publication.]

Scope: Phase 1 (Setup), Phase 2 (Conversation Trace), Phase 3 (Defect Matrix),
       Phase 4 (Fallback Chain), Phase 5 (Adversarial Turn), Phase 6 (Findings and Amendments)

| Prohibited term | Status | Section (if FOUND) | Line (if FOUND) | Required replacement |
|-----------------|--------|---------------------|-----------------|----------------------|
| intent          | CLEAN / FOUND | [Phase N] | [quote or "—"] | "trigger phrase" or "topic activation" |
| dialog          | CLEAN / FOUND | [Phase N] | [quote or "—"] | "conversation" or "topic sequence" |
| slot            | CLEAN / FOUND | [Phase N] | [quote or "—"] | "session variable" or "question node input" |
| NLU             | CLEAN / FOUND | [Phase N] | [quote or "—"] | "trigger phrase matching" |
| utterance       | CLEAN / FOUND | [Phase N] | [quote or "—"] | "user input" or "trigger phrase" |
| chatbot         | CLEAN / FOUND | [Phase N] | [quote or "—"] | "agent" |
| handoff         | CLEAN / FOUND | [Phase N] | [quote or "—"] | "escalation" |
| context         | CLEAN / FOUND | [Phase N] | [quote or "—"] | "session variables" |
| fallback intent | CLEAN / FOUND | [Phase N] | [quote or "—"] | "fallback topic" |
| bot             | CLEAN / FOUND | [Phase N] | [quote or "—"] | "agent" |

PROHIBITED TERM AUDIT result: CLEAN (all 10 terms absent from Phases 1-6) /
  VIOLATIONS FOUND ([N] terms require replacement before artifact is published)

PHASE 7 GATE: Prohibited term audit complete. Vocabulary verified.
[If violations found: list them and their replacements before writing the artifact.]

---

Write artifact: simulations/flow/conversation/{topic}-conversation-{date}.md
Frontmatter: skill, topic, date, agent_name, topic_count, topics_visited, topics_visited_pct,
trigger_phrases_exercised, turns_simulated, defects_found (list), fallback_quality,
adversarial_outcome (GRACEFUL / BRITTLE / SILENT FAILURE),
turns_spec_conformant ([N] of [TOTAL]), spec_deviations (count),
vocabulary_clean (CLEAN / VIOLATIONS [N]).
```

---

## Round 2 Design Notes

### Rubric coverage by variation (v2 criteria)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 Dialog path as turns | Turn blocks required | TRACE GATE + turn blocks | Turn blocks required | Typed TURN[N] blocks required | TRACE GATE + turn blocks |
| C-02 All four defect classes | Defect analysis, all four named | DEFECT GATE, all four named | DEVELOPER defect analysis | DEFECT_MATRIX typed table | Pre-printed matrix + DEFECT GATE |
| C-03 Session state tracked | Variables delta per turn | Variables block + TRACE GATE | Variables block per turn | SESSION_VARIABLES_DELTA typed | Variables block + TRACE GATE |
| C-04 Copilot Studio framing | VOCABULARY GATE | Topology spec reference + CS vocabulary | VOCABULARY_REGISTRY + topology spec | VOCABULARY_REGISTRY typed map | VOCABULARY GATE + prohibited terms |
| C-05 Reproduction steps | Trigger phrase sequence per amendment | Trigger phrase sequence + observable failure | Trigger phrase sequence per amendment | REPRODUCTION typed per amendment | Trigger phrase sequence + observable failure |
| C-06 Fallback chain coverage | FALLBACK CHAIN TRACE to terminal | FALLBACK GATE to terminal | FALLBACK CHAIN TRACE to terminal | FALLBACK_CHAIN_TRACE typed | Phase 4 to terminal + FALLBACK GATE |
| C-07 Intent collision disambiguation | In defect analysis if FOUND | In defect analysis if FOUND | In DEVELOPER defect analysis | In DEFECT_MATRIX row if FOUND | In Phase 3 matrix if FOUND |
| C-08 Graph coverage metric | Not present | Not present | Not present | Not present | Phase 6 coverage report pre-printed |
| C-09 Adversarial turn injection | Not present | Not present | Not present | Not present | Phase 5: Adversarial turn pre-printed |
| **C-10** Prohibited vocabulary gate | VOCABULARY GATE + post-trace PROHIBITED TERM AUDIT table | Vocabulary gate only (weak) | AUDITOR: PROHIBITED TERM AUDIT post-trace | Per-turn PROHIBITED_TERM_SCAN + VOCABULARY_AUDIT table | PHASE 7: PROHIBITED TERM AUDIT (post-trace, covers all phases) |
| **C-11** Turn-level conformance verdict | Not present | SPEC_CONFORMANCE required field per turn; cites CS-SPEC-N | AUDITOR: per-turn annotations with CS-SPEC reference | SPEC_CONFORMANCE typed enum per turn | SPEC_CONFORMANCE in every Phase 2 turn block |

### Predicted scores under v2 rubric

| Variation | C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | C-10 | C-11 | Score | Golden |
|-----------|------|------|------|------|------|------|------|------|------|------|------|-------|--------|
| V-01 | P | P | P | P | P | P | P | — | — | **P** | — | 95 | YES |
| V-02 | P | P | P | P | P | P | P | — | — | — | **P** | 95 | YES |
| V-03 | P | P | P | P | P | P | P | — | — | **P** | **P** | 97.5 | YES |
| V-04 | P | P | P | P | P | P | P | — | — | **P** | **P** | 97.5 | YES |
| V-05 | P | P | P | P | P | P | P | P | P | **P** | **P** | **100** | YES |

Scoring formula (v2): `(essential_pass/4 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/4 * 10)`

V-01 and V-02: 60 + 30 + 1/4*10 = **95**
V-03 and V-04: 60 + 30 + 2/4*10 = **97.5**
V-05: 60 + 30 + 4/4*10 = **100**

**Risk analysis:** V-05's Phase 7 PROHIBITED TERM AUDIT adds the post-trace verification that C-10 specifically requires. V-03/V-04's advantage over V-01/V-02 is covering both C-10 and C-11 in a single variation, but they lose C-08 and C-09 by not inheriting R1 V-05's coverage report and adversarial turn phases. This tradeoff is intentional -- V-03 and V-04 are isolated-axis explorations. V-05 is the only variation that claims all four aspirational criteria.

```json
{"top_score_predicted": 100, "new_patterns": ["post-trace prohibited term audit (Phase 7) closes the C-10 gap left by start-of-trace instruction alone", "pre-stated topology spec with CS-SPEC-N labels enables precise SPEC_CONFORMANCE verdicts per turn that cite specific properties, not just pass/fail", "Compliance Auditor as a second role produces more rigorous prohibited term detection because it reads finished output rather than producing it", "typed enum fields (SPEC_CONFORMANCE, PROHIBITED_TERM_SCAN) prevent narrative drift in verdict fields and make artifacts parseable downstream"]}
```
