Here are the 5 complete variations for Round 3:

---

## Round 3 Variations — flow-conversation

**Baseline:** R2 V-05 scores **96.67** under v3 — misses C-12 and C-13.

| V | Axis | Key mechanism | C-12 | C-13 | Predicted |
|---|------|---------------|------|------|-----------|
| **V-01** | Role sequence | Phase 7 Auditor expanded: reads finished Phase 2 and produces separate per-turn SPEC_CONFORMANCE annotations + discrepancy detection | YES | — | 98.33 |
| **V-02** | Phrasing register | `PROHIBITED_TERM_SCAN: CLEAN | FOUND` typed field per turn + all DEFECT_VERDICT positions use constrained `|` enum format | — | YES | 98.33 |
| **V-03** | Lifecycle emphasis | Hard `=== DEVELOPER ARTIFACT === / === AUDITOR ARTIFACT ===` boundary; Auditor Artifact declares the Developer Artifact as its input document | YES | — | 98.33 |
| **V-04** | Role sequence + Phrasing register | V-01 Auditor per-turn annotations + V-02 typed enums; both C-12 and C-13 | YES | YES | **100** |
| **V-05** | Full synthesis | R2 V-05 7-phase gate architecture + V-01 C-12 (Phase 7 per-turn annotations) + V-02 C-13 (typed enums + per-turn PROHIBITED_TERM_SCAN) | YES | YES | **100** |

**Key design decision:** C-11 (inline per-turn conformance) and C-12 (Auditor separate audit layer) are **not mutually exclusive** — the correct architecture uses dual conformance layers. Developer self-reports inline (C-11), Auditor independently re-annotates post-trace (C-12). C-12's value is **DISCREPANCY detection**: turns where Developer reported CONFORMS but topology evidence shows a violation.

**C-13 core mechanism:** R2 V-05 had SPEC_CONFORMANCE per turn but not `PROHIBITED_TERM_SCAN`. Without a typed per-turn field, term violations in the trace body only surface at Phase 7's post-hoc scan. The per-turn `PROHIBITED_TERM_SCAN: CLEAN | FOUND` field creates point-of-production enforcement — the model evaluates vocabulary compliance as it writes each turn, not only retroactively.
or to produce it as a *separate* layer. The correct resolution is: Developer produces inline SPEC_CONFORMANCE per turn (satisfying C-11), AND the Auditor independently re-annotates those turns from a second-pass audit perspective (satisfying C-12). Two conformance layers: one produced inline by the Developer, one produced post-trace by the Auditor. The Auditor's value is catching discrepancies where the Developer's self-reported verdict is wrong.

---

## V-01: Role Sequence -- Auditor Produces Separate Per-Turn Spec Annotations

**Axis:** Role sequence -- Phase 7 Compliance Auditor scope expanded. Developer (Phases 1-6) produces the full trace including inline SPEC_CONFORMANCE per turn. Phase 7 Auditor then reads the *finished* Developer trace and produces an independent per-turn SPEC_CONFORMANCE annotation layer, plus the prohibited term audit table. Two conformance layers: Developer self-reports, Auditor independently verifies.

**Hypothesis:** R2 V-05's Auditor only scans for prohibited terms. Per-turn SPEC_CONFORMANCE is produced by the Developer role — making the Developer the sole certifier of its own spec compliance. C-12 requires role separation specifically to "prevent the producer from self-certifying." Adding per-turn annotations to Phase 7 gives the Auditor the ability to catch cases where the Developer produced a CONFORMS verdict but the topology evidence shows a deviation. The Auditor reads the Phase 2 output as a finished text, not under simulation load, and can catch spec violations the Developer missed or rationalized away. C-13 is not addressed: Developer turn blocks still use "/" syntax and there is no per-turn PROHIBITED_TERM_SCAN typed field.

```
You are running /flow:conversation for topic "{topic}".

Read: simulations/flow/conversation/{topic}-conversation-{date}.md if it exists.
Read: any signal artifacts in simulations/ relevant to "{topic}".

Roles execute in sequence: Conversation Designer (Phase 1), then Copilot Studio Developer
(Phases 2-6), then Compliance Auditor (Phase 7).
All phases are gates. Complete each phase fully before advancing.
Do not describe the topic graph abstractly -- walk it turn by turn in Phase 2.

Use Copilot Studio vocabulary exclusively throughout:
  Topics, Trigger phrases, Conditions, Fallback topics, Escalation, Session variables,
  Topic redirects, Actions, Generative answers, Knowledge sources, End of conversation nodes.
Do not use: intent, dialog, slot, NLU, chatbot, handoff, context.

---

## PHASE 1: SETUP + VOCABULARY GATE
[Conversation Designer speaks. Define agent topology, intended flow, and topology spec before
any simulation begins.]

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

Topology spec (for Phase 2 and Phase 7 SPEC_CONFORMANCE verdicts):
  CS-SPEC-01: Trigger phrase matching activates topic above confidence threshold. Sub-threshold activation is a violation.
  CS-SPEC-02: Topic-scoped session variables cleared at topic boundary (redirect or end of conversation node). Cross-boundary carry is a violation.
  CS-SPEC-03: Condition nodes require a default branch. Missing default branch routes unhandled cases to fallback topic silently.
  CS-SPEC-04: Redirect nodes do not carry topic-scoped variables to the target topic.
  CS-SPEC-05: End of conversation nodes terminate the session. No further input is processed.
  CS-SPEC-06: Escalation nodes open human agent session; agent stops responding.
  CS-SPEC-07: Fallback topic activates when no trigger phrase exceeds threshold.

Prohibited terms (must not appear anywhere in Phases 2-6; verified by Auditor in Phase 7):
  intent | dialog | slot | NLU | utterance (use "user input") | chatbot (use "agent") |
  handoff (use "escalation") | context (use "session variables") | fallback intent (use "fallback topic") | bot (use "agent")

SETUP GATE: Topic count confirmed. Turn sequence defined. Session variables enumerated. Coverage scope stated.
Topology spec stated. Prohibited terms listed. Advance to Phase 2.

## PHASE 2: CONVERSATION TRACE
[Copilot Studio Developer speaks. Walk every turn from the Phase 1 turn sequence.
No turns may be skipped or collapsed. Each turn requires its own block.
SPEC_CONFORMANCE is required on every turn -- this is the Developer's inline self-report.
The Compliance Auditor in Phase 7 will independently verify each turn using the same spec.
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
    [If DEVIATES: describe what was intended (from Phase 1) vs. what happened. Severity: P1/P2/P3]

[Repeat for every turn. Each Turn block is mandatory. SPEC_CONFORMANCE required on every turn.]

TRACE GATE: All [N] turns completed. SPEC_CONFORMANCE present on every turn. Session state carried
across all transitions. All implementation deviations flagged. Advance to Phase 3.

## PHASE 3: DEFECT MATRIX
[Complete all four rows. FOUND or CONFIRMED ABSENT -- no other verdict is valid.
"CONFIRMED ABSENT" requires an explicit scope statement. If FOUND for trigger phrase collisions,
include a disambiguation strategy with rationale.]

| Defect class | Verdict | Evidence / Confirmation |
|--------------|---------|------------------------|
| Dead ends | FOUND / CONFIRMED ABSENT | [FOUND: turn N, topic name, terminal node type, user experience. CONFIRMED ABSENT: "All [N] topic exits route to redirect node, escalation node, or fallback topic. Exit paths confirmed: [list]."] |
| Infinite loops | FOUND / CONFIRMED ABSENT | [FOUND: full loop path and triggering condition. CONFIRMED ABSENT: "Topic redirect graph is acyclic across [N] redirects traced. Redirect map: [A->B (terminal)], [C->D (terminal)]."] |
| Trigger phrase collisions | FOUND / CONFIRMED ABSENT | [FOUND: the trigger phrase, competing topics, confidence scores. Disambiguation strategy: entity enrichment / condition ordering / trigger phrase refactor -- rationale: [why this resolves it]. CONFIRMED ABSENT: "All [N] trigger phrases resolve to single topic above 0.7, runner-up below 0.4."] |
| Missing fallbacks | FOUND / CONFIRMED ABSENT | [FOUND: topic name, condition expression, unhandled branch. CS-SPEC-03 violation -- cross-reference Phase 2 SPEC_CONFORMANCE. CONFIRMED ABSENT: "All condition nodes in [N] topics carry default branch or fallback topic redirect. Default branches confirmed: [list topics]."] |

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
  Spec conformance (Developer self-report): [N] CONFORMS, [N] DEVIATES of [N+1] total turns

Findings [priority-ordered; reference topic names and node types]:
  P1 [session-breaking]: [Topic name], [node type], [what fails and user experience]
  P2 [significant degradation]: [Topic name], [node type], [what degrades]
  P3 [minor]: [Topic name], [improvement opportunity]

Amendments [each names the topic, node type, and specific Copilot Studio change]:

1. Topic "[Topic name]", [node type]: [Specific change]
   Trigger phrase sequence: "[phrase 1]" -> "[phrase 2]" -> [observable failure at this step]
   Observable failure: [What the user sees or experiences]

2. [Amendment]
   Trigger phrase sequence: [sequence] -> [failure]
   Observable failure: [What the user sees]

[Continue for all P1 and P2 findings.]

PHASE 6 GATE: Coverage report complete. Findings prioritized. All P1 and P2 amendments include
reproduction steps. Advance to Phase 7.

## PHASE 7: COMPLIANCE AUDIT
[Compliance Auditor speaks. You are reading the COMPLETED Developer output (Phases 1-6) as a
finished artifact. Do not re-simulate. You have two responsibilities:
(1) Per-turn spec conformance review -- annotate each Phase 2 turn independently.
(2) Prohibited term audit -- scan the full output for each prohibited term.
Your annotations are a separate Auditor-generated layer, distinct from the Developer's
Phase 2 SPEC_CONFORMANCE fields. Where your verdict conflicts with the Developer's,
flag the discrepancy explicitly. Role separation is the point: the Developer cannot
self-certify spec compliance.]

### AUDITOR: TOPOLOGY SPEC REFERENCE

CS-SPEC-01: Topic activation uses confidence-threshold matching. Sub-threshold activation is a violation.
CS-SPEC-02: Topic-scoped session variables are cleared when the topic ends. Carry across topic boundary is a violation.
CS-SPEC-03: Condition nodes must have a default branch. Missing default branch routes unhandled cases silently.
CS-SPEC-04: Redirect nodes do not carry topic-scoped variables to the target topic.
CS-SPEC-05: End of conversation nodes terminate the session. No further input is processed.
CS-SPEC-06: Escalation nodes open a human agent session. The Copilot Studio agent stops responding.
CS-SPEC-07: Fallback topic activates when no trigger phrase exceeds threshold.

### AUDITOR: PER-TURN SPEC CONFORMANCE ANNOTATIONS

[Read the Phase 2 CONVERSATION TRACE above as a finished document.
For each turn, produce an independent SPEC_CONFORMANCE verdict using the topology spec above.
You are auditing the Developer's output, not producing simulation. Your vantage is the full
completed trace -- you can see what happens in later turns when evaluating earlier ones.
Annotate every turn. Do not skip any. Flag any discrepancy between your verdict and the
Developer's Phase 2 verdict.]

Turn [N] -- Auditor review:
  SPEC_CONFORMANCE: CONFORMS / DEVIATES
  [CONFORMS: "CS-SPEC-01 through CS-SPEC-07 all satisfied. Developer verdict confirmed."]
  [DEVIATES: "CS-SPEC-[N] violated: [precise description of the violation found in Developer output].
    Developer reported: [CONFORMS / DEVIATES].
    Discrepancy: [YES -- Developer missed this violation / NO -- Developer correctly reported DEVIATES]"]

Turn [N+1] -- Auditor review:
  SPEC_CONFORMANCE: CONFORMS / DEVIATES
  [Same structure.]

[Continue for all turns, including the Phase 5 adversarial turn.]

Auditor spec conformance summary:
  Developer self-reported: [N] CONFORMS, [N] DEVIATES of [TOTAL] turns
  Auditor independent review: [N] CONFORMS, [N] DEVIATES of [TOTAL] turns
  Discrepancies: [Turn N: Developer reported CONFORMS, Auditor found DEVIATES -- CS-SPEC-[N]: [description] / "none"]

### AUDITOR: PROHIBITED TERM AUDIT

[Scan the full output from Phases 1-6 for each prohibited term.
Record CLEAN or FOUND for each. If FOUND, quote the exact line and name the required replacement.
This is a post-trace scan of the completed Developer output -- not an instruction.]

Scope: Phase 1 (Setup), Phase 2 (Conversation Trace), Phase 3 (Defect Matrix),
       Phase 4 (Fallback Chain), Phase 5 (Adversarial Turn), Phase 6 (Findings and Amendments)

| Prohibited term | Status | Section (if FOUND) | Line (if FOUND) | Required replacement |
|-----------------|--------|---------------------|-----------------|----------------------|
| intent          | CLEAN / FOUND | [Phase N] | [quote or "--"] | "trigger phrase" or "topic activation" |
| dialog          | CLEAN / FOUND | [Phase N] | [quote or "--"] | "conversation" or "topic sequence" |
| slot            | CLEAN / FOUND | [Phase N] | [quote or "--"] | "session variable" or "question node input" |
| NLU             | CLEAN / FOUND | [Phase N] | [quote or "--"] | "trigger phrase matching" |
| utterance       | CLEAN / FOUND | [Phase N] | [quote or "--"] | "user input" or "trigger phrase" |
| chatbot         | CLEAN / FOUND | [Phase N] | [quote or "--"] | "agent" |
| handoff         | CLEAN / FOUND | [Phase N] | [quote or "--"] | "escalation" |
| context         | CLEAN / FOUND | [Phase N] | [quote or "--"] | "session variables" |
| fallback intent | CLEAN / FOUND | [Phase N] | [quote or "--"] | "fallback topic" |
| bot             | CLEAN / FOUND | [Phase N] | [quote or "--"] | "agent" |

PROHIBITED TERM AUDIT result: CLEAN (all 10 terms absent from Phases 1-6) /
  VIOLATIONS FOUND ([N] terms require replacement before artifact is published)

PHASE 7 GATE: Prohibited term audit complete. Per-turn spec annotations complete.
Auditor discrepancies documented. Vocabulary verified.
[If violations found: list them and their replacements before writing the artifact.]

---

Write artifact: simulations/flow/conversation/{topic}-conversation-{date}.md
Frontmatter: skill, topic, date, agent_name, topic_count, topics_visited, topics_visited_pct,
trigger_phrases_exercised, turns_simulated, defects_found (list), fallback_quality,
adversarial_outcome (GRACEFUL / BRITTLE / SILENT FAILURE),
developer_spec_conformance ([N] CONFORMS of [TOTAL]),
auditor_spec_conformance ([N] CONFORMS of [TOTAL]),
auditor_discrepancies (count),
vocabulary_clean (CLEAN / VIOLATIONS [N]).
```

---

## V-02: Phrasing Register -- Full Typed Enum Architecture + PROHIBITED_TERM_SCAN Per Turn

**Axis:** Phrasing register -- typed assertion fields throughout. Two specific additions over R2 V-05: (1) `PROHIBITED_TERM_SCAN: CLEAN | FOUND["term": "line"]` in every Phase 2 turn block, and (2) defect matrix rows use typed enum syntax `DEFECT_VERDICT[class]: FOUND | CONFIRMED_ABSENT`. All other verdict positions that used prose "/" notation are converted to typed "|" enum format. This is the architectural change that satisfies C-13's requirement that "no free-text hedging permitted in verdict positions."

**Hypothesis:** R2 V-05 uses "/" notation for most verdicts (`FOUND / CONFIRMED ABSENT`, `CONFORMS / DEVIATES`) which is structurally ambiguous -- a "/" list reads as a menu of options rather than a constrained type. The "|" notation in typed fields (`FIELD: VALUE1 | VALUE2`) signals a constrained enum with exactly one valid value per instance. The critical missing piece for C-13 is the per-turn `PROHIBITED_TERM_SCAN` field. Without it, vocabulary compliance is only checked post-trace, meaning a term violation in Turn 3 passes through the Developer phase unchallenged until Phase 7. Adding `PROHIBITED_TERM_SCAN` per turn catches violations at the point of production. The combination of per-turn scanning + typed "|" enum syntax across all assertion positions satisfies C-13. C-12 is not addressed: Phase 7 Auditor still only does the prohibited term table -- no separate per-turn spec annotations.

```
You are running /flow:conversation for topic "{topic}".

Read: simulations/flow/conversation/{topic}-conversation-{date}.md if it exists.
Read: any signal artifacts in simulations/ relevant to "{topic}".

Roles execute in sequence: Conversation Designer (Phase 1), then Copilot Studio Developer
(Phases 2-6), then Compliance Auditor (Phase 7).
All phases are gates. Complete each phase fully before advancing.
Do not describe the topic graph abstractly -- walk it turn by turn in Phase 2.

Output format: typed assertion fields throughout. All verdict positions use constrained
enum syntax (VALUE_A | VALUE_B). Do not use "/" in verdict positions. Fill every field.

Use Copilot Studio vocabulary exclusively throughout:
  Topics, Trigger phrases, Conditions, Fallback topics, Escalation, Session variables,
  Topic redirects, Actions, Generative answers, Knowledge sources, End of conversation nodes.
Do not use: intent, dialog, slot, NLU, chatbot, handoff, context.

---

## PHASE 1: SETUP + VOCABULARY GATE
[Conversation Designer speaks. Define agent topology, intended flow, and topology spec before
any simulation begins.]

AGENT_NAME: [Name or description]
TOPIC_COUNT: [N]
TOPICS: [[Topic 1], [Topic 2], [Topic 3], ...]
TRIGGER_PHRASES:
  [Topic 1]: ["[phrase]", "[phrase]"]
  [Topic 2]: ["[phrase]", "[phrase]"]
FALLBACK_TOPIC: [Topic name / "System Fallback Topic" / "not configured"]
ESCALATION_PATH: [Topic name containing escalation node / "not configured"]
SESSION_VARIABLES:
  [VarName]: {scope: "topic-scoped" | "global", type: "Text" | "Number" | "Boolean", initial: "[value]" | "unset"}
KNOWLEDGE_SOURCES:
  [Name]: {type: "SharePoint" | "Dataverse" | "file", content: "[description]"} | NONE

INTENDED_FLOW:
  USER_GOAL: [What the user is trying to accomplish]
  TOPIC_SEQUENCE: [Topic A] -> [Topic B] -> [Topic C] -> [terminal: "escalation" | "end_of_conversation" | "root"]
  INTENDED_TURN_COUNT: [N]
  INTENDED_FALLBACK: [Designed behavior for off-script inputs]
  ANTICIPATED_WEAKNESSES: [Known gaps | "none identified"]

COVERAGE_SCOPE: [N] topics total. This simulation visits [N] topics ([N/total * 100]%).
UNVISITED_TOPICS: [List | "none -- full coverage"]

TOPOLOGY_SPEC:
  CS-SPEC-01: topic activation above confidence threshold
  CS-SPEC-02: topic-scoped variables cleared at topic boundary
  CS-SPEC-03: condition nodes require default branch
  CS-SPEC-04: redirect nodes do not carry topic-scoped variables
  CS-SPEC-05: end of conversation terminates session
  CS-SPEC-06: escalation opens human agent session; agent stops responding
  CS-SPEC-07: fallback topic activates when no trigger phrase exceeds threshold

PROHIBITED_TERM_LIST:
  intent | dialog | slot | NLU | utterance | chatbot | handoff | context | fallback intent | bot

SETUP_GATE: COMPLETE -- topology mapped, spec stated, prohibited terms listed.

---

## PHASE 2: CONVERSATION TRACE
[Copilot Studio Developer speaks. Walk every turn. No turns may be skipped or collapsed.
SPEC_CONFORMANCE and PROHIBITED_TERM_SCAN are required on every turn.
SPEC_CONFORMANCE: use constrained enum CONFORMS | DEVIATES[CS-SPEC-N: description].
PROHIBITED_TERM_SCAN: use constrained enum CLEAN | FOUND["term": "exact line"].]

### Turn [N] of [TOTAL]

USER_INPUT: "[what the user typed or said]"
TOPIC_ACTIVATED: [Topic name]
TRIGGER_PHRASE_MATCHED: "[exact phrase]"
CONFIDENCE: [X.XX]
RUNNER_UP_TOPIC: "[Topic name]" ([X.XX]) | NONE
NODE_PATH: [Trigger phrase node] -> [Message node | Question node | Condition node | Action node | Redirect node | End of conversation node]
ACTION_NODE: {name: "[Action name]", result: "[return value]"} | NONE
CONDITION_EVALUATED: {expression: "[expr]", branch_taken: "[label]" | "default"} | NONE
SESSION_VARIABLES_DELTA:
  [VarName]: {value: "[value]", scope: "topic-scoped" | "global", changed: true | false}
  [VarName]: {value: "awaiting_input", scope: "[scope]"}
  [VarName]: {value: "[value]", scope: "[scope]", carried_from: "Turn [N-1]"}
  [VarName]: {value: "cleared", scope: "topic-scoped", reason: "topic ended this turn"}
AGENT_RESPONSE: "[exact text shown to user]"
SPEC_CONFORMANCE: CONFORMS | DEVIATES[CS-SPEC-[N]: [description of violation]]
PROHIBITED_TERM_SCAN: CLEAN | FOUND["[term]": "[exact line where term appears in this turn block]"]
IMPLEMENTATION_VS_DESIGN: MATCHES_INTENT | DEVIATES["[intended]" vs "[actual]", severity: P1 | P2 | P3]

### Turn [N+1] of [TOTAL]
[Same structure. SPEC_CONFORMANCE and PROHIBITED_TERM_SCAN required. Do not omit.]

[Continue for all turns.]

TRACE_GATE: COMPLETE -- all [N] turns produced. SPEC_CONFORMANCE and PROHIBITED_TERM_SCAN present
on every turn. Session state tracked across all transitions.

---

## PHASE 3: DEFECT MATRIX
[All four defect classes required. DEFECT_VERDICT constrained to FOUND | CONFIRMED_ABSENT.
No other value is valid. If CONFIRMED_ABSENT, explicit scope statement required.
If FOUND for trigger phrase collisions, DISAMBIGUATION_STRATEGY is required.]

DEFECT_VERDICT[dead_ends]: FOUND | CONFIRMED_ABSENT
EVIDENCE:
  [FOUND: {turn: [N], topic: "[name]", terminal_node: "[type]", user_experience: "[description]"}]
  [CONFIRMED_ABSENT: "All [N] topics traced exit via redirect node, escalation node, or fallback topic.
    Exit paths confirmed: [list]. No topic terminates without a valid exit path."]

DEFECT_VERDICT[infinite_loops]: FOUND | CONFIRMED_ABSENT
EVIDENCE:
  [FOUND: {path: "[Topic A] redirect -> [Topic B] redirect -> [Topic A]", trigger: "[condition or trigger phrase]"}]
  [CONFIRMED_ABSENT: "Redirect graph acyclic across [N] redirects. Map: [A->B (terminal)], [C->D (terminal)]. No cycle."]

DEFECT_VERDICT[trigger_phrase_collisions]: FOUND | CONFIRMED_ABSENT
EVIDENCE:
  [FOUND: {user_input: "[phrase]", competing_topics: ["[A] ([X.XX])", "[B] ([X.XX])"],
    disambiguation_strategy: "entity_enrichment" | "condition_ordering" | "trigger_phrase_refactor",
    rationale: "[why this resolves the collision in Copilot Studio's matching model]"}]
  [CONFIRMED_ABSENT: "All [N] trigger phrases resolve to single topic above 0.7 confidence, runner-up below 0.4."]

DEFECT_VERDICT[missing_fallbacks]: FOUND | CONFIRMED_ABSENT
EVIDENCE:
  [FOUND: {topic: "[name]", condition_expression: "[expr]", unhandled_branch: "[description]",
    cs_spec_violation: "CS-SPEC-03 -- cross-reference Phase 2 SPEC_CONFORMANCE"}]
  [CONFIRMED_ABSENT: "All condition nodes in [N] topics carry default branch or fallback topic redirect.
    Default branches confirmed: [list topics and their default branch targets]."]

DEFECT_GATE: COMPLETE -- all four DEFECT_VERDICT fields present.

---

## PHASE 4: FALLBACK CHAIN TRACE
[Walk one complete fallback path from unrecognized input to terminal state.
Every step is required. Reference CS-SPEC-07 for correct fallback activation behavior.]

UNRECOGNIZED_INPUT: "[phrase that matches no trigger phrase above threshold]"
STEP[1]: {action: "trigger phrase matching", topics_evaluated: [N], matches_above_threshold: 0,
  cs_spec: "CS-SPEC-07", routes_to: "[Fallback topic / System Fallback Topic]"}
STEP[2]: {node: "[first node type]", behavior: "[what it does]"}
STEP[3]: {node: "[next node]", behavior: "[behavior]"}
...
STEP[N]: {terminal_state: "escalation" | "end_of_conversation" | "redirect_to_root",
  detail: "[closing message or target topic]"}

FALLBACK_CHAIN_QUALITY: COMPLETE | LOOPS | TRUNCATED

FALLBACK_GATE: COMPLETE -- chain traced to terminal state.

---

## PHASE 5: ADVERSARIAL TURN INJECTION
[Inject one adversarial scenario. Walk the actual agent node path.]

ADVERSARIAL_SCENARIO_TYPE: "topic_switch_mid_collection" | "unexpected_off_topic_input" | "session_timeout" | "repeated_same_input"
INJECTED_AT: Turn [N], before [VarName] is collected
ADVERSARIAL_INPUT: "[unexpected user input]"
AGENT_NODE_PATH:
  trigger_phrase_matching: [new topic activated | current topic handles it]
  node_path: [nodes executed]
  session_variables: {[VarName]: "carried" | "lost" | "reset", scope: "[scope]"}
  response_shown: "[agent response]"
OUTCOME: [describe what the user experiences]
ADVERSARIAL_ASSESSMENT: GRACEFUL | BRITTLE | SILENT_FAILURE

---

## PHASE 6: FINDINGS, COVERAGE, AND AMENDMENTS

COVERAGE_REPORT:
  topics_visited: [N] of [TOTAL] ([N/TOTAL * 100]%)
  topics_unvisited: [list | "none -- full coverage"]
  trigger_phrases_exercised: [N] of approximately [est] ([N/est * 100]%)
  turns_simulated: [N] scenario + 1 adversarial = [N+1] total
  spec_conformance: [N] CONFORMS, [N] DEVIATES of [N+1] total turns

FINDINGS:
  P1[session_breaking]: {topic: "[name]", node: "[type]", failure: "[description]", user_experience: "[description]"}
  P2[significant_degradation]: {topic: "[name]", node: "[type]", degradation: "[description]"}
  P3[minor]: {topic: "[name]", improvement: "[description]"}

AMENDMENTS:
1. {topic: "[name]", node_type: "[type]", change: "[Specific Copilot Studio change]"}
   REPRODUCTION: {trigger_phrase_sequence: ["[phrase 1]", "[phrase 2]"], failure_point: "[where it breaks]"}
   OBSERVABLE_FAILURE: "[What the user sees or experiences]"

2. {topic: "[name]", node_type: "[type]", change: "[change]"}
   REPRODUCTION: {trigger_phrase_sequence: ["[phrase]"], failure_point: "[failure]"}
   OBSERVABLE_FAILURE: "[What the user sees]"

PHASE_6_GATE: COMPLETE -- coverage report produced, findings prioritized, amendments with reproduction steps.

---

## PHASE 7: PROHIBITED TERM AUDIT
[Compliance Auditor speaks. Scan the full output from Phases 1-6 for each prohibited term.
Note: per-turn PROHIBITED_TERM_SCAN fields in Phase 2 caught violations at point of production.
This post-trace audit provides independent verification that the full output is clean.
If Phase 2 PROHIBITED_TERM_SCAN marked any turn FOUND, those violations must appear here too.]

AUDIT_SCOPE: Phase 1 through Phase 6

| TERM_ID | TERM | STATUS | SECTION (if FOUND) | LINE (if FOUND) |
|---------|------|--------|--------------------|-----------------|
| [1] | intent | CLEAN \| FOUND | [Phase N] | [quote or "--"] |
| [2] | dialog | CLEAN \| FOUND | [Phase N] | [quote or "--"] |
| [3] | slot | CLEAN \| FOUND | [Phase N] | [quote or "--"] |
| [4] | NLU | CLEAN \| FOUND | [Phase N] | [quote or "--"] |
| [5] | utterance | CLEAN \| FOUND | [Phase N] | [quote or "--"] |
| [6] | chatbot | CLEAN \| FOUND | [Phase N] | [quote or "--"] |
| [7] | handoff | CLEAN \| FOUND | [Phase N] | [quote or "--"] |
| [8] | context | CLEAN \| FOUND | [Phase N] | [quote or "--"] |
| [9] | fallback intent | CLEAN \| FOUND | [Phase N] | [quote or "--"] |
| [10] | bot | CLEAN \| FOUND | [Phase N] | [quote or "--"] |

VOCABULARY_AUDIT_RESULT: CLEAN | VIOLATIONS_FOUND[[N] terms require replacement]

PHASE_7_GATE: COMPLETE -- prohibited term audit covers Phases 1-6. Vocabulary verified.
[If violations found: list remediation before writing artifact.]

---

Write artifact: simulations/flow/conversation/{topic}-conversation-{date}.md
Frontmatter: skill, topic, date, agent_name, topic_count, topics_visited, topics_visited_pct,
trigger_phrases_exercised, turns_simulated, defects_found (list), fallback_quality,
adversarial_outcome (GRACEFUL | BRITTLE | SILENT_FAILURE),
turns_spec_conformant ([N] of [TOTAL]), spec_deviations (count),
vocabulary_audit_result (CLEAN | VIOLATIONS_FOUND[N]).
```

---

## V-03: Lifecycle Emphasis -- Hard Developer Artifact / Auditor Artifact Boundary

**Axis:** Lifecycle emphasis -- the output is explicitly structured as two physically separate documents separated by hard === markers: a DEVELOPER ARTIFACT and an AUDITOR ARTIFACT. The Auditor Artifact declares that it reads the completed Developer Artifact as its input. The Auditor produces: per-turn spec conformance annotations (keyed by turn number) and a prohibited term audit table. The developer does not know or care about the Auditor's output format; the Auditor does not re-simulate.

**Hypothesis:** The phase-7 approach in R2 V-05 and V-01 embeds the Auditor inside the same numbered-phase sequence as the Developer, which creates ambiguity about whether the Auditor is a continuation of the same cognitive task or a genuinely separate role. Hard === markers with explicit ARTIFACT labels and a role switch declaration ("You are now reading the completed Developer Artifact as input") force a cleaner cognitive shift. The Auditor Artifact begins with an explicit scope statement referencing the Developer Artifact as a finished document. This structural separation is a different enforcement mechanism for C-12 than phase numbering: the artifact boundary is visible in the output structure itself. C-13 is not addressed in this variation -- Developer turn blocks still use "/" notation rather than typed "|" enum fields.

```
You are running /flow:conversation for topic "{topic}".

Read: simulations/flow/conversation/{topic}-conversation-{date}.md if it exists.
Read: any signal artifacts in simulations/ relevant to "{topic}".

EXECUTION MODEL:
Two artifacts are produced in strict sequence:
  (1) DEVELOPER ARTIFACT -- produced by the Copilot Studio Developer role
  (2) AUDITOR ARTIFACT -- produced by the Compliance Auditor role, reading the
      completed Developer Artifact as a finished document

The Developer Artifact must be complete before the Auditor Artifact begins.
The Auditor reads -- does not re-simulate. The Auditor's per-turn annotations
are a separate layer, not embedded in the Developer's turn blocks.

Use Copilot Studio vocabulary throughout the Developer Artifact:
  Topics, Trigger phrases, Conditions, Fallback topics, Escalation, Session variables,
  Topic redirects, Actions, Generative answers, Knowledge sources, End of conversation nodes.
Do not use: intent, dialog, slot, NLU, chatbot, handoff, context.

===================================
DEVELOPER ARTIFACT
(Copilot Studio Developer role)
===================================

## DA-1: SETUP

Agent name: [Name or description]
Topics in graph: [N] -- [Topic 1], [Topic 2], [Topic 3], ...
Trigger phrases (2-3 per topic):
  [Topic 1]: "[phrase]", "[phrase]"
  [Topic 2]: "[phrase]", "[phrase]"
Fallback topic: [Name / "System Fallback Topic" / "not configured"]
Escalation path: [Topic name containing escalation node, or "not configured"]
Session variables:
  [VarName]: scope=[topic-scoped / global], type=[Text/Number/Boolean]
Knowledge sources: [Name, type, content / "none configured"]

User goal: [What the user is trying to accomplish]
Intended topic sequence: [Topic A] -> [Topic B] -> [terminal: escalation / end / root]
Intended turn count: [N]
Prohibited terms (not for use in this artifact):
  intent | dialog | slot | NLU | utterance | chatbot | handoff | context | fallback intent | bot

Topology spec (reference for turn SPEC_CONFORMANCE):
  CS-SPEC-01: topic activation above confidence threshold
  CS-SPEC-02: topic-scoped variables cleared at topic boundary
  CS-SPEC-03: condition nodes require default branch
  CS-SPEC-04: redirect nodes do not carry topic-scoped variables
  CS-SPEC-05: end of conversation terminates session
  CS-SPEC-06: escalation opens human agent session
  CS-SPEC-07: fallback topic activates when no trigger phrase exceeds threshold

Coverage scope: [N] topics in graph. This trace visits [N] ([N/total * 100]%).

## DA-2: CONVERSATION TRACE

[Walk every turn. No turns may be skipped. SPEC_CONFORMANCE required on every turn.]

Turn [N] of [TOTAL]:
  User: "[exact user input]"
  Trigger phrase matched: "[phrase]" in topic "[Topic name]"
  Confidence: [X.XX] | Runner-up: "[Topic name]" ([X.XX])
  Node path: [Trigger phrase node > Message node > Question node > Condition node >
    Action node > Redirect node > End of conversation node]
  Action node (if any): [Action name] -> result: [value] / "none"
  Condition evaluated (if any): [expression] -> branch: [label] / default branch
  Session variables after this turn:
    [VarName] = [value] (scope: topic-scoped / global, changed: yes/no)
    [VarName] = awaiting_input
    [VarName] = [carried from Turn N-1]
    [VarName] = cleared (topic-scoped, topic ended this turn)
  Response: "[agent response text]"
  SPEC_CONFORMANCE: CONFORMS / DEVIATES
    [CONFORMS: "CS-SPEC-01 through CS-SPEC-07 satisfied."]
    [DEVIATES: "Violates CS-SPEC-[N]: [description]" -- severity: P1/P2/P3]

[Repeat for every turn. SPEC_CONFORMANCE required on every turn.]

TRACE GATE: All [N] turns completed. SPEC_CONFORMANCE on every turn. Session state tracked.

## DA-3: DEFECT MATRIX

| Defect class | Verdict | Evidence / Confirmation |
|--------------|---------|------------------------|
| Dead ends | FOUND / CONFIRMED ABSENT | [Evidence or scope statement] |
| Infinite loops | FOUND / CONFIRMED ABSENT | [Evidence or scope statement. CONFIRMED ABSENT: "Redirect graph acyclic across [N] redirects. Map: [list]."] |
| Trigger phrase collisions | FOUND / CONFIRMED ABSENT | [Evidence. If FOUND: disambiguation strategy (entity enrichment / condition ordering / trigger phrase refactor) + rationale] |
| Missing fallbacks | FOUND / CONFIRMED ABSENT | [Evidence or scope statement. CS-SPEC-03 cross-reference if FOUND.] |

DEFECT GATE: All four classes with verdict + evidence.

## DA-4: FALLBACK CHAIN TRACE

Unrecognized input: "[phrase matching no trigger phrase above threshold]"
Step 1: [N] topics evaluated, 0 match -> CS-SPEC-07 activates -> [Fallback topic]
Step 2: [First fallback topic node] -- [behavior]
...
Step N: Terminal state: [escalation / end of conversation / redirect to root topic]
Fallback chain quality: COMPLETE / LOOPS / TRUNCATED

## DA-5: ADVERSARIAL TURN INJECTION

Adversarial scenario: [Type]
Injected at: Turn [N], [context]
Adversarial input: "[unexpected user input]"
Agent node path: [trace nodes executed]
Session variables: [VarName] = [carried / lost / reset]
Outcome: [what user experiences]
Assessment: GRACEFUL / BRITTLE / SILENT FAILURE

## DA-6: FINDINGS, COVERAGE, AND AMENDMENTS

Coverage:
  Topics visited: [N] of [TOTAL] ([N/TOTAL * 100]%)
  Trigger phrases exercised: [N] of approximately [est] ([N/est * 100]%)
  Turns simulated: [N] + 1 adversarial = [N+1] total
  Spec conformance (Developer): [N] CONFORMS, [N] DEVIATES of [N+1] turns

P1 [session-breaking]: [Topic], [node type], [failure and user experience]
P2 [significant degradation]: [Topic], [node type], [degradation]
P3 [minor]: [Topic], [improvement]

Amendments:
1. Topic "[Topic name]", [node type]: [Specific Copilot Studio change]
   Trigger phrase sequence: "[phrase 1]" -> "[phrase 2]" -> [observable failure]
   Observable failure: [What the user sees]

===================================
END OF DEVELOPER ARTIFACT
===================================

===================================
AUDITOR ARTIFACT
(Compliance Auditor role)
Input: Developer Artifact above (read as a finished document)
Mode: SCAN -- do not re-simulate. Annotate the completed Developer output.
===================================

## AA-1: AUDIT SCOPE STATEMENT

Artifact audited: Developer Artifact (DA-1 through DA-6)
Auditor role: Compliance Auditor
Audit mode: Read-only scan of completed Developer output
Topology spec applied: CS-SPEC-01 through CS-SPEC-07 as stated in DA-1
Prohibited terms checked: intent | dialog | slot | NLU | utterance | chatbot | handoff | context | fallback intent | bot

## AA-2: PER-TURN SPEC CONFORMANCE ANNOTATIONS

[Read DA-2 CONVERSATION TRACE (including DA-5 adversarial turn) as a finished document.
Annotate each turn independently. Cite the turn number from DA-2.
You have full-trace context: you can see later turns when evaluating earlier ones.
Where your verdict conflicts with the Developer's DA-2 SPEC_CONFORMANCE, flag the discrepancy.]

Turn [N] -- Auditor annotation:
  SPEC_CONFORMANCE: CONFORMS / DEVIATES
  [CONFORMS: "CS-SPEC-01 through CS-SPEC-07 satisfied. Developer verdict confirmed."]
  [DEVIATES: "CS-SPEC-[N] violated: [precise description].
    Developer reported CONFORMS / DEVIATES. DISCREPANCY: YES / NO."]

Turn [N+1] -- Auditor annotation:
  SPEC_CONFORMANCE: CONFORMS / DEVIATES
  [Same structure.]

[Continue for all turns, including adversarial.]

Audit conformance summary:
  Developer reported: [N] CONFORMS, [N] DEVIATES
  Auditor independent: [N] CONFORMS, [N] DEVIATES
  Discrepancies: [list / "none"]

## AA-3: PROHIBITED TERM AUDIT

[Scan DA-1 through DA-6 for each prohibited term. Record CLEAN or FOUND.
If FOUND, quote the line and name the required replacement.]

| Term | Status | Location (if FOUND) | Required replacement |
|------|--------|---------------------|----------------------|
| intent | CLEAN / FOUND | [DA-N, description] | "trigger phrase" or "topic activation" |
| dialog | CLEAN / FOUND | [DA-N, description] | "conversation" or "topic sequence" |
| slot | CLEAN / FOUND | [DA-N, description] | "session variable" or "question node input" |
| NLU | CLEAN / FOUND | [DA-N, description] | "trigger phrase matching" |
| utterance | CLEAN / FOUND | [DA-N, description] | "user input" or "trigger phrase" |
| chatbot | CLEAN / FOUND | [DA-N, description] | "agent" |
| handoff | CLEAN / FOUND | [DA-N, description] | "escalation" |
| context | CLEAN / FOUND | [DA-N, description] | "session variables" |
| fallback intent | CLEAN / FOUND | [DA-N, description] | "fallback topic" |
| bot | CLEAN / FOUND | [DA-N, description] | "agent" |

## AA-4: AUDIT VERDICT

DEVELOPER_ARTIFACT_SPEC_CONFORMANCE: [N] CONFORMS, [N] DEVIATES of [TOTAL] turns
DEVELOPER_ARTIFACT_VOCABULARY: CLEAN / VIOLATIONS_FOUND[[N] terms]
AUDITOR_DISCREPANCIES: [N] turns where Auditor and Developer verdicts conflict
AUDIT_STATUS: APPROVED (no violations, no discrepancies) / REQUIRES_REMEDIATION (violations or discrepancies found)

[If REQUIRES_REMEDIATION: list each item and required action before artifact is published.]

===================================
END OF AUDITOR ARTIFACT
===================================

---

Write artifact: simulations/flow/conversation/{topic}-conversation-{date}.md
Frontmatter: skill, topic, date, agent_name, topic_count, topics_visited, topics_visited_pct,
trigger_phrases_exercised, turns_simulated, defects_found (list), fallback_quality,
adversarial_outcome (GRACEFUL / BRITTLE / SILENT FAILURE),
developer_spec_conformance ([N] CONFORMS of [TOTAL]),
auditor_spec_conformance ([N] CONFORMS of [TOTAL]),
auditor_discrepancies (count), vocabulary_clean (CLEAN / VIOLATIONS [N]),
audit_status (APPROVED / REQUIRES_REMEDIATION).
```

---

## V-04: Role Sequence + Phrasing Register -- C-12 and C-13 Combined

**Axes:** Role sequence (V-01's Auditor per-turn annotations) + phrasing register (V-02's typed enum fields throughout). Developer produces full trace with typed assertion fields including `PROHIBITED_TERM_SCAN: CLEAN | FOUND` per turn. Phase 7 Auditor independently annotates each turn with a separate `SPEC_CONFORMANCE` verdict and produces the prohibited term audit table. Both C-12 and C-13 pass. Coverage metric and adversarial turns included from R2 V-05 base (C-08 and C-09).

**Hypothesis:** V-01 adds C-12 but leaves verdict fields as "/" prose. V-02 adds C-13 (typed enums + PROHIBITED_TERM_SCAN per turn) but leaves C-12 unaddressed (Auditor only does prohibited term table). Combining both gives: typed enum fields throughout the Developer phases (C-13) AND the Auditor independently annotating each turn with a separate conformance layer (C-12). The two axes do not conflict -- typed fields in the Developer phase make the Auditor's job easier because each field value is unambiguous. The Auditor annotation section references typed turn output rather than parsing prose. Expected score: 100 under v3 rubric.

```
You are running /flow:conversation for topic "{topic}".

Read: simulations/flow/conversation/{topic}-conversation-{date}.md if it exists.
Read: any signal artifacts in simulations/ relevant to "{topic}".

Roles execute in sequence: Conversation Designer (Phase 1), Copilot Studio Developer
(Phases 2-6), Compliance Auditor (Phase 7).
All phases are gates. Complete each phase fully before advancing.
Phase 7 reads the completed Phases 1-6 output as a finished artifact -- do not re-simulate.

Output format: typed assertion fields. All verdict positions use constrained enum syntax
(VALUE_A | VALUE_B). Brackets indicate fill-in values; pipes indicate constrained choices.

Use Copilot Studio vocabulary throughout:
  Topics, Trigger phrases, Conditions, Fallback topics, Escalation, Session variables,
  Topic redirects, Actions, Generative answers, Knowledge sources, End of conversation nodes.
Do not use: intent, dialog, slot, NLU, chatbot, handoff, context.

---

## PHASE 1: SETUP + VOCABULARY GATE
[Conversation Designer speaks.]

AGENT_NAME: [Name or description]
TOPIC_COUNT: [N]
TOPICS: [[Topic 1], [Topic 2], ...]
TRIGGER_PHRASES:
  [Topic 1]: ["[phrase]", "[phrase]"]
  [Topic 2]: ["[phrase]", "[phrase]"]
FALLBACK_TOPIC: [name | "System Fallback Topic" | "not configured"]
ESCALATION_PATH: [Topic name | "not configured"]
SESSION_VARIABLES:
  [VarName]: {scope: "topic-scoped" | "global", type: "Text" | "Number" | "Boolean"}
KNOWLEDGE_SOURCES: [{name: "[Name]", type: "SharePoint" | "Dataverse" | "file", content: "[desc]"}] | NONE

INTENDED_FLOW:
  USER_GOAL: [What the user is trying to accomplish]
  TOPIC_SEQUENCE: [A] -> [B] -> [terminal: "escalation" | "end_of_conversation" | "root"]
  INTENDED_TURN_COUNT: [N]
  ANTICIPATED_WEAKNESSES: [gaps | "none identified"]

COVERAGE_SCOPE: [N] topics total. Simulation visits [N] ([N/total * 100]%).

TOPOLOGY_SPEC:
  CS-SPEC-01: topic activation above confidence threshold
  CS-SPEC-02: topic-scoped variables cleared at topic boundary
  CS-SPEC-03: condition nodes require default branch
  CS-SPEC-04: redirect nodes do not carry topic-scoped variables
  CS-SPEC-05: end of conversation terminates session
  CS-SPEC-06: escalation opens human agent session; agent stops responding
  CS-SPEC-07: fallback topic activates when no trigger phrase exceeds threshold

PROHIBITED_TERM_LIST:
  [1] intent | [2] dialog | [3] slot | [4] NLU | [5] utterance |
  [6] chatbot | [7] handoff | [8] context | [9] fallback intent | [10] bot

SETUP_GATE: COMPLETE

---

## PHASE 2: CONVERSATION TRACE
[Copilot Studio Developer speaks. Walk every turn. Each turn block is mandatory.
SPEC_CONFORMANCE and PROHIBITED_TERM_SCAN are required on every turn.
Phase 7 Auditor will independently re-annotate each turn -- these fields are Developer self-reports.]

### Turn [N] of [TOTAL]

USER_INPUT: "[what the user typed or said]"
TOPIC_ACTIVATED: [Topic name]
TRIGGER_PHRASE_MATCHED: "[exact phrase]"
CONFIDENCE: [X.XX]
RUNNER_UP: {topic: "[name]", confidence: [X.XX]} | NONE
NODE_PATH: [Trigger phrase node] -> [Message | Question | Condition | Action | Redirect | End of conversation]
ACTION_NODE: {name: "[name]", result: "[value]"} | NONE
CONDITION_EVALUATED: {expression: "[expr]", branch: "[label]" | "default"} | NONE
SESSION_VARIABLES_DELTA:
  [VarName]: {value: "[value]", scope: "topic-scoped" | "global", changed: true | false}
  [VarName]: {value: "awaiting_input", scope: "[scope]"}
  [VarName]: {value: "[value]", carried_from: "Turn [N-1]"}
  [VarName]: {value: "cleared", scope: "topic-scoped", reason: "topic ended"}
AGENT_RESPONSE: "[exact text shown to user]"
SPEC_CONFORMANCE: CONFORMS | DEVIATES[CS-SPEC-[N]: [description of violation], severity: P1 | P2 | P3]
PROHIBITED_TERM_SCAN: CLEAN | FOUND["[term]": "[exact line in this turn block]"]

### Turn [N+1] of [TOTAL]
[Same structure. Both typed fields required. Do not omit.]

[Continue for all turns.]

TRACE_GATE: COMPLETE -- all [N] turns. SPEC_CONFORMANCE and PROHIBITED_TERM_SCAN on every turn.
Session state tracked. Advance to Phase 3.

---

## PHASE 3: DEFECT MATRIX
[All four DEFECT_VERDICT fields required. Constrained to FOUND | CONFIRMED_ABSENT only.]

DEFECT_VERDICT[dead_ends]: FOUND | CONFIRMED_ABSENT
EVIDENCE: [FOUND: {turn: [N], topic: "[name]", node: "[type]", user_experience: "[desc]"}]
          [CONFIRMED_ABSENT: "All [N] topics exit via redirect, escalation, or fallback topic.
            Exits: [list]. No dead-end exit found."]

DEFECT_VERDICT[infinite_loops]: FOUND | CONFIRMED_ABSENT
EVIDENCE: [FOUND: {path: "[A] -> [B] -> [A]", trigger: "[condition]"}]
          [CONFIRMED_ABSENT: "Redirect graph acyclic across [N] redirects. Map: [list]. No cycle."]

DEFECT_VERDICT[trigger_phrase_collisions]: FOUND | CONFIRMED_ABSENT
EVIDENCE: [FOUND: {user_input: "[phrase]", competing_topics: ["[A] ([X.XX])", "[B] ([X.XX])"],
            disambiguation_strategy: "entity_enrichment" | "condition_ordering" | "trigger_phrase_refactor",
            rationale: "[why this resolves it in Copilot Studio's matching model]"}]
          [CONFIRMED_ABSENT: "All [N] phrases resolve to single topic >0.7, runner-up <0.4."]

DEFECT_VERDICT[missing_fallbacks]: FOUND | CONFIRMED_ABSENT
EVIDENCE: [FOUND: {topic: "[name]", expression: "[expr]", unhandled_branch: "[desc]",
            cs_spec_cross_ref: "CS-SPEC-03"}]
          [CONFIRMED_ABSENT: "All condition nodes in [N] topics carry default branch or fallback redirect.
            Default branches: [list]."]

DEFECT_GATE: COMPLETE

---

## PHASE 4: FALLBACK CHAIN TRACE
[Walk one complete fallback path to terminal state. Reference CS-SPEC-07.]

UNRECOGNIZED_INPUT: "[phrase matching no trigger phrase above threshold]"
STEP[1]: {action: "trigger phrase matching", topics_evaluated: [N], matches: 0,
  cs_spec: "CS-SPEC-07", routes_to: "[Fallback topic]"}
STEP[2]: {node: "[type]", behavior: "[description]"}
...
STEP[N]: {terminal_state: "escalation" | "end_of_conversation" | "redirect_to_root",
  detail: "[closing message or target topic]"}

FALLBACK_CHAIN_QUALITY: COMPLETE | LOOPS | TRUNCATED

FALLBACK_GATE: COMPLETE

---

## PHASE 5: ADVERSARIAL TURN INJECTION
[Inject one adversarial scenario. Walk the actual node path.]

ADVERSARIAL_TYPE: "topic_switch_mid_collection" | "unexpected_off_topic_input" | "session_timeout" | "repeated_same_input"
INJECTED_AT: Turn [N] of scenario, context: [why this is adversarial here]
ADVERSARIAL_INPUT: "[unexpected user input]"
NODE_PATH_ACTUAL: [trace nodes executed in response]
SESSION_VARIABLE_OUTCOME: {[VarName]: "carried" | "lost" | "reset", scope: "[scope]"}
RESPONSE_SHOWN: "[agent response]"
USER_EXPERIENCE: [describe what happens to the user]
ADVERSARIAL_ASSESSMENT: GRACEFUL | BRITTLE | SILENT_FAILURE

---

## PHASE 6: FINDINGS, COVERAGE, AND AMENDMENTS

COVERAGE_REPORT:
  TOPICS_VISITED: [N] of [TOTAL] ([N/TOTAL * 100]%)
  TOPICS_UNVISITED: [list | "none -- full coverage"]
  TRIGGER_PHRASES_EXERCISED: [N] of approximately [est] ([N/est * 100]%)
  TURNS_TOTAL: [N] scenario + 1 adversarial = [N+1]
  SPEC_CONFORMANCE_SUMMARY: [N] CONFORMS, [N] DEVIATES of [N+1] turns (Developer self-report)

FINDINGS:
  P1[session_breaking]: {topic: "[name]", node: "[type]", failure: "[desc]", user_experience: "[desc]"}
  P2[degradation]: {topic: "[name]", node: "[type]", degradation: "[desc]"}
  P3[minor]: {topic: "[name]", improvement: "[desc]"}

AMENDMENTS:
1. {topic: "[name]", node_type: "[type]", change: "[Specific Copilot Studio change]"}
   REPRODUCTION: {sequence: ["[phrase 1]", "[phrase 2]"], failure_point: "[where it breaks]"}
   OBSERVABLE_FAILURE: "[What the user sees]"

[Continue for all P1 and P2 findings.]

PHASE_6_GATE: COMPLETE

---

## PHASE 7: COMPLIANCE AUDIT
[Compliance Auditor speaks. You are reading the COMPLETED output from Phases 1-6 as a
finished artifact. You have two tasks:
(1) Independently annotate each Phase 2 turn with a SPEC_CONFORMANCE verdict.
    This is a separate audit layer -- not embedded in the Developer's typed turn blocks.
    You are not re-simulating. You are reading the Developer's NODE_PATH, SESSION_VARIABLES_DELTA,
    and AGENT_RESPONSE for each turn and applying CS-SPEC-01 through CS-SPEC-07.
    Flag discrepancies where the Developer's SPEC_CONFORMANCE field is wrong.
(2) Post-trace prohibited term audit -- scan the full output for prohibited terms.
Role separation is structural: the Developer produced Phase 2 under simulation load.
You read the finished output with full-trace context and scan-mode attention.]

### AUDITOR: TOPOLOGY SPEC

CS-SPEC-01: topic activation above confidence threshold
CS-SPEC-02: topic-scoped variables cleared at topic boundary
CS-SPEC-03: condition nodes require default branch
CS-SPEC-04: redirect nodes do not carry topic-scoped variables
CS-SPEC-05: end of conversation terminates session
CS-SPEC-06: escalation opens human agent session
CS-SPEC-07: fallback topic activates when no trigger phrase exceeds threshold

### AUDITOR: PER-TURN SPEC CONFORMANCE ANNOTATIONS

[Read Phase 2 CONVERSATION TRACE (all turns including Phase 5 adversarial) as finished output.
Annotate every turn. Key by turn number. Do not skip any.]

Turn [N] -- Auditor:
  SPEC_CONFORMANCE: CONFORMS | DEVIATES[CS-SPEC-[N]: [precise description from reading Developer output]]
  DEVELOPER_VERDICT: CONFORMS | DEVIATES[as reported in Phase 2]
  DISCREPANCY: NONE | FOUND["Developer reported [X], Auditor finds [Y]: [explanation]"]

Turn [N+1] -- Auditor:
  SPEC_CONFORMANCE: CONFORMS | DEVIATES[...]
  DEVELOPER_VERDICT: CONFORMS | DEVIATES[...]
  DISCREPANCY: NONE | FOUND[...]

[Continue for all turns, including adversarial turn from Phase 5.]

AUDIT_CONFORMANCE_SUMMARY:
  developer_self_reported: [N] CONFORMS, [N] DEVIATES of [TOTAL]
  auditor_independent: [N] CONFORMS, [N] DEVIATES of [TOTAL]
  discrepancies: [N] | NONE

### AUDITOR: PROHIBITED TERM AUDIT

[Post-trace scan of Phases 1-6. Per-turn PROHIBITED_TERM_SCAN fields in Phase 2 caught
inline violations. This audit verifies the full output independently.]

| TERM_ID | TERM | AUDIT_STATUS | SECTION (if FOUND) | LINE (if FOUND) |
|---------|------|-------------|---------------------|-----------------|
| [1] | intent | CLEAN \| FOUND | [Phase N] | [quote or "--"] |
| [2] | dialog | CLEAN \| FOUND | [Phase N] | [quote or "--"] |
| [3] | slot | CLEAN \| FOUND | [Phase N] | [quote or "--"] |
| [4] | NLU | CLEAN \| FOUND | [Phase N] | [quote or "--"] |
| [5] | utterance | CLEAN \| FOUND | [Phase N] | [quote or "--"] |
| [6] | chatbot | CLEAN \| FOUND | [Phase N] | [quote or "--"] |
| [7] | handoff | CLEAN \| FOUND | [Phase N] | [quote or "--"] |
| [8] | context | CLEAN \| FOUND | [Phase N] | [quote or "--"] |
| [9] | fallback intent | CLEAN \| FOUND | [Phase N] | [quote or "--"] |
| [10] | bot | CLEAN \| FOUND | [Phase N] | [quote or "--"] |

VOCABULARY_AUDIT_RESULT: CLEAN | VIOLATIONS_FOUND[[N] terms]

PHASE_7_GATE: COMPLETE -- per-turn annotations done, prohibited term audit done,
discrepancies documented. Vocabulary verified.
[If REQUIRES_REMEDIATION: list each violation and required action before writing artifact.]

---

Write artifact: simulations/flow/conversation/{topic}-conversation-{date}.md
Frontmatter: skill, topic, date, agent_name, topic_count, topics_visited, topics_visited_pct,
trigger_phrases_exercised, turns_simulated, defects_found (list), fallback_quality,
adversarial_outcome (GRACEFUL | BRITTLE | SILENT_FAILURE),
developer_spec_conformance ([N] CONFORMS of [TOTAL]),
auditor_spec_conformance ([N] CONFORMS of [TOTAL]),
auditor_discrepancies (count),
vocabulary_audit_result (CLEAN | VIOLATIONS_FOUND[N]).
```

---

## V-05: Full Synthesis -- R2 V-05 + C-12 + C-13

**Axes:** All axes combined. Starts from R2 V-05 (7-phase gate architecture, scored 100 under v2). Two targeted additions: (1) Phase 7 Compliance Auditor scope expanded to include per-turn SPEC_CONFORMANCE annotations as a separate audit layer (C-12), and (2) PROHIBITED_TERM_SCAN typed enum added per turn in Phase 2, and all verdict positions converted to constrained "|" enum format (C-13). Every other phase from R2 V-05 is preserved. Gate architecture, coverage metric, adversarial, findings/amendments structure -- all unchanged.

**Hypothesis:** R2 V-05's seven-phase gate architecture is proven: it scored 100 under v2. The gap under v3 is precisely two missing mechanisms. C-12: Phase 7 Auditor only produced the prohibited term table; Developer self-certified spec compliance. C-13: verdict fields used "/" notation rather than typed "|" enums; no per-turn PROHIBITED_TERM_SCAN field. The minimum-change path to 100 under v3 is: expand Phase 7's Auditor section with per-turn annotations (C-12), and add PROHIBITED_TERM_SCAN per turn + convert "/" to "|" in all assertion positions (C-13). No phases are removed. No gates are changed. The additions slot cleanly into the existing architecture because Phase 7 already declares the Auditor role and the topology spec, and Phase 2 already has SPEC_CONFORMANCE per turn -- both changes are additive to an existing structure that works.

```
You are running /flow:conversation for topic "{topic}".

Read: simulations/flow/conversation/{topic}-conversation-{date}.md if it exists.
Read: any signal artifacts in simulations/ relevant to "{topic}".

Roles execute in sequence: Conversation Designer (Phase 1), Copilot Studio Developer
(Phases 2-6), Compliance Auditor (Phase 7).
All phases are gates. Complete each phase fully before advancing.
Do not describe the topic graph abstractly -- walk it turn by turn in Phase 2.
Phase 7 reads the COMPLETED Phases 1-6 output as a finished artifact. Do not re-simulate.

Output format: typed assertion fields throughout. All verdict positions use constrained
enum syntax (VALUE_A | VALUE_B). Do not use "/" in verdict positions.

Use Copilot Studio vocabulary exclusively:
  Topics, Trigger phrases, Conditions, Fallback topics, Escalation, Session variables,
  Topic redirects, Actions, Generative answers, Knowledge sources, End of conversation nodes.
Do not use: intent, dialog, slot, NLU, chatbot, handoff, context.

---

## PHASE 1: SETUP + VOCABULARY GATE
[Conversation Designer speaks. Define agent topology, intended flow, and topology spec
before any simulation begins.]

AGENT_NAME: [Name or description]
TOPIC_COUNT: [N]
TOPICS: [[Topic 1], [Topic 2], [Topic 3], ...]
TRIGGER_PHRASES:
  [Topic 1]: ["[phrase]", "[phrase]"]
  [Topic 2]: ["[phrase]", "[phrase]"]
FALLBACK_TOPIC: [name | "System Fallback Topic" | "not configured"]
ESCALATION_PATH: [Topic name | "not configured"]
SESSION_VARIABLES:
  [VarName]: {scope: "topic-scoped" | "global", type: "Text" | "Number" | "Boolean", initial: "[value]" | "unset"}
KNOWLEDGE_SOURCES:
  [Name]: {type: "SharePoint" | "Dataverse" | "file", content: "[brief description]"} | NONE

INTENDED_FLOW:
  USER_GOAL: [What the user is trying to accomplish]
  TOPIC_SEQUENCE: [Topic A] -> [Topic B] -> [Topic C] -> [terminal: "escalation" | "end_of_conversation" | "root"]
  INTENDED_TURN_COUNT: [N]
  INTENDED_FALLBACK: [Designed behavior for off-script inputs]
  ANTICIPATED_WEAKNESSES: [Known gaps | "none identified"]

COVERAGE_SCOPE: [N] topics total. Simulation visits [N] ([N/total * 100]%).
UNVISITED_TOPICS: [list | "none -- full coverage"]

TOPOLOGY_SPEC:
  CS-SPEC-01: Trigger phrase matching activates topic above confidence threshold. Sub-threshold activation is a violation.
  CS-SPEC-02: Topic-scoped session variables cleared at topic boundary (redirect or end of conversation). Cross-boundary carry is a violation.
  CS-SPEC-03: Condition nodes require a default branch. Missing default routes unhandled cases silently.
  CS-SPEC-04: Redirect nodes do not carry topic-scoped variables to target topic.
  CS-SPEC-05: End of conversation nodes terminate session. No further input processed.
  CS-SPEC-06: Escalation nodes open human agent session. Copilot Studio agent stops responding.
  CS-SPEC-07: Fallback topic activates when no trigger phrase exceeds threshold.

PROHIBITED_TERM_LIST:
  [1] intent -> "trigger phrase" or "topic activation"
  [2] dialog -> "conversation" or "topic sequence"
  [3] slot -> "session variable" or "question node input"
  [4] NLU -> "trigger phrase matching"
  [5] utterance -> "user input" or "trigger phrase"
  [6] chatbot -> "agent"
  [7] handoff -> "escalation"
  [8] context -> "session variables"
  [9] fallback intent -> "fallback topic"
  [10] bot -> "agent"

SETUP_GATE: COMPLETE -- topology mapped, turn sequence defined, session variables enumerated,
coverage scope stated, topology spec stated (CS-SPEC-01..07), prohibited terms listed.
Advance to Phase 2.

---

## PHASE 2: CONVERSATION TRACE
[Copilot Studio Developer speaks. Walk every turn from the Phase 1 turn sequence.
No turns may be skipped or collapsed. Each turn requires its own block.
SPEC_CONFORMANCE and PROHIBITED_TERM_SCAN are required on every turn.
These are Developer self-reports. Phase 7 Auditor independently reviews all turns.
Note: SPEC_CONFORMANCE uses constrained enum CONFORMS | DEVIATES[CS-SPEC-N: description].
      PROHIBITED_TERM_SCAN uses constrained enum CLEAN | FOUND["term": "line"].]

### Turn [N] of [TOTAL]

USER_INPUT: "[what the user typed or said]"
TOPIC_ACTIVATED: [Topic name]
TRIGGER_PHRASE_MATCHED: "[exact phrase]"
CONFIDENCE: [X.XX]
RUNNER_UP: {topic: "[name]", confidence: [X.XX]} | NONE
NODE_PATH: [Trigger phrase node] -> [Message | Question | Condition | Action | Redirect | End of conversation]
ACTION_NODE: {name: "[name]", result: "[value]"} | NONE
CONDITION_EVALUATED: {expression: "[expr]", branch: "[label]" | "default"} | NONE
SESSION_VARIABLES_DELTA:
  [VarName]: {value: "[value]", scope: "topic-scoped" | "global", changed: true | false}
  [VarName]: {value: "awaiting_input", scope: "[scope]"}
  [VarName]: {value: "[value]", carried_from: "Turn [N-1]"}
  [VarName]: {value: "cleared", scope: "topic-scoped", reason: "topic ended this turn"}
AGENT_RESPONSE: "[exact text shown to user]"
SPEC_CONFORMANCE: CONFORMS | DEVIATES[CS-SPEC-[N]: [exact description of violation], severity: P1 | P2 | P3]
PROHIBITED_TERM_SCAN: CLEAN | FOUND["[term]": "[exact line in this turn block where term appears]"]
IMPLEMENTATION_VS_DESIGN: MATCHES_INTENT | DEVIATES["intended: [from Phase 1]" vs "actual: [what happened]", severity: P1 | P2 | P3]

### Turn [N+1] of [TOTAL]
[Same structure. SPEC_CONFORMANCE, PROHIBITED_TERM_SCAN, and IMPLEMENTATION_VS_DESIGN required.
Do not omit any field.]

[Continue for all turns. Each turn block is mandatory.]

TRACE_GATE: COMPLETE -- all [N] turns produced. SPEC_CONFORMANCE | PROHIBITED_TERM_SCAN |
IMPLEMENTATION_VS_DESIGN present on every turn. Session state tracked across all transitions.
Advance to Phase 3.

---

## PHASE 3: DEFECT MATRIX
[All four DEFECT_VERDICT fields required. Constrained to FOUND | CONFIRMED_ABSENT only.
CONFIRMED_ABSENT requires explicit scope statement. If FOUND for trigger phrase collisions,
DISAMBIGUATION_STRATEGY is required with rationale.]

DEFECT_VERDICT[dead_ends]: FOUND | CONFIRMED_ABSENT
EVIDENCE:
  [FOUND: {turn: [N], topic: "[name]", terminal_node: "[type]",
    user_experience: "[what user sees -- session hangs / generic error / silent exit]"}]
  [CONFIRMED_ABSENT: "All [N] topics traced exit via redirect node, escalation node, or fallback topic.
    Exits confirmed: [list]. No topic terminates without a valid exit path."]

DEFECT_VERDICT[infinite_loops]: FOUND | CONFIRMED_ABSENT
EVIDENCE:
  [FOUND: {path: "[Topic A] redirect -> [Topic B] redirect -> [Topic A]",
    trigger: "[condition or trigger phrase that causes the loop]"}]
  [CONFIRMED_ABSENT: "Topic redirect graph is acyclic across [N] redirects. No cycle.
    Redirect map: [A->B (terminal)], [C->D (terminal)]."]

DEFECT_VERDICT[trigger_phrase_collisions]: FOUND | CONFIRMED_ABSENT
EVIDENCE:
  [FOUND: {user_input: "[phrase]", competing_topics: ["[A] ([X.XX])", "[B] ([X.XX])"],
    disambiguation_strategy: "entity_enrichment" | "condition_ordering" | "trigger_phrase_refactor",
    rationale: "[why this resolves the collision in Copilot Studio's matching model]"}]
  [CONFIRMED_ABSENT: "All [N] trigger phrases tested resolve to single topic above 0.7 confidence.
    Runner-up below 0.4 on all inputs tested."]

DEFECT_VERDICT[missing_fallbacks]: FOUND | CONFIRMED_ABSENT
EVIDENCE:
  [FOUND: {topic: "[name]", condition_expression: "[expr]", unhandled_branch: "[description]",
    cs_spec_cross_ref: "CS-SPEC-03 violation -- see Phase 2 SPEC_CONFORMANCE for this turn"}]
  [CONFIRMED_ABSENT: "All condition nodes in [N] topics carry default branch or explicit fallback
    topic redirect. Default branches confirmed: [list topics and their default branch targets]."]

DEFECT_GATE: COMPLETE -- all four DEFECT_VERDICT fields present with evidence. Advance to Phase 4.

---

## PHASE 4: FALLBACK CHAIN TRACE
[Walk one complete fallback path from unrecognized input to terminal state.
Every step is required. Do not stop at first fallback topic activation.
Reference CS-SPEC-07 for correct fallback activation behavior.]

UNRECOGNIZED_INPUT: "[phrase that matches no trigger phrase above threshold]"
STEP[1]: {action: "trigger phrase matching", topics_evaluated: [N], matches_above_threshold: 0,
  cs_spec: "CS-SPEC-07 activates", routes_to: "[Fallback topic | System Fallback Topic]"}
STEP[2]: {node: "[first fallback topic node type]", behavior: "[what it does]"}
STEP[3]: {node: "[next node]", behavior: "[behavior]"}
...
STEP[N]: {terminal_state: "escalation" | "end_of_conversation" | "redirect_to_root",
  detail: "[closing message or target topic name]"}

FALLBACK_CHAIN_QUALITY: COMPLETE | LOOPS | TRUNCATED

FALLBACK_GATE: COMPLETE -- chain traced to terminal state. Quality verdict recorded. Advance to Phase 5.

---

## PHASE 5: ADVERSARIAL TURN INJECTION
[Inject one adversarial scenario: unexpected user input mid-flow, topic switch during session
variable collection, session variable loss, or session timeout. Walk the actual node path.]

ADVERSARIAL_TYPE: "topic_switch_mid_collection" | "unexpected_off_topic_input" | "session_timeout" | "repeated_same_input"
INJECTION_POINT: Turn [N] of scenario, before [VarName] is collected / after [action] completes
ADVERSARIAL_INPUT: "[the unexpected user input]"
AGENT_NODE_PATH_ACTUAL:
  trigger_phrase_matching: [new topic activates | current topic handles it | fallback topic activates]
  nodes_executed: [node chain]
  session_variable_outcome: {[VarName]: "carried" | "lost" | "reset", scope: "[scope]"}
  response_shown: "[agent response]"
USER_EXPERIENCE: [what happens to the user -- conversation recovers / loops / ends abruptly / loses data]
ADVERSARIAL_ASSESSMENT: GRACEFUL | BRITTLE | SILENT_FAILURE

---

## PHASE 6: FINDINGS, COVERAGE, AND AMENDMENTS

COVERAGE_REPORT:
  TOPICS_VISITED: [N] of [TOTAL] ([N/TOTAL * 100]%)
  TOPICS_UNVISITED: [list | "none -- full coverage achieved"]
  TRIGGER_PHRASES_EXERCISED: [N] of approximately [est] ([N/est * 100]%)
  TURNS_TOTAL: [N] scenario + 1 adversarial = [N+1] total
  SPEC_CONFORMANCE_SUMMARY: [N] CONFORMS, [N] DEVIATES of [N+1] turns (Developer self-report;
    Auditor independent review in Phase 7)

FINDINGS:
  P1[session_breaking]: {topic: "[name]", node: "[type]", failure: "[description]", user_experience: "[description]"}
  P2[significant_degradation]: {topic: "[name]", node: "[type]", degradation: "[description]"}
  P3[minor]: {topic: "[name]", improvement_opportunity: "[description]"}

AMENDMENTS:
1. {topic: "[name]", node_type: "[type]",
    change: "[Specific Copilot Studio change -- e.g., 'add redirect node to [Fallback topic] after Question node when [VarName] null after 2 attempts' / 'add default branch to Condition node on [expression]' / 'refactor trigger phrases: remove [phrase] from [Topic], add entity question node']"}
   REPRODUCTION: {sequence: ["[phrase 1]", "[phrase 2]"], failure_point: "[where it breaks]"}
   OBSERVABLE_FAILURE: "[What the user sees or experiences]"

2. {topic: "[name]", node_type: "[type]", change: "[change]"}
   REPRODUCTION: {sequence: ["[phrase]"], failure_point: "[failure]"}
   OBSERVABLE_FAILURE: "[What the user sees]"

[Continue for all P1 and P2 findings.]

PHASE_6_GATE: COMPLETE -- coverage report done, findings prioritized, all P1/P2 amendments
have reproduction steps. Advance to Phase 7.

---

## PHASE 7: COMPLIANCE AUDIT
[Compliance Auditor speaks. You are reading the COMPLETED output from Phases 1-6 as a
finished artifact. You have two responsibilities:

(1) PER-TURN SPEC CONFORMANCE ANNOTATIONS -- independently annotate each Phase 2 turn
    (and the Phase 5 adversarial turn). This is a separate Auditor-generated audit layer,
    distinct from the Developer's Phase 2 SPEC_CONFORMANCE fields. You are reading the
    Developer's NODE_PATH, SESSION_VARIABLES_DELTA, and AGENT_RESPONSE for each turn and
    applying CS-SPEC-01 through CS-SPEC-07 independently. You have full-trace context:
    you can see what happens in later turns when evaluating earlier ones.
    Where your verdict conflicts with the Developer's, flag the discrepancy. The purpose
    of role separation is to catch cases where the Developer self-certified CONFORMS but
    the topology evidence shows a violation.

(2) PROHIBITED TERM AUDIT -- scan the full Phases 1-6 output for each prohibited term.
    The Developer's per-turn PROHIBITED_TERM_SCAN fields caught inline violations.
    This post-trace audit provides independent verification of the full completed output.

Do not re-simulate. Operate entirely from the finished output above.]

### AUDITOR: TOPOLOGY SPEC REFERENCE

CS-SPEC-01: topic activation above confidence threshold
CS-SPEC-02: topic-scoped variables cleared at topic boundary
CS-SPEC-03: condition nodes require default branch
CS-SPEC-04: redirect nodes do not carry topic-scoped variables
CS-SPEC-05: end of conversation terminates session
CS-SPEC-06: escalation opens human agent session; agent stops responding
CS-SPEC-07: fallback topic activates when no trigger phrase exceeds threshold

### AUDITOR: PER-TURN SPEC CONFORMANCE ANNOTATIONS

[Annotate every turn in Phase 2 CONVERSATION TRACE plus the Phase 5 adversarial turn.
Key by turn number. Annotate all turns -- do not skip any.]

Turn [N] -- Auditor:
  SPEC_CONFORMANCE: CONFORMS | DEVIATES[CS-SPEC-[N]: [precise description from reading Developer output]]
  DEVELOPER_PHASE2_VERDICT: CONFORMS | DEVIATES[as stated in Phase 2]
  DISCREPANCY: NONE | FOUND["Developer reported [verdict], Auditor finds [verdict]. [Explanation of what the Developer missed or misclassified.]"]

Turn [N+1] -- Auditor:
  SPEC_CONFORMANCE: CONFORMS | DEVIATES[...]
  DEVELOPER_PHASE2_VERDICT: CONFORMS | DEVIATES[...]
  DISCREPANCY: NONE | FOUND[...]

[Continue for all turns, including Phase 5 adversarial turn.]

AUDIT_CONFORMANCE_SUMMARY:
  DEVELOPER_REPORTED: [N] CONFORMS, [N] DEVIATES of [TOTAL] turns
  AUDITOR_INDEPENDENT: [N] CONFORMS, [N] DEVIATES of [TOTAL] turns
  DISCREPANCY_COUNT: [N] | NONE
  DISCREPANT_TURNS: [list turn numbers with explanation | "none"]

### AUDITOR: PROHIBITED TERM AUDIT

[Post-trace scan of Phases 1-6. Per-turn PROHIBITED_TERM_SCAN fields in Phase 2 caught
inline violations at point of production. This audit verifies the complete output
independently. If Phase 2 PROHIBITED_TERM_SCAN marked any turn FOUND, those violations
must appear here with section and line confirmed.]

AUDIT_SCOPE: Phase 1 (Setup), Phase 2 (Conversation Trace), Phase 3 (Defect Matrix),
  Phase 4 (Fallback Chain), Phase 5 (Adversarial Turn), Phase 6 (Findings and Amendments)

| TERM_ID | TERM | AUDIT_STATUS | SECTION (if FOUND) | LINE (if FOUND) | REQUIRED_REPLACEMENT |
|---------|------|-------------|---------------------|-----------------|----------------------|
| [1] | intent | CLEAN \| FOUND | [Phase N] | [quote or "--"] | "trigger phrase" or "topic activation" |
| [2] | dialog | CLEAN \| FOUND | [Phase N] | [quote or "--"] | "conversation" or "topic sequence" |
| [3] | slot | CLEAN \| FOUND | [Phase N] | [quote or "--"] | "session variable" or "question node input" |
| [4] | NLU | CLEAN \| FOUND | [Phase N] | [quote or "--"] | "trigger phrase matching" |
| [5] | utterance | CLEAN \| FOUND | [Phase N] | [quote or "--"] | "user input" or "trigger phrase" |
| [6] | chatbot | CLEAN \| FOUND | [Phase N] | [quote or "--"] | "agent" |
| [7] | handoff | CLEAN \| FOUND | [Phase N] | [quote or "--"] | "escalation" |
| [8] | context | CLEAN \| FOUND | [Phase N] | [quote or "--"] | "session variables" |
| [9] | fallback intent | CLEAN \| FOUND | [Phase N] | [quote or "--"] | "fallback topic" |
| [10] | bot | CLEAN \| FOUND | [Phase N] | [quote or "--"] | "agent" |

VOCABULARY_AUDIT_RESULT: CLEAN | VIOLATIONS_FOUND[[N] terms require replacement]

PHASE_7_GATE: COMPLETE -- per-turn spec annotations done (all [N+1] turns annotated),
prohibited term audit done (Phases 1-6 scanned), discrepancies documented, vocabulary verified.
[If VOCABULARY_AUDIT_RESULT is VIOLATIONS_FOUND: list all violations and replacements before
writing the artifact.]

---

Write artifact: simulations/flow/conversation/{topic}-conversation-{date}.md
Frontmatter: skill, topic, date, agent_name, topic_count, topics_visited, topics_visited_pct,
trigger_phrases_exercised, turns_simulated, defects_found (list), fallback_quality,
adversarial_outcome (GRACEFUL | BRITTLE | SILENT_FAILURE),
developer_spec_conformance ([N] CONFORMS of [TOTAL]),
auditor_spec_conformance ([N] CONFORMS of [TOTAL]),
auditor_discrepancy_count ([N] | 0),
vocabulary_audit_result (CLEAN | VIOLATIONS_FOUND[N]).
```

---

## Round 3 Design Notes

### Rubric coverage by variation (v3 criteria)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 Dialog path as turns | Phase 2 mandatory turn blocks | Typed TURN[N] blocks required | DA-2 mandatory turn blocks | Phase 2 typed turn blocks | Phase 2 typed turn blocks |
| C-02 All four defect classes | Phase 3 matrix, 4 rows | DEFECT_VERDICT[x] constrained enum | DA-3 matrix, 4 rows | DEFECT_VERDICT[x] constrained | DEFECT_VERDICT[x] constrained |
| C-03 Session state tracked | Phase 2 SESSION_VARIABLES per turn | SESSION_VARIABLES_DELTA typed per turn | DA-2 per-turn session vars | Typed SESSION_VARIABLES_DELTA | Typed SESSION_VARIABLES_DELTA |
| C-04 Copilot Studio framing | CS vocabulary gate + topology spec | VOCABULARY_REGISTRY + TOPOLOGY_SPEC | DA-1 setup + CS vocabulary | Phase 1 typed CS topology | Phase 1 typed CS topology |
| C-05 Defect reproduction | Phase 6 amendments with trigger sequence + observable failure | REPRODUCTION typed per amendment | DA-6 amendments | REPRODUCTION typed | REPRODUCTION typed |
| C-06 Fallback chain | Phase 4 traces to terminal, CS-SPEC-07 | FALLBACK_CHAIN_QUALITY typed | DA-4 traces to terminal | FALLBACK_CHAIN_QUALITY typed | FALLBACK_CHAIN_QUALITY typed |
| C-07 Intent collision disambiguation | Phase 3 trigger phrase collisions with strategy + rationale | DISAMBIGUATION_STRATEGY constrained enum | DA-3 collisions | DISAMBIGUATION_STRATEGY constrained | DISAMBIGUATION_STRATEGY constrained |
| C-08 Graph coverage metric | Phase 6 coverage report with % | COVERAGE_REPORT with % | DA-6 coverage | COVERAGE_REPORT with % | COVERAGE_REPORT with % |
| C-09 Adversarial turn injection | Phase 5 mandatory | ADVERSARIAL_ASSESSMENT typed | DA-5 mandatory | ADVERSARIAL_ASSESSMENT typed | ADVERSARIAL_ASSESSMENT typed |
| C-10 Prohibited vocabulary gate | Phase 7 prohibited term audit table | Per-turn PROHIBITED_TERM_SCAN + Phase 7 post-trace audit | AA-3 prohibited term audit | Per-turn scan + Phase 7 audit | Per-turn scan + Phase 7 audit |
| C-11 Turn-level conformance verdict | Phase 2 SPEC_CONFORMANCE per turn (Developer) | SPEC_CONFORMANCE typed enum per turn | DA-2 SPEC_CONFORMANCE per turn | SPEC_CONFORMANCE typed per turn | SPEC_CONFORMANCE typed per turn |
| **C-12** | **Phase 7 Auditor per-turn annotations separate from Phase 2 Developer self-report** | **NOT present -- Auditor only does prohibited term table** | **AA-2 per-turn annotations as separate Auditor document** | **Phase 7 typed SPEC_CONFORMANCE + DISCREPANCY per turn** | **Phase 7 typed SPEC_CONFORMANCE + DISCREPANCY per turn** |
| **C-13** | **NOT present -- verdict fields still use "/" prose** | **PROHIBITED_TERM_SCAN per turn + all DEFECT_VERDICT typed enum "|" format** | **NOT present -- DA turn blocks use "/" prose** | **Full typed enum throughout: all verdict positions use "|"** | **Full typed enum throughout: all verdict positions use "|"** |

### C-12 vs C-11 tension and resolution

C-11 requires SPEC_CONFORMANCE inline in every Developer turn block. C-12 requires the Auditor to produce it as a separate audit layer. These are NOT mutually exclusive: the correct architecture is **dual conformance layers** -- Developer self-reports inline (C-11), Auditor independently reviews post-trace (C-12). The value of C-12 is the DISCREPANCY detection: cases where the Developer reported CONFORMS but the Auditor finds a CS-SPEC violation. This is why role separation is architecturally meaningful rather than redundant annotation.

### Key distinction between V-03 and V-01/V-04/V-05

V-03 uses hard === document boundary markers to enforce the Developer/Auditor split structurally. V-01/V-04/V-05 use phase numbering within a single document. Both approaches satisfy C-12. V-03's DEVELOPER ARTIFACT / AUDITOR ARTIFACT framing makes the "finished document" concept explicit in the output structure -- the Auditor Artifact begins with an AUDIT SCOPE STATEMENT naming the Developer Artifact as its input. This is a different enforcement mechanism, not merely a style choice.

### Why C-13 requires PROHIBITED_TERM_SCAN per turn

R2 V-05's Phase 2 turn blocks had SPEC_CONFORMANCE but not PROHIBITED_TERM_SCAN. Without a per-turn typed field, the model can produce prohibited terms in any turn block and the only check is the end-of-trace Phase 7 audit (a post-hoc scan). The per-turn PROHIBITED_TERM_SCAN field creates point-of-production enforcement: the model must evaluate each turn for prohibited terms AS IT PRODUCES THE TURN, not only when it reaches Phase 7. Combined with the post-trace audit, this creates dual coverage: catch-at-production + independent verification. C-13's constraint that "no free-text hedging permitted in verdict positions" is satisfied because `CLEAN | FOUND["term": "line"]` accepts no middle ground.
