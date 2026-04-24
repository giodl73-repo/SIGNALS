1,257 lines, all 5 variations complete with correct structure. Here is the summary:

---

## Round 6 — flow-conversation Variations

**5 variations written** to `simulations/quest/variations/flow-conversation-variations-R6-2026-03-14.md`.

---

### Variation Summary

| V | Axis | Key innovation | Predicted |
|---|------|----------------|-----------|
| **V-01** | Phrasing Register (boundary marker isolation) | SHALL/MUST sequencing ONLY — no `=== DEVELOPER ARTIFACT COMPLETE ===` hard separator. C-16 + C-17 fully present. | C-12: **unknown** |
| **V-02** | Lifecycle Emphasis (gap-closure as primary structure) | Prompt organized around CS Test Bot gaps (Gap-CS-01 through Gap-CS-07), not phases. C-17 is the structural backbone, not an annotation. | **100** |
| **V-03** | Role Sequence (topology invariants as C-16 layer) | Developer Phase 0-D pre-commits INVARIANT-TOPO-NN claims (design-time structural, distinct from CS-SPEC runtime). CONFIRMED_ABSENT defect verdicts must cite the invariant that precludes the defect — making them falsifiable, not just asserted. Auditor adds 4th mandatory column: INVARIANT_CONFORMANCE. | **100** |
| **V-04** | Role Seq + Lifecycle + Output Format (full synthesis) | Maximum density: bidirectional pre-contracts + topology invariants + per-phase gap-closure + hard boundary + 4-column table + SHALL/MUST. Reference implementation. | **100** |
| **V-05** | Lifecycle (minimal) + Phrasing (SHALL-only, no hard marker) | R5 V-02 minimal 3-phase extended with C-16 (sub-section 1-A) and C-17 (per-sub-section gap-closure). No hard boundary marker. Cross-checks V-01: if C-12 fails here but passes in V-01, minimal structure + normative boundary is insufficient. | C-12: **unknown** |

---

### Two diagnostic bets

**V-01 vs V-05 (C-12 isolation):** Both strip the hard `=== DEVELOPER ARTIFACT COMPLETE ===` marker. V-01 uses the full phase structure; V-05 uses minimal. Three possible outcomes:
- Both pass → hard marker is never load-bearing; normative gating alone is sufficient
- Both fail → hard marker is always load-bearing regardless of structure
- V-01 passes, V-05 fails → hard marker matters only in minimal structure
- V-05 passes, V-01 fails → structurally impossible (minimal is a subset)

### New patterns introduced

- **Topology invariants as falsifiable C-16 pre-commitment** (V-03, V-04): INVARIANT-TOPO-NN claims make `CONFIRMED_ABSENT` defect rows testable against a pre-committed structural claim, not just a scope assertion
- **Gap-closure as structural backbone** (V-02): organizing around CS Test Bot gaps (not numbered phases) makes C-17 load-bearing throughout, preventing decorative compliance
- **Invariant testability map** (V-03, V-04): Phase 1 explicitly declares which INVARIANT-TOPO-NN are verifiable within the simulation's coverage scope before trace begins
ion/{topic}-conversation-{date}.md if it exists.
Read: any signal artifacts in simulations/ relevant to "{topic}".

BOUNDARY MARKER TEST: Four roles execute in strict normative sequence. Each role
transition is enforced by a SHALL NOT rule ONLY. No hard boundary separators appear
in this prompt. This tests whether normative sequencing instructions are sufficient
for C-12 role isolation.

  (1) Copilot Studio Developer  -- Phase 0-D: domain pre-contract
  (2) Compliance Auditor        -- Phase 0-A: assertion contract
                                   [SHALL NOT begin until Phase 0-D complete]
  (3) Copilot Studio Developer  -- Phases 1-5: trace and analysis
                                   [SHALL NOT begin until Phase 0-A complete]
  (4) Compliance Auditor        -- Phase 6: post-production audit
                                   [SHALL NOT begin until Developer declares phases complete]

CS vocabulary mandatory in all Developer output:
  Topics, Trigger phrases, Conditions, Fallback topics, Escalation nodes,
  Session variables, Topic redirects, Actions, Generative answers,
  Knowledge sources, End of conversation nodes.
Prohibited in all Developer output:
  intent | dialog | slot | NLU | utterance | chatbot | handoff | context | bot

---

## PHASE 0-D: DEVELOPER DOMAIN PRE-CONTRACT
[Copilot Studio Developer speaks first.]
[Gap-R6-01 closure: C-16 is now a formal criterion. Developer declares domain inventory
and CS vocabulary binding before the Auditor writes any schema. This declaration is
binding: the Auditor writes Phase 0-A against it. Domain declarations are not trace
output; Auditor independence is preserved.]

Agent name: [Name or description]
Topics in graph: [N total]: [Topic-A], [Topic-B], [Topic-C (Fallback)], ...
Trigger phrases (2-3 per topic):
  [Topic-A]: "[phrase-1]", "[phrase-2]"
  [Topic-B]: "[phrase-1]", "[phrase-2]"
Fallback topic: [Name / System Fallback Topic / not configured]
Escalation path: [Topic / not configured]
Session variables:
  [VarName]: scope=[topic-scoped | global], type=[Text|Number|Boolean], initial=[value | unset]
Coverage scope: [N] of [Total] topics ([pct]%).

CS Vocabulary Binding:
  dialog unit  -> "topic"
  routing      -> "trigger phrase", "condition", "topic transition"
  state        -> "session variable"
  no-match     -> "fallback topic", "escalation"
  session end  -> "end of conversation node"

Topology Spec (Developer pre-commits before trace):
  CS-SPEC-01: Trigger phrase matching activates topic above confidence threshold.
  CS-SPEC-02: Topic-scoped session variables cleared at topic boundary.
  CS-SPEC-03: Condition nodes require a default branch.
  CS-SPEC-04: Redirect nodes do not carry topic-scoped variables.
  CS-SPEC-05: End of conversation nodes terminate the session.
  CS-SPEC-06: Escalation nodes open human agent session.
  CS-SPEC-07: Fallback topic activates when no trigger phrase exceeds threshold.

Session Variable Invariants (pre-committed before trace):
  INVARIANT-SV-01: [VarName] persists within [Topic] and clears at topic exit.
  INVARIANT-SV-02: [VarName] is global-scoped and survives all topic transitions.

Developer SHALL NOT alter this contract in later phases.
The Auditor SHALL NOT begin Phase 0-A until this block is complete.
GAP_CLOSURE_VERDICT: CLOSED | OPEN [Gap-R6-01: Developer domain pre-contract declared
before any trace output exists. Auditor independence preserved.]

---

## PHASE 0-A: AUDITOR ASSERTION CONTRACT
[Compliance Auditor speaks. The Auditor SHALL NOT begin until Phase 0-D is complete.]
[Gap-R4-01 closure: Auditor declares schema before Developer trace begins. Written
against Developer Phase 0-D declaration.]

Per-turn Trace Table columns (mandatory on every row; blank cell = structural violation):
  SPEC_CONFORMANCE: CONFORMS | DEVIATES[CS-SPEC-NN: description]
  INVARIANT_STATUS: HOLDS | VIOLATED[INVARIANT-NN: description]
  PROHIBITED_TERM_SCAN: CLEAN | FOUND[term at exact location]

Defect matrix (all four rows mandatory):
  DEFECT_VERDICT: FOUND | CONFIRMED_ABSENT
  -- CONFIRMED_ABSENT: scope statement required.
  -- FOUND: exact reproduction sequence required (inputs -> failure mode).
  -- Free-text in DEFECT_VERDICT is a contract violation.

Terminal verdicts:
  FALLBACK_QUALITY: COMPLETE | LOOPS | TRUNCATED
  ADVERSARIAL_OUTCOME: GRACEFUL | BRITTLE | SILENT_FAILURE

Coverage fields:
  GRAPH_COVERAGE: [visited] / [total] = [ratio]
  TRIGGER_COVERAGE: [exercised] / [total] = [ratio]

Gap-Closure Contract:
  Each Developer phase SHALL carry GAP_CLOSURE_VERDICT: CLOSED | OPEN with gap tag.
  A phase without GAP_CLOSURE_VERDICT is a contract violation.

Auditor-only fields (Phase 6 only):
  AUDITOR_SPEC_CONFORMANCE: CONFORMS | DEVIATES[CS-SPEC-NN: description]
  AUDITOR_INVARIANT_STATUS: HOLDS | VIOLATED[INVARIANT-NN: description]
  AUDITOR_PROHIBITED_TERM_SCAN: CLEAN | FOUND[term at exact location]
  DISCREPANCY: NONE | FOUND[SPEC_CONFORMANCE] | FOUND[INVARIANT_STATUS] |
               FOUND[PROHIBITED_TERM] | FOUND[MULTIPLE: list]

Prohibited terms scanned in Phase 6 (full Developer artifact):
  intent | dialog | slot | NLU | utterance | chatbot | handoff | context | bot

Developer SHALL NOT begin Phase 1 until this contract is complete.
GAP_CLOSURE_VERDICT: CLOSED | OPEN [Gap-R4-01: Auditor contract precedes Developer trace]

---

## PHASE 1: AGENT TOPOLOGY CONFIRMATION
[Copilot Studio Developer. SHALL NOT begin until Phase 0-A complete. Gap-R5-01 closure.]

Coverage: [N] of [Total] topics ([pct]%).
Visited: [Topic-A], [Topic-B], ...
Not visited: [Topic-X], ... / [none -- full coverage]

GAP_CLOSURE_VERDICT: CLOSED | OPEN [Gap-R5-01: coverage scope confirmed]

---

## PHASE 2: CONVERSATION TRACE TABLE
[Copilot Studio Developer. Gap-R4-01 closure: per-turn assertion fields.]

Walk every turn. All three assertion columns mandatory. Blank cell = violation.

| Turn | User Input | Trigger Phrase Matched | Topic | Nodes Executed | Session Variables (name=value; scope; changed/held/cleared) | Agent Response | SPEC_CONFORMANCE | INVARIANT_STATUS | PROHIBITED_TERM_SCAN |
|------|-----------|----------------------|-------|----------------|-------------------------------------------------------------|---------------|-----------------|-----------------|---------------------|
| T-01 | "[input]" | "[phrase]" (HIGH/MED/LOW) | [Topic-A] | Trigger>Message>Question | var1=X (topic-scoped, changed) | "[response]" | CONFORMS \| DEVIATES[CS-SPEC-NN: desc] | HOLDS \| VIOLATED[INVARIANT-NN: desc] | CLEAN \| FOUND[term] |
| T-02 | "[input]" | "[phrase]" (HIGH/MED/LOW) | [Topic-B] | Trigger>Condition(default)>Redirect | var1=cleared (topic exited); var2=Y (global, held) | "[response]" | CONFORMS \| DEVIATES[CS-SPEC-NN: desc] | HOLDS \| VIOLATED[INVARIANT-NN: desc] | CLEAN \| FOUND[term] |
[...continue for all turns. No turns skipped. All three columns populated on every row.]

GAP_CLOSURE_VERDICT: CLOSED | OPEN [Gap-R4-01: per-turn SPEC_CONFORMANCE + INVARIANT_STATUS
+ PROHIBITED_TERM_SCAN on every row; session state tracked at every transition]

---

## PHASE 3: DEFECT MATRIX
[Copilot Studio Developer. Gap-R4-02 closure: all four classes with DEFECT_VERDICT enum.]

| Defect Class | DEFECT_VERDICT | Evidence | Reproduction Sequence |
|-------------|---------------|----------|----------------------|
| Dead end | FOUND \| CONFIRMED_ABSENT | [FOUND: T-NN, topic, dead node path. CONFIRMED_ABSENT: "All [N] exits verified: [list]."] | [FOUND: "[input-1]"->"[input-2]"->dead state. CONFIRMED_ABSENT: N/A] |
| Infinite loop | FOUND \| CONFIRMED_ABSENT | [FOUND: loop path, missing condition. CONFIRMED_ABSENT: "Redirect graph acyclic. Map: [list]."] | [FOUND: cycle. CONFIRMED_ABSENT: N/A] |
| Trigger phrase collision | FOUND \| CONFIRMED_ABSENT | [FOUND: phrase, competing topics, scores, disambiguation strategy + rationale. CONFIRMED_ABSENT: "All [N] phrases unique; runner-up below 0.4."] | [FOUND: "[phrase]"->Topic-A+Topic-B. CONFIRMED_ABSENT: N/A] |
| Missing fallback | FOUND \| CONFIRMED_ABSENT | [FOUND: topic, condition, missing default, CS-SPEC-03 violated. CONFIRMED_ABSENT: "All condition nodes carry default. Confirmed: [list]."] | [FOUND: "[input]"->no default. CONFIRMED_ABSENT: N/A] |

GAP_CLOSURE_VERDICT: CLOSED | OPEN [Gap-R4-02: all four classes, DEFECT_VERDICT enum,
disambiguation strategy where COLLISION FOUND]

---

## PHASE 4: FALLBACK CHAIN + ADVERSARIAL INJECTION
[Copilot Studio Developer. Gap-R4-03: fallback to terminal. Gap-R4-04: adversarial.]

Fallback chain:
  Unrecognized input: "[phrase matching no trigger phrase]"
  Step 1: [N] topics evaluated, 0 match -> CS-SPEC-07 activates -> [Fallback topic]
  Step 2: [node type] -- [action]
  ...
  Terminal: [escalation node opened | end of conversation node | loop detected]
  FALLBACK_QUALITY: COMPLETE | LOOPS | TRUNCATED

Adversarial injection:
  Scenario: [mid-flow topic switch | unexpected input | session timeout]
  Description: "[what the user does to destabilize the flow]"
  Injected at T-[NN], state: [snapshot]
  Node path: [trace from injection through agent response]
  Session variable impact: [what changes, is corrupted, or is lost]
  ADVERSARIAL_OUTCOME: GRACEFUL | BRITTLE | SILENT_FAILURE

GAP_CLOSURE_VERDICT: CLOSED | OPEN [Gap-R4-03: fallback traced to terminal;
Gap-R4-04: adversarial turn included with ADVERSARIAL_OUTCOME enum]

---

## PHASE 5: COVERAGE + AMENDMENTS
[Copilot Studio Developer. Gap-R4-05 closure: quantified ratios.]

Coverage:
| Metric | Visited | Total | Ratio |
|--------|---------|-------|-------|
| Topics | [N] | [Total] | [N/Total] ([pct]%) |
| Trigger phrases exercised | [N] | [Total] | [N/Total] ([pct]%) |

Invariant status summary:
| Invariant | Status | Turns where VIOLATED |
|-----------|--------|----------------------|
| INVARIANT-SV-01 | HOLDS \| VIOLATED | [T-NN list / N/A] |
| INVARIANT-SV-02 | HOLDS \| VIOLATED | [T-NN list / N/A] |

Amendments (all FOUND defects, all DEVIATES and VIOLATED rows):
- CS-SPEC-NN / INVARIANT-NN: [description]. Trigger: "[input]"->[failure]. Fix: [change]. P1|P2|P3.

Developer declaration: Phases 0-D through 5 are complete.
The Auditor SHALL NOT have begun Phase 6 before this declaration appears.
GAP_CLOSURE_VERDICT: CLOSED | OPEN [Gap-R4-05: coverage ratios present as fractions]

---

## PHASE 6: AUDITOR POST-PRODUCTION AUDIT
[Compliance Auditor. The Auditor SHALL NOT have begun this phase before the Developer
completion declaration in Phase 5. Read Phases 0-D through 5 as a finished artifact.
Developer role has ended. Apply Phase 0-A assertion contract.]
[Gap-R6-02 closure: C-17 -- per-phase gap-closure annotations verified.]

Per-turn re-annotation (full Developer Phase 2 trace table re-audited independently):
| Turn | Dev SPEC_CONFORMANCE | Aud SPEC_CONFORMANCE | Dev INVARIANT_STATUS | Aud INVARIANT_STATUS | Dev PROHIBITED_TERM_SCAN | Aud PROHIBITED_TERM_SCAN | DISCREPANCY |
|------|---------------------|---------------------|---------------------|---------------------|--------------------------|--------------------------|-------------|
| T-01 | [Phase 2] | CONFORMS \| DEVIATES[CS-SPEC-NN: desc] | [Phase 2] | HOLDS \| VIOLATED[INVARIANT-NN: desc] | [Phase 2] | CLEAN \| FOUND[term] | NONE \| FOUND[...] |
[...one row per turn from Phase 2]

Prohibited term body scan (Phases 0-D through 5, full text):
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
PROHIBITED_TERM_BODY_SCAN: CLEAN | FOUND[list terms and locations]

Gap-closure audit (C-17 verification):
| Phase | Gap Tag | Developer GAP_CLOSURE_VERDICT | Auditor Verification |
|-------|---------|-------------------------------|----------------------|
| 0-D | Gap-R6-01 | CLOSED \| OPEN | CLOSED \| OPEN \| REGRESSION |
| 0-A | Gap-R4-01 | CLOSED \| OPEN | CLOSED \| OPEN \| REGRESSION |
| 1 | Gap-R5-01 | CLOSED \| OPEN | CLOSED \| OPEN \| REGRESSION |
| 2 | Gap-R4-01 | CLOSED \| OPEN | CLOSED \| OPEN \| REGRESSION |
| 3 | Gap-R4-02 | CLOSED \| OPEN | CLOSED \| OPEN \| REGRESSION |
| 4 | Gap-R4-03,04 | CLOSED \| OPEN | CLOSED \| OPEN \| REGRESSION |
| 5 | Gap-R4-05 | CLOSED \| OPEN | CLOSED \| OPEN \| REGRESSION |

Auditor summary:
  Contracts: Phase 0-D (domain pre-contract) + Phase 0-A (assertion schema)
  Turns audited: [N]. DISCREPANCY: [N] -- SPEC: [N]; INV: [N]; PROHIBITED: [N].
  GAP_CLOSURE_REGRESSIONS: [N] | NONE
  AUDIT_VERDICT: CLEAN | ISSUES_FOUND
```

---

## V-02: Lifecycle Emphasis -- Gap-Closure as Primary Structure

**Axis:** Lifecycle Emphasis -- the entire prompt organized around GAPS, not phases. Each
section IS a named gap-closure exercise. C-17 is the structural backbone, not an annotation.

**Hypothesis:** R5 V-04 added gap-closure annotations TO a phase-based structure. V-02 inverts
this: the gap IS the organizing unit. When the structure itself is the gap registry, satisfying
C-17 superficially becomes harder -- you cannot paste GAP_CLOSURE_VERDICT onto a section
that does not actually close anything. The gaps map to specific holes in Copilot Studio
Test Bot (CS Test Bot) coverage. The Developer closes each gap; the Auditor verifies each
closure. C-16 is Gap-CS-06; C-17 is the organizing principle of the entire trace.

**Predicted score:** 100.

```
You are running /flow:conversation for topic "{topic}".

Read: simulations/flow/conversation/{topic}-conversation-{date}.md if it exists.
Read: any signal artifacts in simulations/ relevant to "{topic}".

This trace is a gap-closure registry. Each section closes one specific testing gap that
Copilot Studio Test Bot (CS Test Bot) leaves open. The closing role and required output
for each gap are defined below.

Testing gaps in scope:
  Gap-CS-06: CS Test Bot does not verify developer domain claims before trace runs.   [C-16]
  Gap-CS-01: CS Test Bot does not track session variable scope transitions turn-by-turn.
  Gap-CS-02: CS Test Bot does not identify trigger phrase collisions across topics.
  Gap-CS-03: CS Test Bot does not verify fallback chain reaches a terminal state.
  Gap-CS-04: CS Test Bot does not inject adversarial turns mid-flow.
  Gap-CS-05: CS Test Bot does not report graph coverage ratios.
  Gap-CS-07: CS Test Bot does not produce a role-separated audit of the trace artifact.

Closing sequence:
  (A) Auditor declares assertion contract -- Gap-CS-07 pre-work.
      [Auditor SHALL NOT begin until invoked; Developer SHALL NOT begin until (A) complete.]
  (B) Developer closes Gap-CS-06 through Gap-CS-05 in order.
      [Each gap section must complete before the next begins.]
  (C) Developer declares artifact complete.
      [Auditor SHALL NOT begin (D) until this declaration appears.]
  (D) Auditor closes Gap-CS-07 by auditing the completed Developer artifact.

CS vocabulary mandatory in all Developer output:
  Topics, Trigger phrases, Conditions, Fallback topics, Escalation nodes,
  Session variables, Topic redirects, Actions, Generative answers,
  Knowledge sources, End of conversation nodes.
Prohibited: intent | dialog | slot | NLU | utterance | chatbot | handoff | context | bot

---

## GAP-CS-07 PRE-WORK: AUDITOR ASSERTION CONTRACT
[Compliance Auditor. Declare the complete assertion contract before Developer output begins.
The Developer must use these exact fields and enum values in all gap-closure sections.]

Topology Spec:
  CS-SPEC-01: Trigger phrase matching activates topic above confidence threshold.
  CS-SPEC-02: Topic-scoped session variables cleared at topic boundary.
  CS-SPEC-03: Condition nodes require a default branch.
  CS-SPEC-04: Redirect nodes do not carry topic-scoped variables.
  CS-SPEC-05: End of conversation nodes terminate the session.
  CS-SPEC-06: Escalation nodes open human agent session.
  CS-SPEC-07: Fallback topic activates when no trigger phrase exceeds threshold.

Prohibited terms (Developer output): intent | dialog | slot | NLU | utterance |
  chatbot | handoff | context | bot

Per-turn Trace Table (Gap-CS-01 closure artifact -- mandatory columns, blank = violation):
  SPEC_CONFORMANCE: CONFORMS | DEVIATES[CS-SPEC-NN: description]
  SESSION_STATE: [name=value (scope, changed/held/cleared) per variable]
  PROHIBITED_TERM_SCAN: CLEAN | FOUND[term at exact location]

Defect matrix (Gap-CS-02, Gap-CS-03 closure artifacts):
  DEFECT_VERDICT: FOUND | CONFIRMED_ABSENT
  [CONFIRMED_ABSENT: scope required. FOUND: reproduction required. Free-text = violation.]
  FALLBACK_QUALITY: COMPLETE | LOOPS | TRUNCATED

Adversarial verdict (Gap-CS-04): ADVERSARIAL_OUTCOME: GRACEFUL | BRITTLE | SILENT_FAILURE
Coverage fields (Gap-CS-05): GRAPH_COVERAGE: [N]/[total]. TRIGGER_COVERAGE: [N]/[total].

Auditor-only (Gap-CS-07):
  AUDITOR_SPEC_CONFORMANCE: CONFORMS | DEVIATES[CS-SPEC-NN: description]
  AUDITOR_PROHIBITED_TERM_SCAN: CLEAN | FOUND[term at exact location]
  DISCREPANCY: NONE | FOUND[SPEC_CONFORMANCE] | FOUND[PROHIBITED_TERM] | FOUND[BOTH]

GAP_CLOSURE_VERDICT: CLOSED | OPEN [Gap-CS-07 pre-work: assertion schema declared;
all enum values stated; prohibited terms registered before any Developer output]

---

## GAP-CS-06 CLOSURE: DEVELOPER DOMAIN PRE-CONTRACT
[Copilot Studio Developer. Closes Gap-CS-06: CS Test Bot does not verify developer domain
claims before trace runs. This is the C-16 closure: domain inventory and CS vocabulary
binding declared before any trace output. Domain declarations are not trace output.]

Agent name: [Name or description]
Topics in graph: [N total]:
  [Topic-A]: trigger phrases: "[phrase-1]", "[phrase-2]"; terminal: [Resolved|Escalated|Abandoned]
  [Topic-B]: trigger phrases: "[phrase-1]", "[phrase-2]"; terminal: [Resolved|Escalated|Abandoned]
  [Topic-C (Fallback)]: activates on: no trigger phrase match; terminal: [Escalated|Abandoned]
Session variables:
  [VarName]: scope=[topic-scoped | global], type=[Text|Number|Boolean], initial=[value | unset]
Coverage scope: [N] of [Total] topics ([pct]%).

CS vocabulary binding:
  dialog unit -> "topic" | routing -> "trigger phrase", "condition" |
  state -> "session variable" | no-match -> "fallback topic", "escalation"

GAP_CLOSURE_VERDICT: CLOSED | OPEN
[Gap-CS-06 CLOSED when: agent topology declared, vocabulary bound, coverage scope stated,
no trace output produced yet. Developer domain claims are now auditable.]

---

## GAP-CS-01 CLOSURE: SESSION STATE TRACE TABLE
[Copilot Studio Developer. Closes Gap-CS-01: CS Test Bot does not track session variable
scope transitions turn-by-turn.]

Walk every turn. One row per turn. All three mandatory columns required. Blank = violation.

| Turn | User Input | Trigger Phrase Matched | Topic | Nodes Executed | SESSION_STATE (name=value; scope; changed/held/cleared) | Agent Response | SPEC_CONFORMANCE | PROHIBITED_TERM_SCAN |
|------|-----------|----------------------|-------|----------------|--------------------------------------------------------|---------------|-----------------|---------------------|
| T-01 | "[input]" | "[phrase]" (HIGH/MED/LOW) | [Topic] | Trigger>Message>Question | var1=X (topic-scoped, changed) | "[response]" | CONFORMS \| DEVIATES[CS-SPEC-NN] | CLEAN \| FOUND[term] |
| T-02 | "[input]" | "[phrase]" (HIGH/MED/LOW) | [Topic] | Trigger>Condition(default)>Redirect | var1=cleared (topic exited) | "[response]" | CONFORMS \| DEVIATES[CS-SPEC-NN] | CLEAN \| FOUND[term] |
[...all turns. No turns skipped. All three columns populated.]

GAP_CLOSURE_VERDICT: CLOSED | OPEN
[Gap-CS-01 CLOSED when: all turns present; SESSION_STATE shows scope transitions per
variable; SPEC_CONFORMANCE and PROHIBITED_TERM_SCAN on every row.]

---

## GAP-CS-02 CLOSURE: DEFECT MATRIX
[Copilot Studio Developer. Closes Gap-CS-02: CS Test Bot does not identify trigger phrase
collisions. All four defect classes addressed; collision row is primary gap evidence.]

| Defect Class | DEFECT_VERDICT | Evidence | Reproduction Sequence |
|-------------|---------------|----------|----------------------|
| Dead end | FOUND \| CONFIRMED_ABSENT | [FOUND: topic+node+path. CONFIRMED_ABSENT: "All [N] exits verified: [list]."] | [FOUND: sequence. CONFIRMED_ABSENT: N/A] |
| Infinite loop | FOUND \| CONFIRMED_ABSENT | [FOUND: cycle+condition. CONFIRMED_ABSENT: "Redirect graph acyclic. Map: [list]."] | [FOUND: cycle. CONFIRMED_ABSENT: N/A] |
| Trigger phrase collision | FOUND \| CONFIRMED_ABSENT | [FOUND: phrase, topics, scores, disambiguation strategy (entity enrichment \| condition ordering \| trigger phrase refactor) + rationale. CONFIRMED_ABSENT: "All [N] phrases unique; runner-up below 0.4."] | [FOUND: "[phrase]"->Topic-A+Topic-B. CONFIRMED_ABSENT: N/A] |
| Missing fallback | FOUND \| CONFIRMED_ABSENT | [FOUND: topic, condition, missing default, CS-SPEC-03. CONFIRMED_ABSENT: "All conditions carry default. Confirmed: [list]."] | [FOUND: sequence. CONFIRMED_ABSENT: N/A] |

GAP_CLOSURE_VERDICT: CLOSED | OPEN
[Gap-CS-02 CLOSED when: trigger phrase collision row has DEFECT_VERDICT + evidence +
reproduction or scope. All four rows present with DEFECT_VERDICT enum.]

---

## GAP-CS-03 CLOSURE: FALLBACK CHAIN TO TERMINAL STATE
[Copilot Studio Developer. Closes Gap-CS-03: CS Test Bot does not verify fallback chain
reaches terminal. Chain MUST be traced from unrecognized input to terminal state.]

Unrecognized user input: "[phrase matching no trigger phrase]"
Step 1: [N] topics evaluated, 0 match -> CS-SPEC-07 activates -> [Fallback topic]
Step 2: [node type] -- [action]
...
Terminal state: [escalation node opened | end of conversation node reached | loop detected]
FALLBACK_QUALITY: COMPLETE | LOOPS | TRUNCATED

GAP_CLOSURE_VERDICT: CLOSED | OPEN
[Gap-CS-03 CLOSED when: chain traced from unrecognized input through all nodes to a
terminal state. FALLBACK_QUALITY enum used. TRUNCATED = gap not closed.]

---

## GAP-CS-04 CLOSURE: ADVERSARIAL TURN INJECTION
[Copilot Studio Developer. Closes Gap-CS-04: CS Test Bot does not inject adversarial turns.]

Scenario type: [mid-flow topic switch | unexpected input during active question | session timeout]
Scenario: "[description of what the user does to destabilize the flow]"
Injected at: Turn T-[NN], after session state: [snapshot]
Node path: [trace from injection point through agent response]
Session variable impact: [what changes, is corrupted, or is lost]
Agent response: "[text]"
ADVERSARIAL_OUTCOME: GRACEFUL | BRITTLE | SILENT_FAILURE

GAP_CLOSURE_VERDICT: CLOSED | OPEN
[Gap-CS-04 CLOSED when: adversarial scenario described with injection point, node path
traced, session variable impact stated, ADVERSARIAL_OUTCOME enum used.]

---

## GAP-CS-05 CLOSURE: GRAPH COVERAGE METRIC
[Copilot Studio Developer. Closes Gap-CS-05: CS Test Bot does not report coverage ratios.]

Coverage:
| Metric | Visited | Total (from Gap-CS-06 inventory) | Ratio |
|--------|---------|----------------------------------|-------|
| Topics | [N] | [Total] | [N/Total] ([pct]%) |
| Trigger phrases exercised | [N] | [Total] | [N/Total] ([pct]%) |

Amendments (all FOUND defects and DEVIATES rows from Gap-CS-01 and Gap-CS-02):
- CS-SPEC-NN: [violation]. Trigger: "[input]"->[failure]. Fix: [change]. P1|P2|P3.

Developer artifact complete. Gap-CS-06 through Gap-CS-05 are closed.

GAP_CLOSURE_VERDICT: CLOSED | OPEN
[Gap-CS-05 CLOSED when: coverage ratios present as fractions with percentages;
all FOUND and DEVIATES items have amendments.]

=== DEVELOPER ARTIFACT COMPLETE (Gap-CS-06 through Gap-CS-05) ===

=== AUDITOR NOW READS THE COMPLETED ARTIFACT ===

---

## GAP-CS-07 CLOSURE: AUDITOR POST-PRODUCTION AUDIT
[Compliance Auditor. Read the Developer artifact (Gap-CS-06 through Gap-CS-05) as a
finished document. Developer role ended. Apply the Gap-CS-07 Pre-Work assertion contract.
Re-annotate every Trace Table row from Gap-CS-01 independently.]

Per-turn re-annotation:
| Turn | Dev SPEC_CONFORMANCE | Aud SPEC_CONFORMANCE | Dev PROHIBITED_TERM_SCAN | Aud PROHIBITED_TERM_SCAN | DISCREPANCY |
|------|---------------------|---------------------|--------------------------|--------------------------|-------------|
| T-01 | [from Gap-CS-01] | CONFORMS \| DEVIATES[CS-SPEC-NN] | [from Gap-CS-01] | CLEAN \| FOUND[term] | NONE \| FOUND[...] |
[...one row per turn from Gap-CS-01]

Prohibited term body scan (all Developer gap-closure sections, full text):
| Term | Present | Location |
|------|---------|----------|
| intent | YES \| NO | [Gap-CS-NN / N/A] |
| dialog | YES \| NO | [Gap-CS-NN / N/A] |
| slot | YES \| NO | [Gap-CS-NN / N/A] |
| NLU | YES \| NO | [Gap-CS-NN / N/A] |
| utterance | YES \| NO | [Gap-CS-NN / N/A] |
| chatbot | YES \| NO | [Gap-CS-NN / N/A] |
| handoff | YES \| NO | [Gap-CS-NN / N/A] |
| context | YES \| NO | [Gap-CS-NN / N/A] |
| bot | YES \| NO | [Gap-CS-NN / N/A] |
PROHIBITED_TERM_BODY_SCAN: CLEAN | FOUND[list]

Gap-closure registry audit:
| Gap | CS Test Bot miss | Developer closure | Auditor verification |
|-----|-----------------|-------------------|----------------------|
| Gap-CS-06 | Domain unverified | Domain + vocab declared | GAP_CLOSURE_VERDICT: CLOSED \| OPEN \| REGRESSION |
| Gap-CS-01 | Session scope missed | Per-turn SESSION_STATE | GAP_CLOSURE_VERDICT: CLOSED \| OPEN \| REGRESSION |
| Gap-CS-02 | Cross-topic collisions missed | Defect matrix all four classes | GAP_CLOSURE_VERDICT: CLOSED \| OPEN \| REGRESSION |
| Gap-CS-03 | Fallback terminal unverified | Fallback chain to terminal | GAP_CLOSURE_VERDICT: CLOSED \| OPEN \| REGRESSION |
| Gap-CS-04 | No adversarial injection | Adversarial scenario with ADVERSARIAL_OUTCOME | GAP_CLOSURE_VERDICT: CLOSED \| OPEN \| REGRESSION |
| Gap-CS-05 | No coverage ratios | Graph and trigger coverage ratios | GAP_CLOSURE_VERDICT: CLOSED \| OPEN \| REGRESSION |

Auditor summary:
  Contract: Gap-CS-07 Pre-Work assertion schema. Turns audited: [N].
  DISCREPANCY: [N]. GAP_CLOSURE_REGRESSIONS: [N] | NONE.
  AUDIT_VERDICT: CLEAN | ISSUES_FOUND

GAP_CLOSURE_VERDICT: CLOSED | OPEN
[Gap-CS-07 CLOSED when: per-turn re-annotation complete; prohibited term scan complete;
gap-closure registry audit complete; auditor summary produced.]
```

---

## V-03: Role Sequence -- Topology Invariants as Explicit C-16 Layer

**Axis:** Role Sequence -- Developer Phase 0-D extends beyond domain and vocabulary declarations
to full topology invariant pre-commitment (INVARIANT-TOPO-NN). These are design-time structural
claims about the agent graph, distinct from CS-SPEC runtime behavioral rules.

**Hypothesis:** R5 V-01 had session variable and exit invariants (INVARIANT-SV-NN, INVARIANT-EXIT-NN)
as part of Phase 0-D. R5 V-05 had topology invariants as a new pattern but did not tie them to
C-16 or C-17 explicitly. V-03 makes topology invariants the primary C-16 pre-commitment signal.
The Auditor adds INVARIANT_CONFORMANCE as mandatory 4th per-turn column. Each invariant carries a
gap-closure annotation (C-17). The defect matrix references topology invariants by ID: a
CONFIRMED_ABSENT verdict MUST cite the INVARIANT-TOPO-NN that structurally precludes the defect,
making it falsifiable rather than just asserted.

**Predicted score:** 100.

```
You are running /flow:conversation for topic "{topic}".

Read: simulations/flow/conversation/{topic}-conversation-{date}.md if it exists.
Read: any signal artifacts in simulations/ relevant to "{topic}".

Four roles execute in strict phase sequence. Each phase is a gate.

  (1) Copilot Studio Developer (Phase 0-D: domain + topology invariants)
  (2) Compliance Auditor      (Phase 0-A: assertion contract bound to Phase 0-D)
  (3) Copilot Studio Developer (Phases 1-5: trace and analysis)
  (4) Compliance Auditor      (Phase 6: post-production audit)

TWO STRUCTURAL LAYERS are tracked throughout this trace:
  Layer 1 -- CS-SPEC (runtime behavioral): rules that govern behavior at execution time.
    Checked per-turn as SPEC_CONFORMANCE.
  Layer 2 -- INVARIANT-TOPO (design-time structural): claims about the agent graph that
    must be true independent of any specific conversation path. Pre-committed by Developer
    in Phase 0-D. Checked per-turn as INVARIANT_CONFORMANCE. Cross-verified in Phase 6.
  Neither layer substitutes for the other.

CS vocabulary mandatory in all Developer output:
  Topics, Trigger phrases, Conditions, Fallback topics, Escalation nodes,
  Session variables, Topic redirects, Actions, Generative answers,
  Knowledge sources, End of conversation nodes.
Prohibited: intent | dialog | slot | NLU | utterance | chatbot | handoff | context | bot

---

## PHASE 0-D: DEVELOPER DOMAIN PRE-CONTRACT + TOPOLOGY INVARIANTS
[Copilot Studio Developer speaks first.]
[Gap-R6-01 closure: C-16 -- Developer declares domain inventory AND topology invariants
before the Auditor writes any schema. Topology invariants are design-time structural claims,
not trace output; Auditor independence is preserved.]

### Agent Topology
Agent name: [Name or description]
Topics in graph: [N total]:
  [Topic-A]: trigger phrases: "[phrase-1]", "[phrase-2]"
  [Topic-B]: trigger phrases: "[phrase-1]", "[phrase-2]"
  [Topic-C (Fallback)]: activates on: no trigger phrase match
Fallback topic: [Name / System Fallback Topic / not configured]
Escalation path: [Topic / not configured]
Session variables:
  [VarName]: scope=[topic-scoped | global], type=[Text|Number|Boolean], initial=[value | unset]
Coverage scope: [N] of [Total] topics ([pct]%).

### CS Vocabulary Binding
  dialog unit -> "topic" | routing -> "trigger phrase", "condition" |
  state -> "session variable" | no-match -> "fallback topic", "escalation"

### Topology Invariants (design-time structural claims -- pre-committed before trace)
Each invariant states a structural property that must hold across the agent graph.
The Auditor binds these claims into the assertion schema. Defect matrix rows for
topology-related defect classes MUST reference the relevant invariant.

  INVARIANT-TOPO-01: All condition nodes in the graph have at least one default branch.
    [Design-time equivalent of CS-SPEC-03. Verifiable via defect matrix missing-fallback row
     and per-turn INVARIANT_CONFORMANCE at condition nodes.]

  INVARIANT-TOPO-02: No unconditional topic redirect cycle exists. All redirect paths
    eventually reach an escalation node or end of conversation node.
    [Verifiable via defect matrix infinite-loop row and fallback chain trace.]

  INVARIANT-TOPO-03: All trigger phrases in the graph are unique at the topic level.
    No trigger phrase activates more than one topic above confidence threshold without
    an explicit disambiguation condition node.
    [Verifiable via defect matrix trigger phrase collision row.]

  INVARIANT-TOPO-04: Every topic has at least one defined exit path: a topic redirect,
    an escalation node, or an end of conversation node.
    [Verifiable via defect matrix dead-end row and Phase 5 invariant summary.]

### Session Variable Invariants
  INVARIANT-SV-01: [VarName] persists within [Topic] and clears at topic exit.
  INVARIANT-SV-02: [VarName] is global-scoped and survives all topic transitions.

Developer SHALL NOT alter this contract. Auditor SHALL NOT begin Phase 0-A until complete.
GAP_CLOSURE_VERDICT: CLOSED | OPEN [Gap-R6-01: Developer domain pre-contract + topology
invariants declared before any trace output. INVARIANT-TOPO-01 through 04 committed.]

---

## PHASE 0-A: AUDITOR ASSERTION CONTRACT
[Compliance Auditor. Auditor SHALL NOT begin until Phase 0-D complete. Gap-R4-01 closure.
Contract written against Phase 0-D topology and invariant declarations.]

### Topology Spec (runtime behavioral -- Layer 1)
  CS-SPEC-01 through CS-SPEC-07 [as declared in Phase 0-D]

### Assertion Schema

Per-turn Trace Table columns (ALL FOUR mandatory; blank cell = structural violation):
  SPEC_CONFORMANCE: CONFORMS | DEVIATES[CS-SPEC-NN: description]
  INVARIANT_CONFORMANCE: HOLDS | VIOLATED[INVARIANT-TOPO-NN: description]
    [Check applicable Phase 0-D topology invariants at turns where they are testable.
     HOLDS = no violation observable at this turn.
     VIOLATED = trace at this turn reveals the pre-committed claim does not hold.]
  SESSION_STATE: [name=value (scope, changed/held/cleared) per variable]
  PROHIBITED_TERM_SCAN: CLEAN | FOUND[term at exact location]

Defect matrix (all four rows mandatory):
  DEFECT_VERDICT: FOUND | CONFIRMED_ABSENT
  [CONFIRMED_ABSENT for topology-related defects MUST cite the INVARIANT-TOPO-NN
   that structurally precludes the defect class. Generic scope statements insufficient.]
  [FOUND must state reproduction sequence AND which INVARIANT-TOPO-NN is violated.]
  Free-text in DEFECT_VERDICT = contract violation.

Terminal verdicts:
  FALLBACK_QUALITY: COMPLETE | LOOPS | TRUNCATED
  ADVERSARIAL_OUTCOME: GRACEFUL | BRITTLE | SILENT_FAILURE

Coverage: GRAPH_COVERAGE: [N]/[total]. TRIGGER_COVERAGE: [N]/[total].
Gap-Closure: Each Developer phase SHALL carry GAP_CLOSURE_VERDICT: CLOSED | OPEN + gap tag.

Auditor-only fields (Phase 6):
  AUDITOR_SPEC_CONFORMANCE: CONFORMS | DEVIATES[CS-SPEC-NN: description]
  AUDITOR_INVARIANT_CONFORMANCE: HOLDS | VIOLATED[INVARIANT-TOPO-NN: description]
  AUDITOR_PROHIBITED_TERM_SCAN: CLEAN | FOUND[term at exact location]
  DISCREPANCY: NONE | FOUND[SPEC_CONFORMANCE] | FOUND[INVARIANT_CONFORMANCE] |
               FOUND[PROHIBITED_TERM] | FOUND[MULTIPLE: list]

Prohibited terms: intent | dialog | slot | NLU | utterance | chatbot | handoff | context | bot

Developer SHALL NOT begin Phase 1 until contract complete.
GAP_CLOSURE_VERDICT: CLOSED | OPEN [Gap-R4-01: Auditor contract precedes Developer trace;
topology invariants from Phase 0-D incorporated into assertion schema]

---

## PHASE 1: TOPOLOGY CONFIRMATION + INVARIANT TESTABILITY MAP
[Copilot Studio Developer. Gap-R5-01 closure. Maps which INVARIANT-TOPO-NN are testable
within the coverage scope of this simulation.]

Coverage: [N] of [Total] topics ([pct]%). Visited: [list]. Not visited: [list | none].

Invariant testability map:
  INVARIANT-TOPO-01: testable at [topic conditions encountered in coverage scope -- T-NN list]
  INVARIANT-TOPO-02: testable at [redirect paths in coverage scope]
  INVARIANT-TOPO-03: testable via [trigger phrases exercised in coverage scope]
  INVARIANT-TOPO-04: testable at [exit paths of topics in coverage scope]

GAP_CLOSURE_VERDICT: CLOSED | OPEN [Gap-R5-01: coverage scope confirmed;
invariant testability mapped before trace begins]

---

## PHASE 2: CONVERSATION TRACE TABLE
[Copilot Studio Developer. Gap-R4-01 closure. ALL FOUR assertion columns mandatory.]

Walk every turn. All four columns mandatory. Blank cell = violation.
INVARIANT_CONFORMANCE applies INVARIANT-TOPO-NN claims from Phase 0-D at testable turns.

| Turn | User Input | Trigger Phrase Matched | Topic | Nodes Executed | SESSION_STATE | Agent Response | SPEC_CONFORMANCE | INVARIANT_CONFORMANCE | PROHIBITED_TERM_SCAN |
|------|-----------|----------------------|-------|----------------|---------------|---------------|-----------------|----------------------|---------------------|
| T-01 | "[input]" | "[phrase]" (HIGH/MED/LOW) | [Topic] | Trigger>Message>Question | var1=X (topic-scoped, set) | "[response]" | CONFORMS \| DEVIATES[CS-SPEC-NN] | HOLDS \| VIOLATED[INVARIANT-TOPO-NN: desc] | CLEAN \| FOUND[term] |
| T-02 | "[input]" | "[phrase]" (HIGH/MED/LOW) | [Topic] | Trigger>Condition(default)>Redirect | var1=cleared (topic exited) | "[response]" | CONFORMS \| DEVIATES[CS-SPEC-NN] | HOLDS \| VIOLATED[INVARIANT-TOPO-NN: desc] | CLEAN \| FOUND[term] |
[...all turns. No turns skipped. All four columns populated.]

GAP_CLOSURE_VERDICT: CLOSED | OPEN [Gap-R4-01: per-turn SPEC_CONFORMANCE, INVARIANT_CONFORMANCE,
SESSION_STATE, PROHIBITED_TERM_SCAN on every row]

---

## PHASE 3: DEFECT MATRIX WITH TOPOLOGY INVARIANT CROSS-REFERENCE
[Copilot Studio Developer. Gap-R4-02 closure. CONFIRMED_ABSENT rows MUST cite the
INVARIANT-TOPO-NN that structurally precludes the defect.]

| Defect Class | DEFECT_VERDICT | Evidence + Invariant Reference | Reproduction Sequence |
|-------------|---------------|-------------------------------|----------------------|
| Dead end | FOUND \| CONFIRMED_ABSENT | [FOUND: topic+node+path, INVARIANT-TOPO-04 VIOLATED. CONFIRMED_ABSENT: "All [N] topic exits verified. INVARIANT-TOPO-04 holds across all topics in coverage scope: [exit map]."] | [FOUND: sequence. CONFIRMED_ABSENT: N/A] |
| Infinite loop | FOUND \| CONFIRMED_ABSENT | [FOUND: redirect cycle, missing condition, INVARIANT-TOPO-02 VIOLATED. CONFIRMED_ABSENT: "Redirect graph acyclic. INVARIANT-TOPO-02 holds. Map: [A->B], [C->terminal]."] | [FOUND: cycle. CONFIRMED_ABSENT: N/A] |
| Trigger phrase collision | FOUND \| CONFIRMED_ABSENT | [FOUND: phrase, topics, scores, INVARIANT-TOPO-03 VIOLATED, disambiguation strategy (entity enrichment \| condition ordering \| trigger phrase refactor) + rationale. CONFIRMED_ABSENT: "All [N] phrases unique. INVARIANT-TOPO-03 holds; runner-up below 0.4."] | [FOUND: "[phrase]"->Topic-A+Topic-B. CONFIRMED_ABSENT: N/A] |
| Missing fallback | FOUND \| CONFIRMED_ABSENT | [FOUND: condition node, no default, CS-SPEC-03 violated, INVARIANT-TOPO-01 VIOLATED. CONFIRMED_ABSENT: "All condition nodes have default. INVARIANT-TOPO-01 holds. CS-SPEC-03 holds. Verified: [list]."] | [FOUND: "[input]"->no default. CONFIRMED_ABSENT: N/A] |

GAP_CLOSURE_VERDICT: CLOSED | OPEN [Gap-R4-02: all four classes, DEFECT_VERDICT enum,
INVARIANT-TOPO cross-reference on every row -- CONFIRMED_ABSENT is falsifiable]

---

## PHASE 4: FALLBACK CHAIN + ADVERSARIAL INJECTION
[Copilot Studio Developer. Gap-R4-03: fallback to terminal. Gap-R4-04: adversarial injection.
Include INVARIANT-TOPO-02 verification for fallback chain terminal state.]

Fallback chain:
  Unrecognized input: "[phrase]"
  Step 1: [N] topics evaluated, 0 match -> CS-SPEC-07 -> [Fallback topic]
  ...
  Terminal: [escalation | end of conversation | loop]
  FALLBACK_QUALITY: COMPLETE | LOOPS | TRUNCATED
  INVARIANT-TOPO-02 check: fallback chain exits to terminal. HOLDS | VIOLATED[path].

Adversarial injection:
  Scenario: [mid-flow switch | unexpected input | timeout]
  Injected at T-[NN], state: [snapshot]. Node path: [trace]. Variable impact: [changes].
  ADVERSARIAL_OUTCOME: GRACEFUL | BRITTLE | SILENT_FAILURE

GAP_CLOSURE_VERDICT: CLOSED | OPEN [Gap-R4-03, Gap-R4-04]

---

## PHASE 5: COVERAGE + TOPOLOGY INVARIANT SUMMARY + AMENDMENTS
[Copilot Studio Developer. Gap-R4-05: quantified ratios. Gap-R6-01 extended: topology
invariant summary cross-checks all Phase 0-D INVARIANT-TOPO-NN claims against trace evidence.]

Coverage:
| Metric | Visited | Total | Ratio |
|--------|---------|-------|-------|
| Topics | [N] | [Total] | [pct]% |
| Trigger phrases | [N] | [Total] | [pct]% |

Topology Invariant Summary:
| Invariant | Pre-committed claim | Trace evidence | Final status |
|-----------|--------------------|--------------------|-------------|
| INVARIANT-TOPO-01 | All conditions have default | Phase 2 condition nodes + Phase 3 missing-fallback row | HOLDS \| VIOLATED[topic+turn] |
| INVARIANT-TOPO-02 | No redirect cycle | Phase 2 redirect turns + Phase 3 loop row + Phase 4 fallback chain | HOLDS \| VIOLATED[cycle path] |
| INVARIANT-TOPO-03 | All trigger phrases unique | Phase 3 collision row + Phase 2 trigger columns | HOLDS \| VIOLATED[phrase+topics] |
| INVARIANT-TOPO-04 | All topics have exit path | Phase 3 dead-end row + Phase 2 exit turns | HOLDS \| VIOLATED[topic+node] |
| INVARIANT-SV-01 | [Var] persists within topic | Phase 2 SESSION_STATE column | HOLDS \| VIOLATED[turn] |
| INVARIANT-SV-02 | [Var] global-scoped | Phase 2 SESSION_STATE column | HOLDS \| VIOLATED[turn] |

Amendments (all FOUND defects and VIOLATED invariants):
- INVARIANT-TOPO-NN / CS-SPEC-NN: [description]. Trigger: "[input]"->[failure]. Fix: [change]. P1|P2|P3.

GAP_CLOSURE_VERDICT: CLOSED | OPEN [Gap-R4-05: coverage ratios present;
Gap-R6-01 extended: topology invariant summary cross-checks all pre-committed claims]

=== DEVELOPER ARTIFACT COMPLETE (Phases 0-D through 5) ===

=== AUDITOR NOW READS THE COMPLETED ARTIFACT ===

---

## PHASE 6: AUDITOR POST-PRODUCTION AUDIT
[Compliance Auditor. Read Phases 0-D through 5 as finished artifact. Developer role ended.
Apply Phase 0-A assertion contract. Re-annotate all Phase 2 rows with four columns.]
[Gap-R6-02 closure: C-17 -- per-phase gap-closure annotations verified; topology invariant
cross-audit confirms Developer invariant summary claims.]

Per-turn re-annotation (ALL FOUR columns):
| Turn | Dev SPEC | Aud SPEC | Dev INV_CONF | Aud INV_CONF | Dev PROHIBITED | Aud PROHIBITED | DISCREPANCY |
|------|---------|---------|-------------|-------------|----------------|----------------|-------------|
| T-01 | [Phase 2] | CONFORMS\|DEVIATES[NN] | [Phase 2] | HOLDS\|VIOLATED[NN] | [Phase 2] | CLEAN\|FOUND | NONE\|FOUND[...] |
[...one row per turn]

Topology invariant cross-audit:
| Invariant | Dev Phase 5 | Aud Phase 6 | DISCREPANCY |
|-----------|------------|------------|-------------|
| TOPO-01 | HOLDS\|VIOLATED | HOLDS\|VIOLATED | NONE\|FOUND[desc] |
| TOPO-02 | HOLDS\|VIOLATED | HOLDS\|VIOLATED | NONE\|FOUND[desc] |
| TOPO-03 | HOLDS\|VIOLATED | HOLDS\|VIOLATED | NONE\|FOUND[desc] |
| TOPO-04 | HOLDS\|VIOLATED | HOLDS\|VIOLATED | NONE\|FOUND[desc] |

Prohibited term body scan (all Developer phases, full text):
| Term | Present | Location |
|------|---------|----------|
| intent | YES\|NO | [Phase/N/A] | dialog | YES\|NO | [Phase/N/A] | slot | YES\|NO | [Phase/N/A] |
| NLU | YES\|NO | [Phase/N/A] | utterance | YES\|NO | [Phase/N/A] | chatbot | YES\|NO | [Phase/N/A] |
| handoff | YES\|NO | [Phase/N/A] | context | YES\|NO | [Phase/N/A] | bot | YES\|NO | [Phase/N/A] |
PROHIBITED_TERM_BODY_SCAN: CLEAN | FOUND[list]

Gap-closure audit:
| Phase | Gap | Dev VERDICT | Aud Verification |
|-------|-----|-------------|-----------------|
| 0-D | Gap-R6-01 | CLOSED\|OPEN | CLOSED\|OPEN\|REGRESSION |
| 0-A | Gap-R4-01 | CLOSED\|OPEN | CLOSED\|OPEN\|REGRESSION |
| 1 | Gap-R5-01 | CLOSED\|OPEN | CLOSED\|OPEN\|REGRESSION |
| 2 | Gap-R4-01 | CLOSED\|OPEN | CLOSED\|OPEN\|REGRESSION |
| 3 | Gap-R4-02 | CLOSED\|OPEN | CLOSED\|OPEN\|REGRESSION |
| 4 | Gap-R4-03,04 | CLOSED\|OPEN | CLOSED\|OPEN\|REGRESSION |
| 5 | Gap-R4-05, Gap-R6-01 ext | CLOSED\|OPEN | CLOSED\|OPEN\|REGRESSION |

Auditor summary:
  Contracts: Phase 0-D (domain + topology invariants) + Phase 0-A.
  Turns: [N]. DISCREPANCY: [N]. INVARIANT_CONFORMANCE discrepancies: [N].
  GAP_CLOSURE_REGRESSIONS: [N] | NONE. AUDIT_VERDICT: CLEAN | ISSUES_FOUND
```

---

## V-04: Full Synthesis -- Bidirectional Pre-Contracts + Topology Invariants + Gap-Closure

**Axes combined:** Role Sequence + Lifecycle Emphasis + Output Format

**Hypothesis:** V-01 tests boundary marker isolation. V-02 tests gap-closure as structure.
V-03 tests topology invariants. V-04 combines all three at maximum density WITH hard
boundary markers (retaining C-12 certainty) and SHALL/MUST phrasing. This is the
reference implementation. If any criterion is fragile under individual axes, the full
synthesis will surface it. V-04 is the expected 100 that all other variations are
measured against.

**Predicted score:** 100.

```
You are running /flow:conversation for topic "{topic}".

Read: simulations/flow/conversation/{topic}-conversation-{date}.md if it exists.
Read: any signal artifacts in simulations/ relevant to "{topic}".

FULL SYNTHESIS PROTOCOL. Four phases execute in strict sequence. Each phase is a gate.
No role may produce output outside its designated phase.

  Phase 0-D: Copilot Studio Developer -- domain pre-contract + topology invariants
             [Gap-R6-01 closure: C-16. SHALL complete before Phase 0-A.]
  Phase 0-A: Compliance Auditor -- assertion contract bound to Phase 0-D
             [Gap-R4-01 closure: C-14. SHALL complete before Phases 1-5.]
  Phases 1-5: Copilot Studio Developer -- trace and analysis
              [Per-phase gap-closure annotations: C-17. SHALL complete before Phase 6.]
  Phase 6:   Compliance Auditor -- post-production audit
             [Gap-R6-02 closure: C-17 verification.]

TWO STRUCTURAL LAYERS:
  CS-SPEC (runtime behavioral): rules checked per-turn as SPEC_CONFORMANCE.
  INVARIANT-TOPO (design-time structural): pre-committed claims about the graph,
    checked per-turn as INVARIANT_CONFORMANCE, cross-verified by Auditor in Phase 6.

CS vocabulary SHALL appear in all Developer output. The following terms are PROHIBITED:
  intent | dialog | slot | NLU | utterance | chatbot | handoff | context | bot

---

## PHASE 0-D: DEVELOPER DOMAIN PRE-CONTRACT + TOPOLOGY INVARIANTS
[Copilot Studio Developer speaks first. Gap-R6-01 closure.]

Agent name: [Name]
Topics: [N total]: [Topic-A], [Topic-B], [Topic-C (Fallback)], ...
Trigger phrases: [Topic-A]: "[p1]", "[p2]". [Topic-B]: "[p1]", "[p2]".
Fallback topic: [Name | not configured]. Escalation: [Topic | not configured].
Session variables: [VarName]: scope=[topic-scoped|global], type=[T|N|B], initial=[v|unset].
Coverage scope: [N] of [Total] topics ([pct]%).

CS vocabulary binding:
  dialog unit->"topic" | routing->"trigger phrase","condition" |
  state->"session variable" | no-match->"fallback topic","escalation"

Topology Spec:
  CS-SPEC-01 through CS-SPEC-07 [as in V-03 Phase 0-D above]

Topology Invariants (design-time structural pre-commitment):
  INVARIANT-TOPO-01: All condition nodes have a default branch. [verifies CS-SPEC-03 structurally]
  INVARIANT-TOPO-02: No unconditional redirect cycle. All paths reach escalation or end of conversation.
  INVARIANT-TOPO-03: All trigger phrases unique at topic level. No ambiguous activation without condition.
  INVARIANT-TOPO-04: Every topic has a defined exit path (redirect | escalation | end of conversation).

Session variable invariants:
  INVARIANT-SV-01: [VarName] persists within [Topic] and clears at exit.
  INVARIANT-SV-02: [VarName] is global-scoped and survives transitions.

Developer SHALL NOT alter this contract. Auditor SHALL NOT begin Phase 0-A until complete.
GAP_CLOSURE_VERDICT: CLOSED | OPEN [Gap-R6-01]

---

## PHASE 0-A: AUDITOR ASSERTION CONTRACT
[Compliance Auditor. SHALL NOT begin until Phase 0-D complete. Gap-R4-01 closure.
Written against Developer Phase 0-D; topology invariants incorporated into schema.]

Per-turn Trace Table -- ALL FOUR columns mandatory (blank = structural violation):
  SPEC_CONFORMANCE: CONFORMS | DEVIATES[CS-SPEC-NN: description]
  INVARIANT_CONFORMANCE: HOLDS | VIOLATED[INVARIANT-TOPO-NN: description]
  SESSION_STATE: [name=value (scope, changed/held/cleared)]
  PROHIBITED_TERM_SCAN: CLEAN | FOUND[term at exact location]

Defect matrix (all four rows):
  DEFECT_VERDICT: FOUND | CONFIRMED_ABSENT
  [CONFIRMED_ABSENT: MUST cite INVARIANT-TOPO-NN that precludes the defect class.
   FOUND: reproduction + INVARIANT-TOPO-NN that is violated. Free-text = violation.]

Terminal verdicts:
  FALLBACK_QUALITY: COMPLETE | LOOPS | TRUNCATED
  ADVERSARIAL_OUTCOME: GRACEFUL | BRITTLE | SILENT_FAILURE

Coverage: GRAPH_COVERAGE: [N]/[total]. TRIGGER_COVERAGE: [N]/[total].

Gap-Closure Contract:
  Each Developer phase SHALL carry GAP_CLOSURE_VERDICT: CLOSED | OPEN + gap tag.
  A phase without GAP_CLOSURE_VERDICT is a contract violation.

Auditor-only fields (Phase 6):
  AUDITOR_SPEC_CONFORMANCE: CONFORMS | DEVIATES[CS-SPEC-NN]
  AUDITOR_INVARIANT_CONFORMANCE: HOLDS | VIOLATED[INVARIANT-TOPO-NN]
  AUDITOR_PROHIBITED_TERM_SCAN: CLEAN | FOUND[term]
  DISCREPANCY: NONE | FOUND[SPEC_CONFORMANCE] | FOUND[INVARIANT_CONFORMANCE] |
               FOUND[PROHIBITED_TERM] | FOUND[MULTIPLE: list]

Prohibited: intent | dialog | slot | NLU | utterance | chatbot | handoff | context | bot.
Developer SHALL NOT begin Phase 1 until complete.
GAP_CLOSURE_VERDICT: CLOSED | OPEN [Gap-R4-01]

---

## PHASE 1: TOPOLOGY CONFIRMATION
[Developer. Gap-R5-01 closure. Invariant testability mapped for this coverage scope.]

Coverage: [N]/[Total] ([pct]%). Visited: [list]. Not visited: [list|none].
Invariant testability: TOPO-01 at [T-NN list], TOPO-02 at [T-NN list], TOPO-03 via [phrases], TOPO-04 at [exits].
GAP_CLOSURE_VERDICT: CLOSED | OPEN [Gap-R5-01]

---

## PHASE 2: CONVERSATION TRACE TABLE
[Developer. Gap-R4-01 closure. All FOUR columns mandatory. Blank = violation.]

| Turn | User Input | Trigger Phrase Matched | Topic | Nodes Executed | SESSION_STATE | Agent Response | SPEC_CONFORMANCE | INVARIANT_CONFORMANCE | PROHIBITED_TERM_SCAN |
|------|-----------|----------------------|-------|----------------|---------------|---------------|-----------------|----------------------|---------------------|
| T-01 | "[input]" | "[phrase]" (HIGH/MED/LOW) | [Topic] | Trigger>Message>Question | var1=X (topic-scoped, set) | "[response]" | CONFORMS \| DEVIATES[CS-SPEC-NN] | HOLDS \| VIOLATED[TOPO-NN] | CLEAN \| FOUND[term] |
| T-02 | "[input]" | "[phrase]" (HIGH/MED/LOW) | [Topic] | Trigger>Condition(default)>Redirect | var1=cleared (topic exited) | "[response]" | CONFORMS \| DEVIATES[CS-SPEC-NN] | HOLDS \| VIOLATED[TOPO-NN] | CLEAN \| FOUND[term] |
[...all turns. All four columns populated. No turns skipped.]
GAP_CLOSURE_VERDICT: CLOSED | OPEN [Gap-R4-01]

---

## PHASE 3: DEFECT MATRIX
[Developer. Gap-R4-02 closure. All four rows. INVARIANT-TOPO cross-reference mandatory.]

| Defect Class | DEFECT_VERDICT | Evidence + Invariant Reference | Reproduction |
|-------------|---------------|-------------------------------|-------------|
| Dead end | FOUND\|CONFIRMED_ABSENT | [TOPO-04 ref] | [seq/N/A] |
| Infinite loop | FOUND\|CONFIRMED_ABSENT | [TOPO-02 ref] | [cycle/N/A] |
| Trigger phrase collision | FOUND\|CONFIRMED_ABSENT | [TOPO-03 ref + disambiguation strategy if FOUND] | [phrase->2+topics/N/A] |
| Missing fallback | FOUND\|CONFIRMED_ABSENT | [TOPO-01 + CS-SPEC-03 ref] | [input->no default/N/A] |

GAP_CLOSURE_VERDICT: CLOSED | OPEN [Gap-R4-02]

---

## PHASE 4: FALLBACK CHAIN + ADVERSARIAL INJECTION
[Developer. Gap-R4-03,04 closure.]

Fallback: "[phrase]" -> CS-SPEC-07 -> [steps] -> Terminal: [escalation|end|loop].
FALLBACK_QUALITY: COMPLETE | LOOPS | TRUNCATED. INVARIANT-TOPO-02: HOLDS | VIOLATED.

Adversarial: [type]. Injected T-[NN]. Path: [trace]. Impact: [vars]. ADVERSARIAL_OUTCOME: GRACEFUL|BRITTLE|SILENT_FAILURE.
GAP_CLOSURE_VERDICT: CLOSED | OPEN [Gap-R4-03, Gap-R4-04]

---

## PHASE 5: COVERAGE + INVARIANT SUMMARY + AMENDMENTS
[Developer. Gap-R4-05 + Gap-R6-01 extended closure.]

Coverage: Topics [N]/[Total] ([pct]%). Trigger phrases [N]/[Total] ([pct]%).

Topology Invariant Summary:
| Invariant | Claim | Trace evidence | Status |
|-----------|-------|----------------|--------|
| TOPO-01 | All conditions have default | Phase 2 + Phase 3 missing-fallback | HOLDS \| VIOLATED[location] |
| TOPO-02 | No redirect cycle | Phase 2 redirects + Phase 3 loop + Phase 4 fallback | HOLDS \| VIOLATED[cycle] |
| TOPO-03 | All trigger phrases unique | Phase 3 collision row | HOLDS \| VIOLATED[phrase] |
| TOPO-04 | All topics have exit | Phase 3 dead-end row | HOLDS \| VIOLATED[topic] |
| SV-01 | [var] persists within topic | Phase 2 SESSION_STATE | HOLDS \| VIOLATED[turn] |
| SV-02 | [var] global-scoped | Phase 2 SESSION_STATE | HOLDS \| VIOLATED[turn] |

Amendments: [all FOUND+VIOLATED with trigger sequence, fix, P1|P2|P3]
GAP_CLOSURE_VERDICT: CLOSED | OPEN [Gap-R4-05, Gap-R6-01 ext]

=== DEVELOPER ARTIFACT COMPLETE (Phases 0-D through 5) ===

=== AUDITOR NOW READS THE COMPLETED ARTIFACT ===

---

## PHASE 6: AUDITOR POST-PRODUCTION AUDIT
[Compliance Auditor. Read Phases 0-D through 5 as finished artifact. Developer role ended.
Gap-R6-02 closure: C-17 verification across all Developer phases.]

Per-turn re-annotation (all four columns):
| Turn | Dev SPEC | Aud SPEC | Dev INV | Aud INV | Dev PROHIBITED | Aud PROHIBITED | DISCREPANCY |
|------|---------|---------|---------|---------|----------------|----------------|-------------|
| T-01 | [P2] | CONFORMS\|DEVIATES[NN] | [P2] | HOLDS\|VIOLATED[NN] | [P2] | CLEAN\|FOUND | NONE\|FOUND[...] |
[...one row per turn]

Topology invariant cross-audit:
| Invariant | Dev Phase 5 | Aud Phase 6 | DISCREPANCY |
|-----------|------------|------------|-------------|
| TOPO-01 | HOLDS\|VIOLATED | HOLDS\|VIOLATED | NONE\|FOUND |
| TOPO-02 | HOLDS\|VIOLATED | HOLDS\|VIOLATED | NONE\|FOUND |
| TOPO-03 | HOLDS\|VIOLATED | HOLDS\|VIOLATED | NONE\|FOUND |
| TOPO-04 | HOLDS\|VIOLATED | HOLDS\|VIOLATED | NONE\|FOUND |

Prohibited term body scan:
  intent:YES\|NO. dialog:YES\|NO. slot:YES\|NO. NLU:YES\|NO. utterance:YES\|NO.
  chatbot:YES\|NO. handoff:YES\|NO. context:YES\|NO. bot:YES\|NO.
PROHIBITED_TERM_BODY_SCAN: CLEAN | FOUND[list]

Gap-closure audit:
| Phase | Gap | Dev | Aud |
|-------|-----|-----|-----|
| 0-D | Gap-R6-01 | CLOSED\|OPEN | CLOSED\|OPEN\|REGRESSION |
| 0-A | Gap-R4-01 | CLOSED\|OPEN | CLOSED\|OPEN\|REGRESSION |
| 1 | Gap-R5-01 | CLOSED\|OPEN | CLOSED\|OPEN\|REGRESSION |
| 2 | Gap-R4-01 | CLOSED\|OPEN | CLOSED\|OPEN\|REGRESSION |
| 3 | Gap-R4-02 | CLOSED\|OPEN | CLOSED\|OPEN\|REGRESSION |
| 4 | Gap-R4-03,04 | CLOSED\|OPEN | CLOSED\|OPEN\|REGRESSION |
| 5 | Gap-R4-05, R6-01 ext | CLOSED\|OPEN | CLOSED\|OPEN\|REGRESSION |

Auditor summary: Turns [N]. DISCREPANCY [N]. INVARIANT_CONF discrepancies [N].
REGRESSIONS: [N]|NONE. AUDIT_VERDICT: CLEAN | ISSUES_FOUND
GAP_CLOSURE_VERDICT: CLOSED | OPEN [Gap-R6-02]
```

---

## V-05: Lifecycle (Minimal) + Phrasing (SHALL-Only, No Hard Marker) + C-16 + C-17

**Axes combined:** Lifecycle Emphasis (minimal 3-phase from R5 V-02) + Phrasing Register
(SHALL/MUST only -- no hard boundary separators).

**Hypothesis:** R5 V-02 proved intermediate gates are cosmetic (all 15 criteria passed with
3-phase minimal structure). R5 V-03 left the C-12 diagnostic bet unresolved (kept both
normative AND hard marker). V-05 combines: (a) minimal architecture, AND (b) SHALL-only
boundary, AND (c) explicit C-16 and C-17 compliance. If C-12 passes in V-05 AND fails
in V-01: failure is specific to minimal structure -- boundary marker alone fails in minimal
context but works with full phase structure. If both pass: hard marker is cosmetic in all
structures. If both fail: normative gating alone is never sufficient, hard marker is
always load-bearing.

**Predicted score:** C-12 verdict unknown. All other criteria: PASS.

```
You are running /flow:conversation for topic "{topic}".

Read: simulations/flow/conversation/{topic}-conversation-{date}.md if it exists.
Read: any signal artifacts in simulations/ relevant to "{topic}".

MINIMAL ARCHITECTURE + NORMATIVE BOUNDARY TEST. Three phases execute in strict sequence.
Role transitions enforced by SHALL NOT rules ONLY. No hard boundary separators.

  Phase 0: Compliance Auditor -- assertion contract.
           The Developer SHALL NOT begin Phase 1 until Phase 0 complete.
  Phase 1: Copilot Studio Developer -- domain pre-contract (1-A) and all trace output (1-B to 1-F).
           The Auditor SHALL NOT begin Phase 2 until the Developer declares 1-A through 1-F complete.
  Phase 2: Compliance Auditor -- post-production audit. Reads Phase 1 as a completed artifact.
           Developer role has ended.

CS vocabulary mandatory in all Developer output:
  Topics, Trigger phrases, Conditions, Fallback topics, Escalation nodes,
  Session variables, Topic redirects, Actions, Generative answers,
  Knowledge sources, End of conversation nodes.
Prohibited: intent | dialog | slot | NLU | utterance | chatbot | handoff | context | bot

---

## PHASE 0: AUDITOR ASSERTION CONTRACT
[Compliance Auditor speaks. Declare complete assertion contract before any Developer output.]
[Gap-R4-01 closure: Auditor contract precedes Developer trace. Gap-R6-01 acknowledgement:
Developer WILL declare a domain pre-contract as Phase 1-A before trace begins; schema
is written in anticipation of that declaration.]

Topology Spec:
  CS-SPEC-01: Trigger phrase matching activates topic above confidence threshold.
  CS-SPEC-02: Topic-scoped session variables cleared at topic boundary.
  CS-SPEC-03: Condition nodes require a default branch.
  CS-SPEC-04: Redirect nodes do not carry topic-scoped variables.
  CS-SPEC-05: End of conversation nodes terminate the session.
  CS-SPEC-06: Escalation nodes open human agent session.
  CS-SPEC-07: Fallback topic activates when no trigger phrase exceeds threshold.

Prohibited in all Developer output:
  intent | dialog | slot | NLU | utterance | chatbot | handoff | context | bot

Per-turn Trace Table -- Phase 1-C (mandatory columns; blank = structural violation):
  SPEC_CONFORMANCE: CONFORMS | DEVIATES[CS-SPEC-NN: description]
  SESSION_STATE: [name=value (scope, changed/held/cleared)]
  PROHIBITED_TERM_SCAN: CLEAN | FOUND[term at exact location]

Defect matrix -- Phase 1-D (all four rows):
  DEFECT_VERDICT: FOUND | CONFIRMED_ABSENT
  [CONFIRMED_ABSENT: scope required. FOUND: reproduction required. Free-text = violation.]

Terminal verdicts:
  FALLBACK_QUALITY: COMPLETE | LOOPS | TRUNCATED
  ADVERSARIAL_OUTCOME: GRACEFUL | BRITTLE | SILENT_FAILURE

Coverage -- Phase 1-F:
  GRAPH_COVERAGE: [N]/[total] = [ratio]. TRIGGER_COVERAGE: [N]/[total] = [ratio].

Gap-Closure Contract:
  Each Developer sub-section SHALL carry GAP_CLOSURE_VERDICT: CLOSED | OPEN + gap tag.
  A sub-section without GAP_CLOSURE_VERDICT is a contract violation.

Auditor-only fields (Phase 2):
  AUDITOR_SPEC_CONFORMANCE: CONFORMS | DEVIATES[CS-SPEC-NN: description]
  AUDITOR_PROHIBITED_TERM_SCAN: CLEAN | FOUND[term at exact location]
  DISCREPANCY: NONE | FOUND[SPEC_CONFORMANCE] | FOUND[PROHIBITED_TERM] | FOUND[BOTH]

Developer SHALL begin Phase 1 now.
GAP_CLOSURE_VERDICT: CLOSED | OPEN [Gap-R4-01: Auditor contract complete before Developer trace]

---

## PHASE 1: DEVELOPER OUTPUT
[Copilot Studio Developer speaks. Complete sub-sections 1-A through 1-F in order.
The Auditor SHALL NOT begin Phase 2 until the Developer declares all sub-sections complete.]

### Phase 1-A: Developer Domain Pre-Contract
[Gap-R6-01 closure: C-16 -- Developer declares domain inventory before trace begins.
Domain declarations are not trace output. Auditor independence for Phase 2 is preserved.]

Agent name: [Name]
Topics: [N total]: [Topic-A]: "[p1]","[p2]", terminal=[R|E|A]. [Topic-B]: "[p1]","[p2]", terminal=[R|E|A]. [Fallback].
Session variables: [VarName]: scope=[topic-scoped|global], type=[T|N|B], initial=[v|unset].
Coverage: [N] of [Total] topics ([pct]%).
CS vocab: dialog unit->"topic", routing->"trigger phrase","condition", state->"session variable", no-match->"fallback topic".

GAP_CLOSURE_VERDICT: CLOSED | OPEN [Gap-R6-01: Developer domain pre-contract declared
before any trace output. CS vocabulary bound. Auditor independence preserved.]

### Phase 1-B: Agent Topology Summary
Visited: [list]. Not visited: [list | none].
GAP_CLOSURE_VERDICT: CLOSED | OPEN [Gap-R5-01: coverage scope confirmed]

### Phase 1-C: Conversation Trace Table
[Gap-R4-01 closure. Three mandatory columns. Blank = violation.]

| Turn | User Input | Trigger Phrase Matched | Topic | Nodes Executed | SESSION_STATE | Agent Response | SPEC_CONFORMANCE | PROHIBITED_TERM_SCAN |
|------|-----------|----------------------|-------|----------------|---------------|---------------|-----------------|---------------------|
| T-01 | "[input]" | "[phrase]" (HIGH/MED/LOW) | [Topic] | Trigger>Message>Question | var1=X (topic-scoped, set) | "[response]" | CONFORMS \| DEVIATES[CS-SPEC-NN] | CLEAN \| FOUND[term] |
| T-02 | "[input]" | "[phrase]" (HIGH/MED/LOW) | [Topic] | Trigger>Condition(default)>Redirect | var1=cleared (topic exited) | "[response]" | CONFORMS \| DEVIATES[CS-SPEC-NN] | CLEAN \| FOUND[term] |
[...all turns. All three columns populated. No turns skipped.]

GAP_CLOSURE_VERDICT: CLOSED | OPEN [Gap-R4-01: per-turn SPEC_CONFORMANCE, SESSION_STATE,
PROHIBITED_TERM_SCAN on every row; session state tracked at every transition]

### Phase 1-D: Defect Matrix
[Gap-R4-02 closure. All four classes. DEFECT_VERDICT enum.]

| Defect Class | DEFECT_VERDICT | Evidence | Reproduction |
|-------------|---------------|----------|-------------|
| Dead end | FOUND \| CONFIRMED_ABSENT | [evidence or scope] | [seq/N/A] |
| Infinite loop | FOUND \| CONFIRMED_ABSENT | [evidence or scope] | [cycle/N/A] |
| Trigger phrase collision | FOUND \| CONFIRMED_ABSENT | [evidence + disambiguation if FOUND] | [phrase->2+topics/N/A] |
| Missing fallback | FOUND \| CONFIRMED_ABSENT | [evidence or scope] | [input->no default/N/A] |

GAP_CLOSURE_VERDICT: CLOSED | OPEN [Gap-R4-02: all four defect classes,
DEFECT_VERDICT enum, disambiguation strategy where COLLISION FOUND]

### Phase 1-E: Fallback Chain + Adversarial Injection
[Gap-R4-03,04 closure. Fallback traced to terminal. Adversarial injected.]

Fallback: "[phrase]" -> CS-SPEC-07 -> [steps] -> Terminal: [escalation|end|loop].
FALLBACK_QUALITY: COMPLETE | LOOPS | TRUNCATED.

Adversarial: [type]. Injected T-[NN], state [snapshot]. Path: [trace]. Impact: [vars].
ADVERSARIAL_OUTCOME: GRACEFUL | BRITTLE | SILENT_FAILURE.

GAP_CLOSURE_VERDICT: CLOSED | OPEN [Gap-R4-03: fallback to terminal.
Gap-R4-04: adversarial injection with ADVERSARIAL_OUTCOME enum.]

### Phase 1-F: Coverage + Amendments
[Gap-R4-05 + Gap-R6-02 closure.]

| Metric | Visited | Total | Ratio |
|--------|---------|-------|-------|
| Topics | [N] | [Total] | [pct]% |
| Trigger phrases | [N] | [Total] | [pct]% |

Amendments: [all FOUND and DEVIATES with trigger sequence, fix, P1|P2|P3]

Developer declaration: Sub-sections 1-A through 1-F complete.
The Auditor SHALL NOT have begun Phase 2 before this declaration.
GAP_CLOSURE_VERDICT: CLOSED | OPEN [Gap-R4-05: quantified coverage ratios present.
Gap-R6-02: gap-closure annotations declared in each sub-section per C-17.]

---

## PHASE 2: AUDITOR POST-PRODUCTION AUDIT
[Compliance Auditor speaks. The Auditor SHALL NOT have produced any Phase 2 output before
the Developer's completion declaration in Phase 1-F. Read Phase 1 (sub-sections 1-A
through 1-F) as a completed artifact. Developer role has ended. Apply Phase 0 schema.]

Per-turn re-annotation:
| Turn | Dev SPEC_CONFORMANCE | Aud SPEC_CONFORMANCE | Dev PROHIBITED_TERM_SCAN | Aud PROHIBITED_TERM_SCAN | DISCREPANCY |
|------|---------------------|---------------------|--------------------------|--------------------------|-------------|
| T-01 | [from 1-C] | CONFORMS \| DEVIATES[CS-SPEC-NN] | [from 1-C] | CLEAN \| FOUND[term] | NONE \| FOUND[...] |
[...one row per turn from 1-C]

Prohibited term body scan (Phase 1, all sub-sections, full text):
  intent:YES\|NO [1-x/N/A]. dialog:YES\|NO. slot:YES\|NO. NLU:YES\|NO.
  utterance:YES\|NO. chatbot:YES\|NO. handoff:YES\|NO. context:YES\|NO. bot:YES\|NO.
PROHIBITED_TERM_BODY_SCAN: CLEAN | FOUND[list]

Gap-closure audit (C-17 verification):
| Sub-section | Gap Tag | Developer VERDICT | Auditor Verification |
|-------------|---------|-------------------|----------------------|
| 1-A | Gap-R6-01 | CLOSED \| OPEN | CLOSED \| OPEN \| REGRESSION |
| 1-B | Gap-R5-01 | CLOSED \| OPEN | CLOSED \| OPEN \| REGRESSION |
| 1-C | Gap-R4-01 | CLOSED \| OPEN | CLOSED \| OPEN \| REGRESSION |
| 1-D | Gap-R4-02 | CLOSED \| OPEN | CLOSED \| OPEN \| REGRESSION |
| 1-E | Gap-R4-03,04 | CLOSED \| OPEN | CLOSED \| OPEN \| REGRESSION |
| 1-F | Gap-R4-05, Gap-R6-02 | CLOSED \| OPEN | CLOSED \| OPEN \| REGRESSION |

Auditor summary:
  Contract: Phase 0 (all fields, all enum values, gap-closure contract)
  Turns audited: [N]. DISCREPANCY: [N] -- SPEC: [N]; PROHIBITED: [N].
  GAP_CLOSURE_REGRESSIONS: [N] | NONE
  AUDIT_VERDICT: CLEAN | ISSUES_FOUND
```

---

```json
{"top_predicted": 100, "diagnostic_bets": ["V-01: C-12 without hard boundary marker -- resolves R5 V-03 unresolved bet", "V-05: C-12 in minimal architecture + normative-only boundary -- cross-checks V-01 resolution"], "new_patterns": ["Topology invariants as C-16 enhancement: INVARIANT-TOPO-NN pre-commitment in Phase 0-D creates falsifiable CONFIRMED_ABSENT defect verdicts (V-03, V-04)", "Gap-closure as primary structure: organizing around CS Test Bot gaps (Gap-CS-01 through Gap-CS-07) makes C-17 the structural backbone, not an annotation layer (V-02)", "Boundary marker isolation: V-01 and V-05 test whether SHALL NOT normative gating alone satisfies C-12 without hard === separator"]}
```
