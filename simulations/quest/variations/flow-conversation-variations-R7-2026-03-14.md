Now I have the full picture. V-03 and V-04 from R6 hit 100/100 by introducing topology invariant registry (C-18). For R7 I need axes that might surface patterns not yet in C-01–C-18. The gaps I see:

- **Reachability completeness** — C-18 covers node-level structural invariants, but not path-level: "is every topic reachable from entry?"
- **State persistence classification** — C-03 tracks state per-turn but doesn't require pre-classifying each variable's persistence scope (EPHEMERAL vs PERSISTENT vs SESSION-SCOPED)
- **Recovery path closure** — C-05 requires reproduction steps for found defects, but not: "what is the escape path back to a healthy state?"
- **Defect severity triage** — FOUND/CONFIRMED_ABSENT (C-13) says nothing about P0/P1/P2 business impact

Writing the 5 variations now.

---

# Variations — flow-conversation — Round 7 (2026-03-14)

**Rubric version:** v6 | **Skill:** flow-conversation

---

## V-01

**Axis:** Lifecycle emphasis — recovery path closure phase
**Hypothesis:** Inserting a mandatory post-defect-identification phase that traces the escape path from each found defect back to a healthy agent state may surface a new criterion: recovery path completeness. C-05 requires reproduction (how do you arrive at the defect?) but not recovery (how does the agent leave it?). An unrecoverable defect is categorically different from a recoverable one and the current rubric cannot distinguish them.

---

You are simulating a multi-turn Copilot Studio conversation-flow trace. You will play two roles sequentially: **Developer** and **Auditor**. The Developer produces the trace and classification artifacts. The Auditor reads the completed Developer artifact and produces an independent audit layer. A hard phase-gate boundary marker separates production from audit. The Developer SHALL NOT self-certify. The Auditor SHALL NOT produce output before the boundary marker appears.

You are the domain expert for Copilot Studio. All analysis uses Copilot Studio vocabulary throughout.

---

### PHASE 0-D — Developer Domain Pre-Contract

*You are the Developer. Declare the following before any trace output exists. The Auditor SHALL NOT begin Phase 0-A until this block is complete.*

**0-D-1 Agent Topology Declaration**

Enumerate every topic in the agent graph:

```
TOPIC_REGISTRY:
  - ID: TOPIC-NN
    Name: [topic name]
    Type: CONVERSATIONAL | SYSTEM | FALLBACK
    Entry_Trigger_Phrases: [list all registered trigger phrases]
    Condition_Nodes: [list condition evaluations]
    Terminal_Exit: YES | NO
    Redirect_Targets: [list topics this topic may redirect to]
```

**0-D-2 Copilot Studio Vocabulary Binding**

Declare the CS-to-generic term mapping. Every generic term on the right is PROHIBITED in all subsequent output:

```
CS_VOCABULARY_BINDING:
  topic         → NOT: dialog, skill, intent handler
  trigger phrase → NOT: intent, utterance class, NLU slot
  condition      → NOT: if-block, branch logic
  fallback topic → NOT: default handler, catch-all
  escalation     → NOT: handoff, transfer
  session variable → NOT: slot, context variable, state variable
  redirect       → NOT: goto, jump, transfer
```

**0-D-3 Session Variable Registry with Persistence Classification**

Declare every session variable used in the agent:

```
SESSION_VARIABLE_REGISTRY:
  - Name: [variable name]
    PERSISTENCE_CLASS: EPHEMERAL | PERSISTENT | SESSION-SCOPED
    Set_By: [topic name]
    Cleared_By: [topic name or "topic-exit" or "session-end"]
    Used_By: [list of topics that read this variable]
```

`EPHEMERAL`: cleared automatically on topic exit.
`PERSISTENT`: survives topic transitions within the session.
`SESSION-SCOPED`: survives until session ends or explicit clear.

**0-D-4 Structural Invariants**

Pre-commit named invariants representing design-time guarantees about the topology:

```
INVARIANT_REGISTRY:
  - ID: INVARIANT-TOPO-01
    Claim: [structural claim about the topology]
    Scope: ALL_TOPICS | [specific topic IDs]
  - ID: INVARIANT-SV-01
    Claim: [structural claim about session variable lifecycle]
    Scope: [variable name]
```

Every `CONFIRMED_ABSENT` defect row in Phase 3 MUST cite the INVARIANT-TOPO-NN or INVARIANT-SV-NN that structurally precludes the defect. A CONFIRMED_ABSENT row without an invariant citation is a contract violation.

---

### PHASE 0-A — Auditor Assertion Contract

*You are the Auditor. Declare the complete assertion schema before the Developer begins Phase 1. The Developer is bound to this schema in all subsequent phases. The Developer SHALL NOT begin Phase 1 until this block is complete.*

**Trace Table Schema (Phase 1)**

Every row in the Phase 1 trace table SHALL contain exactly these columns. A blank cell in any mandatory column is a structural violation:

```
| TURN | USER_UTTERANCE | TRIGGER_PHRASE_MATCHED | TOPIC | NODES_EXECUTED | SESSION_STATE | AGENT_RESPONSE | SPEC_CONFORMANCE | PROHIBITED_TERM_SCAN | INVARIANT_CONFORMANCE |
```

Column definitions:
- `TURN`: T-NN sequential integer
- `SESSION_STATE`: show all active session variables with current values and persistence class; mark CLEARED on topic exit per PERSISTENCE_CLASS declaration
- `SPEC_CONFORMANCE`: `CONFORMS | DEVIATES[CS-SPEC-NN: description]`
- `PROHIBITED_TERM_SCAN`: `CLEAN | FOUND[term]`
- `INVARIANT_CONFORMANCE`: `HOLDS | VIOLATED[INVARIANT-ID: description]`

**Defect Classification Schema (Phase 3)**

```
DEFECT_CLASS: DEAD_END | INFINITE_LOOP | TRIGGER_PHRASE_COLLISION | MISSING_FALLBACK
DEFECT_VERDICT: FOUND | CONFIRMED_ABSENT
```

For FOUND rows: reproduction sequence required (exact utterance path → failure mode). For CONFIRMED_ABSENT rows: cite the INVARIANT-TOPO-NN or INVARIANT-SV-NN that structurally guarantees absence. A CONFIRMED_ABSENT row without an invariant citation is a contract violation.

**Recovery Path Schema (Phase 3-R)**

For every FOUND defect row, a corresponding RECOVERY record is required:

```
DEFECT_REF: [DEFECT_CLASS and turn reference]
RECOVERY_PATH: [minimum utterance sequence that returns agent to TOPIC-NN healthy state]
RECOVERY_VERDICT: RECOVERABLE[min_turns=N, target=TOPIC-NN] | UNRECOVERABLE[reason]
UNRECOVERABLE_CONSEQUENCE: [what happens if defect is never escaped — session stuck, escalation forced, etc.]
```

`UNRECOVERABLE` means no utterance sequence can restore normal flow without a session restart or forced escalation. This is a categorically distinct defect class from a recoverable one.

**Other typed fields:**

```
FALLBACK_QUALITY: COMPLETE | LOOPS | TRUNCATED
ADVERSARIAL_OUTCOME: HANDLED | REDIRECT | FALLBACK_TRIGGERED | SESSION_CORRUPTED
GAP_CLOSURE_VERDICT: CLOSED | OPEN
```

No free-text in any verdict position. Free-text = contract violation.

---

### PHASE 1 — Developer: Dialog Trace

*You are the Developer. Simulate the full multi-turn conversation. One row per turn. Do not skip turns. Do not collapse turns into summaries.*

Produce the mandatory 9-column trace table. All columns populated on every row.

Walk the happy path first, then at least one alternate path, then at least one adversarial injection scenario.

---

### PHASE 2 — Developer: Defect Classification

*You are the Developer. Address all four defect classes explicitly. No class may be omitted.*

```
| DEFECT_CLASS | DEFECT_VERDICT | EVIDENCE | INVARIANT_CITE |
```

- `DEAD_END`: FOUND with reproduction OR CONFIRMED_ABSENT citing INVARIANT-TOPO-NN
- `INFINITE_LOOP`: FOUND with reproduction OR CONFIRMED_ABSENT citing INVARIANT-TOPO-NN
- `TRIGGER_PHRASE_COLLISION`: FOUND with competing topics + disambiguation strategy OR CONFIRMED_ABSENT citing scope
- `MISSING_FALLBACK`: FOUND with missing branch OR CONFIRMED_ABSENT citing INVARIANT-TOPO-NN

*GAP_CLOSURE_VERDICT: CLOSED | OPEN [Gap-R1-02: all four defect classes addressed]*

---

### PHASE 3-R — Developer: Recovery Path Closure

*You are the Developer. For every FOUND defect row in Phase 2, produce a recovery record. If Phase 2 has zero FOUND rows, produce one entry stating RECOVERY_REQUIRED: NONE with citation to all CONFIRMED_ABSENT invariants.*

```
| DEFECT_REF | RECOVERY_PATH | RECOVERY_VERDICT | UNRECOVERABLE_CONSEQUENCE |
```

Walk the minimum recovery sequence for each FOUND defect. Count the turns. Name the target topic the agent reaches when healthy. If no path exists, state UNRECOVERABLE and describe what a user experiences.

*GAP_CLOSURE_VERDICT: CLOSED | OPEN [Gap-R7-01: recovery path completeness not verified in prior rounds]*

---

### PHASE 4 — Developer: Fallback Chain Trace

*You are the Developer. Trace one complete fallback path from unrecognized input to terminal state.*

Show each node in the fallback chain. Include escalation if present. Show session variable state at each step.

`FALLBACK_QUALITY: COMPLETE | LOOPS | TRUNCATED`

If LOOPS: cite the INVARIANT-TOPO-NN that is VIOLATED.
If TRUNCATED: describe where the chain stops and why.

Inject one adversarial turn during fallback chain. Show `ADVERSARIAL_OUTCOME`.

*GAP_CLOSURE_VERDICT: CLOSED | OPEN [Gap-R2-04: fallback to terminal traced]*

---

### PHASE 5 — Developer: Coverage Summary

*You are the Developer. Report coverage ratios.*

```
| METRIC | VISITED | TOTAL | RATIO |
| Topics exercised | N | M | N/M |
| Trigger phrases exercised | N | M | N/M |
| Invariants verified HOLDS | N | M | N/M |
| Session variables verified per PERSISTENCE_CLASS | N | M | N/M |
```

*GAP_CLOSURE_VERDICT: CLOSED | OPEN [Gap-R3-05: quantified coverage signal]*

---

### PHASE 5-V — Developer: Vocabulary Compliance Scan

*You are the Developer. Scan the full output above for prohibited terms.*

```
| PROHIBITED_TERM | FOUND_IN_OUTPUT | LOCATION |
| intent | YES | NO |
| dialog | YES | NO |
| slot | YES | NO |
| NLU | YES | NO |
| chatbot | YES | NO |
| handoff | YES | NO |
```

*GAP_CLOSURE_VERDICT: CLOSED | OPEN [Gap-R4-10: active vocabulary enforcement]*

---

```
=== DEVELOPER ARTIFACT COMPLETE (Phases 0-D through 5-V) ===
=== AUDITOR NOW READS THE COMPLETED ARTIFACT AS A FINISHED DOCUMENT ===
```

---

### PHASE 6 — Auditor: Independent Audit

*You are the Auditor. You are now reading the Developer's completed artifact. Do not produce inline commentary during trace. Read the full artifact, then produce this audit layer.*

**6-A: Trace Table Audit**

For each turn row, verify all mandatory columns are populated and enums are valid. Report:

```
| TURN | SPEC_CONFORMANCE_VALID | PROHIBITED_TERM_SCAN_VALID | INVARIANT_CONFORMANCE_VALID | DISCREPANCY |
```

`DISCREPANCY: NONE | FOUND[column: issue]`

**6-B: Defect Matrix Audit**

For each defect class row, verify CONFIRMED_ABSENT rows carry valid invariant citations. Report:

```
| DEFECT_CLASS | INVARIANT_CITE_VALID | DISCREPANCY |
```

**6-C: Recovery Path Audit**

For each recovery record, independently verify the recovery path is minimal and the verdict is correctly assigned:

```
| DEFECT_REF | RECOVERY_PATH_VALID | VERDICT_VALID | AUDITOR_RECOVERY_VERDICT | DISCREPANCY |
```

If Developer declared UNRECOVERABLE but Auditor can identify a recovery path: DISCREPANCY = FOUND[RECOVERY_PATH: shorter path exists].
If Developer declared RECOVERABLE but path is incomplete: DISCREPANCY = FOUND[RECOVERY_PATH: path does not reach healthy state].

**6-D: Invariant Cross-Audit**

For each INVARIANT-TOPO-NN and INVARIANT-SV-NN declared in Phase 0-D:

```
| INVARIANT_ID | DEVELOPER_PHASE5_VERDICT | AUDITOR_PHASE6_VERDICT | DISCREPANCY |
```

`DISCREPANCY: NONE | FOUND[INVARIANT-ID: Developer claims HOLDS but trace shows VIOLATED]`

**6-E: Gap-Closure Audit**

```
| PHASE | GAP_TAG | DEVELOPER_CLOSURE | AUDITOR_VERIFICATION | REGRESSION |
```

`REGRESSION: YES | NO` — YES if a gap closed in a prior round is re-opened by this trace.

*GAP_CLOSURE_VERDICT: CLOSED | OPEN [Gap-R6-02: cross-auditor invariant verification]*

---

## V-02

**Axis:** Output format — state persistence classification registry as structural enforcement layer
**Hypothesis:** C-03 tracks session state per-turn but does not require pre-classifying each variable's persistence scope. Promoting PERSISTENCE_CLASS to a first-class pre-contract — with per-turn verification that variables clear on topic exit or survive as declared — may surface a new criterion: state persistence contract enforcement. This is distinct from C-18 (INVARIANT-SV-NN) in that C-18 names an invariant; this variation makes the persistence declaration the derivation source for per-turn expected behavior, with a mandatory mismatch column.

---

You are simulating a multi-turn Copilot Studio conversation-flow trace. You play two roles sequentially: **Developer** (produces trace and classification) and **Auditor** (reads completed artifact, produces independent audit). The hard boundary marker below separates production from audit.

You are the Copilot Studio domain expert. All analysis uses Copilot Studio vocabulary throughout.

---

### PHASE 0-D — Developer Domain Pre-Contract

*You are the Developer. Complete this block before the Auditor writes Phase 0-A. The Auditor SHALL NOT begin Phase 0-A until Phase 0-D is complete.*

**0-D-1 Topic Inventory**

```
TOPIC_REGISTRY:
  - ID: TOPIC-NN
    Name: [topic name]
    Type: CONVERSATIONAL | SYSTEM | FALLBACK
    Trigger_Phrases: [list]
    Exits_To: [list of redirect targets]
    Terminal: YES | NO
```

**0-D-2 CS Vocabulary Binding (prohibited terms listed)**

```
PROHIBITED_TERMS: intent, dialog, slot, NLU, chatbot, handoff, utterance class, context variable, state variable, if-block
```

**0-D-3 State Persistence Contract**

This is the load-bearing declaration for Phase 1 session state verification. Declare every session variable:

```
STATE_PERSISTENCE_CONTRACT:
  - Variable: [name]
    PERSISTENCE_CLASS: EPHEMERAL | PERSISTENT | SESSION-SCOPED
    Set_By: [topic ID]
    Expected_Clear_Event: topic-exit | explicit-clear | session-end | never
    Read_By: [list of topic IDs]
    Expected_Value_After_Topic_Exit: NULL | [retained_value]
```

`EPHEMERAL`: `Expected_Value_After_Topic_Exit = NULL`. If any topic reads this variable after the Set_By topic has exited and finds a non-NULL value, that is a `PERSISTENCE_MISMATCH: FOUND`.

`PERSISTENT`: value retained across topic transitions until explicit-clear.

`SESSION-SCOPED`: retained until session ends.

The Phase 1 trace table SHALL include a `PERSISTENCE_MISMATCH` column derived from these declarations.

**0-D-4 Topology Invariants**

```
INVARIANT_REGISTRY:
  - ID: INVARIANT-TOPO-NN
    Claim: [structural claim]
  - ID: INVARIANT-SV-NN
    Claim: [state persistence structural claim, e.g., "All EPHEMERAL variables are cleared on TOPIC-NN exit"]
```

Every CONFIRMED_ABSENT defect row SHALL cite the invariant that precludes the defect.

---

### PHASE 0-A — Auditor Assertion Contract

*You are the Auditor. Declare the complete assertion schema now. The Developer is bound to this schema. The Developer SHALL NOT begin Phase 1 until Phase 0-A is complete.*

**Trace Table Schema**

Mandatory columns — blank cell = structural violation:

```
| TURN | USER_UTTERANCE | TRIGGER_PHRASE_MATCHED | TOPIC | NODES_EXECUTED | SESSION_STATE_VALUES | PERSISTENCE_MISMATCH | AGENT_RESPONSE | SPEC_CONFORMANCE | PROHIBITED_TERM_SCAN | INVARIANT_CONFORMANCE |
```

`SESSION_STATE_VALUES`: for each variable, show `[name]=[value] (class=EPHEMERAL|PERSISTENT|SESSION-SCOPED, status=SET|HELD|CLEARED)`. Topic-exit turn MUST show CLEARED for all EPHEMERAL variables.

`PERSISTENCE_MISMATCH: NONE | FOUND[variable: expected_class vs observed_behavior]`

A PERSISTENCE_MISMATCH of FOUND is automatically a defect — it represents a state persistence contract violation.

**Defect Classification Schema**

```
DEFECT_CLASS: DEAD_END | INFINITE_LOOP | TRIGGER_PHRASE_COLLISION | MISSING_FALLBACK | PERSISTENCE_CONTRACT_VIOLATION
DEFECT_VERDICT: FOUND | CONFIRMED_ABSENT
```

Note: `PERSISTENCE_CONTRACT_VIOLATION` is a fifth defect class in this variation. It surfaces any case where a variable's observed persistence behavior contradicts the STATE_PERSISTENCE_CONTRACT declaration.

For CONFIRMED_ABSENT: cite INVARIANT-TOPO-NN or INVARIANT-SV-NN.

**Other typed fields:**

```
SPEC_CONFORMANCE: CONFORMS | DEVIATES[CS-SPEC-NN: desc]
PROHIBITED_TERM_SCAN: CLEAN | FOUND[term]
INVARIANT_CONFORMANCE: HOLDS | VIOLATED[ID: desc]
FALLBACK_QUALITY: COMPLETE | LOOPS | TRUNCATED
ADVERSARIAL_OUTCOME: HANDLED | REDIRECT | FALLBACK_TRIGGERED | SESSION_CORRUPTED
GAP_CLOSURE_VERDICT: CLOSED | OPEN
```

No free-text in verdict positions.

---

### PHASE 1 — Developer: Dialog Trace

*You are the Developer. Walk the conversation turn-by-turn. Do not skip turns. Do not summarize.*

Produce the 10-column trace table per the Phase 0-A schema. For every topic-exit turn: all EPHEMERAL variables MUST show `status=CLEARED`. If an EPHEMERAL variable shows HELD after topic exit, record `PERSISTENCE_MISMATCH: FOUND`.

Walk at least: happy path, one redirect path, one adversarial injection.

*GAP_CLOSURE_VERDICT: CLOSED | OPEN [Gap-R1-01: turn-by-turn dialog trace]*

---

### PHASE 2 — Developer: Defect Classification

*You are the Developer. Address all five defect classes: DEAD_END, INFINITE_LOOP, TRIGGER_PHRASE_COLLISION, MISSING_FALLBACK, PERSISTENCE_CONTRACT_VIOLATION.*

```
| DEFECT_CLASS | DEFECT_VERDICT | EVIDENCE | INVARIANT_CITE |
```

For PERSISTENCE_CONTRACT_VIOLATION: cite the STATE_PERSISTENCE_CONTRACT entry violated and the turn where the mismatch occurred. Reproduction sequence: exact topic sequence that causes the wrong persistence behavior.

For CONFIRMED_ABSENT: cite INVARIANT-SV-NN (for persistence-class violations) or INVARIANT-TOPO-NN (for structural defects).

*GAP_CLOSURE_VERDICT: CLOSED | OPEN [Gap-R1-02: all defect classes addressed]*

---

### PHASE 3 — Developer: Fallback Chain Trace

*You are the Developer. Trace one complete fallback path from unrecognized input to terminal state. Include escalation if present.*

Show session variable state (with persistence class) at each fallback node. Show `FALLBACK_QUALITY`.

Inject one adversarial turn. Show `ADVERSARIAL_OUTCOME`. If SESSION_CORRUPTED: describe which variables were corrupted and whether that contradicts their PERSISTENCE_CLASS declaration.

*GAP_CLOSURE_VERDICT: CLOSED | OPEN [Gap-R2-04: fallback to terminal traced]*

---

### PHASE 4 — Developer: Coverage and Persistence Contract Summary

*You are the Developer.*

**4-A Coverage Ratios**

```
| METRIC | VISITED | TOTAL | RATIO |
| Topics | N | M | N/M |
| Trigger phrases | N | M | N/M |
| Invariants verified | N | M | N/M |
```

**4-B State Persistence Contract Verification Summary**

```
| VARIABLE | PERSISTENCE_CLASS | CONTRACT_HONORED | EVIDENCE |
```

`CONTRACT_HONORED: YES | NO[turn reference]`

One row per variable declared in STATE_PERSISTENCE_CONTRACT. This is the completeness certificate for persistence contract enforcement.

*GAP_CLOSURE_VERDICT: CLOSED | OPEN [Gap-R3-05: quantified coverage; Gap-R7-02: persistence contract verification summary]*

---

### PHASE 4-V — Developer: Vocabulary Compliance Scan

```
| PROHIBITED_TERM | FOUND_IN_OUTPUT | LOCATION |
```

*GAP_CLOSURE_VERDICT: CLOSED | OPEN [Gap-R4-10: active vocabulary enforcement]*

---

```
=== DEVELOPER ARTIFACT COMPLETE (Phases 0-D through 4-V) ===
=== AUDITOR NOW READS THE COMPLETED ARTIFACT AS A FINISHED DOCUMENT ===
```

---

### PHASE 5 — Auditor: Independent Audit

*You are the Auditor. Read the completed Developer artifact. Produce the following.*

**5-A: Trace Table Audit**

```
| TURN | PERSISTENCE_MISMATCH_VALID | SPEC_CONFORMANCE_VALID | INVARIANT_CONFORMANCE_VALID | DISCREPANCY |
```

Pay particular attention to topic-exit turns: verify EPHEMERAL variables show CLEARED per the STATE_PERSISTENCE_CONTRACT.

**5-B: Defect Matrix Audit**

```
| DEFECT_CLASS | VERDICT_VALID | INVARIANT_CITE_VALID | DISCREPANCY |
```

Verify that PERSISTENCE_CONTRACT_VIOLATION rows correctly cross-reference the STATE_PERSISTENCE_CONTRACT entry.

**5-C: Persistence Contract Cross-Audit**

For each variable in STATE_PERSISTENCE_CONTRACT:

```
| VARIABLE | PERSISTENCE_CLASS | DEVELOPER_PHASE4B_VERDICT | AUDITOR_VERDICT | DISCREPANCY |
```

`DISCREPANCY: NONE | FOUND[variable: Developer claims CONTRACT_HONORED=YES but trace shows PERSISTENCE_MISMATCH at T-NN]`

**5-D: Gap-Closure Audit**

```
| PHASE | GAP_TAG | DEVELOPER_CLOSURE | AUDITOR_VERIFICATION | REGRESSION |
```

*GAP_CLOSURE_VERDICT: CLOSED | OPEN [Gap-R6-02: cross-auditor verification]*

---

## V-03

**Axis:** Role sequence — Auditor-first reachability completeness envelope
**Hypothesis:** C-18 covers structural invariants at the node level (every topic has a fallback exit, every variable clears correctly). It does not cover path-level reachability: "is every topic reachable from at least one valid entry point?" A topic that exists in the registry but is unreachable from any trigger phrase or redirect is a structural defect invisible to all current criteria. Requiring the Auditor to pre-commit a topic reachability assertion table — and requiring the Developer to produce a reachability trace that confirms or violates each assertion — may surface a new criterion: reachability completeness envelope.

---

You are simulating a multi-turn Copilot Studio conversation-flow trace. You play two roles sequentially: **Developer** (produces trace and classification) and **Auditor** (reads completed artifact, produces independent audit). The hard boundary marker below separates production from audit.

You are the Copilot Studio domain expert. All analysis uses Copilot Studio vocabulary throughout.

---

### PHASE 0-D — Developer Domain Pre-Contract

*You are the Developer. Complete this block before the Auditor writes Phase 0-A. The Auditor SHALL NOT begin Phase 0-A until Phase 0-D is complete.*

**0-D-1 Topic Inventory with Entry Path Declaration**

For each topic, declare how it can be reached:

```
TOPIC_REGISTRY:
  - ID: TOPIC-NN
    Name: [topic name]
    Type: CONVERSATIONAL | SYSTEM | FALLBACK
    Trigger_Phrases: [list — empty if only reachable via redirect]
    Reachable_Via: TRIGGER_PHRASE | REDIRECT_FROM[TOPIC-MM] | SYSTEM_EVENT | BOTH | NONE
    If_REACHABLE_Via_NONE: this topic is declared UNREACHABLE — structural defect
    Terminal: YES | NO
    Exits_To: [list of redirect targets]
```

**0-D-2 CS Vocabulary Binding**

```
PROHIBITED_TERMS: intent, dialog, slot, NLU, chatbot, handoff, utterance class, context variable, state variable
```

**0-D-3 Session Variable Registry**

```
SESSION_VARIABLE_REGISTRY:
  - Name: [var name]
    Set_By: [topic ID]
    Cleared_By: [topic ID or "topic-exit"]
    Used_By: [list]
```

**0-D-4 Structural Invariants**

```
INVARIANT_REGISTRY:
  - ID: INVARIANT-TOPO-01
    Claim: [e.g., "Every CONVERSATIONAL topic is reachable via at least one trigger phrase or redirect from a CONVERSATIONAL topic"]
  - ID: INVARIANT-TOPO-02
    Claim: [e.g., "Every FALLBACK topic is reachable from the system fallback chain"]
  - ID: INVARIANT-SV-01
    Claim: [session variable structural claim]
```

---

### PHASE 0-A — Auditor Assertion Contract

*You are the Auditor. Declare the complete assertion schema before the Developer begins Phase 1. The Developer is bound to this schema. The Developer SHALL NOT begin Phase 1 until Phase 0-A is complete.*

**Reachability Completeness Envelope**

You are asserting the reachability status of every topic declared in Phase 0-D before the trace exists. This is the Auditor's pre-commitment:

```
REACHABILITY_ENVELOPE:
  - TOPIC_ID: TOPIC-NN
    AUDITOR_REACHABILITY_ASSERTION: REACHABLE | UNREACHABLE | CONDITIONALLY_REACHABLE[condition]
    AUDITOR_ENTRY_PATH_CLAIM: [trigger phrase text OR "redirect from TOPIC-MM" OR "system event"]
    ASSERTION_ID: REACH-NN
```

This envelope is written against the Developer's Phase 0-D topic inventory. Every topic in the inventory MUST have one row. The Developer's Phase 1 reachability trace SHALL confirm or violate each REACH-NN assertion.

**Trace Table Schema**

Mandatory columns — blank cell = structural violation:

```
| TURN | USER_UTTERANCE | TRIGGER_PHRASE_MATCHED | TOPIC | NODES_EXECUTED | SESSION_STATE | AGENT_RESPONSE | SPEC_CONFORMANCE | PROHIBITED_TERM_SCAN | INVARIANT_CONFORMANCE | REACHABILITY_CONFORMANCE |
```

`REACHABILITY_CONFORMANCE: CONFIRMS[REACH-NN] | VIOLATES[REACH-NN: description] | N/A`

`CONFIRMS[REACH-NN]`: this turn demonstrates that TOPIC-NN is reachable via the path declared in REACH-NN.
`VIOLATES[REACH-NN]`: this turn shows TOPIC-NN is NOT reachable via the declared path, or IS reachable when declared UNREACHABLE.

**Reachability Verdict Schema (Phase 2-R)**

After the trace, a mandatory reachability verdict table:

```
REACH_NN_VERDICT:
  ASSERTION_ID: REACH-NN
  AUDITOR_CLAIM: REACHABLE | UNREACHABLE | CONDITIONALLY_REACHABLE
  TRACE_EVIDENCE: CONFIRMED | VIOLATED | NOT_EXERCISED
  FINAL_VERDICT: CONFORMS | DEVIATES[description]
```

`NOT_EXERCISED`: the topic was declared reachable but no turn in the trace exercised it — this is a coverage gap, not necessarily a defect, but MUST be flagged.

**Other typed fields:**

```
DEFECT_CLASS: DEAD_END | INFINITE_LOOP | TRIGGER_PHRASE_COLLISION | MISSING_FALLBACK | UNREACHABLE_TOPIC
DEFECT_VERDICT: FOUND | CONFIRMED_ABSENT
SPEC_CONFORMANCE: CONFORMS | DEVIATES[CS-SPEC-NN]
PROHIBITED_TERM_SCAN: CLEAN | FOUND[term]
INVARIANT_CONFORMANCE: HOLDS | VIOLATED[ID]
FALLBACK_QUALITY: COMPLETE | LOOPS | TRUNCATED
ADVERSARIAL_OUTCOME: HANDLED | REDIRECT | FALLBACK_TRIGGERED | SESSION_CORRUPTED
GAP_CLOSURE_VERDICT: CLOSED | OPEN
```

Note: `UNREACHABLE_TOPIC` is a fifth defect class in this variation. Any topic declared UNREACHABLE in Phase 0-D INVARIANT_REGISTRY — or found unreachable by trace evidence — is a structural defect.

No free-text in verdict positions.

---

### PHASE 1 — Developer: Dialog Trace

*You are the Developer. Walk the conversation turn-by-turn. Do not skip turns. Do not summarize.*

Produce the 10-column trace table per Phase 0-A schema.

For each turn where a new topic is entered, populate `REACHABILITY_CONFORMANCE` with the appropriate REACH-NN verdict. Topics entered via trigger phrase confirm the trigger phrase path assertion. Topics entered via redirect confirm the redirect assertion.

Walk at least: happy path, one redirect path, one adversarial injection.

*GAP_CLOSURE_VERDICT: CLOSED | OPEN [Gap-R1-01: turn-by-turn dialog trace]*

---

### PHASE 2 — Developer: Defect Classification

*You are the Developer. Address all five defect classes: DEAD_END, INFINITE_LOOP, TRIGGER_PHRASE_COLLISION, MISSING_FALLBACK, UNREACHABLE_TOPIC.*

```
| DEFECT_CLASS | DEFECT_VERDICT | EVIDENCE | INVARIANT_CITE |
```

For `UNREACHABLE_TOPIC` FOUND: cite the topic ID and explain why no trigger phrase or redirect reaches it. This is a structural gap in the agent design, not a runtime conversational defect.

For `UNREACHABLE_TOPIC` CONFIRMED_ABSENT: cite INVARIANT-TOPO-01 (or whichever invariant guarantees all topics are reachable) and reference the Reachability Envelope row that confirms reachability.

*GAP_CLOSURE_VERDICT: CLOSED | OPEN [Gap-R1-02: all defect classes addressed]*

---

### PHASE 2-R — Developer: Reachability Envelope Verdict Table

*You are the Developer. For every REACH-NN assertion in the Auditor's Phase 0-A Reachability Envelope, produce one row.*

```
| ASSERTION_ID | TOPIC_ID | AUDITOR_CLAIM | TRACE_EVIDENCE | FINAL_VERDICT |
```

Topics with `NOT_EXERCISED` are flagged as coverage gaps. If a topic is declared REACHABLE by the Auditor but `NOT_EXERCISED` in the trace, a rationale is required: either the trace scope was limited by design or this is a coverage defect.

*GAP_CLOSURE_VERDICT: CLOSED | OPEN [Gap-R7-03: reachability completeness envelope not verified in prior rounds]*

---

### PHASE 3 — Developer: Fallback Chain Trace

*You are the Developer.*

Trace one complete fallback path to terminal. Show `FALLBACK_QUALITY`.

Inject one adversarial turn. Show `ADVERSARIAL_OUTCOME`.

*GAP_CLOSURE_VERDICT: CLOSED | OPEN [Gap-R2-04: fallback to terminal]*

---

### PHASE 4 — Developer: Coverage Summary

```
| METRIC | VISITED | TOTAL | RATIO |
| Topics | N | M | N/M |
| Trigger phrases | N | M | N/M |
| Invariants verified | N | M | N/M |
| Reachability assertions confirmed | N | M | N/M |
```

Note: `Reachability assertions confirmed` = REACH-NN rows with `TRACE_EVIDENCE: CONFIRMED` / total REACH-NN rows.

*GAP_CLOSURE_VERDICT: CLOSED | OPEN [Gap-R3-05: quantified coverage]*

---

### PHASE 4-V — Developer: Vocabulary Compliance Scan

```
| PROHIBITED_TERM | FOUND_IN_OUTPUT | LOCATION |
```

*GAP_CLOSURE_VERDICT: CLOSED | OPEN [Gap-R4-10: vocabulary enforcement]*

---

```
=== DEVELOPER ARTIFACT COMPLETE (Phases 0-D through 4-V) ===
=== AUDITOR NOW READS THE COMPLETED ARTIFACT AS A FINISHED DOCUMENT ===
```

---

### PHASE 5 — Auditor: Independent Audit

*You are the Auditor. Read the completed artifact.*

**5-A: Trace Table Audit**

```
| TURN | REACHABILITY_CONFORMANCE_VALID | SPEC_CONFORMANCE_VALID | INVARIANT_CONFORMANCE_VALID | DISCREPANCY |
```

**5-B: Reachability Envelope Cross-Audit**

For every REACH-NN assertion:

```
| ASSERTION_ID | AUDITOR_ORIGINAL_CLAIM | DEVELOPER_PHASE2R_VERDICT | AUDITOR_INDEPENDENT_VERDICT | DISCREPANCY |
```

`DISCREPANCY: NONE | FOUND[REACH-NN: Developer claims CONFIRMED but turn evidence is ambiguous | Developer claims NOT_EXERCISED but turn T-NN shows TOPIC-NN entered]`

This is the primary new audit layer in this variation. The Auditor pre-committed reachability claims before the trace. The cross-audit verifies whether those claims are confirmed, violated, or untested.

**5-C: Invariant Cross-Audit**

```
| INVARIANT_ID | DEVELOPER_VERDICT | AUDITOR_VERDICT | DISCREPANCY |
```

**5-D: Gap-Closure Audit**

```
| PHASE | GAP_TAG | DEVELOPER_CLOSURE | AUDITOR_VERIFICATION | REGRESSION |
```

*GAP_CLOSURE_VERDICT: CLOSED | OPEN [Gap-R6-02: cross-auditor verification]*

---

## V-04

**Axis:** Combined — Recovery path closure (V-01) + Reachability completeness envelope (V-03)
**Hypothesis:** Recovery paths and reachability assertions target the same structural completeness gap from opposite directions. Reachability asks "can you get to every topic?" Recovery asks "can you leave every defect state?" Together they may surface a unified new criterion: structural completeness envelope — a pre-committed contract covering both entry-path completeness and exit-path completeness, with Auditor-verified cross-audit on both dimensions.

---

You are simulating a multi-turn Copilot Studio conversation-flow trace. You play two roles sequentially: **Developer** (trace and classification) and **Auditor** (independent audit of completed artifact). Hard boundary marker below separates production from audit.

You are the Copilot Studio domain expert. All analysis uses Copilot Studio vocabulary.

---

### PHASE 0-D — Developer Domain Pre-Contract

*You are the Developer. The Auditor SHALL NOT begin Phase 0-A until this block is complete.*

**0-D-1 Topic Inventory with Entry + Exit Paths**

```
TOPIC_REGISTRY:
  - ID: TOPIC-NN
    Name: [name]
    Type: CONVERSATIONAL | SYSTEM | FALLBACK
    Trigger_Phrases: [list]
    Reachable_Via: TRIGGER_PHRASE | REDIRECT_FROM[TOPIC-MM] | SYSTEM_EVENT | BOTH | NONE
    Terminal: YES | NO
    Exits_To: [list of redirect targets or "TERMINAL"]
```

**0-D-2 CS Vocabulary Binding**

```
PROHIBITED_TERMS: intent, dialog, slot, NLU, chatbot, handoff, utterance class, context variable, state variable
```

**0-D-3 Session Variable Registry**

```
SESSION_VARIABLE_REGISTRY:
  - Name: [var]
    Set_By: [topic ID]
    Cleared_By: [topic ID or "topic-exit" or "session-end"]
    Used_By: [list]
```

**0-D-4 Structural Invariants**

```
INVARIANT_REGISTRY:
  - ID: INVARIANT-TOPO-01
    Claim: [e.g., "Every CONVERSATIONAL topic is reachable from at least one trigger phrase or redirect"]
  - ID: INVARIANT-TOPO-02
    Claim: [e.g., "Every FALLBACK topic is reachable from the system fallback chain"]
  - ID: INVARIANT-TOPO-03
    Claim: [e.g., "No dead-end topic exists — all terminal topics have explicit exit or escalation"]
  - ID: INVARIANT-SV-01
    Claim: [session variable lifecycle claim]
```

CONFIRMED_ABSENT defect rows MUST cite the invariant that structurally precludes the defect. No free-form scope assertions.

---

### PHASE 0-A — Auditor Assertion Contract

*You are the Auditor. Declare the complete schema before the Developer begins Phase 1. The Developer SHALL NOT begin Phase 1 until Phase 0-A is complete.*

**Reachability Completeness Envelope**

Pre-commit reachability assertions for every topic in Phase 0-D:

```
REACHABILITY_ENVELOPE:
  - TOPIC_ID: TOPIC-NN
    AUDITOR_REACHABILITY_ASSERTION: REACHABLE | UNREACHABLE | CONDITIONALLY_REACHABLE[condition]
    AUDITOR_ENTRY_PATH_CLAIM: [trigger phrase OR "redirect from TOPIC-MM" OR "system event"]
    ASSERTION_ID: REACH-NN
```

**Defect Recovery Schema**

Pre-declare the recovery verdict structure for each possible FOUND defect:

```
RECOVERY_SCHEMA:
  DEFECT_REF: [class + turn]
  RECOVERY_PATH: [minimum utterance sequence → healthy topic]
  RECOVERY_VERDICT: RECOVERABLE[turns=N, target=TOPIC-NN] | UNRECOVERABLE
  UNRECOVERABLE_CONSEQUENCE: [user experience if defect is never escaped]
```

The Developer SHALL produce one recovery record per FOUND defect in Phase 3-R. The Auditor will independently verify each recovery record in Phase 6.

**Trace Table Schema**

Mandatory 11 columns — blank cell = structural violation:

```
| TURN | USER_UTTERANCE | TRIGGER_PHRASE_MATCHED | TOPIC | NODES_EXECUTED | SESSION_STATE | AGENT_RESPONSE | SPEC_CONFORMANCE | PROHIBITED_TERM_SCAN | INVARIANT_CONFORMANCE | REACHABILITY_CONFORMANCE |
```

`REACHABILITY_CONFORMANCE: CONFIRMS[REACH-NN] | VIOLATES[REACH-NN: desc] | N/A`
`INVARIANT_CONFORMANCE: HOLDS | VIOLATED[ID: desc]`
`SPEC_CONFORMANCE: CONFORMS | DEVIATES[CS-SPEC-NN: desc]`
`PROHIBITED_TERM_SCAN: CLEAN | FOUND[term]`

**Other typed fields:**

```
DEFECT_CLASS: DEAD_END | INFINITE_LOOP | TRIGGER_PHRASE_COLLISION | MISSING_FALLBACK | UNREACHABLE_TOPIC
DEFECT_VERDICT: FOUND | CONFIRMED_ABSENT
FALLBACK_QUALITY: COMPLETE | LOOPS | TRUNCATED
ADVERSARIAL_OUTCOME: HANDLED | REDIRECT | FALLBACK_TRIGGERED | SESSION_CORRUPTED
GAP_CLOSURE_VERDICT: CLOSED | OPEN
```

No free-text in verdict positions.

---

### PHASE 1 — Developer: Dialog Trace

*You are the Developer. Walk conversation turn-by-turn. No skips. No summaries.*

Produce 11-column trace table. For every new topic entry: populate REACHABILITY_CONFORMANCE with CONFIRMS[REACH-NN] or VIOLATES[REACH-NN].

Walk: happy path, one redirect path, one adversarial injection.

*GAP_CLOSURE_VERDICT: CLOSED | OPEN [Gap-R1-01: turn-by-turn trace]*

---

### PHASE 2 — Developer: Defect Classification

*You are the Developer. Address all five defect classes.*

```
| DEFECT_CLASS | DEFECT_VERDICT | EVIDENCE | INVARIANT_CITE |
```

For FOUND rows: reproduction sequence required.
For CONFIRMED_ABSENT rows: cite INVARIANT-TOPO-NN or INVARIANT-SV-NN.
For UNREACHABLE_TOPIC CONFIRMED_ABSENT: cite REACH-NN (reachability envelope row) AND INVARIANT-TOPO-NN (structural invariant).

A CONFIRMED_ABSENT row for UNREACHABLE_TOPIC that cites only the reachability envelope but no structural invariant is a partial citation — flag as `CITATION_INCOMPLETE`.

*GAP_CLOSURE_VERDICT: CLOSED | OPEN [Gap-R1-02: all defect classes]*

---

### PHASE 2-R — Developer: Reachability Envelope Verdict

*You are the Developer. For every REACH-NN in the Auditor's Phase 0-A envelope.*

```
| ASSERTION_ID | TOPIC_ID | AUDITOR_CLAIM | TRACE_EVIDENCE | FINAL_VERDICT |
```

`TRACE_EVIDENCE: CONFIRMED | VIOLATED | NOT_EXERCISED`

For NOT_EXERCISED: state whether this is a deliberate coverage scope limitation or a coverage gap requiring additional trace turns.

*GAP_CLOSURE_VERDICT: CLOSED | OPEN [Gap-R7-03: reachability completeness envelope]*

---

### PHASE 3-R — Developer: Recovery Path Closure

*You are the Developer. For every FOUND defect row in Phase 2, produce a recovery record.*

```
| DEFECT_REF | RECOVERY_PATH | RECOVERY_VERDICT | UNRECOVERABLE_CONSEQUENCE |
```

Walk the minimum recovery sequence. Count turns. Name target topic. State RECOVERABLE or UNRECOVERABLE. If no FOUND defects: produce one row stating `RECOVERY_REQUIRED: NONE` with citations to all CONFIRMED_ABSENT invariants.

*GAP_CLOSURE_VERDICT: CLOSED | OPEN [Gap-R7-01: recovery path completeness]*

---

### PHASE 4 — Developer: Fallback Chain Trace

*You are the Developer.*

Trace fallback path from unrecognized input to terminal. `FALLBACK_QUALITY`. Adversarial injection with `ADVERSARIAL_OUTCOME`.

*GAP_CLOSURE_VERDICT: CLOSED | OPEN [Gap-R2-04: fallback chain]*

---

### PHASE 5 — Developer: Coverage Summary

```
| METRIC | VISITED | TOTAL | RATIO |
| Topics | N | M | N/M |
| Trigger phrases | N | M | N/M |
| Invariants verified | N | M | N/M |
| Reachability assertions confirmed | N | M | N/M |
| Recovery paths verified RECOVERABLE | N | M | N/M |
```

*GAP_CLOSURE_VERDICT: CLOSED | OPEN [Gap-R3-05: quantified coverage]*

---

### PHASE 5-V — Developer: Vocabulary Compliance Scan

```
| PROHIBITED_TERM | FOUND_IN_OUTPUT | LOCATION |
```

*GAP_CLOSURE_VERDICT: CLOSED | OPEN [Gap-R4-10: vocabulary enforcement]*

---

```
=== DEVELOPER ARTIFACT COMPLETE (Phases 0-D through 5-V) ===
=== AUDITOR NOW READS THE COMPLETED ARTIFACT AS A FINISHED DOCUMENT ===
```

---

### PHASE 6 — Auditor: Independent Audit

*You are the Auditor. Read the completed artifact.*

**6-A: Trace Table Audit**

```
| TURN | REACHABILITY_CONFORMANCE_VALID | INVARIANT_CONFORMANCE_VALID | SPEC_CONFORMANCE_VALID | DISCREPANCY |
```

**6-B: Reachability Envelope Cross-Audit**

```
| ASSERTION_ID | AUDITOR_ORIGINAL_CLAIM | DEVELOPER_PHASE2R_VERDICT | AUDITOR_INDEPENDENT_VERDICT | DISCREPANCY |
```

**6-C: Recovery Path Cross-Audit**

```
| DEFECT_REF | DEVELOPER_RECOVERY_VERDICT | AUDITOR_RECOVERY_VERDICT | PATH_VALID | DISCREPANCY |
```

Developer claims RECOVERABLE but path does not reach a healthy topic → `DISCREPANCY: FOUND[RECOVERY_PATH: path incomplete]`.
Developer claims UNRECOVERABLE but Auditor can identify a recovery sequence → `DISCREPANCY: FOUND[RECOVERY_PATH: path exists at min N turns]`.

**6-D: Structural Completeness Cross-Audit**

This is the combined reachability + recovery completeness check:

```
| TOPIC_ID | REACHABILITY_VERDICT | HAS_RECOVERY_PATH_IF_DEFECT | STRUCTURAL_COMPLETENESS |
```

`STRUCTURAL_COMPLETENESS: COMPLETE | ENTRY_GAP[REACH-NN] | EXIT_GAP[defect ref] | BOTH_GAPS`

A topic with `ENTRY_GAP` is not reachable. A topic with `EXIT_GAP` cannot be escaped if a defect occurs. A topic with `BOTH_GAPS` is both unreachable and unescapable — a structural island.

**6-E: Invariant Cross-Audit**

```
| INVARIANT_ID | DEVELOPER_VERDICT | AUDITOR_VERDICT | DISCREPANCY |
```

**6-F: Gap-Closure Audit**

```
| PHASE | GAP_TAG | DEVELOPER_CLOSURE | AUDITOR_VERIFICATION | REGRESSION |
```

*GAP_CLOSURE_VERDICT: CLOSED | OPEN [Gap-R6-02: cross-auditor verification]*

---

## V-05

**Axis:** Combined — State persistence classification (V-02) + defect severity triage + phrasing register (conversational imperative rather than SHALL/MUST formalism)
**Hypothesis:** Two new properties may surface together. First, severity triage — assigning P0/P1/P2/P3 impact tier to each FOUND defect beyond the binary FOUND/CONFIRMED_ABSENT — is not required by any current criterion. Second, if the lighter phrasing register produces weaker structural enforcement in some dimensions, the scorecard may reveal which criteria are register-sensitive (i.e., they require SHALL/MUST formalism to hold). The state persistence classification axis (V-02) is preserved to maintain the persistence contract signal.

---

You are a Copilot Studio domain expert simulating a multi-turn conversation flow. Work in two phases: first as the **Developer** who traces the conversation and classifies defects, then as the **Auditor** who reviews the completed trace. A boundary marker separates the two phases. Do not mix roles.

Use Copilot Studio vocabulary throughout — topics, trigger phrases, conditions, fallback topics, escalation, session variables, redirects. Do not use: intent, dialog, slot, NLU, chatbot, handoff, context variable.

---

### Developer Pre-Work

Before starting the trace, declare the following. The Auditor reads this declaration to write the review schema.

**Topic Map**

List every topic:

```
- TOPIC-NN: [name] | Type: CONVERSATIONAL / SYSTEM / FALLBACK | Trigger phrases: [list] | Exits to: [list]
```

**CS Vocabulary Binding**

Map domain terms to CS terms here. Include the prohibited list:

```
Prohibited: intent, dialog, slot, NLU, chatbot, handoff, utterance class
```

**State Persistence Registry**

For every session variable, declare its persistence class:

```
- [variable name]: EPHEMERAL (cleared on topic exit) / PERSISTENT (held until explicit clear) / SESSION-SCOPED (held until session ends)
  Set by: TOPIC-NN | Cleared by: [topic or event] | Read by: [topics]
```

**Structural Invariants**

Name the design-time guarantees you want the simulation to verify:

```
- INVARIANT-TOPO-NN: [claim about the topic graph structure]
- INVARIANT-SV-NN: [claim about session variable lifecycle]
```

---

### Auditor Pre-Work

Write the review schema before the Developer starts the trace. The Developer follows this schema exactly.

**Trace Table**

The trace table has these required columns. Leave any column blank and the row fails:

```
Turn | User Utterance | Trigger Phrase Matched | Topic | Nodes Executed | Session State | Agent Response | Spec Conformance | Prohibited Term Scan | Invariant Conformance | Persistence Mismatch
```

- **Session State**: show variable name, current value, persistence class, and status (SET / HELD / CLEARED) for every variable. On topic exit, all EPHEMERAL variables must show CLEARED.
- **Spec Conformance**: `CONFORMS` or `DEVIATES[spec ref: why]`
- **Prohibited Term Scan**: `CLEAN` or `FOUND[term]`
- **Invariant Conformance**: `HOLDS` or `VIOLATED[invariant ID: why]`
- **Persistence Mismatch**: `NONE` or `FOUND[variable: expected vs observed]` — a FOUND here is automatically a defect

**Defect Table**

```
Defect Class | Verdict | Evidence | Invariant Cite | Severity Tier
```

Defect classes: DEAD_END, INFINITE_LOOP, TRIGGER_PHRASE_COLLISION, MISSING_FALLBACK, PERSISTENCE_CONTRACT_VIOLATION

Verdict options: `FOUND` (with reproduction) or `CONFIRMED_ABSENT` (with invariant cite — no invariant cite = contract violation)

Severity tiers for FOUND defects:
- `P0-BLOCKER`: session cannot continue without agent restart or human escalation
- `P1-CRITICAL`: user cannot complete their primary task without workaround
- `P2-MODERATE`: degraded experience, primary task is completable with friction
- `P3-LOW`: cosmetic or edge-case issue, no impact on primary flow

For CONFIRMED_ABSENT rows: no severity tier required.

**Other verdict options:**

```
Fallback quality: COMPLETE / LOOPS / TRUNCATED
Adversarial outcome: HANDLED / REDIRECT / FALLBACK_TRIGGERED / SESSION_CORRUPTED
Gap closure: CLOSED / OPEN
```

No free-text in verdict cells.

---

### Developer — Turn-by-Turn Trace

Walk the full conversation, one row per turn. Do not skip turns or roll them up into summaries. Populate every column.

Start with the happy path. Then trace at least one redirect scenario. Then inject one adversarial turn mid-flow.

For every topic exit turn: all EPHEMERAL variables must show CLEARED in Session State. If one shows HELD instead, mark Persistence Mismatch as FOUND and note the variable.

*Gap closure: CLOSED — this phase closes Gap-R1-01 (turn-by-turn trace required)*

---

### Developer — Defect Classification

Address all five defect classes. No class may be omitted.

Fill the defect table with one row per class. For FOUND: write the exact utterance sequence that triggers it and the failure mode. For CONFIRMED_ABSENT: cite the invariant that structurally precludes it. Assign a severity tier for every FOUND row.

Think through: does any topic-exit turn show an EPHEMERAL variable held instead of cleared? If so, that is a PERSISTENCE_CONTRACT_VIOLATION — FOUND.

*Gap closure: CLOSED — this phase closes Gap-R1-02 (all defect classes addressed)*

---

### Developer — Fallback Chain

Trace the fallback path for an unrecognized input from the first no-match node all the way to a terminal state (graceful exit or escalation). Show session variable state at each node. Report fallback quality.

Inject one adversarial turn during the fallback chain. Show adversarial outcome.

*Gap closure: CLOSED — closes Gap-R2-04 (fallback to terminal traced)*

---

### Developer — Coverage Summary

Report:

```
Topics visited / total: N/M
Trigger phrases exercised / total: N/M
Invariants verified / total: N/M
Session variables with contract honored / total: N/M
```

For session variable contract: check that each variable was cleared per its PERSISTENCE_CLASS declaration at the expected event. Report `CONTRACT_HONORED: YES / NO[turn ref]` per variable.

*Gap closure: CLOSED — closes Gap-R3-05 (coverage metric) and Gap-R7-02 (persistence contract summary)*

---

### Developer — Vocabulary Scan

Scan your output for prohibited terms. Report:

```
[term]: FOUND at [location] / NOT FOUND
```

One row per prohibited term.

*Gap closure: CLOSED — closes Gap-R4-10 (active vocabulary enforcement)*

---

```
=== DEVELOPER ARTIFACT COMPLETE (Pre-Work through Vocabulary Scan) ===
=== AUDITOR NOW READS THE COMPLETED ARTIFACT AS A FINISHED DOCUMENT ===
```

---

### Auditor — Trace Review

You are now reading the completed Developer artifact as a finished document. Go through it systematically.

**Trace Table Review**

For each turn row, check: are all columns populated? Are enum values valid? Does Session State correctly show CLEARED for EPHEMERAL variables on topic exit? Report:

```
Turn | Persistence Mismatch Valid | Spec Conformance Valid | Invariant Conformance Valid | Issue
```

**Defect Table Review**

For each defect row: is the verdict valid? For CONFIRMED_ABSENT: is the invariant cited and does it actually preclude the defect class? For FOUND: is the severity tier correctly assigned?

```
Defect Class | Verdict Valid | Invariant Cite Valid | Severity Tier Valid | Issue
```

Flag any FOUND defect where the assigned severity tier seems miscalibrated — e.g., a dead end that strands the user forever classified as P3-LOW is likely a mismatch.

**Severity Tier Cross-Audit**

This is the primary new audit layer in this variation:

```
Defect Class | Developer Severity Tier | Auditor Independent Severity Tier | Calibration | Discrepancy
```

`Calibration: AGREES / DISAGREES[reason]`

If Developer assigned P3-LOW but Auditor reads the reproduction steps and concludes the user cannot continue → `DISAGREES[severity underestimated: user blocked]`.

If Developer assigned P0-BLOCKER but Auditor identifies a recovery path via topic redirect → `DISAGREES[severity overestimated: recovery path exists via TOPIC-NN]`.

**Persistence Contract Cross-Audit**

For each variable in the Developer's State Persistence Registry:

```
Variable | Persistence Class | Developer Contract Honored | Auditor Verdict | Discrepancy
```

**Invariant Cross-Audit**

```
Invariant ID | Developer Verdict | Auditor Verdict | Discrepancy
```

**Gap-Closure Audit**

```
Phase | Gap Tag | Developer Closure | Auditor Verification | Regression
```

Regression = YES if a gap that was closed in a previous scoring round is re-opened by this trace.

---
