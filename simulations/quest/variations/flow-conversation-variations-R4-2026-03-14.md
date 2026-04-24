Round 4 variations written to `simulations/quest/variations/flow-conversation-variations-R4-2026-03-14.md`.

---

## Round 4 — flow-conversation Variations

**Baseline:** R3 V-04 and V-05 both hit 100.00. R4 explores whether the same score is reachable through structurally different architectures — and whether any new production patterns emerge that could inform v4.

**Three new axes introduced:**

| V | Axis | Key innovation | Predicted |
|---|------|---------------|-----------|
| V-01 | **Output Format** (table trace) | SPEC_CONFORMANCE + PROHIBITED_TERM_SCAN as mandatory typed table columns — blank cell = structural failure | 100 |
| V-02 | **Phrasing Register** (imperative checklist) | 11 numbered commands, no phase scaffolding — tests whether C-12 survives without phase gates | **98.33** |
| V-03 | **Lifecycle Emphasis** (contract-first) | Auditor pre-declares assertion schema before any Developer work — inverts schema authorship | 100 |
| V-04 | Output Format + Lifecycle Emphasis | Auditor pre-declares table schemas; Developer fills them; schema authorship = audit contract | 100 |
| V-05 | Full synthesis | Contract-first + Table + 7-phase gates + typed enums + dual conformance layers | 100 |

**The V-02 predicted miss** is the key signal: imperative phrasing strips the phase gate that enforces C-12. Without `=== DEVELOPER ARTIFACT COMPLETE ===` and a sequenced gate, the model runs the Auditor section as an inline continuation rather than a post-production read. The phase gate appears to be **load-bearing** for C-12, not cosmetic.

**The R4 causal inversion insight:** R3 — Developer declares its own assertion schema, Auditor reads the result retroactively. R4 contract-first — Auditor declares the schema upstream, Developer fills it. The Auditor cannot reverse-engineer criteria post-hoc when it committed to the contract before seeing a single turn. Whether this yields a measurable output quality difference over R3 is the open empirical question for scoring.
*Hypothesis:** A table forces parallel structure across all turns and makes gaps immediately
visible — a blank cell cannot pass. `SPEC_CONFORMANCE` and `PROHIBITED_TERM_SCAN` as mandatory
table columns enforce C-11 and C-13 structurally: the model must fill each cell with the exact
constrained enum value or the table is malformed. Auditor post-production pass re-annotates the
same table schema from an independent read. Tests whether block-per-turn (R3 style) is the only
format that satisfies the criteria, or whether format is fungible.

```
You are running /flow:conversation for topic "{topic}".

Read: simulations/flow/conversation/{topic}-conversation-{date}.md if it exists.
Read: any signal artifacts in simulations/ relevant to "{topic}".

Roles execute in sequence: Conversation Designer (Setup), then Copilot Studio Developer
(Trace + Defect + Fallback + Adversarial + Coverage), then Compliance Auditor (Audit Table).
All phases are gates. Complete each phase fully before advancing.
Walk the conversation turn by turn -- do not summarize or collapse turns.

Use Copilot Studio vocabulary exclusively:
  Topics, Trigger phrases, Conditions, Fallback topics, Escalation nodes, Session variables,
  Topic redirects, Actions, Generative answers, Knowledge sources, End of conversation nodes.
Do not use: intent, dialog, slot, NLU, utterance (use "user input"), chatbot (use "agent"),
  handoff (use "escalation"), context (use "session variables"), bot (use "agent").

---

## SETUP GATE
[Conversation Designer speaks.]

Agent name: [Name or description]
Topics in graph: [N total] -- list all:
  [Topic-A], [Topic-B], [Topic-C], ...
Trigger phrases (2-3 per topic):
  [Topic-A]: "[phrase-1]", "[phrase-2]"
  [Topic-B]: "[phrase-1]", "[phrase-2]"
Fallback topic: [Name / "System Fallback Topic" / "not configured"]
Escalation path: [Topic containing escalation node / "not configured"]
Session variables:
  [VarName]: scope=[topic-scoped / global], type=[Text/Number/Boolean], initial=[value or "unset"]
Coverage scope: This simulation visits [N] of [Total] topics ([pct]%).

Topology spec (referenced in SPEC_CONFORMANCE column):
  CS-SPEC-01: Trigger phrase matching activates topic above confidence threshold.
  CS-SPEC-02: Topic-scoped session variables cleared at topic boundary.
  CS-SPEC-03: Condition nodes require a default branch.
  CS-SPEC-04: Redirect nodes do not carry topic-scoped variables.
  CS-SPEC-05: End of conversation nodes terminate the session.
  CS-SPEC-06: Escalation nodes open human agent session.
  CS-SPEC-07: Fallback topic activates when no trigger phrase exceeds threshold.

Prohibited terms (must not appear in Developer trace; Auditor verifies in Audit Table):
  intent | dialog | slot | NLU | utterance | chatbot | handoff | context | bot

SETUP GATE: Topics listed. Session variables enumerated. Coverage scope stated.
Topology spec declared. Prohibited terms listed. Advance to Trace Table.

---

## TRACE TABLE
[Copilot Studio Developer speaks. One row per turn -- no rows may be skipped.
All columns are mandatory. Use exactly the enum values shown in brackets.
SPEC_CONFORMANCE and PROHIBITED_TERM_SCAN are typed columns -- no free text in these cells.]

| Turn | User Input | Trigger Phrase Matched | Topic | Nodes Executed | Session Variables (name=value; changed/held/cleared) | Agent Response | SPEC_CONFORMANCE | PROHIBITED_TERM_SCAN |
|------|-----------|----------------------|-------|----------------|------------------------------------------------------|---------------|-----------------|---------------------|
| T-01 | "[input]" | "[phrase]" (HIGH/MED/LOW) | [Topic-A] | Trigger>Message>Question | scope=X, var1=Y (changed); var2=Z (held) | "[response]" | CONFORMS \| DEVIATES[CS-SPEC-NN: description] | CLEAN \| FOUND[term] |
| T-02 | "[input]" | "[phrase]" (HIGH/MED/LOW) | [Topic-B] | Trigger>Condition(branch=label)>Redirect | var1=Y (held); var2=cleared (topic ended) | "[response]" | CONFORMS \| DEVIATES[CS-SPEC-NN: description] | CLEAN \| FOUND[term] |
[...continue for all turns. Each row is mandatory. Blank cells are not permitted.]

TRACE GATE: All [N] turns present. SPEC_CONFORMANCE column populated on every row.
PROHIBITED_TERM_SCAN column populated on every row. Session state carried or cleared at every
transition. Advance to Defect Matrix.

---

## DEFECT MATRIX
[All four rows required. FOUND or CONFIRMED_ABSENT -- no other value permitted.
CONFIRMED_ABSENT requires explicit scope statement (which topics were checked).]

| Defect Class | DEFECT_VERDICT | Evidence | Reproduction Sequence |
|-------------|---------------|----------|----------------------|
| Dead end | FOUND \| CONFIRMED_ABSENT | [FOUND: Turn T-NN, topic name, node has no outgoing path. CONFIRMED_ABSENT: "All [N] topic exits route to redirect, escalation, or end-of-conversation node. Exit paths: [list]."] | [FOUND: "[utterance-1]" -> "[utterance-2]" -> dead state. CONFIRMED_ABSENT: N/A] |
| Infinite loop | FOUND \| CONFIRMED_ABSENT | [FOUND: loop path, triggering condition, cycle count. CONFIRMED_ABSENT: "Topic redirect graph is acyclic. Redirect map: [A->B], [C->terminal]."] | [FOUND: utterance sequence that cycles. CONFIRMED_ABSENT: N/A] |
| Trigger phrase collision | FOUND \| CONFIRMED_ABSENT | [FOUND: phrase, competing topics, confidence scores. Disambiguation strategy: entity enrichment / condition ordering / trigger phrase refactor. Rationale: [why]. CONFIRMED_ABSENT: "All [N] phrases resolve to single topic above 0.7; runner-up below 0.4."] | [FOUND: "[ambiguous utterance]" -> both Topic-A and Topic-B activate. CONFIRMED_ABSENT: N/A] |
| Missing fallback | FOUND \| CONFIRMED_ABSENT | [FOUND: topic, condition node, unhandled branch, CS-SPEC-03 violation. CONFIRMED_ABSENT: "All condition nodes in [N] topics carry default branch or fallback redirect. Confirmed: [list topics]."] | [FOUND: "[input]" at condition node with no default branch -> silent routing. CONFIRMED_ABSENT: N/A] |

DEFECT GATE: All four classes have DEFECT_VERDICT + evidence + reproduction. Advance to Fallback.

---

## FALLBACK CHAIN TRACE
[Walk one complete fallback path from unrecognized input to terminal state.
Reference CS-SPEC-07. Do not stop at first fallback activation -- trace to terminal.]

Unrecognized input: "[phrase matching no trigger phrase]"
Step 1: [N] topics evaluated, 0 match above threshold -> CS-SPEC-07 activates -> routes to [Fallback topic]
Step 2: [First fallback node type] -- [what it does]
Step 3: [Next node] -- [what it does]
...
Terminal state: [Escalation node opened / End of conversation node reached / Loop detected]

FALLBACK_QUALITY: COMPLETE | LOOPS | TRUNCATED

FALLBACK GATE: Complete path traced to terminal state. FALLBACK_QUALITY verdict assigned.
Advance to Adversarial.

---

## ADVERSARIAL INJECTION
[One adversarial scenario: unexpected input mid-flow, topic switch during active question node,
or session timeout mid-flow.]

Scenario type: [mid-flow topic switch / unexpected input / session timeout]
Description: "[what happens]"
Injected at: Turn T-[NN], after [session state at injection point]
Node path: [trace from injection through agent response]
Session variable impact: [what changes, what is lost or corrupted]
Agent response: "[what the agent says]"
ADVERSARIAL_OUTCOME: GRACEFUL | BRITTLE | SILENT_FAILURE

ADVERSARIAL GATE: Scenario described. Node path traced. Outcome verdict assigned. Advance to Coverage.

---

## COVERAGE REPORT + AMENDMENTS

Coverage:
| Metric | Visited | Total (estimated) | Ratio |
|--------|---------|-------------------|-------|
| Topics | [N] | [Total] | [N/Total] ([pct]%) |
| Trigger phrases exercised | [N] | [Total] | [N/Total] ([pct]%) |

Amendments (for each FOUND defect and each DEVIATES row in Trace Table):
- **CS-SPEC-NN:** [spec name] -- [description of violation]
  Trigger sequence: "[utterance-1]" -> "[utterance-2]" -> [failure mode]
  Proposed fix: [trigger phrase refactor / condition amendment / default branch addition / session variable scope correction]
  Priority: P1 (breaks flow) / P2 (degrades experience) / P3 (minor)

COVERAGE GATE: Metrics reported. All FOUND/DEVIATES items have amendments. Advance to Audit Table.

---

## === DEVELOPER ARTIFACT COMPLETE ===

---

## AUDIT TABLE
[Compliance Auditor speaks. Read the completed Developer Artifact (Setup through Coverage) as a
finished document. This is a post-production scan -- the Developer role has ended.
Re-annotate every row from the Trace Table independently. Do not consult the Developer.]

Input document: Developer Artifact, Trace Table rows T-01 through T-[N].
Auditor reads each row and assigns independent verdicts.

| Turn | Developer SPEC_CONFORMANCE | Auditor SPEC_CONFORMANCE | Developer PROHIBITED_TERM_SCAN | Auditor PROHIBITED_TERM_SCAN | DISCREPANCY |
|------|--------------------------|-------------------------|-------------------------------|-----------------------------|-----------:|
| T-01 | [from Trace Table] | CONFORMS \| DEVIATES[CS-SPEC-NN: description] | [from Trace Table] | CLEAN \| FOUND[term] | NONE \| FOUND[SPEC_CONFORMANCE / PROHIBITED_TERM] |
| T-02 | [from Trace Table] | CONFORMS \| DEVIATES[CS-SPEC-NN: description] | [from Trace Table] | CLEAN \| FOUND[term] | NONE \| FOUND[SPEC_CONFORMANCE / PROHIBITED_TERM] |
[...one row per turn from Trace Table]

DISCREPANCY values: NONE | FOUND[SPEC_CONFORMANCE] | FOUND[PROHIBITED_TERM] | FOUND[BOTH]

Auditor Summary:
  Total turns audited: [N]
  Discrepancies found: [N]
    - False-clean SPEC_CONFORMANCE (Developer said CONFORMS, Auditor finds DEVIATES): [N]
    - False-clean PROHIBITED_TERM_SCAN (Developer said CLEAN, Auditor finds FOUND): [N]
  Prohibited terms found in Developer trace: [list / NONE]
  Audit verdict: CLEAN | ISSUES_FOUND
```

---

## V-02: Phrasing Register — Imperative Checklist

**Axis:** Phrasing Register — numbered imperative commands, no phase scaffolding, direct
second-person address throughout. No "Phase X" labels.

**Hypothesis:** Stripping phase scaffolding and replacing with "Do X, then do Y" numbered
commands tests whether role separation (C-12) survives without an explicit phase boundary.
The hypothesis is that C-12 requires a structural boundary (the Developer artifact must end
before the Auditor begins) and imperative list format may collapse the roles into a single
production pass — failing C-12 by losing the post-production audit distinction. If true,
this reveals that phase scaffolding is load-bearing for C-12, not just cosmetic. C-13 is
preserved through inline numbered field specifications. Predicted 98.33 (misses C-12).

```
You are a Copilot Studio domain expert. Simulate a multi-turn conversation flow for
topic "{topic}". Complete every numbered step in order. Do not skip steps.

Read simulations/flow/conversation/{topic}-conversation-{date}.md if it exists.
Read any signal artifacts in simulations/ relevant to "{topic}".

Use only Copilot Studio vocabulary: topics, trigger phrases, conditions, fallback topics,
escalation nodes, session variables, topic redirects, actions, generative answers,
knowledge sources, end of conversation nodes.
Never use: intent, dialog, slot, NLU, utterance, chatbot, handoff, context, bot.

---

1. **List the agent topology.**
   State: agent name, all topics in the graph (N total), trigger phrases for each topic
   (2-3 per topic), fallback topic name, escalation path, all session variables with scope
   and type, knowledge sources. State coverage scope: N topics this simulation will visit
   of M total.

2. **Declare the topology spec.**
   State CS-SPEC-01 through CS-SPEC-07. These are the rules you will check per turn:
   - CS-SPEC-01: Trigger phrase matching activates topic above confidence threshold.
   - CS-SPEC-02: Topic-scoped session variables cleared at topic boundary.
   - CS-SPEC-03: Condition nodes require a default branch.
   - CS-SPEC-04: Redirect nodes do not carry topic-scoped variables.
   - CS-SPEC-05: End of conversation nodes terminate the session.
   - CS-SPEC-06: Escalation nodes open human agent session.
   - CS-SPEC-07: Fallback topic activates when no trigger phrase exceeds threshold.

3. **List the prohibited terms.**
   These terms must not appear anywhere in your simulation output:
   intent | dialog | slot | NLU | utterance | chatbot | handoff | context | bot
   You will scan for these in step 10.

4. **Walk every conversation turn.** For each turn from 1 to N, produce:
   - User input: "[exact text]"
   - Trigger phrase matched: "[phrase]" in topic "[Name]", confidence: HIGH / MED / LOW
   - Nodes executed: [ordered chain, e.g., Trigger > Message > Question > Condition > Redirect]
   - Session variables after this turn: [name=value (scope, changed/held/cleared) for each variable]
   - Agent response: "[text shown to user]"
   - SPEC_CONFORMANCE: CONFORMS | DEVIATES[CS-SPEC-NN: description]
   - PROHIBITED_TERM_SCAN: CLEAN | FOUND[term]
   Do not skip or collapse any turn. Repeat this block for every turn.

5. **Fill the defect matrix.** For each defect class, give DEFECT_VERDICT: FOUND | CONFIRMED_ABSENT.
   CONFIRMED_ABSENT requires an explicit scope statement.
   - Dead end: FOUND | CONFIRMED_ABSENT -- [evidence / scope statement] -- [reproduction sequence if FOUND]
   - Infinite loop: FOUND | CONFIRMED_ABSENT -- [evidence / scope statement] -- [reproduction sequence if FOUND]
   - Trigger phrase collision: FOUND | CONFIRMED_ABSENT -- [evidence / scope statement + disambiguation strategy if FOUND]
   - Missing fallback: FOUND | CONFIRMED_ABSENT -- [evidence / scope statement] -- [reproduction sequence if FOUND]

6. **Trace one complete fallback path.**
   Start with an unrecognized input. Walk every step to terminal state (escalation node
   or end of conversation node). Do not stop at the first fallback topic activation.
   End with: FALLBACK_QUALITY: COMPLETE | LOOPS | TRUNCATED

7. **Inject one adversarial scenario.**
   Choose: unexpected mid-flow input, topic switch during active question node, or
   session timeout. Describe the scenario, show the node path, show session variable impact.
   End with: ADVERSARIAL_OUTCOME: GRACEFUL | BRITTLE | SILENT_FAILURE

8. **Report coverage.**
   Topics visited / total topics = [N/M] ([pct]%).
   Trigger phrases exercised / estimated total = [N/M] ([pct]%).

9. **Write amendments.**
   For every FOUND defect and every DEVIATES turn: state the CS-SPEC-NN violation,
   the exact trigger sequence, the proposed fix, and priority P1/P2/P3.

10. **Run the prohibited term scan.**
    List every prohibited term from step 3. For each: state whether it appears in steps
    4-9 and give the exact location if found. End with:
    PROHIBITED_TERM_SCAN_RESULT: CLEAN | FOUND[term at step N, turn T-NN]

11. **Write the Auditor section.**
    Switch to Compliance Auditor role. You have finished producing the simulation above.
    Re-read steps 4-9 as a completed document. For every turn from step 4, produce an
    independent SPEC_CONFORMANCE verdict and PROHIBITED_TERM_SCAN verdict. Compare to
    the Developer's verdicts from step 4. Flag any discrepancy where Developer said
    CONFORMS but topology evidence shows DEVIATES, or Developer said CLEAN but the
    Auditor scan finds a prohibited term.

    Format:
    | Turn | Developer SPEC_CONFORMANCE | Auditor SPEC_CONFORMANCE | Developer PROHIBITED_TERM_SCAN | Auditor PROHIBITED_TERM_SCAN | DISCREPANCY |
    |------|--------------------------|-------------------------|-------------------------------|-----------------------------|-----------:|
    [one row per turn]

    DISCREPANCY values: NONE | FOUND[SPEC_CONFORMANCE] | FOUND[PROHIBITED_TERM] | FOUND[BOTH]

    Auditor summary: total turns, discrepancies found (type and count), audit verdict:
    CLEAN | ISSUES_FOUND
```

---

## V-03: Lifecycle Emphasis — Contract-First Audit

**Axis:** Lifecycle Emphasis — Auditor pre-declares the verification contract (assertion
positions, field names, valid enum values) before any Developer production begins. Developer
traces against the pre-committed contract. Auditor then applies its contract to the finished
trace.

**Hypothesis:** R3's Auditor role is reactive — it reads what the Developer produced and
retroactively checks it. A contract-first Auditor commits upstream: it defines exactly what
assertion positions exist, what the legal enum values are, and what it will look for before
seeing a single Developer turn. This prevents the Auditor from reverse-engineering criteria
post-hoc and prevents the Developer from producing output that technically avoids audit surface
(e.g., no typed verdict field = nothing for the Auditor to flag). Pre-commitment to the contract
satisfies C-12 (role-separated) and C-13 (typed fields with constrained enums) through a
different causal chain than R3. The Developer does not define the verdict schema — the Auditor
does.

```
You are running /flow:conversation for topic "{topic}".

Read: simulations/flow/conversation/{topic}-conversation-{date}.md if it exists.
Read: any signal artifacts in simulations/ relevant to "{topic}".

Three roles execute in strict sequence: Compliance Auditor (Phase 0), then Copilot Studio
Developer (Phases 1-6), then Compliance Auditor (Phase 7).
The Auditor runs twice: once to pre-declare the contract, once to apply it.
The Developer may not alter the contract declared in Phase 0.
All phases are gates. Complete each phase fully before advancing.

Use Copilot Studio vocabulary exclusively:
  Topics, Trigger phrases, Conditions, Fallback topics, Escalation nodes, Session variables,
  Topic redirects, Actions, Generative answers, Knowledge sources, End of conversation nodes.
Do not use: intent, dialog, slot, NLU, utterance (use "user input"), chatbot (use "agent"),
  handoff (use "escalation"), context (use "session variables"), bot (use "agent").

---

## PHASE 0: AUDITOR CONTRACT DECLARATION
[Compliance Auditor speaks first. Declare the complete verification contract before any
Developer work begins. This contract is binding -- the Developer must use exactly these
assertion fields and exactly these enum values. The Auditor will apply this contract in
Phase 7.]

### 0-A: Topology Spec (Developer must check each turn against these rules)
  CS-SPEC-01: Trigger phrase matching activates topic above confidence threshold.
  CS-SPEC-02: Topic-scoped session variables cleared at topic boundary.
  CS-SPEC-03: Condition nodes require a default branch.
  CS-SPEC-04: Redirect nodes do not carry topic-scoped variables.
  CS-SPEC-05: End of conversation nodes terminate the session.
  CS-SPEC-06: Escalation nodes open human agent session.
  CS-SPEC-07: Fallback topic activates when no trigger phrase exceeds threshold.

### 0-B: Prohibited Terms (Developer must scan each turn; Auditor will re-scan in Phase 7)
  Prohibited: intent | dialog | slot | NLU | utterance | chatbot | handoff | context | bot
  Note: "utterance" is prohibited; use "user input". "chatbot" is prohibited; use "agent".

### 0-C: Assertion Schema (Developer must use these exact field names and enum values in Phase 2)
  Per-turn assertion fields (mandatory on every turn):
    SPEC_CONFORMANCE: CONFORMS | DEVIATES[CS-SPEC-NN: description]
    PROHIBITED_TERM_SCAN: CLEAN | FOUND[term at exact location]

  Defect matrix verdict field (mandatory on all four defect rows in Phase 3):
    DEFECT_VERDICT: FOUND | CONFIRMED_ABSENT
    -- CONFIRMED_ABSENT requires explicit scope statement (topics checked).
    -- FOUND requires reproduction sequence (exact input sequence -> failure mode).
    -- Free-text in the DEFECT_VERDICT cell is a violation.

  Fallback quality verdict (Phase 4):
    FALLBACK_QUALITY: COMPLETE | LOOPS | TRUNCATED

  Adversarial outcome verdict (Phase 5):
    ADVERSARIAL_OUTCOME: GRACEFUL | BRITTLE | SILENT_FAILURE

  Auditor audit verdicts (Phase 7 only -- Developer does not produce these):
    AUDITOR_SPEC_CONFORMANCE: CONFORMS | DEVIATES[CS-SPEC-NN: description]
    AUDITOR_PROHIBITED_TERM_SCAN: CLEAN | FOUND[term at exact location]
    DISCREPANCY: NONE | FOUND[SPEC_CONFORMANCE] | FOUND[PROHIBITED_TERM] | FOUND[BOTH]

### 0-D: Audit Scope (Auditor commits to checking these in Phase 7)
  - Every turn from Phase 2: SPEC_CONFORMANCE and PROHIBITED_TERM_SCAN
  - All four defect rows from Phase 3: DEFECT_VERDICT and reproduction quality
  - Phase 4 fallback chain: FALLBACK_QUALITY and terminal state reached
  - Phase 5 adversarial: ADVERSARIAL_OUTCOME verdict present
  - Coverage metrics: Phase 6 ratios present
  - Prohibited terms in all Developer output: full body scan

AUDIT CONTRACT GATE: Topology spec declared (7 rules). Prohibited terms listed (10 terms).
Assertion schema declared (all fields + all enum values). Audit scope committed.
Developer may now begin Phase 1. Developer may not modify this contract.

---

## PHASE 1: SETUP
[Copilot Studio Developer speaks. Define the agent topology against the contract from Phase 0.]

Agent name: [Name or description]
Topics in graph: [N total] -- list all:
  [Topic-A], [Topic-B], [Topic-C], ...
Trigger phrases (2-3 per topic):
  [Topic-A]: "[phrase-1]", "[phrase-2]"
  [Topic-B]: "[phrase-1]", "[phrase-2]"
Fallback topic: [Name / "System Fallback Topic" / "not configured"]
Escalation path: [Topic containing escalation node / "not configured"]
Session variables:
  [VarName]: scope=[topic-scoped / global], type=[Text/Number/Boolean], initial=[value or "unset"]
Coverage scope: [N] of [Total] topics visited ([pct]%).

SETUP GATE: Topology declared against Phase 0 contract. Advance to Phase 2.

---

## PHASE 2: CONVERSATION TRACE
[Copilot Studio Developer speaks. Walk every turn. Use Phase 0 assertion schema exactly.
SPEC_CONFORMANCE and PROHIBITED_TERM_SCAN are typed fields -- use Phase 0 enum values only.
No free text in verdict positions.]

Turn [N] of [TOTAL]:
  User input: "[exact user input]"
  Trigger phrase matched: "[phrase]" in topic "[Topic name]", confidence: HIGH / MED / LOW
  Runner-up topic (if any): "[Topic name]" ([score]) / "none"
  Node path: [ordered chain -- Trigger phrase node > Message node > Question node >
    Condition node (branch=[label]) > Action node > Redirect node > End of conversation node]
  Session variables after this turn:
    [VarName] = [value] (scope: topic-scoped / global, changed: yes/no)
    [VarName] = cleared (topic-scoped, topic ended this turn)
  Response: "[agent response text]"
  SPEC_CONFORMANCE: CONFORMS | DEVIATES[CS-SPEC-NN: description]
  PROHIBITED_TERM_SCAN: CLEAN | FOUND[term at exact location]

[Repeat for every turn. No turns may be skipped. Phase 0 assertion schema is binding.]

TRACE GATE: All [N] turns completed. SPEC_CONFORMANCE present on every turn (Phase 0 contract).
PROHIBITED_TERM_SCAN present on every turn (Phase 0 contract). Session state tracked. Advance to Phase 3.

---

## PHASE 3: DEFECT MATRIX
[Use Phase 0 DEFECT_VERDICT enum exclusively. CONFIRMED_ABSENT requires scope statement.
FOUND requires reproduction sequence. No free text in DEFECT_VERDICT cells.]

| Defect Class | DEFECT_VERDICT | Evidence | Reproduction Sequence |
|-------------|---------------|----------|----------------------|
| Dead end | FOUND \| CONFIRMED_ABSENT | [evidence or scope statement] | [utterance sequence -> failure / N/A] |
| Infinite loop | FOUND \| CONFIRMED_ABSENT | [evidence or scope statement] | [cycle path / N/A] |
| Trigger phrase collision | FOUND \| CONFIRMED_ABSENT | [phrase + competing topics + disambiguation strategy + rationale / scope statement] | [ambiguous input -> dual activation / N/A] |
| Missing fallback | FOUND \| CONFIRMED_ABSENT | [topic + condition node + unhandled branch / scope statement] | [input -> silent routing / N/A] |

DEFECT GATE: All four rows use Phase 0 DEFECT_VERDICT enum. Evidence + reproduction present
where FOUND. Scope stated where CONFIRMED_ABSENT. Advance to Phase 4.

---

## PHASE 4: FALLBACK CHAIN TRACE
[Use Phase 0 FALLBACK_QUALITY enum. Walk to terminal state. Reference CS-SPEC-07.]

Unrecognized input: "[phrase]"
Step 1: [N] topics evaluated, 0 match above threshold -> CS-SPEC-07 -> [Fallback topic]
Step 2: [node type] -- [action]
...
Terminal state: [escalation node / end of conversation node / loop detected]

FALLBACK_QUALITY: COMPLETE | LOOPS | TRUNCATED

FALLBACK GATE: Path traced to terminal. Phase 0 FALLBACK_QUALITY enum used. Advance to Phase 5.

---

## PHASE 5: ADVERSARIAL INJECTION
[Use Phase 0 ADVERSARIAL_OUTCOME enum. One scenario required.]

Scenario type: [mid-flow topic switch / unexpected input / session timeout]
Scenario: "[description]"
Injected at: Turn T-[NN], after [session state]
Node path: [trace]
Session variable impact: [what changes or is lost]
Agent response: "[text]"
ADVERSARIAL_OUTCOME: GRACEFUL | BRITTLE | SILENT_FAILURE

ADVERSARIAL GATE: Scenario described. Node path traced. Phase 0 enum used. Advance to Phase 6.

---

## PHASE 6: COVERAGE + AMENDMENTS

Coverage:
  Topics visited: [N] / [Total] = [pct]%
  Trigger phrases exercised: [N] / [Total estimated] = [pct]%

Amendments (FOUND defects and DEVIATES turns):
  CS-SPEC-NN: [violation description]
    Trigger sequence: [exact inputs -> failure]
    Proposed fix: [specific change]
    Priority: P1 / P2 / P3

COVERAGE GATE: Ratios reported. All FOUND/DEVIATES items have amendments. Advance to Phase 7.

---

## === DEVELOPER ARTIFACT COMPLETE ===
## === AUDITOR NOW READS THE COMPLETED ARTIFACT ===

---

## PHASE 7: AUDITOR APPLIES CONTRACT
[Compliance Auditor speaks. Read the Developer Artifact (Phases 1-6) as a finished document.
Apply the contract from Phase 0. The Developer role has ended -- do not consult it.
Re-annotate every turn from Phase 2 independently using Phase 0 AUDITOR_SPEC_CONFORMANCE
and AUDITOR_PROHIBITED_TERM_SCAN enums.]

Contract reference: Phase 0 assertion schema.
Input document: Developer Artifact, Phase 2 turns T-01 through T-[N].

| Turn | Developer SPEC_CONFORMANCE | AUDITOR_SPEC_CONFORMANCE | Developer PROHIBITED_TERM_SCAN | AUDITOR_PROHIBITED_TERM_SCAN | DISCREPANCY |
|------|--------------------------|-------------------------|-------------------------------|-----------------------------|-----------:|
| T-01 | [from Phase 2] | CONFORMS \| DEVIATES[CS-SPEC-NN: description] | [from Phase 2] | CLEAN \| FOUND[term] | NONE \| FOUND[SPEC_CONFORMANCE] \| FOUND[PROHIBITED_TERM] \| FOUND[BOTH] |
[...one row per turn]

Prohibited term body scan (Phases 1-6 full text):
| Term | Present in Developer output | Location |
|------|-----------------------------|----------|
| intent | YES \| NO | [Phase N, Turn T-NN / N/A] |
| dialog | YES \| NO | [location / N/A] |
| slot | YES \| NO | [location / N/A] |
| NLU | YES \| NO | [location / N/A] |
| utterance | YES \| NO | [location / N/A] |
| chatbot | YES \| NO | [location / N/A] |
| handoff | YES \| NO | [location / N/A] |
| context | YES \| NO | [location / N/A] |
| bot | YES \| NO | [location / N/A] |
PROHIBITED_TERM_BODY_SCAN: CLEAN | FOUND[list terms and locations]

Auditor summary:
  Contract applied: Phase 0 schema (all assertion positions, all enum values)
  Turns audited: [N]
  DISCREPANCY cases: [N]
    - False-clean SPEC_CONFORMANCE: [N]
    - False-clean PROHIBITED_TERM_SCAN: [N]
  Prohibited term body scan: CLEAN | FOUND
  AUDIT_VERDICT: CLEAN | ISSUES_FOUND
```

---

## V-04: Output Format + Lifecycle Emphasis — Schema-Driven Trace

**Axes:** Output Format + Lifecycle Emphasis — Auditor pre-declares a table schema in Phase 0.
Developer fills the Auditor's schema exactly. Auditor audits against its own pre-committed schema.
The schema IS the verification contract. No freeform production possible.

**Hypothesis:** Combining contract-first (V-03) with table format (V-01) creates a schema-driven
architecture where the Developer cannot introduce untyped fields or narrative verdict positions.
The Auditor's Phase 0 schema pre-commits both the column structure and the enum values. Developer
filling a pre-declared table cannot substitute prose for typed fields. Tests whether this is
stricter than V-03 alone (which uses blocks) or V-01 alone (which the Developer defines its own
table columns). The schema authorship question: when the Auditor owns the schema, the Developer
cannot declare its own verdict format.

```
You are running /flow:conversation for topic "{topic}".

Read: simulations/flow/conversation/{topic}-conversation-{date}.md if it exists.
Read: any signal artifacts in simulations/ relevant to "{topic}".

Three roles in strict sequence: Compliance Auditor (Phase 0 schema declaration),
Copilot Studio Developer (Phases 1-6 filling the schema), Compliance Auditor (Phase 7 audit).
Developer must use exactly the table schemas declared by the Auditor in Phase 0 -- no
modifications, no additional columns, no narrative substitutions.
All phases are gates. Complete each phase fully before advancing.

Use Copilot Studio vocabulary exclusively:
  Topics, Trigger phrases, Conditions, Fallback topics, Escalation nodes, Session variables,
  Topic redirects, Actions, Generative answers, Knowledge sources, End of conversation nodes.
Do not use: intent, dialog, slot, NLU, utterance (use "user input"), chatbot (use "agent"),
  handoff (use "escalation"), context (use "session variables"), bot (use "agent").

---

## PHASE 0: AUDITOR SCHEMA DECLARATION
[Compliance Auditor declares every table schema the Developer must use. Developer fills these
schemas in Phases 2-6. Auditor audits the filled schemas in Phase 7. Schema authorship belongs
to the Auditor -- Developer may not introduce new schemas or modify declared columns.]

### Schema S-01: Trace Table (Developer fills in Phase 2)
| Turn | User Input | Trigger Phrase Matched | Confidence | Topic | Nodes Executed | Session Variables | Agent Response | SPEC_CONFORMANCE | PROHIBITED_TERM_SCAN |
|------|-----------|----------------------|------------|-------|----------------|------------------|---------------|-----------------|---------------------|

Allowed values:
  Confidence: HIGH | MED | LOW
  SPEC_CONFORMANCE: CONFORMS | DEVIATES[CS-SPEC-NN: description]
  PROHIBITED_TERM_SCAN: CLEAN | FOUND[term at exact location]

### Schema S-02: Defect Matrix (Developer fills in Phase 3)
| Defect Class | DEFECT_VERDICT | Evidence | Reproduction Sequence | Disambiguation (if FOUND collision) |
|-------------|---------------|----------|-----------------------|-------------------------------------|

Allowed values:
  DEFECT_VERDICT: FOUND | CONFIRMED_ABSENT
  -- CONFIRMED_ABSENT: Evidence cell must contain explicit scope statement.
  -- FOUND: Reproduction Sequence cell must contain exact utterance sequence -> failure mode.
  Rows required: Dead end | Infinite loop | Trigger phrase collision | Missing fallback

### Schema S-03: Fallback Chain (Developer fills in Phase 4)
| Step | Node | Action | Next | CS-SPEC Reference |
|------|------|--------|------|-------------------|

Allowed values:
  FALLBACK_QUALITY (declared after table): COMPLETE | LOOPS | TRUNCATED

### Schema S-04: Adversarial Injection (Developer fills in Phase 5)
| Field | Value |
|-------|-------|
| Scenario type | mid-flow topic switch \| unexpected input \| session timeout |
| Description | [text] |
| Injected at | Turn T-[NN], after [state] |
| Node path | [trace] |
| Session variable impact | [what changes or is lost] |
| Agent response | [text] |
| ADVERSARIAL_OUTCOME | GRACEFUL \| BRITTLE \| SILENT_FAILURE |

### Schema S-05: Coverage Report (Developer fills in Phase 6)
| Metric | Visited | Total (estimated) | Ratio |
|--------|---------|-------------------|-------|
| Topics | | | |
| Trigger phrases | | | |

### Schema S-06: Audit Table (Auditor fills in Phase 7 only)
| Turn | Dev SPEC_CONFORMANCE | Audit SPEC_CONFORMANCE | Dev PROHIBITED_TERM_SCAN | Audit PROHIBITED_TERM_SCAN | DISCREPANCY |
|------|---------------------|----------------------|--------------------------|---------------------------|-------------|

Allowed values:
  Audit SPEC_CONFORMANCE: CONFORMS | DEVIATES[CS-SPEC-NN: description]
  Audit PROHIBITED_TERM_SCAN: CLEAN | FOUND[term at exact location]
  DISCREPANCY: NONE | FOUND[SPEC_CONFORMANCE] | FOUND[PROHIBITED_TERM] | FOUND[BOTH]

### Topology Spec (referenced in SPEC_CONFORMANCE cells)
  CS-SPEC-01: Trigger phrase matching activates topic above confidence threshold.
  CS-SPEC-02: Topic-scoped session variables cleared at topic boundary.
  CS-SPEC-03: Condition nodes require a default branch.
  CS-SPEC-04: Redirect nodes do not carry topic-scoped variables.
  CS-SPEC-05: End of conversation nodes terminate the session.
  CS-SPEC-06: Escalation nodes open human agent session.
  CS-SPEC-07: Fallback topic activates when no trigger phrase exceeds threshold.

### Prohibited Terms (used in PROHIBITED_TERM_SCAN cells)
  intent | dialog | slot | NLU | utterance | chatbot | handoff | context | bot

SCHEMA DECLARATION GATE: Six schemas declared (S-01 through S-06). Topology spec declared.
Prohibited terms listed. Developer may now fill schemas in Phases 1-6.

---

## PHASE 1: SETUP
[Copilot Studio Developer speaks. Declare the agent topology in prose (this phase is topology
description, not a schema). All topology facts stated here are referenced in S-01 through S-05.]

Agent name: [Name or description]
Topics in graph: [N total]: [Topic-A], [Topic-B], [Topic-C], ...
Trigger phrases: [Topic-A]: "[phrase-1]", "[phrase-2]"; [Topic-B]: "[phrase-1]", "[phrase-2]"; ...
Fallback topic: [Name / "System Fallback Topic" / "not configured"]
Escalation path: [Topic / "not configured"]
Session variables: [VarName]: scope=[...], type=[...], initial=[...]; ...
Coverage scope: [N] of [Total] topics ([pct]%).

SETUP GATE: Topology declared. Advance to Phase 2.

---

## PHASE 2: TRACE TABLE
[Developer fills Schema S-01. One row per turn. All cells mandatory. Use Auditor-declared
enum values only -- no substitutions.]

[fill Schema S-01 here -- one row per turn, all columns populated]

TRACE GATE: All [N] rows present. SPEC_CONFORMANCE and PROHIBITED_TERM_SCAN populated on every
row using Phase 0 enum values. Advance to Phase 3.

---

## PHASE 3: DEFECT MATRIX
[Developer fills Schema S-02. All four rows required. Use Auditor-declared DEFECT_VERDICT enum.]

[fill Schema S-02 here]

DEFECT GATE: All four rows present with DEFECT_VERDICT + evidence + reproduction. Advance to Phase 4.

---

## PHASE 4: FALLBACK CHAIN
[Developer fills Schema S-03. Trace to terminal state. End with FALLBACK_QUALITY enum.]

Unrecognized input: "[phrase]"
[fill Schema S-03 here]

FALLBACK_QUALITY: COMPLETE | LOOPS | TRUNCATED

FALLBACK GATE: Chain traced to terminal. FALLBACK_QUALITY declared. Advance to Phase 5.

---

## PHASE 5: ADVERSARIAL INJECTION
[Developer fills Schema S-04.]

[fill Schema S-04 here]

ADVERSARIAL GATE: All S-04 fields populated. ADVERSARIAL_OUTCOME declared. Advance to Phase 6.

---

## PHASE 6: COVERAGE + AMENDMENTS
[Developer fills Schema S-05. Then writes amendments for all FOUND/DEVIATES items.]

[fill Schema S-05 here]

Amendments:
  CS-SPEC-NN: [violation] -- Trigger sequence: [inputs -> failure] -- Fix: [change] -- Priority: P1/P2/P3

COVERAGE GATE: S-05 metrics populated. Amendments written. Advance to Phase 7.

---

## === DEVELOPER ARTIFACT COMPLETE ===
## === AUDITOR APPLIES SCHEMA S-06 ===

---

## PHASE 7: AUDIT
[Compliance Auditor reads the completed Developer Artifact (Phases 1-6) as a finished document.
Developer role has ended. Fill Schema S-06 declared in Phase 0 for every row from Phase 2.
Compare Developer verdicts to Auditor independent re-read. Flag discrepancies.]

Input document: Developer Artifact, Phase 2 Trace Table rows T-01 through T-[N].

[fill Schema S-06 here -- one row per turn from Phase 2]

Prohibited term body scan (Phases 1-6 full text scan):
| Term | Present | Location |
|------|---------|----------|
| intent | YES \| NO | [Phase N / N/A] |
| dialog | YES \| NO | [Phase N / N/A] |
| slot | YES \| NO | [Phase N / N/A] |
| NLU | YES \| NO | [Phase N / N/A] |
| utterance | YES \| NO | [Phase N / N/A] |
| chatbot | YES \| NO | [Phase N / N/A] |
| handoff | YES \| NO | [Phase N / N/A] |
| context | YES \| NO | [Phase N / N/A] |
| bot | YES \| NO | [Phase N / N/A] |

PROHIBITED_TERM_BODY_SCAN: CLEAN | FOUND[list]

Auditor summary:
  Schema applied: S-06 (Phase 0 contract)
  Turns audited: [N]
  Discrepancies: [N] -- False-clean SPEC_CONFORMANCE: [N], False-clean PROHIBITED_TERM_SCAN: [N]
  Prohibited term body scan: CLEAN | FOUND
  AUDIT_VERDICT: CLEAN | ISSUES_FOUND
```

---

## V-05: Full Synthesis — Contract-First + Table + 7-Phase Gates + Dual Conformance

**Axes:** All — Contract-first (V-03) + Table format (V-01) + 7-phase gates (R3 V-05) +
Typed enums (R3 V-02/V-04) + Dual conformance layers (Developer inline + Auditor post-production).

**Hypothesis:** Contract-first changes the causal order: typed enum values are declared by the
Auditor before production (not specified inline by the Developer). This closes a gap in R3 V-05
where the Developer defines its own schema — technically self-certifying the assertion shape.
When the Auditor owns the schema pre-production, the Developer fills a pre-committed assertion
contract rather than declaring its own. Gate architecture enforces that Phase 7 cannot begin
until Phases 1-6 are complete, preserving the post-production audit distinction while the
contract-first mechanism ensures both C-12 (role separation) and C-13 (typed enums) have
the same causal root (Auditor pre-commitment) rather than being satisfied through parallel
but independent mechanisms.

```
You are running /flow:conversation for topic "{topic}".

Read: simulations/flow/conversation/{topic}-conversation-{date}.md if it exists.
Read: any signal artifacts in simulations/ relevant to "{topic}".

Roles execute in strict sequence: Compliance Auditor (Phase 0), Conversation Designer (Phase 1),
Copilot Studio Developer (Phases 2-6), Compliance Auditor (Phase 7).
Auditor runs twice: Phase 0 to declare the contract, Phase 7 to apply it.
Phases 1-6 are the Developer Artifact. Phase 7 is the Auditor Artifact.
All phases are gates. Complete each phase fully before advancing.
Developer may not begin Phase 1 until Phase 0 is complete.
Auditor may not begin Phase 7 until Phases 1-6 are gated complete.

Use Copilot Studio vocabulary exclusively:
  Topics, Trigger phrases, Conditions, Fallback topics, Escalation nodes, Session variables,
  Topic redirects, Actions, Generative answers, Knowledge sources, End of conversation nodes.
Do not use: intent, dialog, slot, NLU, utterance (use "user input"), chatbot (use "agent"),
  handoff (use "escalation"), context (use "session variables"), bot (use "agent").

---

## PHASE 0: AUDITOR CONTRACT DECLARATION
[Compliance Auditor speaks. This phase precedes all Developer work.
Declare the complete verification contract: topology spec, prohibited terms, assertion schemas,
and audit scope. This contract is binding on all subsequent phases.]

### 0-A: Topology Spec
  CS-SPEC-01: Trigger phrase matching activates topic above confidence threshold.
  CS-SPEC-02: Topic-scoped session variables cleared at topic boundary.
  CS-SPEC-03: Condition nodes require a default branch.
  CS-SPEC-04: Redirect nodes do not carry topic-scoped variables.
  CS-SPEC-05: End of conversation nodes terminate the session.
  CS-SPEC-06: Escalation nodes open human agent session.
  CS-SPEC-07: Fallback topic activates when no trigger phrase exceeds threshold.

### 0-B: Prohibited Terms
  intent | dialog | slot | NLU | utterance | chatbot | handoff | context | bot
  These terms must not appear in any Developer output (Phases 1-6).
  Developer will scan per turn (PROHIBITED_TERM_SCAN field).
  Auditor will independently re-scan in Phase 7.

### 0-C: Developer Assertion Fields (mandatory on every turn in Phase 2)
  Field: SPEC_CONFORMANCE
    Legal values: CONFORMS | DEVIATES[CS-SPEC-NN: description of violation]
    Illegal: any prose verdict, any qualified statement, any "/" notation

  Field: PROHIBITED_TERM_SCAN
    Legal values: CLEAN | FOUND[term at exact location in this turn]
    Illegal: any narrative scan, any reference to a future phase scan

  Field: DEFECT_VERDICT (Phase 3 defect matrix, all four rows)
    Legal values: FOUND | CONFIRMED_ABSENT
    CONFIRMED_ABSENT requires: explicit scope statement (topics/nodes checked)
    FOUND requires: evidence + reproduction sequence (exact inputs -> failure mode)
    Illegal: "likely absent", "probably clean", "appears to be", "no evidence found"

  Field: FALLBACK_QUALITY (Phase 4 terminal verdict)
    Legal values: COMPLETE | LOOPS | TRUNCATED

  Field: ADVERSARIAL_OUTCOME (Phase 5 terminal verdict)
    Legal values: GRACEFUL | BRITTLE | SILENT_FAILURE

### 0-D: Auditor Assertion Fields (Phase 7 only -- Developer does not use these)
  Field: AUDITOR_SPEC_CONFORMANCE
    Legal values: CONFORMS | DEVIATES[CS-SPEC-NN: description]

  Field: AUDITOR_PROHIBITED_TERM_SCAN
    Legal values: CLEAN | FOUND[term at exact location]

  Field: DISCREPANCY
    Legal values: NONE | FOUND[SPEC_CONFORMANCE] | FOUND[PROHIBITED_TERM] | FOUND[BOTH]

### 0-E: Auditor Scope Commitment (Auditor pre-commits to checking these in Phase 7)
  1. Every turn from Phase 2 Trace Table: independent AUDITOR_SPEC_CONFORMANCE verdict
  2. Every turn from Phase 2 Trace Table: independent AUDITOR_PROHIBITED_TERM_SCAN verdict
  3. DISCREPANCY detection: compare Developer verdict to Auditor verdict per turn
  4. Full prohibited term body scan across Phases 1-6 (not just per-turn fields)
  5. Defect matrix (Phase 3): verify all four rows have legal DEFECT_VERDICT values
  6. Coverage metrics (Phase 6): verify ratios present

PHASE 0 GATE: Topology spec declared (7 rules). Prohibited terms listed (9 terms).
Developer assertion fields declared (5 fields, all enum values specified).
Auditor assertion fields declared (3 fields, all enum values specified).
Auditor scope committed (6 items). Developer may now begin Phase 1.

---

## PHASE 1: SETUP
[Conversation Designer speaks. Define agent topology.]

Agent name: [Name or description]
Topics in graph: [N total]:
  [Topic-A], [Topic-B], [Topic-C], ...
Trigger phrases (2-3 per topic):
  [Topic-A]: "[phrase-1]", "[phrase-2]"
  [Topic-B]: "[phrase-1]", "[phrase-2]"
Fallback topic: [Name / "System Fallback Topic" / "not configured"]
Escalation path: [Topic containing escalation node / "not configured"]
Session variables:
  [VarName]: scope=[topic-scoped / global], type=[Text/Number/Boolean], initial=[value or "unset"]
Knowledge sources:
  [Name]: type=[SharePoint / Dataverse / file upload], content=[description] / "none configured"
Coverage scope: [N] of [Total] topics ([pct]%).
Conversation goal: [What the user is trying to accomplish]
Intended topic sequence: [Topic-A] -> [Topic-B] -> [terminal: escalation / end / root]

SETUP GATE: Topology declared. Session variables enumerated. Coverage scope stated. Advance to Phase 2.

---

## PHASE 2: TRACE TABLE
[Copilot Studio Developer speaks. Fill one row per turn using Phase 0 assertion schema.
All columns mandatory. Use Phase 0 enum values only -- no substitutions, no free text in
SPEC_CONFORMANCE or PROHIBITED_TERM_SCAN cells.]

| Turn | User Input | Trigger Phrase Matched | Confidence | Topic | Nodes Executed | Session Variables (name=value; scope; changed/held/cleared) | Agent Response | SPEC_CONFORMANCE | PROHIBITED_TERM_SCAN |
|------|-----------|----------------------|------------|-------|----------------|-------------------------------------------------------------|---------------|-----------------|---------------------|
| T-01 | "[input]" | "[phrase]" | HIGH/MED/LOW | [Topic] | Trigger>Message>Question | var1=X (global, changed); var2=Y (topic-scoped, held) | "[response]" | CONFORMS \| DEVIATES[CS-SPEC-NN: description] | CLEAN \| FOUND[term at location] |
[...one row per turn, no rows skipped]

TRACE GATE: All [N] rows present. SPEC_CONFORMANCE (Phase 0 schema) on every row.
PROHIBITED_TERM_SCAN (Phase 0 schema) on every row. Session variables tracked. Advance to Phase 3.

---

## PHASE 3: DEFECT MATRIX
[Use Phase 0 DEFECT_VERDICT enum. CONFIRMED_ABSENT requires scope. FOUND requires reproduction.
All four rows required.]

| Defect Class | DEFECT_VERDICT | Evidence | Reproduction Sequence | Disambiguation (if FOUND collision) |
|-------------|---------------|----------|-----------------------|-------------------------------------|
| Dead end | FOUND \| CONFIRMED_ABSENT | [evidence / scope: topics checked] | [utterances -> dead state / N/A] | N/A |
| Infinite loop | FOUND \| CONFIRMED_ABSENT | [loop path / acyclic confirmation] | [cycle sequence / N/A] | N/A |
| Trigger phrase collision | FOUND \| CONFIRMED_ABSENT | [phrase + competing topics + scores / scope] | [ambiguous input -> dual activation / N/A] | [entity enrichment / condition ordering / trigger phrase refactor + rationale / N/A] |
| Missing fallback | FOUND \| CONFIRMED_ABSENT | [topic + node + unhandled branch / scope] | [input -> silent routing / N/A] | N/A |

DEFECT GATE: All four rows use Phase 0 DEFECT_VERDICT enum. Scope or reproduction present on
every row. Advance to Phase 4.

---

## PHASE 4: FALLBACK CHAIN
[Walk to terminal state. Reference CS-SPEC-07. Use Phase 0 FALLBACK_QUALITY enum.]

Unrecognized input: "[phrase]"
| Step | Node | Action | Next | CS-SPEC Reference |
|------|------|--------|------|-------------------|
| F-01 | Trigger phrase matching | [N] topics evaluated, 0 above threshold | Fallback topic activation | CS-SPEC-07 |
| F-02 | [Fallback first node] | [action] | [next node] | |
[...trace to terminal]

FALLBACK_QUALITY: COMPLETE | LOOPS | TRUNCATED

FALLBACK GATE: Path traced to terminal state. Phase 0 FALLBACK_QUALITY enum used. Advance to Phase 5.

---

## PHASE 5: ADVERSARIAL INJECTION
[One scenario. Use Phase 0 ADVERSARIAL_OUTCOME enum.]

| Field | Value |
|-------|-------|
| Scenario type | mid-flow topic switch \| unexpected input \| session timeout |
| Scenario | [description] |
| Injected at | Turn T-[NN], after [session state] |
| Node path | [trace] |
| Session variable impact | [what changes or is lost] |
| Agent response | [text] |
| ADVERSARIAL_OUTCOME | GRACEFUL \| BRITTLE \| SILENT_FAILURE |

ADVERSARIAL GATE: All fields populated. Phase 0 ADVERSARIAL_OUTCOME enum used. Advance to Phase 6.

---

## PHASE 6: COVERAGE + AMENDMENTS

| Metric | Visited | Total (estimated) | Ratio |
|--------|---------|-------------------|-------|
| Topics | [N] | [Total] | [N/Total] ([pct]%) |
| Trigger phrases | [N] | [Total estimated] | [N/Total] ([pct]%) |

Amendments (for each FOUND defect and each DEVIATES row from Phase 2):
  CS-SPEC-NN: [violation]
    Trigger sequence: [exact inputs -> failure]
    Fix: [specific change]
    Priority: P1 / P2 / P3

COVERAGE GATE: Coverage ratios reported. All FOUND/DEVIATES items have amendments.
Phases 1-6 complete. Developer Artifact is closed. Advance to Phase 7.

---

## === DEVELOPER ARTIFACT COMPLETE (Phases 1-6) ===
## === AUDITOR NOW READS THE COMPLETED ARTIFACT ===

---

## PHASE 7: AUDITOR APPLIES CONTRACT
[Compliance Auditor speaks. Phases 1-6 are now a finished artifact.
Apply the Phase 0 contract. Developer role has ended -- do not consult it.
Re-annotate every row from Phase 2 independently.
Use Phase 0 Auditor assertion fields (AUDITOR_SPEC_CONFORMANCE, AUDITOR_PROHIBITED_TERM_SCAN,
DISCREPANCY) -- these fields were declared by the Auditor in Phase 0 and the Developer
never used them. This is the post-production audit layer.]

Input document: Developer Artifact, Phase 2 Trace Table rows T-01 through T-[N].
Contract reference: Phase 0 Section 0-D (Auditor assertion fields and enum values).

### 7-A: Per-Turn Audit Table
| Turn | Dev SPEC_CONFORMANCE | AUDITOR_SPEC_CONFORMANCE | Dev PROHIBITED_TERM_SCAN | AUDITOR_PROHIBITED_TERM_SCAN | DISCREPANCY |
|------|---------------------|------------------------|--------------------------|------------------------------|------------|
| T-01 | [from Phase 2] | CONFORMS \| DEVIATES[CS-SPEC-NN: description] | [from Phase 2] | CLEAN \| FOUND[term at location] | NONE \| FOUND[SPEC_CONFORMANCE] \| FOUND[PROHIBITED_TERM] \| FOUND[BOTH] |
[...one row per turn from Phase 2]

### 7-B: Prohibited Term Body Scan (Phases 1-6 full text)
| Term | Present in Developer Artifact | Location |
|------|------------------------------|----------|
| intent | YES \| NO | [Phase N, Turn T-NN / N/A] |
| dialog | YES \| NO | [location / N/A] |
| slot | YES \| NO | [location / N/A] |
| NLU | YES \| NO | [location / N/A] |
| utterance | YES \| NO | [location / N/A] |
| chatbot | YES \| NO | [location / N/A] |
| handoff | YES \| NO | [location / N/A] |
| context | YES \| NO | [location / N/A] |
| bot | YES \| NO | [location / N/A] |
PROHIBITED_TERM_BODY_SCAN: CLEAN | FOUND[list terms and locations]

### 7-C: Defect Matrix Validation
  Phase 3 rows reviewed: all four rows present? YES | NO
  DEFECT_VERDICT enum compliance: all rows use Phase 0 legal values? YES | NO
  CONFIRMED_ABSENT scope statements: all present? YES | NO
  FOUND reproduction sequences: all present? YES | NO

### 7-D: Auditor Summary
  Phase 0 contract applied: YES
  Turns audited: [N]
  Discrepancies (DISCREPANCY != NONE): [N]
    - False-clean SPEC_CONFORMANCE: [N]
    - False-clean PROHIBITED_TERM_SCAN: [N]
  Prohibited term body scan: CLEAN | FOUND
  Defect matrix compliance: CLEAN | ISSUES_FOUND
  AUDIT_VERDICT: CLEAN | ISSUES_FOUND
```

---

## Variation Summary

| V | New Axes | C-12 Mechanism | C-13 Mechanism | Predicted |
|---|----------|----------------|----------------|-----------|
| V-01 | Output Format (table) | Auditor post-production table re-annotation (same as R3 V-03/V-04) | SPEC_CONFORMANCE + PROHIBITED_TERM_SCAN as mandatory typed table columns | 100 |
| V-02 | Phrasing Register (imperative) | Step 11 Auditor section -- but no hard artifact boundary, no phase gate enforcing Developer completion before Auditor begins | Per-step typed field specification in step 4 | 98.33 |
| V-03 | Lifecycle Emphasis (contract-first) | Phase 0 Auditor pre-declares roles and boundaries; === boundaries + gate enforce post-production separation | Phase 0 declares all assertion fields and enum values before Developer produces any output | 100 |
| V-04 | Output Format + Lifecycle Emphasis | Phase 0 Auditor declares S-06 schema; Developer cannot produce untyped verdicts; Auditor fills S-06 post-production | S-01 through S-05 schemas lock all typed column shapes; Developer fills pre-committed schemas | 100 |
| V-05 | Full synthesis | Phase 0 contract pre-declares separation; gate prevents Phase 7 until Phases 1-6 complete; Auditor uses Phase 0 Auditor fields never used by Developer | Phase 0 explicitly enumerates illegal patterns (prose verdict, "/" notation, "likely absent") alongside legal values -- strongest enum enforcement shape | 100 |

**Key insight in V-02 predicted miss:** Imperative phrasing removes phase scaffolding. Without
"Phase 7 begins after Developer Artifact is complete," the model tends to treat the Auditor
section as a continuation of the same production pass rather than a separate post-production
read. Step 11 becomes an annotation of work-in-progress rather than an audit of a finished
artifact. The phase gate is load-bearing for C-12, not cosmetic.

**Key insight in V-03/V-04/V-05 causal inversion:** R3 mechanisms: Developer declares its own
assertion format (self-defines verdict schema), Auditor reads the result. R4 contract-first
mechanism: Auditor declares the verdict schema, Developer fills it. This inverts the schema
authorship from Developer to Auditor -- the pre-commitment is upstream, not retroactive.
Whether this produces a detectable quality difference in the output (not just in causal structure)
is the open empirical question.
