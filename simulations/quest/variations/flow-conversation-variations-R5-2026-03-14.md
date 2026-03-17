Round 5 variations written to `simulations/quest/variations/flow-conversation-variations-R5-2026-03-14.md`.

---

## Round 5 — flow-conversation Variations

**Three new axes explored:**

| V | Axis | Key innovation | Predicted |
|---|------|----------------|-----------|
| V-01 | **Role Sequence** (bidirectional pre-contracts) | Developer declares domain invariants in Phase 0-D *before* Auditor declares assertion contract in Phase 0-A — symmetric pre-commitment, neither role can reverse-engineer criteria | 100 |
| V-02 | **Lifecycle Emphasis** (minimal 3-phase) | All Developer output in one phase with sub-sections; FALLBACK GATE / ADVERSARIAL GATE / DEFECT GATE removed — tests whether those intermediate gates are load-bearing or cosmetic | 100 |
| V-03 | **Phrasing Register** (formal spec language) | SHALL/MUST throughout; same 7-phase structure as R4 V-05 — cleanest single-axis phrasing fungibility test | 100 |
| V-04 | Role Seq + Inertia Framing | Gap analysis preamble (what CS Test Bot misses) + bidirectional contracts + per-phase gap closure tracking via `GAP_CLOSURE_VERDICT` | 100 |
| V-05 | Full Synthesis + Topology Invariants | New C-16 candidate: Developer pre-commits to design-time structural invariants (INVARIANT-TOPO-NN); Auditor adds `INVARIANT_CONFORMANCE` as mandatory per-turn column; distinct from runtime CS-SPEC checks | 100 |

**Two diagnostic bets in R5:**
- **V-02**: If it hits 100, intermediate gates are cosmetic. If C-06 or C-09 miss, those gates are load-bearing — parallel finding to R4's C-12 discovery.
- **V-03**: If `SHALL NOT begin Phase 7` is weaker than imperative `=== DEVELOPER ARTIFACT COMPLETE ===`, C-12 will miss — revealing that the *boundary marker* is more load-bearing than the *sequencing instruction*.

**V-05 C-16 pattern:** Topology invariant declarations — Developer pre-commits to design-time structural assertions before trace (distinct from CS-SPEC runtime rules); Auditor enforces `INVARIANT_CONFORMANCE` as a mandatory fourth column on every turn. The invariant summary table in Phase 2 cross-checks all four pre-committed claims against the trace evidence.
loper pre-commits to design-time
structural assertions (e.g., "all condition nodes have default branches") before the trace.
These are distinct from CS-SPEC runtime rules. If this produces measurably better structural
defect detection, it warrants promotion to a new criterion.

---

## V-01: Role Sequence — Bidirectional Pre-Contracts

**Axis:** Role Sequence — Developer declares a Domain Contract (Phase 0-D) first, then Auditor
declares Assertion Contract (Phase 0-A). Both roles pre-commit before any trace begins.

**Hypothesis:** R4 contract-first has only the Auditor pre-committing. V-01 asks: what if the
Developer also pre-commits? Forcing the Developer to articulate formal domain invariants
before the trace prevents retroactive adjustment of invariant claims. The Auditor then
declares its assertion contract referencing the Developer's domain contract. Symmetric
pre-commitment: neither role can reverse-engineer criteria post-hoc. Tests whether
Developer pre-commitment adds structural independence beyond Auditor-only contract-first.

```
You are running /flow:conversation for topic "{topic}".

Read: simulations/flow/conversation/{topic}-conversation-{date}.md if it exists.
Read: any signal artifacts in simulations/ relevant to "{topic}".

Four roles execute in strict sequence:
  (1) Copilot Studio Developer (Phase 0-D: domain contract)
  (2) Compliance Auditor (Phase 0-A: assertion contract)
  (3) Copilot Studio Developer (Phases 1-5: trace and artifacts)
  (4) Compliance Auditor (Phase 6: audit)

Phases 0-D and 0-A are pre-commitment phases -- no trace work begins until both complete.
The Developer may not alter the Auditor's Phase 0-A contract.
The Auditor may not alter the Developer's Phase 0-D contract.
All phases are gates. Complete each phase fully before advancing.

Use Copilot Studio vocabulary exclusively:
  Topics, Trigger phrases, Conditions, Fallback topics, Escalation nodes, Session variables,
  Topic redirects, Actions, Generative answers, Knowledge sources, End of conversation nodes.
Do not use: intent, dialog, slot, NLU, utterance (use "user input"), chatbot (use "agent"),
  handoff (use "escalation"), context (use "session variables"), bot (use "agent").

---

## PHASE 0-D: DEVELOPER DOMAIN CONTRACT
[Copilot Studio Developer speaks first. Declare the domain contract before any trace begins.
The Auditor will reference this contract in Phase 0-A. You are binding yourself to these
claims before observing what the trace produces.]

### Agent Topology
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

### Topology Spec
  CS-SPEC-01: Trigger phrase matching activates topic above confidence threshold.
  CS-SPEC-02: Topic-scoped session variables cleared at topic boundary.
  CS-SPEC-03: Condition nodes require a default branch.
  CS-SPEC-04: Redirect nodes do not carry topic-scoped variables.
  CS-SPEC-05: End of conversation nodes terminate the session.
  CS-SPEC-06: Escalation nodes open human agent session.
  CS-SPEC-07: Fallback topic activates when no trigger phrase exceeds threshold.

### Session Variable Invariants (Developer pre-commits before trace)
  INVARIANT-SV-01: [VarName] persists across all turns within [Topic] and clears at exit.
  INVARIANT-SV-02: [VarName] is global-scoped and survives all topic transitions.
  [One invariant per session variable declared above.]

### Topic Exit Invariants (Developer pre-commits before trace)
  INVARIANT-EXIT-01: Every topic exits to a redirect node, escalation node, or end of
    conversation node -- no topic has a path that terminates without a defined exit.
  INVARIANT-EXIT-02: No topic redirect creates a cycle without an intervening condition
    node that carries a fallback exit path.

DOMAIN CONTRACT GATE: Topology declared. CS-SPEC rules stated. Session variable invariants
committed. Topic exit invariants committed. Developer may not alter this contract in later
phases. Advance to Phase 0-A.

---

## PHASE 0-A: AUDITOR ASSERTION CONTRACT
[Compliance Auditor speaks. Read the Developer's Phase 0-D domain contract. Declare the
complete verification contract before any Developer trace work begins. Reference the
Developer's invariants where relevant. The Developer must use exactly these assertion
fields and enum values in Phases 1-5.]

### Assertion Schema (Developer must use these exact fields in Phases 1-5)

Per-turn Trace Table fields (mandatory on every row):
  SPEC_CONFORMANCE: CONFORMS | DEVIATES[CS-SPEC-NN: description]
  INVARIANT_STATUS: HOLDS | VIOLATED[INVARIANT-NN: description]
  PROHIBITED_TERM_SCAN: CLEAN | FOUND[term at exact location]

Defect matrix verdict (mandatory on all four rows):
  DEFECT_VERDICT: FOUND | CONFIRMED_ABSENT
  -- CONFIRMED_ABSENT: must state topics checked as scope.
  -- FOUND: must state reproduction sequence (exact inputs -> failure mode).
  -- Free-text in DEFECT_VERDICT cell is a contract violation.

Sub-section terminal verdicts:
  FALLBACK_QUALITY: COMPLETE | LOOPS | TRUNCATED
  ADVERSARIAL_OUTCOME: GRACEFUL | BRITTLE | SILENT_FAILURE

Auditor-only fields (Phase 6 only -- Developer does not produce these):
  AUDITOR_SPEC_CONFORMANCE: CONFORMS | DEVIATES[CS-SPEC-NN: description]
  AUDITOR_INVARIANT_STATUS: HOLDS | VIOLATED[INVARIANT-NN: description]
  AUDITOR_PROHIBITED_TERM_SCAN: CLEAN | FOUND[term at exact location]
  DISCREPANCY: NONE | FOUND[SPEC_CONFORMANCE] | FOUND[INVARIANT_STATUS] | FOUND[PROHIBITED_TERM] | FOUND[MULTIPLE: list]

### Prohibited Terms
  Prohibited: intent | dialog | slot | NLU | utterance | chatbot | handoff | context | bot
  Auditor will scan all Developer output (Phases 1-5) for these terms in Phase 6.

### Audit Scope (Auditor commits before seeing any Developer trace)
  Phase 2 Trace Table: every row for SPEC_CONFORMANCE, INVARIANT_STATUS, PROHIBITED_TERM_SCAN.
  Phase 3 Defect Matrix: all four rows for DEFECT_VERDICT + evidence quality.
  Phase 4: FALLBACK_QUALITY + terminal state reached; ADVERSARIAL_OUTCOME present.
  Phase 5: coverage ratios present.
  Phases 1-5 full text: prohibited term body scan, all 9 terms.

ASSERTION CONTRACT GATE: Schema declared (all fields, all enum values). Prohibited terms
listed. Audit scope committed. Developer domain contract acknowledged. Developer may
begin Phase 1. Neither role may alter Phase 0-D or Phase 0-A contracts.

---

## PHASE 1: AGENT TOPOLOGY
[Copilot Studio Developer speaks. Topology already declared in Phase 0-D domain contract.
Phase 1 confirms the agent is ready and states coverage scope for the trace.]

Coverage confirmation: [N] of [Total] topics will be visited in this simulation ([pct]%).
Topics visited: [Topic-A], [Topic-B], ...
Topics not visited this simulation: [Topic-X], ... / [none -- full coverage]

SETUP GATE: Coverage confirmed. Phase 0-D topology is the authoritative topology reference.
Advance to Phase 2.

---

## PHASE 2: CONVERSATION TRACE TABLE
[Copilot Studio Developer speaks. Walk every turn. Use Phase 0-A assertion schema exactly.
All three assertion columns are mandatory on every row. A blank cell is a contract violation.
INVARIANT_STATUS checks Phase 0-D session variable and exit invariants at every relevant turn.]

| Turn | User Input | Trigger Phrase Matched | Topic | Nodes Executed | Session Variables (name=value; scope; changed/held/cleared) | Agent Response | SPEC_CONFORMANCE | INVARIANT_STATUS | PROHIBITED_TERM_SCAN |
|------|-----------|----------------------|-------|----------------|-------------------------------------------------------------|---------------|-----------------|-----------------|---------------------|
| T-01 | "[input]" | "[phrase]" (HIGH/MED/LOW) | [Topic-A] | Trigger>Message>Question | var1=X (topic-scoped, changed); var2=Y (global, held) | "[response]" | CONFORMS \| DEVIATES[CS-SPEC-NN: description] | HOLDS \| VIOLATED[INVARIANT-NN: description] | CLEAN \| FOUND[term] |
| T-02 | "[input]" | "[phrase]" (HIGH/MED/LOW) | [Topic-B] | Trigger>Condition(branch=label)>Redirect | var1=cleared (topic-scoped, topic exited); var2=Z (global, held) | "[response]" | CONFORMS \| DEVIATES[CS-SPEC-NN: description] | HOLDS \| VIOLATED[INVARIANT-NN: description] | CLEAN \| FOUND[term] |
[...continue for all turns. Blank cells not permitted.]

TRACE GATE: All [N] turns present. SPEC_CONFORMANCE, INVARIANT_STATUS, PROHIBITED_TERM_SCAN
populated on every row (Phase 0-A contract). Session state tracked at every transition.
Advance to Phase 3.

---

## PHASE 3: DEFECT MATRIX
[All four rows required. Use Phase 0-A DEFECT_VERDICT enum only. CONFIRMED_ABSENT requires
scope statement. FOUND requires reproduction sequence. Reference Phase 0-D invariants
where defects relate to invariant violations.]

| Defect Class | DEFECT_VERDICT | Evidence | Reproduction Sequence |
|-------------|---------------|----------|----------------------|
| Dead end | FOUND \| CONFIRMED_ABSENT | [FOUND: Turn T-NN, topic, node has no outgoing path, INVARIANT-EXIT-01 violation. CONFIRMED_ABSENT: "All [N] topic exits route to redirect, escalation, or end node. Exit paths: [list]. INVARIANT-EXIT-01 holds."] | [FOUND: "[input-1]" -> "[input-2]" -> dead state. CONFIRMED_ABSENT: N/A] |
| Infinite loop | FOUND \| CONFIRMED_ABSENT | [FOUND: loop path, condition, INVARIANT-EXIT-02 violation. CONFIRMED_ABSENT: "Topic redirect graph acyclic. Redirect map: [A->B], [C->terminal]. INVARIANT-EXIT-02 holds."] | [FOUND: cycle sequence. CONFIRMED_ABSENT: N/A] |
| Trigger phrase collision | FOUND \| CONFIRMED_ABSENT | [FOUND: phrase + competing topics + confidence scores + disambiguation strategy (entity enrichment / condition ordering / trigger phrase refactor) + rationale. CONFIRMED_ABSENT: "All [N] phrases resolve single topic; runner-up below 0.4."] | [FOUND: "[phrase]" -> both Topic-A and Topic-B activate. CONFIRMED_ABSENT: N/A] |
| Missing fallback | FOUND \| CONFIRMED_ABSENT | [FOUND: topic + condition node + unhandled branch + CS-SPEC-03 violation. CONFIRMED_ABSENT: "All condition nodes in [N] topics carry default branch. Confirmed: [list]."] | [FOUND: "[input]" at condition node without default -> silent routing. CONFIRMED_ABSENT: N/A] |

DEFECT GATE: All four rows use Phase 0-A enum. Evidence + reproduction present where FOUND.
Scope + invariant reference stated where CONFIRMED_ABSENT. Advance to Phase 4.

---

## PHASE 4: FALLBACK CHAIN + ADVERSARIAL

### Fallback Chain Trace
[Walk one complete fallback path to terminal. Reference CS-SPEC-07. Use Phase 0-A enum.]

Unrecognized user input: "[phrase matching no trigger phrase]"
Step 1: [N] topics evaluated, 0 match above threshold -> CS-SPEC-07 activates -> [Fallback topic]
Step 2: [node type] -- [action]
...
Terminal state: [escalation node opened / end of conversation node reached / loop detected]
FALLBACK_QUALITY: COMPLETE | LOOPS | TRUNCATED

FALLBACK GATE: Path traced to terminal. Phase 0-A enum used. Advance to adversarial.

### Adversarial Injection
[One scenario: unexpected mid-flow input, topic switch during active question node, or
session timeout. Use Phase 0-A enum. Show session variable impact.]

Scenario type: [mid-flow topic switch / unexpected input / session timeout]
Scenario: "[description]"
Injected at: Turn T-[NN], after [session state snapshot]
Node path: [trace from injection through agent response]
Session variable impact: [what changes, what is corrupted or lost]
Agent response: "[text]"
ADVERSARIAL_OUTCOME: GRACEFUL | BRITTLE | SILENT_FAILURE

ADVERSARIAL GATE: Scenario described. Node path traced. Phase 0-A enum used. Advance to Phase 5.

---

## PHASE 5: COVERAGE + AMENDMENTS

Coverage:
| Metric | Visited | Total (estimated) | Ratio |
|--------|---------|-------------------|-------|
| Topics | [N] | [Total] | [N/Total] ([pct]%) |
| Trigger phrases exercised | [N] | [Total] | [N/Total] ([pct]%) |

Invariant status summary (cross-references Phase 0-D):
| Invariant | Status across trace | Turns / topics where VIOLATED |
|-----------|--------------------|-----------------------------|
| INVARIANT-SV-01 | HOLDS \| VIOLATED | [T-NN list / N/A] |
| INVARIANT-SV-02 | HOLDS \| VIOLATED | [T-NN list / N/A] |
| INVARIANT-EXIT-01 | HOLDS \| VIOLATED | [topic / N/A] |
| INVARIANT-EXIT-02 | HOLDS \| VIOLATED | [topic / N/A] |

Amendments (all FOUND defects, all DEVIATES and VIOLATED rows from Phase 2):
- **CS-SPEC-NN / INVARIANT-NN:** [violation description]
  Trigger sequence: "[input-1]" -> "[input-2]" -> [failure mode]
  Proposed fix: [specific change]
  Priority: P1 (breaks flow) / P2 (degrades experience) / P3 (minor)

COVERAGE GATE: Ratios reported. Invariant summary complete. All FOUND/DEVIATES/VIOLATED items
have amendments. Developer artifact complete.

---

## === DEVELOPER ARTIFACT COMPLETE (Phases 0-D through 5) ===

---

## === AUDITOR NOW READS THE COMPLETED ARTIFACT ===

---

## PHASE 6: AUDITOR APPLIES ASSERTION CONTRACT
[Compliance Auditor speaks. Read the Developer Artifact (Phases 0-D through 5) as a finished
document. Apply Phase 0-A assertion contract. Developer role has ended -- do not consult it.
Re-annotate every row from Phase 2 independently, including AUDITOR_INVARIANT_STATUS.]

Input document: Developer Artifact, Phase 2 Trace Table rows T-01 through T-[N].

| Turn | Dev SPEC_CONFORMANCE | Aud SPEC_CONFORMANCE | Dev INVARIANT_STATUS | Aud INVARIANT_STATUS | Dev PROHIBITED_TERM_SCAN | Aud PROHIBITED_TERM_SCAN | DISCREPANCY |
|------|---------------------|---------------------|---------------------|---------------------|--------------------------|--------------------------|-------------|
| T-01 | [from Phase 2] | CONFORMS \| DEVIATES[CS-SPEC-NN: description] | [from Phase 2] | HOLDS \| VIOLATED[INVARIANT-NN: description] | [from Phase 2] | CLEAN \| FOUND[term] | NONE \| FOUND[SPEC_CONFORMANCE] \| FOUND[INVARIANT_STATUS] \| FOUND[PROHIBITED_TERM] \| FOUND[MULTIPLE: list] |
[...one row per turn from Phase 2]

Prohibited term body scan (Phases 0-D through 5 full text):
| Term | Present | Location |
|------|---------|----------|
| intent | YES \| NO | [Phase N / N/A] |
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
  Contracts applied: Phase 0-D (domain + invariants) + Phase 0-A (assertion schema)
  Turns audited: [N]
  DISCREPANCY cases: [N]
    - False-clean SPEC_CONFORMANCE: [N]
    - False-clean INVARIANT_STATUS: [N]
    - False-clean PROHIBITED_TERM_SCAN: [N]
  Invariant violations confirmed: [N] / [Total declared]
  AUDIT_VERDICT: CLEAN | ISSUES_FOUND
```

---

## V-02: Lifecycle Emphasis — Minimal 3-Phase Architecture

**Axis:** Lifecycle Emphasis — maximum compression. All Developer output in a single Phase 1
with named sub-sections but no intermediate phase gates. Tests whether FALLBACK GATE,
ADVERSARIAL GATE, and DEFECT GATE are load-bearing for recommended/aspirational criteria.

**Hypothesis:** R4 V-05 had 7 named phases and 5 intermediate Developer-side gates. V-02 keeps
only the structurally load-bearing boundary: Phase 0 (Auditor contract) must precede Phase 1
(all Developer output) and Phase 2 (Auditor audit) must follow Phase 1. The hard
`=== DEVELOPER ARTIFACT COMPLETE ===` boundary is preserved for C-12. Everything else is
compressed into sub-sections within Phase 1. If all criteria pass, intermediate gates are
cosmetic. If C-06, C-08, or C-09 fail, those specific gates are load-bearing -- parallel
finding to R4's C-12 gate discovery.

```
You are running /flow:conversation for topic "{topic}".

Read: simulations/flow/conversation/{topic}-conversation-{date}.md if it exists.
Read: any signal artifacts in simulations/ relevant to "{topic}".

Three phases execute in strict sequence:
  Phase 0: Compliance Auditor (assertion contract)
  Phase 1: Copilot Studio Developer (all trace and analysis)
  Phase 2: Compliance Auditor (audit)

Phase 0 must complete before Phase 1 begins.
Phase 1 must complete before Phase 2 begins.
The boundary between Phase 1 and Phase 2 is load-bearing -- Phase 2 reads Phase 1
as a completed artifact. Do not begin Phase 2 while producing Phase 1.

Use Copilot Studio vocabulary exclusively:
  Topics, Trigger phrases, Conditions, Fallback topics, Escalation nodes, Session variables,
  Topic redirects, Actions, Generative answers, Knowledge sources, End of conversation nodes.
Do not use: intent, dialog, slot, NLU, utterance (use "user input"), chatbot (use "agent"),
  handoff (use "escalation"), context (use "session variables"), bot (use "agent").

---

## PHASE 0: AUDITOR ASSERTION CONTRACT
[Compliance Auditor speaks. Declare the complete assertion contract before any Developer
output begins. This contract is binding -- the Developer must use exactly these fields
and enum values in Phase 1.]

### Topology Spec
  CS-SPEC-01: Trigger phrase matching activates topic above confidence threshold.
  CS-SPEC-02: Topic-scoped session variables cleared at topic boundary.
  CS-SPEC-03: Condition nodes require a default branch.
  CS-SPEC-04: Redirect nodes do not carry topic-scoped variables.
  CS-SPEC-05: End of conversation nodes terminate the session.
  CS-SPEC-06: Escalation nodes open human agent session.
  CS-SPEC-07: Fallback topic activates when no trigger phrase exceeds threshold.

### Prohibited Terms
  Prohibited: intent | dialog | slot | NLU | utterance | chatbot | handoff | context | bot

### Assertion Schema

Per-turn Trace Table columns (mandatory on every row; blank cell = structural violation):
  SPEC_CONFORMANCE: CONFORMS | DEVIATES[CS-SPEC-NN: description]
  SESSION_STATE: [name=value (scope, changed/held/cleared) for each variable]
  PROHIBITED_TERM_SCAN: CLEAN | FOUND[term at exact location]

Defect matrix (all four rows):
  DEFECT_VERDICT: FOUND | CONFIRMED_ABSENT
  (CONFIRMED_ABSENT: scope required. FOUND: reproduction sequence required.
   Free-text in DEFECT_VERDICT is a violation.)

Terminal verdicts:
  FALLBACK_QUALITY: COMPLETE | LOOPS | TRUNCATED
  ADVERSARIAL_OUTCOME: GRACEFUL | BRITTLE | SILENT_FAILURE

Auditor-only (Phase 2):
  AUDITOR_SPEC_CONFORMANCE: CONFORMS | DEVIATES[CS-SPEC-NN: description]
  AUDITOR_PROHIBITED_TERM_SCAN: CLEAN | FOUND[term at exact location]
  DISCREPANCY: NONE | FOUND[SPEC_CONFORMANCE] | FOUND[PROHIBITED_TERM] | FOUND[BOTH]

CONTRACT GATE: Topology spec declared. Prohibited terms listed. Assertion schema declared
with all enum values. Developer may begin Phase 1.

---

## PHASE 1: DEVELOPER OUTPUT
[Copilot Studio Developer speaks. Complete all sub-sections in order. Use Phase 0 assertion
schema throughout. Do not begin Phase 2 until all sub-sections are complete.]

### 1-A: Agent Topology
Agent name: [Name or description]
Topics in graph: [N total]: [Topic-A], [Topic-B], ...
Trigger phrases:
  [Topic-A]: "[phrase-1]", "[phrase-2]"
  [Topic-B]: "[phrase-1]", "[phrase-2]"
Fallback topic: [Name / "System Fallback Topic" / "not configured"]
Escalation path: [Topic / "not configured"]
Session variables:
  [VarName]: scope=[topic-scoped / global], type=[Text/Number/Boolean], initial=[value / "unset"]
Coverage scope: [N] of [Total] topics ([pct]%).

### 1-B: Conversation Trace Table
[One row per turn. All three columns mandatory. Blank cells violate Phase 0 contract.]

| Turn | User Input | Trigger Phrase Matched | Topic | Nodes Executed | SESSION_STATE | Agent Response | SPEC_CONFORMANCE | PROHIBITED_TERM_SCAN |
|------|-----------|----------------------|-------|----------------|---------------|---------------|-----------------|---------------------|
| T-01 | "[input]" | "[phrase]" (HIGH/MED/LOW) | [Topic-A] | Trigger>Message>Question | var1=X (topic-scoped, changed); var2=Y (global, held) | "[response]" | CONFORMS \| DEVIATES[CS-SPEC-NN: description] | CLEAN \| FOUND[term] |
| T-02 | "[input]" | "[phrase]" (HIGH/MED/LOW) | [Topic-B] | Trigger>Condition(branch=label)>Redirect | var1=cleared (topic-scoped, topic ended); var2=Y (global, held) | "[response]" | CONFORMS \| DEVIATES[CS-SPEC-NN: description] | CLEAN \| FOUND[term] |
[...continue for all turns. No turns may be skipped or collapsed.]

### 1-C: Defect Matrix
| Defect Class | DEFECT_VERDICT | Evidence | Reproduction Sequence |
|-------------|---------------|----------|----------------------|
| Dead end | FOUND \| CONFIRMED_ABSENT | [evidence or scope statement] | [sequence / N/A] |
| Infinite loop | FOUND \| CONFIRMED_ABSENT | [evidence or scope statement] | [cycle / N/A] |
| Trigger phrase collision | FOUND \| CONFIRMED_ABSENT | [evidence + disambiguation strategy if FOUND / scope] | [sequence / N/A] |
| Missing fallback | FOUND \| CONFIRMED_ABSENT | [evidence or scope statement] | [sequence / N/A] |

### 1-D: Fallback Chain Trace
Unrecognized user input: "[phrase matching no trigger phrase]"
Step 1: [N] topics evaluated, 0 match above threshold -> CS-SPEC-07 -> [Fallback topic]
Step 2: [node type] -- [action]
...
Terminal state: [escalation node / end of conversation node / loop detected]
FALLBACK_QUALITY: COMPLETE | LOOPS | TRUNCATED

### 1-E: Adversarial Injection
Scenario: [mid-flow topic switch / unexpected input / session timeout]
Description: "[what happens]"
Injected at: Turn T-[NN], session state: [snapshot]
Node path: [trace from injection through response]
Session variable impact: [what changes or is lost]
Agent response: "[text]"
ADVERSARIAL_OUTCOME: GRACEFUL | BRITTLE | SILENT_FAILURE

### 1-F: Coverage + Amendments
Coverage:
| Metric | Visited | Total (estimated) | Ratio |
|--------|---------|-------------------|-------|
| Topics | [N] | [Total] | [N/Total] ([pct]%) |
| Trigger phrases exercised | [N] | [Total] | [N/Total] ([pct]%) |

Amendments (all FOUND defects and DEVIATES turns):
- **CS-SPEC-NN:** [violation description]
  Trigger sequence: "[input-1]" -> "[input-2]" -> [failure mode]
  Proposed fix: [specific change]
  Priority: P1 / P2 / P3

---

## === DEVELOPER ARTIFACT COMPLETE ===

---

## === AUDITOR NOW READS THE COMPLETED ARTIFACT ===

---

## PHASE 2: AUDITOR APPLIES CONTRACT
[Compliance Auditor speaks. Read Phase 1 as a finished document. Developer role has ended.
Apply Phase 0 assertion schema. Re-annotate every Trace Table row independently.]

| Turn | Dev SPEC_CONFORMANCE | Aud SPEC_CONFORMANCE | Dev PROHIBITED_TERM_SCAN | Aud PROHIBITED_TERM_SCAN | DISCREPANCY |
|------|---------------------|---------------------|--------------------------|--------------------------|-------------|
| T-01 | [from 1-B] | CONFORMS \| DEVIATES[CS-SPEC-NN: description] | [from 1-B] | CLEAN \| FOUND[term] | NONE \| FOUND[SPEC_CONFORMANCE] \| FOUND[PROHIBITED_TERM] \| FOUND[BOTH] |
[...one row per turn from 1-B]

Prohibited term body scan (Phase 1, all sub-sections):
| Term | Present | Location |
|------|---------|----------|
| intent | YES \| NO | [sub-section / N/A] |
| dialog | YES \| NO | [location / N/A] |
| slot | YES \| NO | [location / N/A] |
| NLU | YES \| NO | [location / N/A] |
| utterance | YES \| NO | [location / N/A] |
| chatbot | YES \| NO | [location / N/A] |
| handoff | YES \| NO | [location / N/A] |
| context | YES \| NO | [location / N/A] |
| bot | YES \| NO | [location / N/A] |
PROHIBITED_TERM_BODY_SCAN: CLEAN | FOUND[list]

Auditor summary:
  Contract applied: Phase 0 (all fields, all enum values)
  Turns audited: [N]
  DISCREPANCY cases: [N] -- SPEC_CONFORMANCE: [N]; PROHIBITED_TERM_SCAN: [N]
  AUDIT_VERDICT: CLEAN | ISSUES_FOUND
```

---

## V-03: Phrasing Register — Formal Specification Language

**Axis:** Phrasing Register — all instructions written as normative requirements using formal
specification language (SHALL, MUST, MAY). Same 7-phase structure as R4 V-05; only phrasing.

**Hypothesis:** R4's V-05 used imperative instructions ("walk every turn", "use Phase 0 enum").
RFC/ISO-style language ("the Developer SHALL produce one row per turn", "a blank cell SHALL
constitute a structural violation") addresses the model as a specification-compliant system
rather than an instruction-following assistant. Tests whether formal specification phrasing
achieves the same compliance rate as imperative phrasing. C-12 is the most sensitive: "the
Developer artifact SHALL be complete before the Auditor begins" uses a normative modal
rather than an imperative command -- the question is whether SHALL preserves the load-bearing
property that the R4 phase gate enforces.

```
SPECIFICATION: /flow:conversation simulation for topic "{topic}".

PRECONDITIONS: The Developer SHALL read simulations/flow/conversation/{topic}-conversation-{date}.md
if it exists, and any signal artifacts in simulations/ relevant to "{topic}", before beginning Phase 1.

AGENTS: Three agents are defined. Each agent SHALL operate exclusively within its designated phases.
  - Compliance Auditor: Phases 0 and 7.
  - Copilot Studio Developer: Phases 1 through 6.
  No agent SHALL perform operations assigned to another agent's phases.

VOCABULARY REQUIREMENT: The Developer's output SHALL use only Copilot Studio vocabulary:
  Permitted: Topics, Trigger phrases, Conditions, Fallback topics, Escalation nodes,
    Session variables, Topic redirects, Actions, Generative answers, Knowledge sources,
    End of conversation nodes.
  Prohibited: intent, dialog, slot, NLU, utterance (MUST use "user input"), chatbot
    (MUST use "agent"), handoff (MUST use "escalation"), context (MUST use "session
    variables"), bot (MUST use "agent").
  Developer output that contains a prohibited term SHALL be treated as a specification
  violation at the location where the term appears.

PHASE SEQUENCING: Phases SHALL complete in strictly ascending numerical order.
A phase SHALL NOT begin until all preceding phases are complete and gate conditions satisfied.
The Developer Artifact (Phases 1-6) SHALL be complete before the Auditor begins Phase 7.
This requirement is load-bearing -- the Auditor SHALL read Phase 1-6 as a finished document.

---

## PHASE 0: AUDITOR ASSERTION CONTRACT
[The Compliance Auditor SHALL execute Phase 0 before any Developer output begins.
The Auditor SHALL declare the complete verification contract. The Developer SHALL be bound
by this contract in all subsequent phases. The Auditor SHALL NOT produce trace content in Phase 0.]

### 0-A: Topology Specification
The Developer SHALL verify conformance against the following rules on every turn:
  CS-SPEC-01: Trigger phrase matching SHALL activate a topic above confidence threshold.
  CS-SPEC-02: Topic-scoped session variables SHALL be cleared at topic boundary.
  CS-SPEC-03: Condition nodes SHALL carry a default branch.
  CS-SPEC-04: Redirect nodes SHALL NOT carry topic-scoped variables.
  CS-SPEC-05: End of conversation nodes SHALL terminate the session.
  CS-SPEC-06: Escalation nodes SHALL open a human agent session.
  CS-SPEC-07: The fallback topic SHALL activate when no trigger phrase exceeds threshold.

### 0-B: Prohibited Term Registry
The Developer SHALL ensure the following terms do not appear in its output:
  intent | dialog | slot | NLU | utterance | chatbot | handoff | context | bot
The Auditor SHALL scan all Developer output for these terms in Phase 7.

### 0-C: Developer Assertion Schema
The Developer SHALL use the following field names and enum values in Phases 1-6.
Deviation from specified enum values SHALL constitute a schema violation.

Per-turn Trace Table columns (SHALL appear on every row; a blank cell SHALL constitute
a structural violation):
  SPEC_CONFORMANCE: CONFORMS | DEVIATES[CS-SPEC-NN: description]
    -- The value SHALL be one of the two options. Prose SHALL NOT appear in this field.
  PROHIBITED_TERM_SCAN: CLEAN | FOUND[term at exact location]
    -- The value SHALL be one of the two options.
  Session Variables: [name=value (scope, changed/held/cleared) per variable]
    -- This column SHALL show the state of every declared session variable after each turn.

Defect matrix verdict (SHALL appear on all four rows):
  DEFECT_VERDICT: FOUND | CONFIRMED_ABSENT
    -- CONFIRMED_ABSENT SHALL include an explicit scope statement.
    -- FOUND SHALL include a reproduction sequence (exact inputs -> failure mode).
    -- Qualified verdicts (e.g., "likely absent", "possibly FOUND") SHALL NOT be used.

Terminal verdicts:
  FALLBACK_QUALITY: COMPLETE | LOOPS | TRUNCATED    (Phase 4, mandatory)
  ADVERSARIAL_OUTCOME: GRACEFUL | BRITTLE | SILENT_FAILURE    (Phase 5, mandatory)

### 0-D: Auditor Assertion Schema
The Auditor SHALL use the following fields in Phase 7 ONLY.
The Developer SHALL NOT produce these fields.
  AUDITOR_SPEC_CONFORMANCE: CONFORMS | DEVIATES[CS-SPEC-NN: description]
  AUDITOR_PROHIBITED_TERM_SCAN: CLEAN | FOUND[term at exact location]
  DISCREPANCY: NONE | FOUND[SPEC_CONFORMANCE] | FOUND[PROHIBITED_TERM] | FOUND[BOTH]

AUDIT CONTRACT GATE: Topology specification declared. Prohibited term registry declared.
Developer assertion schema declared with all enum values. Auditor assertion schema declared.
The Compliance Auditor SHALL NOT produce any further output until Phase 7.
The Developer MAY begin Phase 1.

---

## PHASE 1: AGENT TOPOLOGY DECLARATION
[The Copilot Studio Developer SHALL execute Phase 1. The Developer SHALL declare the agent
topology before any trace begins.]

Agent name: [Name or description]
Topics in graph: [N total, all listed]:
  [Topic-A], [Topic-B], ...
Trigger phrases (SHALL list 2-3 per topic):
  [Topic-A]: "[phrase-1]", "[phrase-2]"
  [Topic-B]: "[phrase-1]", "[phrase-2]"
Fallback topic: [Name / "System Fallback Topic" / "not configured"]
Escalation path: [Topic / "not configured"]
Session variables:
  [VarName]: scope=[topic-scoped / global], type=[Text/Number/Boolean], initial=[value / "unset"]
Coverage scope: This simulation SHALL visit [N] of [Total] topics ([pct]%).

SETUP GATE: Topology declared. The Developer SHALL advance to Phase 2.

---

## PHASE 2: CONVERSATION TRACE TABLE
[The Copilot Studio Developer SHALL walk the conversation turn by turn. No turn SHALL be
skipped or collapsed. All three assertion columns SHALL be populated on every row. A blank
cell in any assertion column SHALL constitute a structural violation of Phase 0-C.]

| Turn | User Input | Trigger Phrase Matched | Topic | Nodes Executed | Session Variables (name=value; scope; changed/held/cleared) | Agent Response | SPEC_CONFORMANCE | PROHIBITED_TERM_SCAN |
|------|-----------|----------------------|-------|----------------|-------------------------------------------------------------|---------------|-----------------|---------------------|
| T-01 | "[input]" | "[phrase]" (HIGH/MED/LOW) | [Topic-A] | Trigger>Message>Question | var1=X (ts, changed); var2=Y (global, held) | "[response]" | CONFORMS \| DEVIATES[CS-SPEC-NN: description] | CLEAN \| FOUND[term] |
| T-02 | "[input]" | "[phrase]" (HIGH/MED/LOW) | [Topic-B] | Trigger>Condition(branch=label)>Redirect | var1=cleared (ts, topic ended); var2=Y (global, held) | "[response]" | CONFORMS \| DEVIATES[CS-SPEC-NN: description] | CLEAN \| FOUND[term] |
[...The Developer SHALL continue for all turns. No row SHALL be omitted.]

TRACE GATE: All [N] turns present. SPEC_CONFORMANCE populated on every row (Phase 0-C).
PROHIBITED_TERM_SCAN populated on every row (Phase 0-C). Session variables tracked.
The Developer SHALL advance to Phase 3.

---

## PHASE 3: DEFECT MATRIX
[The Developer SHALL produce all four rows. The Developer SHALL use the DEFECT_VERDICT enum
from Phase 0-C. A CONFIRMED_ABSENT verdict SHALL include an explicit scope statement.
A FOUND verdict SHALL include a reproduction sequence.]

| Defect Class | DEFECT_VERDICT | Evidence | Reproduction Sequence |
|-------------|---------------|----------|----------------------|
| Dead end | FOUND \| CONFIRMED_ABSENT | [FOUND: turn, topic, node. CONFIRMED_ABSENT: scope + all exit paths listed.] | [FOUND: input sequence -> dead state. CONFIRMED_ABSENT: N/A] |
| Infinite loop | FOUND \| CONFIRMED_ABSENT | [FOUND: cycle path + condition. CONFIRMED_ABSENT: scope + redirect map.] | [FOUND: cycle sequence. CONFIRMED_ABSENT: N/A] |
| Trigger phrase collision | FOUND \| CONFIRMED_ABSENT | [FOUND: phrase + competing topics + scores + disambiguation strategy (entity enrichment / condition ordering / trigger phrase refactor) + rationale. CONFIRMED_ABSENT: scope.] | [FOUND: ambiguous input -> dual activation. CONFIRMED_ABSENT: N/A] |
| Missing fallback | FOUND \| CONFIRMED_ABSENT | [FOUND: topic + condition node + missing branch + CS-SPEC-03. CONFIRMED_ABSENT: scope.] | [FOUND: input -> silent routing. CONFIRMED_ABSENT: N/A] |

DEFECT GATE: All four rows use Phase 0-C enum. Evidence + reproduction where FOUND.
Scope where CONFIRMED_ABSENT. The Developer SHALL advance to Phase 4.

---

## PHASE 4: FALLBACK CHAIN TRACE
[The Developer SHALL walk one complete fallback path to a terminal state. The Developer
SHALL reference CS-SPEC-07. The Developer SHALL NOT stop at the first fallback topic
activation -- the path SHALL continue to a terminal state (escalation node or end of
conversation node).]

Unrecognized user input: "[phrase matching no trigger phrase]"
Step 1: [N] topics evaluated, 0 match above threshold -> CS-SPEC-07 activates -> [Fallback topic]
Step 2: [node type] -- [action]
...
Terminal state: [escalation node opened / end of conversation node reached / loop detected]
FALLBACK_QUALITY: COMPLETE | LOOPS | TRUNCATED

FALLBACK GATE: Path traced to terminal. Phase 0-C enum used. The Developer SHALL advance
to Phase 5.

---

## PHASE 5: ADVERSARIAL INJECTION
[The Developer SHALL inject one adversarial scenario. The Developer SHALL choose one of:
unexpected mid-flow user input, topic switch during an active question node, or session
timeout mid-flow. The Developer SHALL use the Phase 0-C ADVERSARIAL_OUTCOME enum.]

Scenario type: [mid-flow topic switch / unexpected input / session timeout]
Description: "[what happens]"
Injected at: Turn T-[NN], after [session state snapshot]
Node path: [trace from injection through agent response]
Session variable impact: [what changes, what is lost or corrupted]
Agent response: "[text shown to user]"
ADVERSARIAL_OUTCOME: GRACEFUL | BRITTLE | SILENT_FAILURE

ADVERSARIAL GATE: Scenario described. Node path traced. Phase 0-C enum used. The Developer
SHALL advance to Phase 6.

---

## PHASE 6: COVERAGE + AMENDMENTS
[The Developer SHALL report quantified coverage ratios. The Developer SHALL provide amendments
for all FOUND defects and all DEVIATES rows from Phase 2.]

Coverage:
| Metric | Visited | Total (estimated) | Ratio |
|--------|---------|-------------------|-------|
| Topics | [N] | [Total] | [N/Total] ([pct]%) |
| Trigger phrases exercised | [N] | [Total] | [N/Total] ([pct]%) |

Amendments (SHALL address every FOUND defect and every DEVIATES row from Phase 2):
- **CS-SPEC-NN:** [violation description]
  Trigger sequence: "[input-1]" -> "[input-2]" -> [failure mode]
  Proposed fix: [specific change to topology, trigger phrases, or session variable scope]
  Priority: P1 (breaks flow) / P2 (degrades experience) / P3 (minor)

COVERAGE GATE: Ratios reported. All FOUND and DEVIATES items have amendments.
The Developer Artifact is complete.

---

## === DEVELOPER ARTIFACT COMPLETE (Phases 1-6) ===

---

## === AUDITOR NOW READS THE COMPLETED ARTIFACT ===

---

## PHASE 7: AUDITOR APPLIES CONTRACT
[The Compliance Auditor SHALL execute Phase 7. Phases 1-6 are a finished artifact.
The Auditor SHALL apply the Phase 0 contract. The Developer role has ended.
The Auditor SHALL re-annotate every row from Phase 2 independently using Phase 0-D fields.
The Auditor SHALL NOT consult the Developer.]

Input document: Developer Artifact, Phase 2 Trace Table rows T-01 through T-[N].

| Turn | Dev SPEC_CONFORMANCE | Aud SPEC_CONFORMANCE | Dev PROHIBITED_TERM_SCAN | Aud PROHIBITED_TERM_SCAN | DISCREPANCY |
|------|---------------------|---------------------|--------------------------|--------------------------|-------------|
| T-01 | [from Phase 2] | CONFORMS \| DEVIATES[CS-SPEC-NN: description] | [from Phase 2] | CLEAN \| FOUND[term] | NONE \| FOUND[SPEC_CONFORMANCE] \| FOUND[PROHIBITED_TERM] \| FOUND[BOTH] |
[...one row per turn. The Auditor SHALL NOT skip any row.]

Prohibited term body scan (Phases 1-6 full text):
| Term | Present in Developer output | Location |
|------|-----------------------------|----------|
| intent | YES \| NO | [Phase N / N/A] |
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
  Contract applied: Phase 0 (all normative requirements)
  Turns audited: [N]
  DISCREPANCY cases: [N] -- False-clean SPEC_CONFORMANCE: [N]; PROHIBITED_TERM_SCAN: [N]
  Prohibited term body scan: CLEAN | FOUND
  AUDIT_VERDICT: CLEAN | ISSUES_FOUND
```

---

## V-04: Role Sequence + Inertia Framing — Gap Analysis Against Status Quo

**Axes:** Role Sequence (bidirectional pre-contracts) + Inertia Framing (prominent gap analysis
against what CS Test Bot and manual walkthroughs miss).

**Hypothesis:** Before either pre-commitment contract, the Developer declares a Preamble
identifying what CS's built-in testing tools do NOT test (single-turn only, no session
state across topics, no confidence threshold modeling, no fallback chain completeness).
Each simulation phase is annotated with which gap it closes. The hypothesis: gap framing
motivates more thorough execution of the specific coverage paths that conventional testing
misses -- particularly C-06 (fallback chain completeness), C-09 (adversarial injection),
and C-08 (coverage metric). If gap framing improves these sections, framing is a quality
driver. If output is identical to unfamed variants, framing is cosmetic.

```
You are running /flow:conversation for topic "{topic}".

Read: simulations/flow/conversation/{topic}-conversation-{date}.md if it exists.
Read: any signal artifacts in simulations/ relevant to "{topic}".

---

## PREAMBLE: TESTING GAPS THIS SIMULATION CLOSES
[Copilot Studio Developer declares this preamble before any contract phases begin.
This gap analysis is part of the Developer's domain contract.]

**CS Test Bot gaps** (what the built-in Copilot Studio test tool does NOT verify):
  Gap-01: CS Test Bot tests topics in isolation. It does NOT track session state continuity
    across topic transitions -- a topic-scoped variable set in Topic-A may be silently
    cleared, retained, or corrupted when Topic-B activates. Multi-turn state corruption
    is invisible to CS Test Bot.
  Gap-02: CS Test Bot activates topics by direct trigger phrase match, bypassing the
    confidence scoring system. Trigger phrase collisions (two topics with overlapping
    phrases competing at runtime) do not surface in CS Test Bot output.
  Gap-03: CS Test Bot terminates when the topic completes. It does NOT trace the fallback
    chain to its terminal state -- whether an unrecognized input eventually reaches an
    escalation node or silently loops in the fallback topic.

**Manual walkthrough gaps:**
  Gap-04: Human reviewers check happy paths. Adversarial scenarios -- mid-flow topic
    switches, unexpected inputs during active question nodes, session timeouts -- require
    systematic injection that ad-hoc walkthroughs rarely perform.
  Gap-05: Manual review does not produce coverage ratios. Without topics-visited / total
    and trigger-phrases-exercised / total metrics, it is unknown what fraction of the
    topic graph has been exercised.

**This simulation closes all five gaps:**
  Phase 2 Trace Table: closes Gap-01 (session state column on every turn).
  Phase 3 Defect Matrix: closes Gap-02 (collision row with confidence scoring).
  Phase 4 Fallback Chain: closes Gap-03 (trace to terminal state required).
  Phase 4 Adversarial Injection: closes Gap-04 (one adversarial scenario injected).
  Phase 5 Coverage: closes Gap-05 (topics and trigger phrases visited / total).

PREAMBLE COMPLETE. Advance to Phase 0-D.

---

Four roles execute in strict sequence:
  (1) Copilot Studio Developer (Preamble + Phase 0-D: domain contract)
  (2) Compliance Auditor (Phase 0-A: assertion contract)
  (3) Copilot Studio Developer (Phases 1-5: trace and artifacts)
  (4) Compliance Auditor (Phase 6: audit)

All phases are gates. Developer may not alter Phase 0-A. Auditor may not alter Phase 0-D.

Use Copilot Studio vocabulary exclusively:
  Topics, Trigger phrases, Conditions, Fallback topics, Escalation nodes, Session variables,
  Topic redirects, Actions, Generative answers, Knowledge sources, End of conversation nodes.
Do not use: intent, dialog, slot, NLU, utterance (use "user input"), chatbot (use "agent"),
  handoff (use "escalation"), context (use "session variables"), bot (use "agent").

---

## PHASE 0-D: DEVELOPER DOMAIN CONTRACT
[Copilot Studio Developer. Declare domain contract. Reference gaps from Preamble when
declaring invariants.]

### Agent Topology
Agent name: [Name or description]
Topics in graph: [N total]: [Topic-A], [Topic-B], ...
Trigger phrases:
  [Topic-A]: "[phrase-1]", "[phrase-2]"
  [Topic-B]: "[phrase-1]", "[phrase-2]"
Fallback topic: [Name / "System Fallback Topic" / "not configured"]
Escalation path: [Topic / "not configured"]
Session variables:
  [VarName]: scope=[topic-scoped / global], type=[Text/Number/Boolean], initial=[value / "unset"]
Coverage scope: [N] of [Total] topics ([pct]%).

### Topology Spec
  CS-SPEC-01 through CS-SPEC-07 [as declared in prior rounds].

### Session Variable Invariants (pre-committed to close Gap-01)
  INVARIANT-SV-NN: [VarName] [scope behavior]. Gap-01 will be verified via this invariant.

### Topic Exit Invariants (pre-committed to close Gap-03)
  INVARIANT-EXIT-01: Every topic has at least one terminal exit path.
  INVARIANT-EXIT-02: No redirect creates an unconditional cycle.

DOMAIN CONTRACT GATE: Topology declared. Gaps cross-referenced. Invariants committed.
Advance to Phase 0-A.

---

## PHASE 0-A: AUDITOR ASSERTION CONTRACT
[Compliance Auditor. Read Developer Preamble and Phase 0-D. Declare assertion contract.
The gap analysis in the Preamble informs audit priorities -- gaps the Developer committed
to close are primary audit targets.]

### Topology Spec (from Phase 0-D)
  CS-SPEC-01 through CS-SPEC-07 as declared.

### Prohibited Terms
  Prohibited: intent | dialog | slot | NLU | utterance | chatbot | handoff | context | bot

### Assertion Schema

Per-turn Trace Table columns (mandatory; blank cell = violation):
  SPEC_CONFORMANCE: CONFORMS | DEVIATES[CS-SPEC-NN: description]
  SESSION_STATE: [name=value (scope, changed/held/cleared)] (Gap-01 closure evidence)
  PROHIBITED_TERM_SCAN: CLEAN | FOUND[term at exact location]

Defect matrix (all four rows):
  DEFECT_VERDICT: FOUND | CONFIRMED_ABSENT
  (Gap-02 closure: collision row MUST include confidence scores.)

Terminal verdicts:
  FALLBACK_QUALITY: COMPLETE | LOOPS | TRUNCATED    (Gap-03 closure)
  ADVERSARIAL_OUTCOME: GRACEFUL | BRITTLE | SILENT_FAILURE    (Gap-04 closure)

Auditor-only (Phase 6):
  AUDITOR_SPEC_CONFORMANCE: CONFORMS | DEVIATES[CS-SPEC-NN: description]
  AUDITOR_PROHIBITED_TERM_SCAN: CLEAN | FOUND[term at exact location]
  DISCREPANCY: NONE | FOUND[SPEC_CONFORMANCE] | FOUND[PROHIBITED_TERM] | FOUND[BOTH]

### Audit Priority (gap-informed)
  Primary targets: SESSION_STATE continuity (Gap-01), collision confidence scores (Gap-02),
    fallback terminal state (Gap-03), adversarial scenario (Gap-04), coverage ratios (Gap-05).

ASSERTION CONTRACT GATE: Schema declared. Gap priorities committed. Developer may begin Phase 1.

---

## PHASE 1: CONVERSATION TRACE TABLE
[Developer. Walk every turn. SESSION_STATE column closes Gap-01 -- show every variable
at every turn. All columns mandatory. Blank cell violates Phase 0-A contract.]

| Turn | User Input | Trigger Phrase Matched (confidence) | Topic | Nodes Executed | SESSION_STATE (name=value; scope; changed/held/cleared) | Agent Response | SPEC_CONFORMANCE | PROHIBITED_TERM_SCAN |
|------|-----------|-------------------------------------|-------|----------------|--------------------------------------------------------|---------------|-----------------|---------------------|
| T-01 | "[input]" | "[phrase]" (HIGH) | [Topic-A] | Trigger>Message>Question | var1=X (ts, changed); var2=Y (global, held) | "[response]" | CONFORMS \| DEVIATES[CS-SPEC-NN: description] | CLEAN \| FOUND[term] |
[...all turns. Blank cells violate Phase 0-A.]

TRACE GATE: All [N] turns present. SESSION_STATE demonstrates Gap-01 closure. All assertion
columns populated. Advance to Phase 2.

---

## PHASE 2: DEFECT MATRIX
[Closes Gap-02: trigger phrase collision row MUST include confidence scores. Use Phase 0-A enum.]

| Defect Class | DEFECT_VERDICT | Evidence | Reproduction Sequence |
|-------------|---------------|----------|----------------------|
| Dead end | FOUND \| CONFIRMED_ABSENT | [evidence + INVARIANT-EXIT-01 reference / scope] | [sequence / N/A] |
| Infinite loop | FOUND \| CONFIRMED_ABSENT | [evidence + INVARIANT-EXIT-02 / scope] | [cycle / N/A] |
| Trigger phrase collision | FOUND \| CONFIRMED_ABSENT | [FOUND: phrase + competing topics + confidence scores (Gap-02) + disambiguation (entity enrichment / condition ordering / trigger phrase refactor) + rationale. CONFIRMED_ABSENT: "All phrases single-topic; max runner-up score: [N] (Gap-02 verified)."] | [sequence / N/A] |
| Missing fallback | FOUND \| CONFIRMED_ABSENT | [evidence + CS-SPEC-03 / scope] | [sequence / N/A] |

DEFECT GATE: All four rows complete. Gap-02 referenced in collision row. Advance to Phase 3.

---

## PHASE 3: FALLBACK CHAIN + ADVERSARIAL

### Fallback Chain Trace (Gap-03 closure -- trace MUST reach terminal state)
Unrecognized user input: "[phrase]"
Step 1: [N] topics evaluated, 0 match -> CS-SPEC-07 -> [Fallback topic]
Step 2: [node type] -- [action]
...
Terminal state: [escalation node / end of conversation node / loop detected]
FALLBACK_QUALITY: COMPLETE | LOOPS | TRUNCATED
Gap-03 closure: [FALLBACK_QUALITY: COMPLETE confirms gap closed / LOOPS or TRUNCATED means gap remains open]

FALLBACK GATE: Terminal reached. Gap-03 closure stated. Advance to adversarial.

### Adversarial Injection (Gap-04 closure -- one scenario injected)
Scenario: [mid-flow topic switch / unexpected input / session timeout]
Description: "[what happens]"
Injected at: T-[NN] | Session state: [snapshot]
Node path: [trace]
Variable impact: [what changes or is lost]
Agent response: "[text]"
ADVERSARIAL_OUTCOME: GRACEFUL | BRITTLE | SILENT_FAILURE
Gap-04 closure: [adversarial scenario injected -- Gap-04 CLOSED]

ADVERSARIAL GATE: Scenario injected. Gap-04 closure stated. Advance to Phase 4.

---

## PHASE 4: COVERAGE + AMENDMENTS
[Gap-05 closure -- report quantified ratios.]

Coverage:
| Metric | Visited | Total (estimated) | Ratio | Gap-05 |
|--------|---------|-------------------|-------|--------|
| Topics | [N] | [Total] | [pct]% | CLOSED |
| Trigger phrases | [N] | [Total] | [pct]% | CLOSED |

Amendments (all FOUND defects and DEVIATES turns):
- **CS-SPEC-NN:** [violation]
  Trigger sequence: "[inputs]" -> [failure]
  Proposed fix: [change]
  Priority: P1 / P2 / P3

COVERAGE GATE: Gap-05 closed. All FOUND/DEVIATES items have amendments. Developer artifact complete.

---

## === DEVELOPER ARTIFACT COMPLETE ===

---

## === AUDITOR NOW READS THE COMPLETED ARTIFACT ===

---

## PHASE 5: AUDITOR APPLIES CONTRACT
[Compliance Auditor. Read Developer Artifact (Preamble through Phase 4) as finished document.
Developer role has ended. Apply Phase 0-A assertion contract. Re-annotate Phase 1 rows
independently. Verify gap closure claims.]

| Turn | Dev SPEC_CONFORMANCE | Aud SPEC_CONFORMANCE | Dev PROHIBITED_TERM_SCAN | Aud PROHIBITED_TERM_SCAN | DISCREPANCY |
|------|---------------------|---------------------|--------------------------|--------------------------|-------------|
| T-01 | [from Phase 1] | CONFORMS \| DEVIATES[CS-SPEC-NN: description] | [from Phase 1] | CLEAN \| FOUND[term] | NONE \| FOUND[SPEC_CONFORMANCE] \| FOUND[PROHIBITED_TERM] \| FOUND[BOTH] |
[...one row per turn]

Gap closure audit (Auditor independently verifies each gap):
| Gap | Developer Claim | Auditor Verification | GAP_CLOSURE_VERDICT |
|-----|----------------|---------------------|---------------------|
| Gap-01 | SESSION_STATE on every Phase 1 row | [confirms / finds row(s) missing] | CLOSED \| OPEN[turns] |
| Gap-02 | Collision row includes confidence scores | [confirms / finds missing score] | CLOSED \| OPEN |
| Gap-03 | FALLBACK_QUALITY: COMPLETE | [confirms terminal reached / finds truncation] | CLOSED \| OPEN |
| Gap-04 | ADVERSARIAL_OUTCOME present | [confirms scenario injected] | CLOSED \| OPEN |
| Gap-05 | Both coverage ratios present | [confirms / finds missing ratio] | CLOSED \| OPEN |

Prohibited term body scan (Preamble through Phase 4):
| Term | Present | Location |
|------|---------|----------|
| intent | YES \| NO | [location / N/A] |
| dialog | YES \| NO | [location / N/A] |
| slot | YES \| NO | [location / N/A] |
| NLU | YES \| NO | [location / N/A] |
| utterance | YES \| NO | [location / N/A] |
| chatbot | YES \| NO | [location / N/A] |
| handoff | YES \| NO | [location / N/A] |
| context | YES \| NO | [location / N/A] |
| bot | YES \| NO | [location / N/A] |
PROHIBITED_TERM_BODY_SCAN: CLEAN | FOUND[list]

Auditor summary:
  Turns audited: [N]
  DISCREPANCY cases: [N]
  Gap closures verified: [N] / 5
  AUDIT_VERDICT: CLEAN | ISSUES_FOUND
```

---

## V-05: Full Synthesis — Topology Invariant Declarations + Bidirectional Contract + Minimal Phases

**Axes:** Full synthesis exploring a potential new pattern: **Topology Invariant Declarations**.
Developer pre-declares formal, checkable topology invariants in Phase 0-D. Auditor adds
INVARIANT_CONFORMANCE as a mandatory Trace Table column. Minimal 4-phase structure
(bidirectional pre-contracts + Developer trace/artifacts + Auditor audit).

**Hypothesis and C-16 candidate:** CS-SPEC rules (CS-SPEC-01 through CS-SPEC-07) are runtime
behavioral rules -- they describe what SHOULD happen during execution. Topology invariants
are design-time structural assertions -- claims about properties the Developer asserts hold
for this specific agent before any runtime observation. Example: INVARIANT-TOPO-01 says "I
assert that all condition nodes in this agent have default branches" -- a pre-trace commitment
the Developer makes about the agent's structure. The trace then either confirms or refutes
each invariant. If the topology invariant declarations pattern produces better structural
defect detection (dead ends and missing fallbacks caught earlier, with explicit invariant
violation references), this pattern warrants promotion to C-16:
  "Topology invariant declarations: Developer pre-commits to design-time structural assertions
  before trace; Auditor includes INVARIANT_CONFORMANCE as mandatory per-turn column; per-turn
  invariant checks are distinct from CS-SPEC runtime rule checks."

```
You are running /flow:conversation for topic "{topic}".

Read: simulations/flow/conversation/{topic}-conversation-{date}.md if it exists.
Read: any signal artifacts in simulations/ relevant to "{topic}".

Four phases execute in strict sequence:
  Phase 0-D: Copilot Studio Developer (domain contract + topology invariants)
  Phase 0-A: Compliance Auditor (assertion contract)
  Phase 1: Copilot Studio Developer (trace table)
  Phase 2: Copilot Studio Developer (defects, fallback, adversarial, coverage, amendments)
  Phase 3: Compliance Auditor (audit)

Phases 0-D and 0-A are pre-commitment phases. No trace begins until both are complete.
Developer Artifact (Phases 1-2) must be complete before Auditor begins Phase 3.
Neither role may alter the other's pre-commitment contract.

Use Copilot Studio vocabulary exclusively:
  Topics, Trigger phrases, Conditions, Fallback topics, Escalation nodes, Session variables,
  Topic redirects, Actions, Generative answers, Knowledge sources, End of conversation nodes.
Do not use: intent, dialog, slot, NLU, utterance (use "user input"), chatbot (use "agent"),
  handoff (use "escalation"), context (use "session variables"), bot (use "agent").

---

## PHASE 0-D: DEVELOPER DOMAIN CONTRACT + TOPOLOGY INVARIANTS
[Copilot Studio Developer speaks first. Declare domain contract AND topology invariants
before any trace begins. Topology invariants are design-time structural assertions -- claims
about properties you assert hold for this specific agent's structure, independent of runtime
behavior. You are pre-committing to these claims before observing the trace. A topology
invariant violation discovered during the trace is a structural finding, not a runtime finding.]

### Agent Topology
Agent name: [Name or description]
Topics in graph: [N total]: [Topic-A], [Topic-B], ...
Trigger phrases (2-3 per topic):
  [Topic-A]: "[phrase-1]", "[phrase-2]"
  [Topic-B]: "[phrase-1]", "[phrase-2]"
Fallback topic: [Name / "System Fallback Topic" / "not configured"]
Escalation path: [Topic / "not configured"]
Session variables:
  [VarName]: scope=[topic-scoped / global], type=[Text/Number/Boolean], initial=[value / "unset"]
Coverage scope: [N] of [Total] topics ([pct]%).

### Runtime Spec Rules
  CS-SPEC-01: Trigger phrase matching activates topic above confidence threshold.
  CS-SPEC-02: Topic-scoped session variables cleared at topic boundary.
  CS-SPEC-03: Condition nodes require a default branch.
  CS-SPEC-04: Redirect nodes do not carry topic-scoped variables.
  CS-SPEC-05: End of conversation nodes terminate the session.
  CS-SPEC-06: Escalation nodes open human agent session.
  CS-SPEC-07: Fallback topic activates when no trigger phrase exceeds threshold.

### Topology Invariants (design-time pre-commitments -- declare before trace)
[Declare one invariant per structural property you assert holds for this agent's design.
These are STRUCTURAL claims about the agent's topology, not runtime behavioral rules.
The trace will either confirm or refute each invariant.]

  INVARIANT-TOPO-01: All condition nodes in this agent have a default branch.
    (Structural assertion -- not derivable from CS-SPEC-03 alone; commits to specific
    topology compliance before execution reveals whether it holds.)
  INVARIANT-TOPO-02: No topic redirect in this agent creates an unconditional cycle
    (a path that returns to the originating topic without an intervening condition node
    offering a fallback exit).
  INVARIANT-TOPO-03: All topic-scoped session variables are explicitly cleared or
    transferred at each topic boundary -- no accidental persistence.
  INVARIANT-TOPO-04: Every topic in this agent has at least one terminal exit path
    (escalation node or end of conversation node reachable from every node in the topic).
  [Add additional topology invariants relevant to this specific agent.]

DOMAIN CONTRACT GATE: Topology declared. Runtime spec rules stated. Topology invariants
pre-committed (design-time, before trace). Developer may not alter invariants in later phases.
Advance to Phase 0-A.

---

## PHASE 0-A: AUDITOR ASSERTION CONTRACT
[Compliance Auditor speaks. Read Phase 0-D. Declare complete assertion schema. Include
INVARIANT_CONFORMANCE as a mandatory per-turn Trace Table column -- this is distinct from
SPEC_CONFORMANCE (runtime rules) and checks the Developer's pre-committed topology invariants.]

### Prohibited Terms
  Prohibited: intent | dialog | slot | NLU | utterance | chatbot | handoff | context | bot

### Developer Assertion Schema (binding for Phases 1-2)

Per-turn Trace Table columns (mandatory on every row; blank cell = structural violation):
  SPEC_CONFORMANCE: CONFORMS | DEVIATES[CS-SPEC-NN: description]
    -- Checks runtime behavioral rules (CS-SPEC-01 through CS-SPEC-07).
  INVARIANT_CONFORMANCE: HOLDS | VIOLATED[INVARIANT-TOPO-NN: description]
    -- Checks design-time topology invariants from Phase 0-D.
    -- HOLDS when no Phase 0-D invariant is testable at this turn (e.g., no condition
       node executed, no topic boundary crossed). State reason: "HOLDS [no invariant
       testable this turn]".
    -- VIOLATED when the turn reveals a topology invariant is false. Cite specific
       INVARIANT-TOPO-NN and describe the violation.
  SESSION_STATE: [name=value (scope, changed/held/cleared) per variable]
  PROHIBITED_TERM_SCAN: CLEAN | FOUND[term at exact location]

Defect matrix (all four rows, Phase 2):
  DEFECT_VERDICT: FOUND | CONFIRMED_ABSENT
  (Defect evidence should reference Phase 0-D invariants where applicable --
   e.g., a dead end finding should reference INVARIANT-TOPO-04 violation.)

Terminal verdicts (Phase 2):
  FALLBACK_QUALITY: COMPLETE | LOOPS | TRUNCATED
  ADVERSARIAL_OUTCOME: GRACEFUL | BRITTLE | SILENT_FAILURE

### Auditor Assertion Schema (Phase 3 only)
  AUDITOR_SPEC_CONFORMANCE: CONFORMS | DEVIATES[CS-SPEC-NN: description]
  AUDITOR_INVARIANT_CONFORMANCE: HOLDS | VIOLATED[INVARIANT-TOPO-NN: description]
  AUDITOR_PROHIBITED_TERM_SCAN: CLEAN | FOUND[term at exact location]
  DISCREPANCY: NONE | FOUND[SPEC_CONFORMANCE] | FOUND[INVARIANT_CONFORMANCE] | FOUND[PROHIBITED_TERM] | FOUND[MULTIPLE: list]

### Audit Scope
  Phase 1 Trace Table: all four columns on every row.
  Phase 2 Defect Matrix: all four DEFECT_VERDICT rows + invariant references.
  Phase 2 Fallback + Adversarial: FALLBACK_QUALITY + ADVERSARIAL_OUTCOME present.
  Phase 2 Coverage: ratios present.
  Phases 1-2 full text: prohibited term body scan.

ASSERTION CONTRACT GATE: Schema declared including INVARIANT_CONFORMANCE as mandatory column.
All enum values specified. Developer may begin Phase 1.

---

## PHASE 1: CONVERSATION TRACE TABLE
[Copilot Studio Developer. Walk every turn. All four assertion columns mandatory. Blank cell
= structural violation. INVARIANT_CONFORMANCE checks Phase 0-D topology invariants at every
relevant turn -- this is separate from CS-SPEC runtime checks.]

| Turn | User Input | Trigger Phrase Matched (HIGH/MED/LOW) | Topic | Nodes Executed | SESSION_STATE | Agent Response | SPEC_CONFORMANCE | INVARIANT_CONFORMANCE | PROHIBITED_TERM_SCAN |
|------|-----------|--------------------------------------|-------|----------------|---------------|---------------|-----------------|----------------------|---------------------|
| T-01 | "[input]" | "[phrase]" (HIGH) | [Topic-A] | Trigger>Message>Question | var1=X (ts, changed); var2=Y (g, held) | "[response]" | CONFORMS \| DEVIATES[CS-SPEC-NN: desc] | HOLDS [no topology invariant testable this turn] \| VIOLATED[INVARIANT-TOPO-NN: desc] | CLEAN \| FOUND[term] |
| T-02 | "[input]" | "[phrase]" (MED) | [Topic-B] | Trigger>Condition(branch=default)>Redirect | var1=cleared (ts, topic ended); var2=Y (g, held) | "[response]" | CONFORMS \| DEVIATES[CS-SPEC-NN: desc] | HOLDS [INVARIANT-TOPO-01: condition node has default branch -- confirmed at this turn] \| VIOLATED[...] | CLEAN \| FOUND[term] |
[...all turns. All four columns mandatory. No blank cells.]

TRACE GATE: All [N] turns present. All four columns populated per Phase 0-A contract.
INVARIANT_CONFORMANCE checked at every relevant topology event. Advance to Phase 2.

---

## PHASE 2: DEFECTS + FALLBACK + ADVERSARIAL + COVERAGE + AMENDMENTS

### 2-A: Defect Matrix
[Reference Phase 0-D topology invariants in evidence where applicable.]

| Defect Class | DEFECT_VERDICT | Evidence | Reproduction Sequence |
|-------------|---------------|----------|----------------------|
| Dead end | FOUND \| CONFIRMED_ABSENT | [FOUND: T-NN, topic, node, INVARIANT-TOPO-04 violated (no terminal exit path reachable). CONFIRMED_ABSENT: scope + "INVARIANT-TOPO-04 holds for all [N] topics: [exit paths listed]."] | [sequence / N/A] |
| Infinite loop | FOUND \| CONFIRMED_ABSENT | [FOUND: cycle path, INVARIANT-TOPO-02 violated. CONFIRMED_ABSENT: "Redirect graph acyclic; INVARIANT-TOPO-02 holds. Redirect map: [A->B], [C->terminal]."] | [cycle / N/A] |
| Trigger phrase collision | FOUND \| CONFIRMED_ABSENT | [FOUND: phrase + competing topics + scores + disambiguation strategy (entity enrichment / condition ordering / trigger phrase refactor) + rationale. CONFIRMED_ABSENT: scope.] | [sequence / N/A] |
| Missing fallback | FOUND \| CONFIRMED_ABSENT | [FOUND: topic + condition node + missing branch + CS-SPEC-03 + INVARIANT-TOPO-01 violated. CONFIRMED_ABSENT: "INVARIANT-TOPO-01 holds for all condition nodes: [list]."] | [sequence / N/A] |

### 2-B: Fallback Chain Trace
Unrecognized user input: "[phrase]"
Step 1: [N] topics evaluated, 0 match -> CS-SPEC-07 -> [Fallback topic]
Step 2: [node type] -- [action]
...
Terminal: [escalation node / end of conversation node / loop detected]
FALLBACK_QUALITY: COMPLETE | LOOPS | TRUNCATED

### 2-C: Adversarial Injection
Scenario: [type + description]
Injected at: T-[NN] | State: [snapshot]
Node path: [trace]
Variable impact: [changes / loss]
Agent response: "[text]"
ADVERSARIAL_OUTCOME: GRACEFUL | BRITTLE | SILENT_FAILURE

### 2-D: Coverage + Topology Invariant Summary
Coverage:
| Metric | Visited | Total (estimated) | Ratio |
|--------|---------|-------------------|-------|
| Topics | [N] | [Total] | [pct]% |
| Trigger phrases | [N] | [Total] | [pct]% |

Topology invariant status (pre-committed in Phase 0-D; verified against trace):
| Invariant | Pre-committed claim | Trace result | Status |
|-----------|--------------------|--------------| -------|
| INVARIANT-TOPO-01 | All condition nodes have default branch | [turns where checked] | HOLDS \| VIOLATED[T-NN: desc] |
| INVARIANT-TOPO-02 | No unconditional redirect cycle | [redirect paths checked] | HOLDS \| VIOLATED[path] |
| INVARIANT-TOPO-03 | All topic-scoped vars cleared at boundary | [boundary turns checked] | HOLDS \| VIOLATED[T-NN: desc] |
| INVARIANT-TOPO-04 | Every topic has terminal exit path | [topics checked] | HOLDS \| VIOLATED[topic: desc] |

Amendments (all FOUND defects, all DEVIATES and VIOLATED rows from Phase 1):
- **CS-SPEC-NN / INVARIANT-TOPO-NN:** [violation description]
  Trigger sequence: "[inputs]" -> [failure]
  Fix: [specific change to agent topology or trigger phrases]
  Priority: P1 / P2 / P3

---

## === DEVELOPER ARTIFACT COMPLETE (Phases 0-D through 2) ===

---

## === AUDITOR NOW READS THE COMPLETED ARTIFACT ===

---

## PHASE 3: AUDITOR APPLIES CONTRACT
[Compliance Auditor. Read Developer Artifact (Phases 0-D through 2) as a finished document.
Developer role has ended. Apply Phase 0-A assertion schema including AUDITOR_INVARIANT_CONFORMANCE.
Re-annotate every Phase 1 Trace Table row independently.]

| Turn | Dev SPEC_CONFORMANCE | Aud SPEC_CONFORMANCE | Dev INVARIANT_CONFORMANCE | Aud INVARIANT_CONFORMANCE | Dev PROHIBITED_TERM_SCAN | Aud PROHIBITED_TERM_SCAN | DISCREPANCY |
|------|---------------------|---------------------|--------------------------|--------------------------|--------------------------|--------------------------|-------------|
| T-01 | [Ph1] | CONFORMS \| DEVIATES[...] | [Ph1] | HOLDS \| VIOLATED[INVARIANT-TOPO-NN: desc] | [Ph1] | CLEAN \| FOUND[term] | NONE \| FOUND[SPEC_CONFORMANCE] \| FOUND[INVARIANT_CONFORMANCE] \| FOUND[PROHIBITED_TERM] \| FOUND[MULTIPLE: list] |
[...one row per turn]

Topology invariant audit (Auditor independently reviews Phase 2-D invariant summary):
| Invariant | Developer claim (2-D) | Auditor scan of Phase 1 | INVARIANT_AUDIT |
|-----------|----------------------|------------------------|-----------------|
| INVARIANT-TOPO-01 | [from 2-D] | [Auditor scans condition node turns] | CONFIRMED \| DISPUTED[T-NN: desc] |
| INVARIANT-TOPO-02 | [from 2-D] | [Auditor scans redirect paths] | CONFIRMED \| DISPUTED[path] |
| INVARIANT-TOPO-03 | [from 2-D] | [Auditor scans topic-boundary turns] | CONFIRMED \| DISPUTED[T-NN: desc] |
| INVARIANT-TOPO-04 | [from 2-D] | [Auditor scans topic exit paths] | CONFIRMED \| DISPUTED[topic] |

Prohibited term body scan (Phases 0-D through 2 full text):
| Term | Present | Location |
|------|---------|----------|
| intent | YES \| NO | [location / N/A] |
| dialog | YES \| NO | [location / N/A] |
| slot | YES \| NO | [location / N/A] |
| NLU | YES \| NO | [location / N/A] |
| utterance | YES \| NO | [location / N/A] |
| chatbot | YES \| NO | [location / N/A] |
| handoff | YES \| NO | [location / N/A] |
| context | YES \| NO | [location / N/A] |
| bot | YES \| NO | [location / N/A] |
PROHIBITED_TERM_BODY_SCAN: CLEAN | FOUND[list]

Auditor summary:
  Contracts applied: Phase 0-D (domain + topology invariants) + Phase 0-A (assertion schema)
  Turns audited: [N]
  DISCREPANCY cases: [N] -- SPEC_CONFORMANCE: [N]; INVARIANT_CONFORMANCE: [N]; PROHIBITED_TERM: [N]
  Topology invariants confirmed: [N] / [Total] -- Disputed: [N]
  AUDIT_VERDICT: CLEAN | ISSUES_FOUND
```

---

## Summary Table

| V | Axis | Key innovation | C-14 | C-15 | Predicted |
|---|------|----------------|------|------|-----------|
| V-01 | Role Sequence | Developer declares domain invariants first; Auditor declares assertion contract second — symmetric bidirectional pre-commitment; neither role can reverse-engineer criteria | PASS | PASS | 100 |
| V-02 | Lifecycle Emphasis | All Developer output in one Phase 1 (sub-sections, no intermediate gates) — tests whether FALLBACK/ADVERSARIAL/DEFECT gates are load-bearing or cosmetic | PASS | PASS | 100 |
| V-03 | Phrasing Register | SHALL/MUST normative specification language throughout; 7-phase structure preserved — phrasing fungibility test | PASS | PASS | 100 |
| V-04 | Role Seq + Inertia Framing | Gap analysis preamble + bidirectional contracts + per-phase gap closure tracking — gap framing as quality driver | PASS | PASS | 100 |
| V-05 | Full Synthesis + Topology Invariants | Developer pre-commits to design-time structural invariants; Auditor adds INVARIANT_CONFORMANCE column; potential C-16 pattern | PASS | PASS | 100 |

**Key R5 open questions:**
1. Does V-02 hit 100? If yes, intermediate gates (FALLBACK GATE, ADVERSARIAL GATE, DEFECT GATE)
   are cosmetic. If it misses C-06/C-09, those gates are load-bearing — parallel to R4's C-12 finding.
2. Does V-03 (SHALL/MUST phrasing) match R4 V-05 at 100? If yes, phrasing register is fungible.
   If C-12 misses, the imperative phase gate ("do not begin Phase 7") may be more load-bearing
   than the normative form ("the Auditor SHALL NOT begin Phase 7").
3. Does V-05's topology invariant pattern produce measurably better structural defect detection?
   If yes, C-16 candidate: Developer pre-commits to design-time topology invariants; Auditor
   includes INVARIANT_CONFORMANCE as mandatory per-turn column distinct from SPEC_CONFORMANCE.
