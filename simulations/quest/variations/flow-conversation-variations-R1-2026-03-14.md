Written to `simulations/quest/variations/flow-conversation-variations-R1-2026-03-14.md`.

---

## Round 1 Variations -- flow-conversation

**5 complete prompt bodies, V-01 through V-05.**

| V | Axis | Key mechanism | Primary rubric risk addressed |
|---|------|---------------|-------------------------------|
| **V-01** | Output format | Pre-printed 4-row defect matrix with mandatory `FOUND / CONFIRMED ABSENT` verdict | C-02 (only reports defects found, never confirms absence) |
| **V-02** | Lifecycle emphasis | 5 phase gates with explicit `TRACE GATE / DEFECT GATE` checkpoints; `Turn N of TOTAL` headers | C-01 (abstract graph description instead of actual turns) |
| **V-03** | Phrasing register | `VOCABULARY GATE` section maps agent concepts to Copilot Studio topology; prohibited terms list | C-04 (generic chatbot framing) |
| **V-04** | Role sequence + output format | Conversation Designer traces intent first; Dev traces implementation second; deviations table surfaces design-level gaps | C-05 (richer reproduction steps from DEVIATES annotations) |
| **V-05** | Full synthesis (all axes) | Vocabulary gate + phase gates + defect matrix + Designer-first + pre-printed coverage metric + adversarial turn section | All 9 criteria structurally guaranteed |

**Predicted ceiling:** V-05 -- every rubric criterion has a pre-printed field. No criterion left to model discretion.

**Closest competitor:** V-04 -- the Designer-intent vs. Developer-trace gap surfaces defect classes that structural enforcement alone cannot find.

**Open research question for R1:** Does V-03's explicit vocabulary prohibition outperform V-01's structural vocabulary embedding for C-04, or does the model drift to generic terms unless the prohibition appears in every section header?
 they carry through all subsequent sections.
- C-01 failure is "abstract graph description." V-02's TRACE GATE forces a Turn N of TOTAL header for
  every turn -- the model cannot substitute a summary for actual simulation.
- V-04 tests whether the design-implementation gap (Designer intent vs. Developer trace) surfaces more
  defects than a single-role trace, and whether the deviations table produces richer C-05 reproduction steps.
- V-05 is the maximum-surface synthesis: all axes + pre-printed coverage metric (C-08) + adversarial turn
  section (C-09). No criterion left to model discretion.

**Predicted ceiling:** V-05 -- all 9 criteria structurally guaranteed. V-04 closest competitor (role gap
surfaces richer defects, but no coverage metric). V-01 strongest single-axis (C-02 is the highest-risk gap).

---

## V-01: Output Format -- Pre-printed Defect Matrix

**Axis:** Output format -- pre-printed 4-row defect matrix with mandatory FOUND/CONFIRMED ABSENT verdict
per defect class; pre-printed session variables delta block per turn
**Hypothesis:** The C-02 failure mode is "output only reports defects found, never confirms absence." If
the matrix row is pre-printed with both verdict options, the model must choose one and cannot silently omit
a class. The pre-printed variable delta block per turn prevents C-03 failure (no carried state) by making
state a required field at every turn boundary.

```
You are running /flow:conversation for topic "{topic}".

Read: simulations/flow/conversation/{topic}-conversation-{date}.md if it exists (amend context).
Read: any signal artifacts in simulations/ relevant to "{topic}" (background context).

Role: Copilot Studio Domain Expert.

---

## AGENT PROFILE
Agent name: [Name or description of the Copilot Studio agent]
Topic count: [N topics in the graph]
Knowledge sources: [List knowledge bases, SharePoint, Dataverse tables, or "none"]
Session variable scope: [Topic-scoped / Global / Mixed -- explain which variables are which]
Scenario: [Describe the conversation scenario -- what the user is trying to accomplish in this turn sequence]

## CONVERSATION TRACE

[Simulate each turn in sequence. Fill in all fields for every turn. Do not skip fields or collapse turns.]

### Turn 1
Utterance: "[Exact user input]"
Topic matched: [Topic name] (confidence [X.XX], runner-up: [Topic name] [X.XX])
Trigger phrase matched: "[Exact trigger phrase from topic definition]"
Nodes executed: [Trigger] -> [Node type: Message/Question/Condition/Action/Redirect] -> [...]
Actions called: [Flow name / Custom API name / "none"] -- result: [return value or "pending"]
Condition evaluated: [expression] -> branch taken: [label] / "no condition in this turn"
Variables delta:
  Set: [VariableName] = [value] (scope: topic / global)
  Awaiting: [VariableName] (scope: topic / global)
  Carried from prior turn: [VariableName] = [value] / "none yet"
Response: "[Exact agent response text]"

### Turn 2
[Same structure as Turn 1. Carried variables must reflect Turn 1 state.]

### Turn N
[Continue for each turn in the scenario. Add turns as needed. Each turn is its own block.]

## DEFECT MATRIX

[Complete all four rows. Each class must carry a verdict of FOUND or CONFIRMED ABSENT.
Do not leave a verdict blank or use any other verdict value.
"CONFIRMED ABSENT" requires an explicit statement of scope -- what was checked and found clear.]

| Defect class | Verdict | Evidence / Confirmation |
|--------------|---------|------------------------|
| Dead ends (topic exits with no valid next intent and no fallback topic redirect) | FOUND / CONFIRMED ABSENT | [If FOUND: which turn, which topic, what utterance leaves the user stranded with no path forward. If CONFIRMED ABSENT: "All [N] topic exits route to a valid redirect node, escalation, or fallback topic. No terminal state without a graceful path."] |
| Infinite loops (Topic A's redirect node points to Topic B which redirects back to Topic A) | FOUND / CONFIRMED ABSENT | [If FOUND: the full loop path (A->B->A) and the condition that triggers it. If CONFIRMED ABSENT: "Topic redirect graph is acyclic across [N] transitions traced. No redirect cycle detected."] |
| Intent collisions (same utterance or near-identical trigger phrases registered in multiple topics) | FOUND / CONFIRMED ABSENT | [If FOUND: the utterance or phrase, the competing topics, and their confidence scores at runtime. If CONFIRMED ABSENT: "All simulated utterances resolved to a single topic above 0.7 confidence with runner-up below 0.4. No overlap detected across [N] trigger phrases examined."] |
| Missing fallbacks (condition node in a topic has no else/default branch) | FOUND / CONFIRMED ABSENT | [If FOUND: the topic name, the condition expression, and the unhandled branch. If CONFIRMED ABSENT: "All condition nodes in [N] topics traced carry a default branch or redirect to the fallback topic."] |

## FALLBACK CHAIN TRACE

[Trace one complete fallback path: what happens when no topic matches the user utterance.
Start from the unrecognized utterance and walk every node to the terminal state.
Do not stop at the first fallback node -- walk to completion.]

Unrecognized utterance: "[utterance that matches no topic above confidence threshold]"
Step 1: Trigger phrase matching: 0 topics match -> [system behavior: route to fallback topic / show generic error / other]
Step 2: [Fallback topic name]: [first node -- Message / Question / Condition / Escalation offer]
Step 3: [Next node in fallback topic and its behavior]
...
Step N: Terminal state -- "[Escalated to human agent via [escalation node] / Session ended gracefully / User returned to main menu topic]"

Fallback chain quality: COMPLETE (reaches a terminal state) / LOOPS (never terminates) / TRUNCATED (drops to generic error with no path forward)

## FINDINGS

[Priority-ordered. P1 = session-breaking defect. P2 = significant user experience degradation. P3 = minor issue or improvement opportunity.
Reference turn number and defect class for each finding.]

P1: [Finding -- Turn N, defect class, what breaks and what the user experiences]
P2: [Finding]
P3: [Finding]
[Continue as needed. Write "No findings at P1 or P2." only if the defect matrix is entirely CONFIRMED ABSENT and the fallback chain is COMPLETE.]

## AMENDMENTS

[Numbered actions. Each traceable to a P1 or P2 finding above.
Reproduction steps are required for every action. Fill in all brackets -- do not omit any line.]

1. [Concrete Copilot Studio action -- name the topic, the node type, and the specific change]:
   [e.g., "In topic 'Product Returns': add a redirect node after the Question node to 'Escalation' topic when OrderNumber remains null after 2 attempts."]
   Reproduction: Utterance sequence "[Turn 1 utterance]" -> "[Turn N utterance]" triggers [defect class].
   Observable failure: [What the user sees or experiences at the point of failure.]

2. [Action]: [Next step]
   Reproduction: [Utterance sequence]
   Observable failure: [What the user sees]

[Continue for all P1 and P2 findings.]

---

Write artifact: simulations/flow/conversation/{topic}-conversation-{date}.md
Frontmatter: skill, topic, date, agent_name, topic_count, turns_simulated, defects_found (list the defect classes that returned FOUND), fallback_quality.
```

---

## V-02: Lifecycle Emphasis -- Phase-Gated Turn Walking

**Axis:** Lifecycle emphasis -- five explicit phases with mandatory GATE checkpoints between them;
turn-by-turn headers (Turn N of TOTAL) prevent collapse into summary
**Hypothesis:** The C-01 failure mode is "output describes the graph abstractly without walking actual turns."
If a TRACE GATE fires after the conversation trace phase and explicitly verifies that every turn in the
defined sequence was walked, the model cannot substitute a narrative summary for a turn-by-turn simulation.
The phase structure also separates defect scanning (Phase 3) from trace walking (Phase 2), which prevents
the C-02 failure of conflating "I walked these turns" with "I checked all defect classes."

```
You are running /flow:conversation for topic "{topic}".

Read: simulations/flow/conversation/{topic}-conversation-{date}.md if it exists.
Read: any signal artifacts in simulations/ relevant to "{topic}".

Role: Copilot Studio Domain Expert. Conversation Designer (secondary, Phase 1 only).

All phases below are gates. Complete each phase fully before advancing to the next.
Do not describe the topic graph abstractly -- walk it turn by turn in Phase 2.

---

## PHASE 1: SETUP
[Complete before any turn simulation begins. The Conversation Designer defines the scenario.]

Agent: [Name or description of the Copilot Studio agent]
Topics in graph: [N] -- list all topic names
Knowledge sources: [List or "none"]
Scenario: [The conversation path you will walk -- user goal and expected turn count]
Turn sequence defined:
  Turn 1: "[planned user utterance]"
  Turn 2: "[planned user utterance]"
  Turn N: "[planned user utterance]"
Session variables in scope:
  [VarName]: type=[string/number/boolean], scope=[topic/global], initial=[value or "unset"]
  [VarName]: type=[...], scope=[...], initial=[...]
Copilot Studio topology note: [Which product area this agent serves -- Customer Service / IT Helpdesk / Sales / HR / other]

SETUP GATE: Topic count N confirmed. Turn sequence defined ([N] turns). Session variables enumerated. Advance to Phase 2.

## PHASE 2: CONVERSATION TRACE
[Copilot Studio Developer speaks. Walk every turn defined in Phase 1 Setup.
Do not skip turns or collapse multiple turns into a summary. Each turn requires its own block.]

Turn [N] of [TOTAL]:
  User: "[exact utterance from the turn sequence above]"
  -> Topic activated: [Topic name]
       Trigger phrase matched: "[phrase from topic's trigger phrase list]"
       Confidence: [X.XX] | Runner-up: [Topic name] ([X.XX])
  -> Node path: [node chain in execution order]
       e.g., Trigger phrase node > Message node > Question node > Condition node > Action node > Redirect node
  -> Action node (if any): [Action name / "none"]
       Call: [Flow name or Custom API endpoint]
       Result: [return value or status]
  -> Condition evaluated (if any): [condition expression] -> branch taken: [branch label]
  -> Session variables after this turn:
       [VarName] = [value] (scope: topic/global, changed this turn: yes/no)
       [VarName] = awaiting_input (scope: topic/global)
       [VarName] = [carried from Turn N-1, unchanged]
  -> Response: "[exact agent response text shown to user]"

[Repeat for every turn. Each Turn block is mandatory.]

TRACE GATE: All [N] turns from Phase 1 Setup completed. Session state carried across all transitions.
Every turn has a node path and variables block. Advance to Phase 3.

## PHASE 3: DEFECT SCAN
[For each defect class: state FOUND or CONFIRMED ABSENT. Both verdicts require evidence.
A verdict without evidence does not satisfy this phase.]

Dead ends (topic exits with no valid next step and no fallback):
  Verdict: FOUND / CONFIRMED ABSENT
  Evidence: [FOUND: turn N, topic name, the utterance that strands the user, why no path forward exists.
             ABSENT: "All [N] topic exits lead to a redirect node, escalation node, or fallback topic. No dead end found across [N] exits traced."]

Infinite loops (redirect cycle between topics):
  Verdict: FOUND / CONFIRMED ABSENT
  Evidence: [FOUND: the loop path (Topic A -> Topic B -> Topic A) and the condition that triggers it.
             ABSENT: "Topic redirect graph is acyclic. [N] redirects traced, no cycle detected."]

Intent collisions (same utterance activates multiple topics):
  Verdict: FOUND / CONFIRMED ABSENT
  Evidence: [FOUND: the utterance, the competing topics, their confidence scores.
             ABSENT: "All [N] utterances in the trace resolved to a single topic above 0.7 confidence with runner-up below 0.4."]

Missing fallbacks (condition node with no default/else branch):
  Verdict: FOUND / CONFIRMED ABSENT
  Evidence: [FOUND: topic name, condition node, the specific branch that has no handler.
             ABSENT: "All condition nodes in [N] topics traced carry a default branch or redirect to fallback topic."]

DEFECT GATE: All four classes have verdict + evidence. Advance to Phase 4.

## PHASE 4: FALLBACK CHAIN TRACE
[Walk the complete fallback path for one unrecognized utterance. Walk every node to terminal state.
Do not stop at the first fallback node -- the path must reach a terminal state.]

Unrecognized utterance: "[phrase that matches no topic above confidence threshold]"
Step 1: Trigger phrase matching: 0 topics match -> [system routes to fallback topic or shows error]
Step 2: [Fallback topic first node]
Step 3: [Next node -- question, redirect, escalation offer, generative answer attempt]
...
Step N: Terminal -- [Escalated to human agent / Graceful session end / User returned to root topic]

Fallback chain quality: COMPLETE / LOOPS / TRUNCATED

FALLBACK GATE: Fallback chain traced to terminal state. Quality verdict recorded. Advance to Phase 5.

## PHASE 5: FINDINGS AND AMENDMENTS
[Priority-ordered findings. Each P1 and P2 includes a reproduction step sequence.]

Findings:
  P1 [session-breaking, if any]: [Finding -- turn reference, defect class, Copilot Studio location (topic + node type)]
  P2 [significant degradation, if any]: [Finding]
  P3 [minor, if any]: [Finding]

Amendments:
  1. [Topic name], [node type]: [Concrete change in Copilot Studio]
     Reproduction: "[utterance 1]" -> "[utterance 2]" -> [observable failure at this step]
  2. [Topic name], [node type]: [Change]
     Reproduction: [utterance sequence] -> [failure]
  [Continue for all P1 and P2 findings.]

---

Write artifact: simulations/flow/conversation/{topic}-conversation-{date}.md
Frontmatter: skill, topic, date, agent_name, topic_count, turns_simulated, defects_found (list), fallback_quality.
```

---

## V-03: Phrasing Register -- Vocabulary Gate

**Axis:** Phrasing register -- mandatory VOCABULARY GATE section pre-maps agent concepts to Copilot Studio
topology before any simulation begins; all subsequent sections must use Copilot Studio vocabulary exclusively
**Hypothesis:** The C-04 failure mode is "generic chatbot framing -- reviewer uses chatbot/dialog/slot/NLU
terms instead of Copilot Studio topology." A VOCABULARY GATE at the top of the prompt forces the model to
establish Copilot Studio terminology (topics, trigger phrases, conditions, fallback topics, escalation,
session variables, actions, redirects, generative answers) as the working vocabulary before any turn is
walked. Terms anchored in a named section carry through because the model's completion naturally references
the vocabulary it just wrote. Also tests whether the vocabulary gate alone (without a defect matrix) is
sufficient to pass C-04 on live model runs, or whether structural enforcement (V-01) is also needed.

```
You are running /flow:conversation for topic "{topic}".

Read: simulations/flow/conversation/{topic}-conversation-{date}.md if it exists.
Read: any signal artifacts in simulations/ relevant to "{topic}".

You are a Copilot Studio Domain Expert. Throughout this analysis, use Copilot Studio vocabulary exclusively.
The vocabulary below is the only terminology valid in this output:

  Topics                -- named conversation units in the Copilot Studio topic graph
  Trigger phrases       -- the phrases registered to a topic that cause it to activate
  Conditions            -- logical branch nodes within a topic
  Fallback topics       -- topics that activate when no other topic matches (System Fallback Topic or custom)
  Escalation            -- handoff from the agent to a human agent via the escalation node
  Session variables     -- named values stored during the conversation (topic-scoped or global)
  Topic redirects       -- nodes that transfer conversation flow to another topic
  Actions               -- nodes that call external flows, APIs, or connectors
  Generative answers    -- AI-generated responses sourced from a configured knowledge source
  Knowledge sources     -- SharePoint libraries, Dataverse tables, or uploaded files configured in the agent
  End of conversation   -- terminal node type that closes the session

Do not use: intent, dialog, slot, NLU, utterance (use "user input" or "trigger phrase"), chatbot (use "agent"),
handoff (use "escalation"), context (use "session variables"), fallback intent (use "fallback topic").

---

## VOCABULARY GATE
[Complete this section before any simulation. Map the agent's components to Copilot Studio topology.
This anchors terminology for all sections below.]

Agent name: [Name or description]
Topics in graph: [List each topic name -- use the exact Copilot Studio topic names]
Trigger phrases (sampled): [List 2-3 trigger phrases per topic, or "inferred from description"]
Fallback topic configured: [Topic name / "System Fallback Topic" / "not configured"]
Escalation path: [Topic name that contains the escalation node, or "not configured"]
Session variables:
  [VarName]: scope=[topic-scoped / global], type=[Text/Number/Boolean], initial=[value or "unset"]
  [VarName]: scope=[...], type=[...], initial=[...]
Knowledge sources:
  [Name]: type=[SharePoint / Dataverse table / file upload], content=[brief description]
  [or "none configured"]

VOCABULARY GATE confirmed. All terms above are mapped. Proceed with Copilot Studio topology only.

## CONVERSATION TRACE

Scenario: [User goal -- what the user is trying to accomplish across these turns]

[Simulate each turn using Copilot Studio vocabulary in every field.]

Turn [N]:
  User input: "[what the user typed or said]"
  Trigger phrase matched: "[exact phrase from the topic's trigger phrase list]" in topic "[Topic name]"
  Topic activated: [Topic name] (confidence: [X.XX])
  Runner-up topic: [Topic name] (confidence: [X.XX])
  Node path: [Trigger phrase node] -> [Message node / Question node / Condition node / Action node / Redirect node / End of conversation node]
  Action node (if any): [Action name] -> result: [return value]
  Condition evaluated (if any): [condition expression] -> branch: [label]
  Session variables after this turn:
    [VarName]: [value] (scope: topic-scoped / global)
    [VarName]: awaiting input (scope: topic-scoped / global)
  Agent response: "[text shown to user]"

[Continue for each turn in the scenario.]

## DEFECT ANALYSIS

For each defect class, apply a verdict and state evidence using Copilot Studio vocabulary.

**Dead ends** -- a topic's node path terminates with no redirect node, no escalation node, and no fallback
topic configured for that exit point:
Verdict: FOUND / CONFIRMED ABSENT
[FOUND: Topic name, the terminal node (Message node / Question node with no follow-up path), and what
the user experiences -- session hangs, generic error, or silent exit.]
[CONFIRMED ABSENT: "All [N] topics traced exit via a redirect node to [Topic names], an escalation node,
or the System Fallback Topic. No topic terminates without a valid exit path."]

**Infinite loops** -- a topic redirect node targets Topic B, and Topic B contains a redirect node that
targets Topic A:
Verdict: FOUND / CONFIRMED ABSENT
[FOUND: The full redirect path (Topic A redirect node -> Topic B redirect node -> Topic A) and the
condition or trigger that initiates the loop.]
[CONFIRMED ABSENT: "Topic redirect graph across [N] topics is acyclic. Redirect targets confirmed:
[Topic A -> Topic B (terminal)], [Topic C -> Topic D (terminal)]. No cycle detected."]

**Intent collisions** -- two or more topics register trigger phrases that are identical or close enough
to produce confidence scores above 0.5 for the same user input:
Verdict: FOUND / CONFIRMED ABSENT
[FOUND: The specific user input, the competing topics, and their confidence scores. Then:
Disambiguation strategy: [Entity enrichment -- add an entity question node to distinguish the topics /
Condition ordering -- add a condition node that checks session variables before activating /
Trigger phrase refactor -- remove overlapping phrases and replace with distinct ones]
Rationale: [Why this strategy resolves the collision in Copilot Studio's matching model]]
[CONFIRMED ABSENT: "Trigger phrases across all [N] topics are lexically distinct. No user input in the
simulation produced confidence above 0.4 for more than one topic simultaneously."]

**Missing fallbacks** -- a condition node within a topic defines branches for specific cases but has no
default/else branch for cases outside those conditions:
Verdict: FOUND / CONFIRMED ABSENT
[FOUND: Topic name, the condition node (with its expression), and the branch that is missing.]
[CONFIRMED ABSENT: "All condition nodes in [N] topics traced carry a default branch. Default branches
confirmed: [list topics and their default branch targets]."]

## FALLBACK CHAIN TRACE

[Walk the complete fallback chain from an unrecognized user input to the terminal state.
Use Copilot Studio node types at every step. Do not stop at the first fallback topic activation.]

User input: "[phrase that matches no trigger phrase list]"
Step 1: Trigger phrase matching: [N] topics evaluated, 0 match above confidence threshold
         -> System routes to: [Fallback topic name / System Fallback Topic]
Step 2: [Fallback topic]: [first node type] -- [what it does]
Step 3: [Next node] -- [behavior, including any knowledge source lookup or generative answers attempt]
...
Step N: Terminal state: [Escalation node activates -> human agent handoff /
                         End of conversation node -> session closes gracefully /
                         Redirect node -> returns to root topic "[Topic name]"]

Fallback chain quality: COMPLETE (reaches a terminal state) / LOOPS (redirect cycle, never terminates) / TRUNCATED (reaches a generic error node with no further path)

## FINDINGS

[Prioritized. Reference topic names and node types, not generic descriptions.]

P1 [session-breaking]: [Topic name], [node type], [what fails and what the user experiences]
P2 [significant degradation]: [Topic name], [node type], [what fails]
P3 [minor issue]: [Topic name], [what could be improved]

## AMENDMENTS

[Each amendment names the Copilot Studio topic and the node type to change.
Reproduction uses trigger phrase sequences, not abstract descriptions.]

1. In topic "[Topic name]": [Specific node change -- "add a redirect node after Question node targeting
   '[Fallback topic]'" / "add a default branch to the Condition node on [expression]" /
   "refactor trigger phrases: remove '[phrase]' from '[Topic A]' and add entity question node to distinguish"]
   Trigger phrase sequence: "[trigger phrase 1]" -> "[trigger phrase 2]" ->
     [observable failure at this step: what the user sees]

2. [Amendment in Copilot Studio terms]
   Trigger phrase sequence: [sequence] -> [failure]

[Continue for all P1 and P2 findings.]

---

Write artifact: simulations/flow/conversation/{topic}-conversation-{date}.md
Frontmatter: skill, topic, date, agent_name, topic_count, turns_simulated, defects_found (list), fallback_quality.
```

---

## V-04: Role Sequence + Output Format

**Axes:** Role sequence (Conversation Designer traces intent before Copilot Studio Developer traces
implementation) + output format (pre-printed defect matrix from V-01) + design-implementation gap table
**Hypothesis:** A single-role trace discovers defects that exist in the implementation. A two-role trace
where the Conversation Designer first defines what *should* happen -- turn sequence, session state
transitions, fallback behavior -- and then the Developer traces what *actually* happens, discovers an
additional class of defect: cases where the implementation behaves as designed but the design itself is
wrong. The gap table (DEVIATES rows from Developer trace) produces richer C-05 reproduction steps because
each deviation is already annotated with its P1/P2/P3 severity. Combined with V-01's defect matrix to
structurally guarantee C-02.

```
You are running /flow:conversation for topic "{topic}".

Read: simulations/flow/conversation/{topic}-conversation-{date}.md if it exists.
Read: any signal artifacts in simulations/ relevant to "{topic}".

Two roles execute in sequence. Conversation Designer speaks first. Copilot Studio Developer speaks second.
Do not merge the perspectives -- each role contributes a distinct view of the conversation.

---

## CONVERSATION DESIGNER: INTENDED FLOW
[Conversation Designer speaks. Define what the user *should* experience -- the ideal conversation path.
Do not simulate implementation details yet. Focus on user goals, topic sequence, and expected outcomes.]

User goal: [What the user is trying to accomplish in this scenario]
Intended topic sequence: [Topic 1] -> [Topic 2] -> [Topic 3] -> [terminal state: end / escalation / redirect to root]
Intended turn count: [N turns]
Expected session state at end of conversation:
  [VarName]: [expected final value]
  [VarName]: [expected final value]
Intended fallback behavior: [What should happen if the user goes off-script or says something unexpected]
Intended escalation trigger: [What condition should cause the agent to escalate to a human agent]
Design weaknesses I anticipate (Conversation Designer):
  [List any known gaps in the design -- missing topic coverage, weak fallback design, scope issues -- or "none identified"]

## COPILOT STUDIO DEVELOPER: IMPLEMENTATION TRACE
[Copilot Studio Developer speaks. Walk the actual implementation turn by turn using Copilot Studio vocabulary.
After each turn, compare to the Conversation Designer's intended flow above.]

### Turn [N] of [TOTAL]:
  User: "[exact utterance]"
  Topic activated: [Topic name]
    Trigger phrase matched: "[phrase]" (confidence: [X.XX])
    Runner-up topic: [Topic name] ([X.XX])
  Node path: [node chain in execution order]
  Action node (if any): [Action name] -> result: [value] / "none"
  Condition evaluated (if any): [expression] -> branch: [label]
  Session variables after this turn:
    [VarName] = [value] (scope: topic / global, changed this turn: yes/no)
    [VarName] = awaiting_input (scope: topic / global)
    [VarName] = [carried unchanged from prior turn]
  Response: "[agent response text]"
  Implementation vs. design: MATCHES INTENT / DEVIATES
    [If DEVIATES: describe what was intended (from Conversation Designer above) and what actually happened.
     Severity: P1 / P2 / P3]

[Repeat for every turn. Each Turn block is mandatory. Flag every deviation.]

## DEFECT MATRIX
[Complete all four rows. Each must carry FOUND or CONFIRMED ABSENT with evidence.
Do not leave a verdict blank. "CONFIRMED ABSENT" requires an explicit scope statement.
If FOUND for intent collisions, include a disambiguation strategy.]

| Defect class | Verdict | Evidence / Confirmation |
|--------------|---------|------------------------|
| Dead ends (topic exits with no valid next intent and no fallback topic redirect) | FOUND / CONFIRMED ABSENT | [FOUND: turn N, topic name, utterance that strands the user, why no forward path exists. CONFIRMED ABSENT: "All [N] topic exits route to a redirect node, escalation node, or fallback topic."] |
| Infinite loops (Topic A redirect -> Topic B redirect -> Topic A) | FOUND / CONFIRMED ABSENT | [FOUND: the full loop path and triggering condition. CONFIRMED ABSENT: "Topic redirect graph is acyclic. [N] redirects traced, no cycle."] |
| Intent collisions (same utterance activates multiple topics above threshold) | FOUND / CONFIRMED ABSENT | [FOUND: utterance, competing topics and confidence scores. Disambiguation strategy: [entity enrichment / condition ordering / trigger phrase refactor] -- rationale: [why this resolves it in Copilot Studio]. CONFIRMED ABSENT: "All [N] utterances resolved to single topic above 0.7, runner-up below 0.4."] |
| Missing fallbacks (condition node with no else/default branch) | FOUND / CONFIRMED ABSENT | [FOUND: topic, condition expression, unhandled branch. CONFIRMED ABSENT: "All condition nodes in [N] topics carry a default branch or redirect to fallback topic."] |

## FALLBACK CHAIN TRACE
[Walk one complete fallback path to terminal state. Do not stop at the first fallback topic activation.]

Unrecognized utterance: "[phrase that matches no topic above threshold]"
Step 1: No topic match -> [system routes to fallback topic or error]
Step 2: [Fallback topic first node]
Step 3: [Next node and its behavior]
...
Step N: Terminal: [Escalation via escalation node / Graceful end / Return to root topic]

Fallback chain quality: COMPLETE / LOOPS / TRUNCATED

## DESIGN-IMPLEMENTATION GAP SUMMARY
[Conversation Designer and Copilot Studio Developer jointly identify gaps.
List every turn where "DEVIATES" was flagged in the implementation trace and why it matters.]

| Turn | Conversation Designer intended | Copilot Studio Developer found | Severity |
|------|-------------------------------|-------------------------------|----------|
| [N] | [Intent] | [Actual behavior] | P1 / P2 / P3 |
| [N] | [Intent] | [Actual behavior] | P1 / P2 / P3 |
[Write "No deviations found." if all turns matched intent.]

## FINDINGS

[Priority-ordered. Draws from both DEVIATES rows and DEFECT MATRIX findings above.]

P1 [session-breaking]: [Finding -- turn reference, source (deviation or defect class), Copilot Studio location]
P2 [significant degradation]: [Finding]
P3 [minor issue]: [Finding]

## AMENDMENTS
[Each amendment names the Copilot Studio topic and node to change.
Reproduction steps required for all P1 and P2 findings.]

1. Topic "[Topic name]", [node type]: [Specific Copilot Studio change]
   Reproduction: "[utterance 1]" -> "[utterance 2]" -> [observable failure at this step]
   Observable failure: [What the user sees or experiences at the point of failure]

2. [Amendment]
   Reproduction: [utterance sequence] -> [failure]
   Observable failure: [What the user sees]

[Continue for all P1 and P2 findings.]

---

Write artifact: simulations/flow/conversation/{topic}-conversation-{date}.md
Frontmatter: skill, topic, date, agent_name, topic_count, turns_simulated, defects_found (list),
design_gaps (count of DEVIATES rows), fallback_quality.
```

---

## V-05: Full Synthesis (All Axes)

**Axes:** Output format (defect matrix, V-01) + lifecycle emphasis (phase gates, V-02) +
phrasing register (vocabulary gate, V-03) + role sequence (Designer-first, V-04) +
coverage metric (C-08) + adversarial turn injection (C-09)
**Hypothesis:** Maximum structural coverage of all 9 rubric criteria. The vocabulary gate anchors
Copilot Studio terminology before any turn is walked. Phase gates prevent the model from skipping phases
or collapsing the trace into a summary. The defect matrix forces FOUND/CONFIRMED ABSENT on all four
classes. The Designer-first role sequence surfaces design-intent gaps in addition to implementation defects.
The pre-printed COVERAGE REPORT section (topics visited / total) turns narrative coverage claims into a
quantified signal. The pre-printed ADVERSARIAL TURN phase forces at least one off-script scenario. No
criterion left to model discretion: every rubric requirement has a pre-printed field that must be filled.
This is the direct golden candidate for R1.

```
You are running /flow:conversation for topic "{topic}".

Read: simulations/flow/conversation/{topic}-conversation-{date}.md if it exists.
Read: any signal artifacts in simulations/ relevant to "{topic}".

Roles execute in sequence: Conversation Designer (Phase 1), then Copilot Studio Developer (Phases 2-6).
All phases are gates. Complete each phase fully before advancing.
Do not describe the topic graph abstractly -- walk it turn by turn in Phase 2.
Use Copilot Studio vocabulary exclusively throughout:
  Topics, Trigger phrases, Conditions, Fallback topics, Escalation, Session variables,
  Topic redirects, Actions, Generative answers, Knowledge sources, End of conversation nodes.
Do not use: intent, dialog, slot, NLU, chatbot, handoff, context.

---

## PHASE 1: SETUP + VOCABULARY GATE
[Conversation Designer speaks. Define agent topology and intended flow before any simulation begins.]

Agent name: [Name or description of the Copilot Studio agent]
Topics in graph: [N] -- list all topic names
  [Topic name 1], [Topic name 2], [Topic name 3], ...
Trigger phrases (sampled, 2-3 per topic):
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

SETUP GATE: Topic count confirmed. Turn sequence defined. Session variables enumerated. Coverage scope stated. Advance to Phase 2.

## PHASE 2: CONVERSATION TRACE
[Copilot Studio Developer speaks. Walk every turn from the Phase 1 turn sequence.
No turns may be skipped or collapsed. Each turn requires its own block.
Compare each turn to the Conversation Designer's intended flow.]

Turn [N] of [TOTAL]:
  User: "[exact utterance]"
  Trigger phrase matched: "[phrase]" in topic "[Topic name]"
  Confidence: [X.XX] | Runner-up topic: "[Topic name]" ([X.XX])
  Node path: [chain in execution order -- use node type names: Trigger phrase node > Message node > Question node > Condition node > Action node > Redirect node > End of conversation node]
  Action node (if any): [Action name] -> result: [return value or status] / "none"
  Condition evaluated (if any): [expression] -> branch taken: [label]
  Session variables after this turn:
    [VarName] = [value] (scope: topic-scoped / global, changed: yes/no)
    [VarName] = awaiting_input (scope: topic-scoped / global)
    [VarName] = [carried unchanged from Turn N-1]
  Response: "[agent response text shown to user]"
  Implementation vs. design: MATCHES INTENT / DEVIATES -- [deviation description if DEVIATES, severity P1/P2/P3]

[Repeat for every turn. Each Turn block is mandatory.]

TRACE GATE: All [N] turns completed. Session state carried across all transitions. All deviations flagged. Advance to Phase 3.

## PHASE 3: DEFECT MATRIX
[Complete all four rows. FOUND or CONFIRMED ABSENT -- no other verdict is valid.
"CONFIRMED ABSENT" requires an explicit scope statement. Do not leave a verdict or evidence field blank.
If FOUND for intent collisions, include a disambiguation strategy with rationale.]

| Defect class | Verdict | Evidence / Confirmation |
|--------------|---------|------------------------|
| Dead ends (topic exits with no valid next intent and no fallback topic redirect) | FOUND / CONFIRMED ABSENT | [FOUND: turn N, topic name, the node that terminates the session with no forward path, what the user experiences. CONFIRMED ABSENT: "All [N] topic exits route to a redirect node, escalation node, or fallback topic. Exit paths confirmed: [list]."] |
| Infinite loops (Topic A redirect node -> Topic B redirect node -> Topic A) | FOUND / CONFIRMED ABSENT | [FOUND: full loop path and triggering condition. CONFIRMED ABSENT: "Topic redirect graph is acyclic across [N] redirects traced. No cycle. Redirect map: [A->B (terminal)], [C->D (terminal)]."] |
| Intent collisions (trigger phrase in multiple topics produces ambiguous confidence scores) | FOUND / CONFIRMED ABSENT | [FOUND: the trigger phrase, competing topics, confidence scores. Disambiguation strategy: [entity enrichment -- add entity question node before topic activation / condition ordering -- add session variable condition before trigger matching / trigger phrase refactor -- remove overlapping phrases, replace with distinct ones] -- rationale: [why this resolves it in Copilot Studio's matching model]. CONFIRMED ABSENT: "All [N] trigger phrases tested resolve to a single topic above 0.7 confidence with runner-up below 0.4."] |
| Missing fallbacks (condition node with no else/default branch) | FOUND / CONFIRMED ABSENT | [FOUND: topic name, condition expression, the unhandled branch. CONFIRMED ABSENT: "All condition nodes in [N] topics carry a default branch or redirect to the fallback topic. Default branches confirmed: [list topics]."] |

DEFECT GATE: All four classes have verdict + evidence. Advance to Phase 4.

## PHASE 4: FALLBACK CHAIN TRACE
[Walk one complete fallback path from unrecognized input to terminal state.
Every step is required. Do not stop at the first fallback topic activation.]

Unrecognized input: "[phrase that matches no trigger phrase list]"
Step 1: Trigger phrase matching: [N] topics evaluated, 0 match above confidence threshold
  -> System routes to: [Fallback topic name / System Fallback Topic]
Step 2: [Fallback topic first node type] -- [what it does]
Step 3: [Next node -- question node / generative answers attempt / escalation offer / condition]
...
Step N: Terminal state:
  [Escalation node activates -> human agent session opened /
   End of conversation node -> session closes with "[closing message]" /
   Redirect node -> returns user to topic "[Topic name]"]

Fallback chain quality: COMPLETE (reaches a terminal state) / LOOPS (redirect cycle) / TRUNCATED (generic error, no path forward)

## PHASE 5: ADVERSARIAL TURN INJECTION
[Inject one adversarial scenario into the traced conversation: unexpected user input mid-flow,
topic switch during session variable collection, session variable loss, or session timeout.
Walk the actual agent node path -- do not describe generically.]

Adversarial scenario type: [Topic switch mid-variable-collection / Unexpected off-topic input mid-flow / Session timeout clears variables / Repeated same input (potential loop)]
Injected at: Turn [N] of the original scenario, before session variable [VarName] is collected
Adversarial input: "[the unexpected user input that breaks the expected flow]"
Agent response (trace the actual node path):
  -> Topic matching: [does a new topic fire, or does the current topic handle it?]
  -> Node path: [what nodes execute in response to this input]
  -> Session variables: [VarName] = [carried / lost / reset] (scope: topic-scoped / global)
  -> Response shown to user: "[agent response]"
Outcome: [Describe what the user experiences -- conversation recovers / loops / ends abruptly / loses context]
Assessment: GRACEFUL (agent handles the deviation and continues) / BRITTLE (agent fails, loops, or gives a confusing response) / SILENT FAILURE (agent produces no error but loses session state)

## PHASE 6: FINDINGS, COVERAGE, AND AMENDMENTS

Coverage report:
  Topics visited: [N] of [TOTAL] ([N/TOTAL * 100]%)
  Topics unvisited: [List, or "none -- full coverage achieved"]
  Trigger phrases exercised: [N] of approximately [estimated total] ([N/est * 100]%)
  Turns simulated: [N] (scenario) + 1 (adversarial) = [N+1] total

Findings [priority-ordered, referencing topic names and node types]:
  P1 [session-breaking, if any]: [Topic name], [node type], [what fails and what the user experiences]
  P2 [significant degradation, if any]: [Topic name], [node type], [what degrades]
  P3 [minor, if any]: [Topic name], [what could be improved]

Amendments [each names the topic, node type, and specific Copilot Studio change;
reproduction steps required for all P1 and P2 findings]:

1. Topic "[Topic name]", [node type]: [Specific change -- "add redirect node to '[Fallback topic]' after
   Question node when [VarName] remains null after 2 attempts" / "add default branch to Condition node
   on [expression]" / "refactor trigger phrases: remove '[phrase]' from '[Topic]', add entity question node"]
   Trigger phrase sequence: "[phrase 1]" -> "[phrase 2]" -> [observable failure at this step]
   Observable failure: [What the user sees or experiences at the point of failure]

2. [Amendment]
   Trigger phrase sequence: [sequence] -> [failure]
   Observable failure: [What the user sees]

[Continue for all P1 and P2 findings.]

---

Write artifact: simulations/flow/conversation/{topic}-conversation-{date}.md
Frontmatter: skill, topic, date, agent_name, topic_count, topics_visited, topics_visited_pct,
trigger_phrases_exercised, turns_simulated, defects_found (list defect classes returning FOUND),
fallback_quality, adversarial_outcome (GRACEFUL / BRITTLE / SILENT FAILURE).
```

---

## Round 1 Design Notes

### Rubric coverage by variation

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 Dialog path traced as actual turns | Turn blocks required | TRACE GATE forces all N turns | Turn blocks per turn | Turn blocks + DEVIATES flag | TRACE GATE + turn blocks |
| C-02 All four defect classes, found + absent | Pre-printed matrix | DEFECT GATE requires all four | All four named, verdict required | Pre-printed matrix | Pre-printed matrix + DEFECT GATE |
| C-03 Session state tracked across turns | Variables delta block per turn | Variables block per turn | Session variables after turn block | Variables block + carried notation | Variables block + TRACE GATE checks carry |
| C-04 Copilot Studio framing | Vocabulary in field names | Vocabulary in phase instructions | VOCABULARY GATE + explicit prohibited terms | Vocabulary in instructions | VOCABULARY GATE + prohibited terms |
| C-05 Defect reproduction steps | "Reproduction:" line per amendment | Reproduction lines in Phase 5 | Trigger phrase sequence in amendments | Reproduction + Observable failure lines | Trigger phrase sequence + Observable failure |
| C-06 Full fallback chain traced | FALLBACK CHAIN section, to terminal state | FALLBACK GATE, to terminal state | Fallback chain trace, to terminal state | Fallback chain, to terminal state | Phase 4, to terminal state |
| C-07 Intent collision disambiguation | Inside matrix row if FOUND | Inside DEFECT SCAN if FOUND | Explicit Disambiguation strategy field | Inside matrix row if FOUND | Inside matrix row if FOUND + rationale |
| C-08 Graph coverage metric | Not present | Not present | Not present | Not present | Coverage report section, pre-printed |
| C-09 Adversarial turn injection | Not present | Not present | Not present | Not present | Phase 5: Adversarial turn, pre-printed |

### Single-axis differentiation

- **V-01 vs V-02**: V-01 is output format (what the output looks like), V-02 is lifecycle (when things
  happen and what gates verify them). Both independently address C-01/C-02 but through different mechanisms.
  V-01's matrix is a stronger C-02 guarantee (verdict field must be filled). V-02's TRACE GATE is a
  stronger C-01 guarantee (cannot advance without all turns).

- **V-01 vs V-03**: V-01 uses structural pre-printing to enforce vocabulary in field names. V-03 uses an
  explicit vocabulary instruction with prohibited terms. Tests whether explicit prohibition or structural
  embedding is more reliable for C-04 on live model runs.

- **V-02 vs V-03**: Orthogonal axes. V-02 controls when phases happen. V-03 controls what words are used.
  They do not interfere. V-04 tests whether combining role sequence with V-01's output format produces
  richer defect discovery than either alone.

### V-golden candidate

**V-05** -- all 9 criteria have pre-printed structural guarantees. No criterion left to model discretion.
The vocabulary gate eliminates C-04 risk; the TRACE GATE eliminates C-01 risk; the defect matrix
eliminates C-02 risk; the variables block eliminates C-03 risk; the reproduction lines eliminate C-05 risk;
Phase 4 eliminates C-06 risk; the disambiguation field eliminates C-07 risk; the coverage report
pre-prints C-08; Phase 5 pre-prints C-09.

**V-04** is the closest competitor. Its role sequence (Designer intent vs. Developer trace) may produce
qualitatively richer defects by surfacing design-level gaps that single-role simulations miss. The gap
between "what should happen" and "what does happen" often reveals defect classes that no amount of
structural enforcement discovers.

**Open research question for R1:** Does V-03's explicit vocabulary prohibition ("do not use: intent,
dialog, slot") outperform V-01's structural vocabulary embedding for C-04, or does the model still drift
to generic terms when the prohibition is not pre-printed in every section header?
