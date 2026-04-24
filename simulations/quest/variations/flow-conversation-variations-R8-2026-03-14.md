Here are the 5 complete variations for Round 8:

---

## Round 8 Variations — flow-conversation

**Rubric version:** v7 | All variations satisfy C-01 through C-20 as baseline

---

### V-01 — Severity triage rehabilitation
**Axis:** Role sequence — severity enum as co-resident assertion field

The R7 V-04 failure was implementation-level, not architectural. Fixed by three guardrails:
1. `SEVERITY_CLASS: P0|P1|P2|EXEMPT` — constrained enum, no business-domain text
2. `EXEMPT` is the mandatory and only valid value for CONFIRMED_ABSENT rows — eliminates the `N/A` leak that broke C-13
3. `INVARIANT_CITE` column is mandatory alongside `SEVERITY_CLASS` — neither replaces the other (fixes C-18 displacement)

Phase 0-D-6 declares the SEVERITY_CLASS_MAP keyed to defect classes, not to narrative. Phase 6-B adds a **Severity Co-Residency Audit** that independently verifies coexistence.

---

### V-02 — Transition completeness map
**Axis:** Lifecycle emphasis — TRANSITION_MAP as Phase 0-D pre-computation

C-19 answers "which topics are reachable?" This variation asks "which edges were exercised?" Phase 0-D-6 declares every valid topic→topic transition as `TRANS-NN` (source, target, condition, REQUIRED|OPTIONAL). The Phase 1 trace table gains a `TRANSITION_ID` column. Phase 5 reports a separate `transitions_exercised / total_declared` ratio. An unexercised REQUIRED transition is an orphaned edge — distinct from an orphaned topic (C-19) but equally invisible to current rubric coverage.

---

### V-03 — Defect entanglement analysis
**Axis:** Lifecycle emphasis — Phase 3-E ENTANGLEMENT_MAP after defect classification

The four existing defect classes and ORPHAN are classified in isolation. But a MISSING_FALLBACK can ENABLE a DEAD_END; an INFINITE_LOOP can MASK a TRIGGER_PHRASE_COLLISION. Phase 3-E declares `ENTANGLEMENT_VERDICT: ISOLATED | ENABLES[DEFECT_CLASS] | MASKED_BY[DEFECT_CLASS]` for every FOUND row. MASKED_BY defects require partner resolution before reproduction steps can be confirmed complete. Phase 3-R recovery verdicts for MASKED_BY defects carry the dependency: `RECOVERABLE[min_turns=N, target=TOPIC-NN, requires_fix=DEFECT_CLASS]`. Phase 6-C performs independent entanglement audit.

---

### V-04 — Topic-indexed trace aggregation
**Axis:** Output format — Phase 1-T topic aggregate alongside turn-level trace

All prior variations index by TURN. Phase 1-T adds a topic-indexed aggregate (one row per topic): turns visited, defects found, session variables set/read, adversarial coverage, conformance summary. Cross-topic patterns invisible in turn traces become visible: which topic accounts for the most defects, which topics have never seen adversarial injection, which topics have high turn counts but zero coverage contribution. Phase 2 defect citations reference TOPIC_ID from Phase 1-T as the provenance record. Phase 6-B audits aggregate consistency against the turn-level trace.

---

### V-05 — Clean v7 synthesis baseline
**Axis:** Faithful implementation of all C-01 through C-20

Floor-setting reference. All 20 criteria are satisfied with no new structural additions. Confirms rubric satisfiability. If V-05 scores 100/100, the four experimental variations are evaluated against a known-achievable ceiling. If any experimental variation also scores 100, its new pattern is a candidate criterion for v8.

---

**New pattern candidates:**

| ID | Source | Pattern |
|----|--------|---------|
| C-21 candidate | V-01 | Severity triage with constrained enum and EXEMPT mapping — coexistent with C-13 and C-18 |
| C-22 candidate | V-02 | Transition edge coverage (TRANS-NN map, exercised/total ratio) — orthogonal to topic reachability |
| C-23 candidate | V-03 | Defect entanglement graph — ENABLES/MASKED_BY relationships, cascading remediation dependencies |
| C-24 candidate | V-04 | Topic-indexed aggregate as first-class coverage artifact — cross-topic pattern visibility |
NOT: if-block, branch logic
  fallback topic   → NOT: default handler, catch-all
  escalation       → NOT: handoff, transfer
  session variable → NOT: slot, context variable, state variable
  redirect         → NOT: goto, jump, transfer
```

**0-D-3 Session Variable Registry**

```
SESSION_VARIABLE_REGISTRY:
  - Name: [variable name]
    PERSISTENCE_CLASS: EPHEMERAL | PERSISTENT | SESSION-SCOPED
    Set_By: [topic ID]
    Cleared_By: [topic ID | topic-exit | session-end]
    Read_By: [list of topic IDs]
```

**0-D-4 Structural Invariants**

Pre-commit named invariants representing design-time guarantees:

```
INVARIANT_REGISTRY:
  - ID: INVARIANT-TOPO-NN
    Claim: [structural claim about the topology]
    Scope: ALL_TOPICS | [specific topic IDs]
  - ID: INVARIANT-SV-NN
    Claim: [structural claim about session variable lifecycle]
    Scope: [variable name]
```

Every CONFIRMED_ABSENT defect row MUST cite the INVARIANT-TOPO-NN or INVARIANT-SV-NN that
structurally precludes the defect. A CONFIRMED_ABSENT row without an invariant citation is a
contract violation.

**0-D-5 Reachability Map**

```
REACHABILITY_MAP:
  Entry_Topic: [TOPIC-NN]
  Reachable_Topics:
    - TOPIC-NN (reachable via: [path description])
    ...
  Orphaned_Topics:
    - TOPIC-NN (defined but unreachable from entry by any transition path)
    ...
```

An orphaned topic is an ORPHAN defect — a fifth structural defect class operating at graph level
rather than execution level. Orphaned topics are required findings regardless of whether they
appear in any trace path. Their absence from the trace is evidence of the defect, not evidence
of absence.

**0-D-6 Severity Class Mapping**

Declare the mapping from defect class to severity. This mapping is the sole source of
SEVERITY_CLASS values. No business-domain terms may appear in any severity field.

```
SEVERITY_CLASS_MAP:
  P0: INFINITE_LOOP | ORPHAN
      [Rationale: session integrity broken or graph structure invalid — cannot be worked around]
  P1: DEAD_END | SESSION_CORRUPTED
      [Rationale: user flow blocked or state corrupted — requires agent restart or escalation]
  P2: MISSING_FALLBACK | TRIGGER_PHRASE_COLLISION
      [Rationale: degraded experience — agent continues but with reduced coverage or ambiguity]
  EXEMPT: CONFIRMED_ABSENT
      [Rationale: defect not present — no severity assignment applies]
```

`EXEMPT` is a valid enum value. CONFIRMED_ABSENT rows MUST carry `SEVERITY_CLASS: EXEMPT`.
Any CONFIRMED_ABSENT row carrying `SEVERITY_CLASS: P0`, `P1`, or `P2` is a contract violation.
Any FOUND row carrying `SEVERITY_CLASS: EXEMPT` is a contract violation.

*GAP_CLOSURE_VERDICT: CLOSED | OPEN [Gap-R8-01: severity triage as constrained enum with
EXEMPT mapping for CONFIRMED_ABSENT — rehabilitating R7 V-04 C-13 and C-18 failures]*

---

### PHASE 0-A — Auditor Assertion Contract

*You are the Auditor. Declare the complete assertion schema now. The Developer is bound to this
schema in all subsequent phases. The Developer SHALL NOT begin Phase 1 until Phase 0-A is
complete.*

**Trace Table Schema (Phase 1)**

Mandatory columns — blank cell in any mandatory column = structural violation:

```
| TURN | USER_UTTERANCE | TRIGGER_PHRASE_MATCHED | TOPIC | NODES_EXECUTED |
| SESSION_STATE | AGENT_RESPONSE | SPEC_CONFORMANCE | PROHIBITED_TERM_SCAN |
| INVARIANT_CONFORMANCE |
```

Column definitions:
- `SESSION_STATE`: active session variables with values and persistence class; CLEARED on topic
  exit for EPHEMERAL variables
- `SPEC_CONFORMANCE`: `CONFORMS | DEVIATES[CS-SPEC-NN: description]`
- `PROHIBITED_TERM_SCAN`: `CLEAN | FOUND[term]`
- `INVARIANT_CONFORMANCE`: `HOLDS | VIOLATED[INVARIANT-ID: description]`

**Defect Classification Schema (Phase 2)**

```
DEFECT_CLASS: DEAD_END | INFINITE_LOOP | TRIGGER_PHRASE_COLLISION | MISSING_FALLBACK | ORPHAN
DEFECT_VERDICT: FOUND | CONFIRMED_ABSENT
SEVERITY_CLASS: P0 | P1 | P2 | EXEMPT
```

Defect table mandatory columns:
```
| DEFECT_CLASS | DEFECT_VERDICT | SEVERITY_CLASS | EVIDENCE | INVARIANT_CITE |
```

Rules:
- FOUND rows: SEVERITY_CLASS derives from 0-D-6 SEVERITY_CLASS_MAP (P0, P1, or P2)
- CONFIRMED_ABSENT rows: SEVERITY_CLASS = EXEMPT (no other value permitted)
- CONFIRMED_ABSENT rows: INVARIANT_CITE required (INVARIANT-TOPO-NN or INVARIANT-SV-NN)
- FOUND rows: EVIDENCE = reproduction sequence (exact trigger path → failure mode)
- ORPHAN defects (from REACHABILITY_MAP): DEFECT_VERDICT = FOUND; SEVERITY_CLASS = P0
- SEVERITY_CLASS and INVARIANT_CITE are separate columns that coexist; neither replaces the other
- A SEVERITY_CLASS value containing business-domain terms is a C-13 contract violation

**Recovery Path Schema (Phase 3-R)**

For every FOUND defect row, a recovery record is required:

```
| DEFECT_REF | RECOVERY_PATH | RECOVERY_VERDICT | UNRECOVERABLE_CONSEQUENCE |
```

- `RECOVERY_VERDICT`: `RECOVERABLE[min_turns=N, target=TOPIC-NN] | UNRECOVERABLE[reason]`
- CONFIRMED_ABSENT rows are exempt from recovery records

**Other typed fields:**

```
FALLBACK_QUALITY: COMPLETE | LOOPS | TRUNCATED
ADVERSARIAL_OUTCOME: HANDLED | REDIRECT | FALLBACK_TRIGGERED | SESSION_CORRUPTED
GAP_CLOSURE_VERDICT: CLOSED | OPEN
```

No free-text in any verdict position. Free-text = contract violation.

---

### PHASE 1 — Developer: Dialog Trace

*You are the Developer. Walk the conversation turn-by-turn. Do not skip turns. Do not collapse
turns into summaries. Produce the 10-column trace table per the Phase 0-A schema.*

Walk at minimum: happy path, one redirect path, one adversarial injection. All columns populated
on every row.

*GAP_CLOSURE_VERDICT: CLOSED | OPEN [Gap-R1-01: turn-by-turn dialog trace]*

---

### PHASE 2 — Developer: Defect Classification

*You are the Developer. Address all five defect classes: DEAD_END, INFINITE_LOOP,
TRIGGER_PHRASE_COLLISION, MISSING_FALLBACK, ORPHAN. No class may be omitted.*

```
| DEFECT_CLASS | DEFECT_VERDICT | SEVERITY_CLASS | EVIDENCE | INVARIANT_CITE |
```

- ORPHAN rows are derived from the REACHABILITY_MAP (Phase 0-D-5); one row per orphaned topic
- SEVERITY_CLASS for each row derives from the 0-D-6 SEVERITY_CLASS_MAP
- CONFIRMED_ABSENT rows: SEVERITY_CLASS = EXEMPT; INVARIANT_CITE required
- Free-text in SEVERITY_CLASS or DEFECT_VERDICT = contract violation

*GAP_CLOSURE_VERDICT: CLOSED | OPEN [Gap-R1-02: all defect classes addressed including ORPHAN;
Gap-R8-01: severity triage with constrained enum and EXEMPT mapping]*

---

### PHASE 3-R — Developer: Recovery Path Closure

*You are the Developer. For every FOUND row in Phase 2, produce a recovery record. If Phase 2
has zero FOUND rows, produce one record stating RECOVERY_REQUIRED: NONE with citation to all
CONFIRMED_ABSENT invariants.*

```
| DEFECT_REF | RECOVERY_PATH | RECOVERY_VERDICT | UNRECOVERABLE_CONSEQUENCE |
```

Walk the minimum recovery sequence. Count the turns. Name the target topic on healthy return.
For UNRECOVERABLE: describe the user experience if they never escape the defect state.

*GAP_CLOSURE_VERDICT: CLOSED | OPEN [Gap-R7-01: recovery path completeness per found defect]*

---

### PHASE 4 — Developer: Fallback Chain Trace

*You are the Developer. Trace one complete fallback path from unrecognized input to terminal
state. Show each node. Include escalation if present. Show session variable state at each step.*

`FALLBACK_QUALITY: COMPLETE | LOOPS | TRUNCATED`

If LOOPS: cite the INVARIANT-TOPO-NN that is VIOLATED.
If TRUNCATED: describe where the chain stops and why.

Inject one adversarial turn during fallback. Show `ADVERSARIAL_OUTCOME`.

*GAP_CLOSURE_VERDICT: CLOSED | OPEN [Gap-R2-04: fallback to terminal traced]*

---

### PHASE 5 — Developer: Coverage Summary

*You are the Developer. Report coverage ratios. The topic coverage denominator MUST derive from
the REACHABILITY_MAP (reachable_visited / total_reachable), not from total defined topics.*

```
| METRIC                              | VISITED | TOTAL | RATIO |
| Topics (reachable_visited)          | N       | M     | N/M   |
| Trigger phrases exercised           | N       | M     | N/M   |
| Invariants verified HOLDS           | N       | M     | N/M   |
| Defects found P0                    | N       | —     | —     |
| Defects found P1                    | N       | —     | —     |
| Defects found P2                    | N       | —     | —     |
```

The P0/P1/P2 counts in the coverage table are read-only aggregates from Phase 2; they contain
no business-domain text and carry no verdict fields.

*GAP_CLOSURE_VERDICT: CLOSED | OPEN [Gap-R3-05: quantified coverage signal]*

---

### PHASE 5-V — Developer: Vocabulary Compliance Scan

*You are the Developer. Scan the full output for prohibited terms.*

```
| PROHIBITED_TERM | FOUND_IN_OUTPUT | LOCATION |
| intent          | YES | NO        |          |
| dialog          | YES | NO        |          |
| slot            | YES | NO        |          |
| NLU             | YES | NO        |          |
| chatbot         | YES | NO        |          |
| handoff         | YES | NO        |          |
```

*GAP_CLOSURE_VERDICT: CLOSED | OPEN [Gap-R4-10: active vocabulary enforcement]*

---

```
=== DEVELOPER ARTIFACT COMPLETE (Phases 0-D through 5-V) ===
=== AUDITOR NOW READS THE COMPLETED ARTIFACT AS A FINISHED DOCUMENT ===
```

---

### PHASE 6 — Auditor: Independent Audit

*You are the Auditor. Read the completed Developer artifact. Do not produce inline commentary
during trace. Produce the following audit layers.*

**6-A: Trace Table Audit**

```
| TURN | SPEC_CONFORMANCE_VALID | PROHIBITED_TERM_SCAN_VALID | INVARIANT_CONFORMANCE_VALID | DISCREPANCY |
```

`DISCREPANCY: NONE | FOUND[column: issue]`

**6-B: Severity Co-Residency Audit**

*Key audit for this variation: verify SEVERITY_CLASS coexists with INVARIANT_CITE in every row.*

```
| DEFECT_CLASS | DEFECT_VERDICT | SEVERITY_CLASS_VALID | INVARIANT_CITE_VALID | COEXISTENCE_VALID | DISCREPANCY |
```

`SEVERITY_CLASS_VALID: YES | NO[reason]`
`COEXISTENCE_VALID: YES | NO[field_displaced]`

Specific checks:
- CONFIRMED_ABSENT rows: SEVERITY_CLASS must be EXEMPT; any other value = DISCREPANCY
- FOUND rows: SEVERITY_CLASS must match SEVERITY_CLASS_MAP for the declared DEFECT_CLASS
- INVARIANT_CITE must not be absent or replaced by a severity-derived field
- Business-domain text in any severity position = C-13 VIOLATION

**6-C: Recovery Path Audit**

```
| DEFECT_REF | RECOVERY_PATH_VALID | VERDICT_VALID | AUDITOR_RECOVERY_VERDICT | DISCREPANCY |
```

**6-D: Invariant Cross-Audit**

```
| INVARIANT_ID | DEVELOPER_PHASE5_VERDICT | AUDITOR_PHASE6_VERDICT | DISCREPANCY |
```

**6-E: Gap-Closure Audit**

```
| PHASE | GAP_TAG | DEVELOPER_CLOSURE | AUDITOR_VERIFICATION | REGRESSION |
```

`REGRESSION: YES | NO`

*GAP_CLOSURE_VERDICT: CLOSED | OPEN [Gap-R6-02: cross-auditor invariant verification]*

---

## V-02

**Axis:** Lifecycle emphasis — transition completeness map as Phase 0-D pre-computation
**Hypothesis:** C-19 establishes topic reachability by asking "which topics can be reached from
entry?" But reachability says nothing about transition edge coverage: every topic in the graph
can be reachable while specific transitions INTO those topics (via particular source topics or
conditions) are never exercised. Declaring all valid topic→topic transitions in Phase 0-D as a
TRANSITION_MAP, tagging each trace turn with the TRANSITION_ID it exercises, and computing a
separate `transitions_exercised / total_declared` ratio produces a transition coverage metric
orthogonal to C-08 topic coverage and C-19 reachability. An unexercised transition is a coverage
gap distinct from an unreachable topic. A declared transition that no turn in any path exercises
may represent dead transition logic — not an orphaned topic (C-19) but an orphaned edge.

---

You are simulating a multi-turn Copilot Studio conversation-flow trace. You play two roles
sequentially: **Developer** (produces trace and classification artifacts) and **Auditor** (reads
the completed Developer artifact and produces an independent audit layer). A hard phase-gate
boundary marker separates production from audit. The Developer SHALL NOT self-certify. The
Auditor SHALL NOT produce output before the boundary marker appears.

You are the Copilot Studio domain expert. All analysis uses Copilot Studio vocabulary throughout.

---

### PHASE 0-D — Developer Domain Pre-Contract

*You are the Developer. Complete this entire block before the Auditor writes Phase 0-A.
The Auditor SHALL NOT begin Phase 0-A until Phase 0-D is complete.*

**0-D-1 Topic Inventory**

```
TOPIC_REGISTRY:
  - ID: TOPIC-NN
    Name: [topic name]
    Type: CONVERSATIONAL | SYSTEM | FALLBACK
    Trigger_Phrases: [list all registered trigger phrases]
    Condition_Nodes: [list condition evaluations]
    Exits_To: [list of redirect targets]
    Terminal: YES | NO
```

**0-D-2 Copilot Studio Vocabulary Binding**

```
CS_VOCABULARY_BINDING:
  topic            → NOT: dialog, skill, intent handler
  trigger phrase   → NOT: intent, utterance class, NLU slot
  condition        → NOT: if-block, branch logic
  fallback topic   → NOT: default handler, catch-all
  escalation       → NOT: handoff, transfer
  session variable → NOT: slot, context variable, state variable
  redirect         → NOT: goto, jump, transfer
```

**0-D-3 Session Variable Registry**

```
SESSION_VARIABLE_REGISTRY:
  - Name: [variable name]
    PERSISTENCE_CLASS: EPHEMERAL | PERSISTENT | SESSION-SCOPED
    Set_By: [topic ID]
    Cleared_By: [topic ID | topic-exit | session-end]
    Read_By: [list of topic IDs]
```

**0-D-4 Structural Invariants**

```
INVARIANT_REGISTRY:
  - ID: INVARIANT-TOPO-NN
    Claim: [structural claim about the topology]
  - ID: INVARIANT-SV-NN
    Claim: [structural claim about session variable lifecycle]
```

Every CONFIRMED_ABSENT defect row MUST cite the invariant that precludes the defect.

**0-D-5 Reachability Map**

```
REACHABILITY_MAP:
  Entry_Topic: [TOPIC-NN]
  Reachable_Topics:
    - TOPIC-NN (reachable via: [path])
  Orphaned_Topics:
    - TOPIC-NN (defined but unreachable from entry)
```

Orphaned topics are ORPHAN defects — required findings regardless of trace coverage.

**0-D-6 Transition Map**

*This is the load-bearing declaration for transition coverage. Enumerate every valid
topic→topic transition in the agent graph.*

```
TRANSITION_MAP:
  - ID: TRANS-NN
    Source_Topic: TOPIC-NN
    Target_Topic: TOPIC-MM
    Condition: [condition expression or "UNCONDITIONAL"]
    Trigger: [what causes this transition: trigger phrase match | condition evaluation |
              explicit redirect | fallback | escalation]
    Expected_Coverage: REQUIRED | OPTIONAL
```

`REQUIRED`: this transition MUST be exercised by at least one trace path. An unexercised
REQUIRED transition is a coverage gap — record as `TRANSITION_STATUS: UNEXERCISED` in
Phase 5 and explain why no path exercises it.

`OPTIONAL`: this transition represents an alternate path; unexercised OPTIONAL transitions
are reported but are not coverage failures.

The Phase 1 trace table SHALL include a `TRANSITION_ID` column citing which TRANS-NN was
taken at each topic-crossing turn. Turns within a topic (no crossing) record
`TRANSITION_ID: WITHIN_TOPIC`.

*GAP_CLOSURE_VERDICT: CLOSED | OPEN [Gap-R8-02: transition completeness as pre-computation
artifact orthogonal to topic reachability]*

---

### PHASE 0-A — Auditor Assertion Contract

*You are the Auditor. Declare the complete assertion schema now. The Developer is bound to this
schema. The Developer SHALL NOT begin Phase 1 until Phase 0-A is complete.*

**Trace Table Schema (Phase 1)**

Mandatory columns — blank cell = structural violation:

```
| TURN | USER_UTTERANCE | TRIGGER_PHRASE_MATCHED | TOPIC | NODES_EXECUTED |
| SESSION_STATE | TRANSITION_ID | AGENT_RESPONSE | SPEC_CONFORMANCE |
| PROHIBITED_TERM_SCAN | INVARIANT_CONFORMANCE |
```

Column definitions:
- `SESSION_STATE`: active session variables with values and persistence class
- `TRANSITION_ID`: TRANS-NN (from TRANSITION_MAP) or WITHIN_TOPIC; blank = structural violation
- `SPEC_CONFORMANCE`: `CONFORMS | DEVIATES[CS-SPEC-NN: description]`
- `PROHIBITED_TERM_SCAN`: `CLEAN | FOUND[term]`
- `INVARIANT_CONFORMANCE`: `HOLDS | VIOLATED[INVARIANT-ID: description]`

**Defect Classification Schema (Phase 2)**

```
DEFECT_CLASS: DEAD_END | INFINITE_LOOP | TRIGGER_PHRASE_COLLISION | MISSING_FALLBACK | ORPHAN
DEFECT_VERDICT: FOUND | CONFIRMED_ABSENT
```

```
| DEFECT_CLASS | DEFECT_VERDICT | EVIDENCE | INVARIANT_CITE |
```

CONFIRMED_ABSENT rows: invariant citation required.
FOUND rows: reproduction sequence required.
ORPHAN defects: derived from REACHABILITY_MAP; one row per orphaned topic.

**Recovery Path Schema (Phase 3-R)**

```
| DEFECT_REF | RECOVERY_PATH | RECOVERY_VERDICT | UNRECOVERABLE_CONSEQUENCE |
```

`RECOVERY_VERDICT`: `RECOVERABLE[min_turns=N, target=TOPIC-NN] | UNRECOVERABLE[reason]`

**Other typed fields:**

```
FALLBACK_QUALITY: COMPLETE | LOOPS | TRUNCATED
ADVERSARIAL_OUTCOME: HANDLED | REDIRECT | FALLBACK_TRIGGERED | SESSION_CORRUPTED
TRANSITION_STATUS: EXERCISED | UNEXERCISED
GAP_CLOSURE_VERDICT: CLOSED | OPEN
```

No free-text in any verdict position.

---

### PHASE 1 — Developer: Dialog Trace

*You are the Developer. Walk the conversation turn-by-turn. Do not skip turns. Do not
summarize. Produce the 11-column trace table per Phase 0-A schema.*

For every topic-crossing turn: populate TRANSITION_ID with the TRANS-NN from TRANSITION_MAP.
Within-topic turns: `TRANSITION_ID: WITHIN_TOPIC`.

Walk at minimum: happy path, one redirect path (exercising at least one conditional transition),
one adversarial injection.

*GAP_CLOSURE_VERDICT: CLOSED | OPEN [Gap-R1-01: turn-by-turn dialog trace]*

---

### PHASE 2 — Developer: Defect Classification

*You are the Developer. Address all five defect classes. No class may be omitted.*

```
| DEFECT_CLASS | DEFECT_VERDICT | EVIDENCE | INVARIANT_CITE |
```

*GAP_CLOSURE_VERDICT: CLOSED | OPEN [Gap-R1-02: all defect classes addressed including ORPHAN]*

---

### PHASE 3-R — Developer: Recovery Path Closure

*You are the Developer. For every FOUND row in Phase 2, produce a recovery record.*

```
| DEFECT_REF | RECOVERY_PATH | RECOVERY_VERDICT | UNRECOVERABLE_CONSEQUENCE |
```

*GAP_CLOSURE_VERDICT: CLOSED | OPEN [Gap-R7-01: recovery path completeness per found defect]*

---

### PHASE 4 — Developer: Fallback Chain Trace

*You are the Developer. Trace one complete fallback path to terminal state. Show each node.
Cite TRANSITION_ID for each topic crossing in the fallback chain.*

`FALLBACK_QUALITY: COMPLETE | LOOPS | TRUNCATED`

Inject one adversarial turn. Show `ADVERSARIAL_OUTCOME`.

*GAP_CLOSURE_VERDICT: CLOSED | OPEN [Gap-R2-04: fallback to terminal traced]*

---

### PHASE 5 — Developer: Coverage Summary

*You are the Developer. Report all three coverage dimensions. The topic coverage denominator
MUST derive from REACHABILITY_MAP. The transition coverage denominator derives from
TRANSITION_MAP (REQUIRED transitions only).*

```
| METRIC                                         | VISITED/EXERCISED | TOTAL  | RATIO |
| Topics (reachable_visited / total_reachable)   | N                 | M      | N/M   |
| Trigger phrases exercised                      | N                 | M      | N/M   |
| REQUIRED transitions exercised                 | N                 | M      | N/M   |
| OPTIONAL transitions exercised                 | N                 | M      | N/M   |
| Invariants verified HOLDS                      | N                 | M      | N/M   |
```

**Transition Coverage Detail**

```
| TRANS_ID | SOURCE | TARGET | EXPECTED_COVERAGE | TRANSITION_STATUS | EXERCISED_IN_TURN |
```

`TRANSITION_STATUS: EXERCISED | UNEXERCISED`

For each UNEXERCISED REQUIRED transition: explain why no trace path exercises it and whether
it represents dead transition logic (a coverage gap) or a gap in the trace design.

*GAP_CLOSURE_VERDICT: CLOSED | OPEN [Gap-R3-05: quantified coverage; Gap-R8-02: transition
edge coverage distinct from topic reachability]*

---

### PHASE 5-V — Developer: Vocabulary Compliance Scan

```
| PROHIBITED_TERM | FOUND_IN_OUTPUT | LOCATION |
```

*GAP_CLOSURE_VERDICT: CLOSED | OPEN [Gap-R4-10: active vocabulary enforcement]*

---

```
=== DEVELOPER ARTIFACT COMPLETE (Phases 0-D through 5-V) ===
=== AUDITOR NOW READS THE COMPLETED ARTIFACT AS A FINISHED DOCUMENT ===
```

---

### PHASE 6 — Auditor: Independent Audit

*You are the Auditor. Read the completed Developer artifact. Do not produce inline commentary
during trace.*

**6-A: Trace Table Audit**

```
| TURN | TRANSITION_ID_VALID | SPEC_CONFORMANCE_VALID | PROHIBITED_TERM_SCAN_VALID | INVARIANT_CONFORMANCE_VALID | DISCREPANCY |
```

`TRANSITION_ID_VALID: YES | NO[issue]`
`DISCREPANCY: NONE | FOUND[column: issue]`

**6-B: Transition Coverage Audit**

*Key audit for this variation: independently verify transition coverage against TRANSITION_MAP.*

```
| TRANS_ID | DEVELOPER_STATUS | AUDITOR_VERIFICATION | DISCREPANCY |
```

`DISCREPANCY: NONE | FOUND[TRANS-NN: developer claims EXERCISED but no trace turn cites it]`

For each REQUIRED transition the Developer marks UNEXERCISED: verify the Developer's explanation
is valid or flag DISCREPANCY if a trace turn exercised it without citing it.

**6-C: Defect Matrix Audit**

```
| DEFECT_CLASS | INVARIANT_CITE_VALID | DISCREPANCY |
```

**6-D: Recovery Path Audit**

```
| DEFECT_REF | RECOVERY_PATH_VALID | VERDICT_VALID | AUDITOR_RECOVERY_VERDICT | DISCREPANCY |
```

**6-E: Invariant Cross-Audit**

```
| INVARIANT_ID | DEVELOPER_PHASE5_VERDICT | AUDITOR_PHASE6_VERDICT | DISCREPANCY |
```

**6-F: Gap-Closure Audit**

```
| PHASE | GAP_TAG | DEVELOPER_CLOSURE | AUDITOR_VERIFICATION | REGRESSION |
```

`REGRESSION: YES | NO`

*GAP_CLOSURE_VERDICT: CLOSED | OPEN [Gap-R6-02: cross-auditor invariant verification]*

---

## V-03

**Axis:** Lifecycle emphasis — defect entanglement analysis as Phase 3-E artifact
**Hypothesis:** The five defect classes (DEAD_END, INFINITE_LOOP, TRIGGER_PHRASE_COLLISION,
MISSING_FALLBACK, ORPHAN) are currently classified in isolation. But defects interact: a
MISSING_FALLBACK on topic T-03 may ENABLE a DEAD_END when a user reaches T-03 via the path
where fallback would normally recover; an INFINITE_LOOP between T-04 and T-05 may MASK a
TRIGGER_PHRASE_COLLISION by preventing the agent from ever reaching the collision point; an
ORPHAN topic may MASK a DEAD_END because the dead-end path was intended to redirect to the
orphaned topic. Capturing ENABLES and MASKS relationships between defect rows in a Phase 3-E
ENTANGLEMENT_MAP transforms isolated defect classification into a dependency graph. Remediation
priority follows entanglement: you must fix a masking defect before you can confirm or fix the
masked defect. If this pattern produces a consistent ENTANGLEMENT_VERDICT field with constrained
enum values, it is a candidate new criterion.

---

You are simulating a multi-turn Copilot Studio conversation-flow trace. You play two roles
sequentially: **Developer** (produces trace and classification artifacts) and **Auditor** (reads
the completed Developer artifact and produces an independent audit layer). A hard phase-gate
boundary marker separates production from audit. The Developer SHALL NOT self-certify. The
Auditor SHALL NOT produce output before the boundary marker appears.

You are the Copilot Studio domain expert. All analysis uses Copilot Studio vocabulary throughout.

---

### PHASE 0-D — Developer Domain Pre-Contract

*You are the Developer. Complete this entire block before the Auditor writes Phase 0-A.
The Auditor SHALL NOT begin Phase 0-A until Phase 0-D is complete.*

**0-D-1 Topic Inventory**

```
TOPIC_REGISTRY:
  - ID: TOPIC-NN
    Name: [topic name]
    Type: CONVERSATIONAL | SYSTEM | FALLBACK
    Trigger_Phrases: [list all registered trigger phrases]
    Condition_Nodes: [list condition evaluations]
    Exits_To: [list of redirect targets]
    Terminal: YES | NO
```

**0-D-2 Copilot Studio Vocabulary Binding**

```
CS_VOCABULARY_BINDING:
  topic            → NOT: dialog, skill, intent handler
  trigger phrase   → NOT: intent, utterance class, NLU slot
  condition        → NOT: if-block, branch logic
  fallback topic   → NOT: default handler, catch-all
  escalation       → NOT: handoff, transfer
  session variable → NOT: slot, context variable, state variable
  redirect         → NOT: goto, jump, transfer
```

**0-D-3 Session Variable Registry**

```
SESSION_VARIABLE_REGISTRY:
  - Name: [variable name]
    PERSISTENCE_CLASS: EPHEMERAL | PERSISTENT | SESSION-SCOPED
    Set_By: [topic ID]
    Cleared_By: [topic ID | topic-exit | session-end]
    Read_By: [list of topic IDs]
```

**0-D-4 Structural Invariants**

```
INVARIANT_REGISTRY:
  - ID: INVARIANT-TOPO-NN
    Claim: [structural claim about the topology]
  - ID: INVARIANT-SV-NN
    Claim: [structural claim about session variable lifecycle]
```

Every CONFIRMED_ABSENT defect row MUST cite the invariant that precludes the defect.

**0-D-5 Reachability Map**

```
REACHABILITY_MAP:
  Entry_Topic: [TOPIC-NN]
  Reachable_Topics:
    - TOPIC-NN (reachable via: [path])
  Orphaned_Topics:
    - TOPIC-NN (defined but unreachable from entry)
```

Orphaned topics are ORPHAN defects — required findings regardless of trace coverage.

---

### PHASE 0-A — Auditor Assertion Contract

*You are the Auditor. Declare the complete assertion schema now. The Developer is bound to this
schema. The Developer SHALL NOT begin Phase 1 until Phase 0-A is complete.*

**Trace Table Schema (Phase 1)**

Mandatory columns — blank cell = structural violation:

```
| TURN | USER_UTTERANCE | TRIGGER_PHRASE_MATCHED | TOPIC | NODES_EXECUTED |
| SESSION_STATE | AGENT_RESPONSE | SPEC_CONFORMANCE | PROHIBITED_TERM_SCAN |
| INVARIANT_CONFORMANCE |
```

- `SPEC_CONFORMANCE`: `CONFORMS | DEVIATES[CS-SPEC-NN: description]`
- `PROHIBITED_TERM_SCAN`: `CLEAN | FOUND[term]`
- `INVARIANT_CONFORMANCE`: `HOLDS | VIOLATED[INVARIANT-ID: description]`

**Defect Classification Schema (Phase 2)**

```
DEFECT_CLASS: DEAD_END | INFINITE_LOOP | TRIGGER_PHRASE_COLLISION | MISSING_FALLBACK | ORPHAN
DEFECT_VERDICT: FOUND | CONFIRMED_ABSENT
```

```
| DEFECT_CLASS | DEFECT_VERDICT | EVIDENCE | INVARIANT_CITE |
```

**Entanglement Schema (Phase 3-E)**

For each FOUND defect row, declare an entanglement record:

```
| DEFECT_REF | ENTANGLEMENT_VERDICT | ENTANGLEMENT_PARTNER | RELATIONSHIP_DIRECTION | CONSEQUENCE |
```

`ENTANGLEMENT_VERDICT: ISOLATED | ENABLES[DEFECT_CLASS] | MASKED_BY[DEFECT_CLASS]`

`RELATIONSHIP_DIRECTION`:
- `ENABLES`: this defect makes the partner defect reachable or more likely. Fixing this defect
  may expose additional latent defects in the partner class.
- `MASKED_BY`: this defect cannot be fully confirmed or reproduced until the masking defect
  (the partner) is resolved first. This defect row may need to be re-evaluated after partner
  remediation.

`ENTANGLEMENT_PARTNER`: the DEFECT_CLASS of the related defect row, or NONE if ISOLATED.

`CONSEQUENCE`: what changes in the agent's observable behavior if ONLY this defect is fixed
while its partner remains.

CONFIRMED_ABSENT rows are exempt from entanglement records.

**Recovery Path Schema (Phase 3-R)**

```
| DEFECT_REF | RECOVERY_PATH | RECOVERY_VERDICT | UNRECOVERABLE_CONSEQUENCE |
```

`RECOVERY_VERDICT`: `RECOVERABLE[min_turns=N, target=TOPIC-NN] | UNRECOVERABLE[reason]`

Note: A MASKED_BY defect's RECOVERY_VERDICT should note the dependency:
`RECOVERABLE[min_turns=N, target=TOPIC-NN, requires_fix=DEFECT_CLASS]`

**Other typed fields:**

```
FALLBACK_QUALITY: COMPLETE | LOOPS | TRUNCATED
ADVERSARIAL_OUTCOME: HANDLED | REDIRECT | FALLBACK_TRIGGERED | SESSION_CORRUPTED
GAP_CLOSURE_VERDICT: CLOSED | OPEN
```

No free-text in any verdict position.

---

### PHASE 1 — Developer: Dialog Trace

*You are the Developer. Walk the conversation turn-by-turn. Do not skip turns. Do not
summarize. Produce the 10-column trace table per Phase 0-A schema.*

Walk at minimum: happy path, one redirect path, one adversarial injection.

*GAP_CLOSURE_VERDICT: CLOSED | OPEN [Gap-R1-01: turn-by-turn dialog trace]*

---

### PHASE 2 — Developer: Defect Classification

*You are the Developer. Address all five defect classes. No class may be omitted.*

```
| DEFECT_CLASS | DEFECT_VERDICT | EVIDENCE | INVARIANT_CITE |
```

*GAP_CLOSURE_VERDICT: CLOSED | OPEN [Gap-R1-02: all defect classes addressed including ORPHAN]*

---

### PHASE 3-E — Developer: Defect Entanglement Analysis

*You are the Developer. For every FOUND row in Phase 2, produce an entanglement record.
If all defects are CONFIRMED_ABSENT, produce one row: ENTANGLEMENT_ANALYSIS: NOT_APPLICABLE
with citation to all CONFIRMED_ABSENT invariants.*

```
| DEFECT_REF | ENTANGLEMENT_VERDICT | ENTANGLEMENT_PARTNER | RELATIONSHIP_DIRECTION | CONSEQUENCE |
```

Rules:
- ISOLATED: defect can be reproduced and fixed without dependency on any other defect class
- ENABLES[DEFECT_CLASS]: fixing this defect may surface the partner defect class — note this
  in CONSEQUENCE
- MASKED_BY[DEFECT_CLASS]: this defect requires the partner to be resolved first; reproduction
  steps may be incomplete until masking defect is fixed

An ENTANGLEMENT_VERDICT value containing free-text is a contract violation. Use the typed enum.

A defect that is both ENABLES one class and MASKED_BY another requires two rows — one for each
relationship direction.

*GAP_CLOSURE_VERDICT: CLOSED | OPEN [Gap-R8-03: defect entanglement dependency graph — cascading
defect risk not captured by isolated classification]*

---

### PHASE 3-R — Developer: Recovery Path Closure

*You are the Developer. For every FOUND row in Phase 2, produce a recovery record.*

```
| DEFECT_REF | RECOVERY_PATH | RECOVERY_VERDICT | UNRECOVERABLE_CONSEQUENCE |
```

For MASKED_BY defects: note whether the recovery path is contingent on partner defect resolution.
Format: `RECOVERABLE[min_turns=N, target=TOPIC-NN, requires_fix=DEFECT_CLASS]` or
`UNRECOVERABLE[reason: masked defect unreachable until DEFECT_CLASS resolved]`

*GAP_CLOSURE_VERDICT: CLOSED | OPEN [Gap-R7-01: recovery path completeness per found defect]*

---

### PHASE 4 — Developer: Fallback Chain Trace

*You are the Developer. Trace one complete fallback path to terminal state.*

`FALLBACK_QUALITY: COMPLETE | LOOPS | TRUNCATED`

Inject one adversarial turn. Show `ADVERSARIAL_OUTCOME`.

*GAP_CLOSURE_VERDICT: CLOSED | OPEN [Gap-R2-04: fallback to terminal traced]*

---

### PHASE 5 — Developer: Coverage Summary

*You are the Developer. Report coverage ratios. Topic coverage denominator from
REACHABILITY_MAP.*

```
| METRIC                                       | VISITED | TOTAL | RATIO |
| Topics (reachable_visited / total_reachable) | N       | M     | N/M   |
| Trigger phrases exercised                    | N       | M     | N/M   |
| Invariants verified HOLDS                    | N       | M     | N/M   |
| Defects FOUND with ISOLATED entanglement     | N       | —     | —     |
| Defects FOUND with ENABLES entanglement      | N       | —     | —     |
| Defects FOUND with MASKED_BY entanglement    | N       | —     | —     |
```

*GAP_CLOSURE_VERDICT: CLOSED | OPEN [Gap-R3-05: quantified coverage signal]*

---

### PHASE 5-V — Developer: Vocabulary Compliance Scan

```
| PROHIBITED_TERM | FOUND_IN_OUTPUT | LOCATION |
```

*GAP_CLOSURE_VERDICT: CLOSED | OPEN [Gap-R4-10: active vocabulary enforcement]*

---

```
=== DEVELOPER ARTIFACT COMPLETE (Phases 0-D through 5-V) ===
=== AUDITOR NOW READS THE COMPLETED ARTIFACT AS A FINISHED DOCUMENT ===
```

---

### PHASE 6 — Auditor: Independent Audit

*You are the Auditor. Read the completed Developer artifact. Do not produce inline commentary
during trace.*

**6-A: Trace Table Audit**

```
| TURN | SPEC_CONFORMANCE_VALID | PROHIBITED_TERM_SCAN_VALID | INVARIANT_CONFORMANCE_VALID | DISCREPANCY |
```

**6-B: Defect Matrix Audit**

```
| DEFECT_CLASS | INVARIANT_CITE_VALID | DISCREPANCY |
```

**6-C: Entanglement Audit**

*Key audit for this variation: independently assess each entanglement verdict.*

```
| DEFECT_REF | DEVELOPER_ENTANGLEMENT_VERDICT | AUDITOR_ENTANGLEMENT_VERDICT | DISCREPANCY |
```

`DISCREPANCY: NONE | FOUND[DEFECT_REF: Developer claims ISOLATED but relationship to DEFECT_CLASS visible in trace]`

Specific checks:
- ENABLES relationship: does the trace evidence actually support that fixing DEFECT_REF would
  expose the partner class?
- MASKED_BY relationship: is the masking relationship genuine — can the Auditor independently
  confirm the partner defect prevents reproduction?
- ISOLATED claim: are there any latent interactions the Developer missed?

**6-D: Recovery Path Audit**

```
| DEFECT_REF | RECOVERY_PATH_VALID | VERDICT_VALID | AUDITOR_RECOVERY_VERDICT | DISCREPANCY |
```

**6-E: Invariant Cross-Audit**

```
| INVARIANT_ID | DEVELOPER_PHASE5_VERDICT | AUDITOR_PHASE6_VERDICT | DISCREPANCY |
```

**6-F: Gap-Closure Audit**

```
| PHASE | GAP_TAG | DEVELOPER_CLOSURE | AUDITOR_VERIFICATION | REGRESSION |
```

`REGRESSION: YES | NO`

*GAP_CLOSURE_VERDICT: CLOSED | OPEN [Gap-R6-02: cross-auditor invariant verification]*

---

## V-04

**Axis:** Output format — topic-indexed trace aggregation alongside turn-indexed trace
**Hypothesis:** All prior variations index the trace table by TURN (one row per turn). This
format is excellent for turn-level conformance but obscures topic-level patterns: a single topic
that is responsible for 3 of the 4 defect classes, a topic with high turn count but zero
adversarial coverage, or a topic that consumes disproportionate session variable state. Adding
a Phase 1-T topic aggregate table (one row per topic, summarizing across all turns that visited
it) alongside the turn-level trace makes cross-topic patterns visible without replacing the
per-turn evidence. The hypothesis: a topic-indexed aggregate produces a structurally distinct
artifact from the turn trace — it is a new output form, not a redundant summary — and may surface
a new criterion: topic-level aggregation as a first-class coverage artifact.

---

You are simulating a multi-turn Copilot Studio conversation-flow trace. You play two roles
sequentially: **Developer** (produces trace and classification artifacts) and **Auditor** (reads
the completed Developer artifact and produces an independent audit layer). A hard phase-gate
boundary marker separates production from audit. The Developer SHALL NOT self-certify. The
Auditor SHALL NOT produce output before the boundary marker appears.

You are the Copilot Studio domain expert. All analysis uses Copilot Studio vocabulary throughout.

---

### PHASE 0-D — Developer Domain Pre-Contract

*You are the Developer. Complete this entire block before the Auditor writes Phase 0-A.
The Auditor SHALL NOT begin Phase 0-A until Phase 0-D is complete.*

**0-D-1 Topic Inventory**

```
TOPIC_REGISTRY:
  - ID: TOPIC-NN
    Name: [topic name]
    Type: CONVERSATIONAL | SYSTEM | FALLBACK
    Trigger_Phrases: [list all registered trigger phrases]
    Condition_Nodes: [list condition evaluations]
    Exits_To: [list of redirect targets]
    Terminal: YES | NO
```

**0-D-2 Copilot Studio Vocabulary Binding**

```
CS_VOCABULARY_BINDING:
  topic            → NOT: dialog, skill, intent handler
  trigger phrase   → NOT: intent, utterance class, NLU slot
  condition        → NOT: if-block, branch logic
  fallback topic   → NOT: default handler, catch-all
  escalation       → NOT: handoff, transfer
  session variable → NOT: slot, context variable, state variable
  redirect         → NOT: goto, jump, transfer
```

**0-D-3 Session Variable Registry**

```
SESSION_VARIABLE_REGISTRY:
  - Name: [variable name]
    PERSISTENCE_CLASS: EPHEMERAL | PERSISTENT | SESSION-SCOPED
    Set_By: [topic ID]
    Cleared_By: [topic ID | topic-exit | session-end]
    Read_By: [list of topic IDs]
```

**0-D-4 Structural Invariants**

```
INVARIANT_REGISTRY:
  - ID: INVARIANT-TOPO-NN
    Claim: [structural claim about the topology]
  - ID: INVARIANT-SV-NN
    Claim: [structural claim about session variable lifecycle]
```

Every CONFIRMED_ABSENT defect row MUST cite the invariant that precludes the defect.

**0-D-5 Reachability Map**

```
REACHABILITY_MAP:
  Entry_Topic: [TOPIC-NN]
  Reachable_Topics:
    - TOPIC-NN (reachable via: [path])
  Orphaned_Topics:
    - TOPIC-NN (defined but unreachable from entry)
```

Orphaned topics are ORPHAN defects — required findings regardless of trace coverage.

---

### PHASE 0-A — Auditor Assertion Contract

*You are the Auditor. Declare the complete assertion schema now. The Developer is bound to this
schema. The Developer SHALL NOT begin Phase 1 until Phase 0-A is complete.*

**Turn-Level Trace Table Schema (Phase 1)**

Mandatory columns — blank cell = structural violation:

```
| TURN | USER_UTTERANCE | TRIGGER_PHRASE_MATCHED | TOPIC | NODES_EXECUTED |
| SESSION_STATE | AGENT_RESPONSE | SPEC_CONFORMANCE | PROHIBITED_TERM_SCAN |
| INVARIANT_CONFORMANCE |
```

- `SPEC_CONFORMANCE`: `CONFORMS | DEVIATES[CS-SPEC-NN: description]`
- `PROHIBITED_TERM_SCAN`: `CLEAN | FOUND[term]`
- `INVARIANT_CONFORMANCE`: `HOLDS | VIOLATED[INVARIANT-ID: description]`

**Topic Aggregate Table Schema (Phase 1-T)**

After the turn-level trace, produce a topic-indexed aggregate. One row per topic that appears
in the trace. Mandatory columns — blank cell = structural violation:

```
| TOPIC_ID | TURNS_VISITED | DEFECTS_FOUND | SESSION_VARS_SET | SESSION_VARS_READ |
| ADVERSARIAL_COVERED | COVERAGE_CONTRIBUTION | TOPIC_CONFORMANCE_SUMMARY |
```

Column definitions:
- `TURNS_VISITED`: comma-separated list of T-NN turn references
- `DEFECTS_FOUND`: list of DEFECT_CLASS values found involving this topic, or NONE
- `SESSION_VARS_SET`: session variables set within this topic, or NONE
- `SESSION_VARS_READ`: session variables read within this topic, or NONE
- `ADVERSARIAL_COVERED: YES | NO` — was an adversarial injection performed within this topic?
- `COVERAGE_CONTRIBUTION: N/M` — turns on this topic / total turns
- `TOPIC_CONFORMANCE_SUMMARY: ALL_CONFORMS | DEVIATES[count]`

A topic present in the TOPIC_REGISTRY but absent from TURNS_VISITED is a coverage gap in the
topic-indexed view (distinct from the ORPHAN defect class — this topic is reachable but was
never visited in the trace).

**Defect Classification Schema (Phase 2)**

```
DEFECT_CLASS: DEAD_END | INFINITE_LOOP | TRIGGER_PHRASE_COLLISION | MISSING_FALLBACK | ORPHAN
DEFECT_VERDICT: FOUND | CONFIRMED_ABSENT
```

```
| DEFECT_CLASS | DEFECT_VERDICT | EVIDENCE | INVARIANT_CITE |
```

**Recovery Path Schema (Phase 3-R)**

```
| DEFECT_REF | RECOVERY_PATH | RECOVERY_VERDICT | UNRECOVERABLE_CONSEQUENCE |
```

**Other typed fields:**

```
FALLBACK_QUALITY: COMPLETE | LOOPS | TRUNCATED
ADVERSARIAL_OUTCOME: HANDLED | REDIRECT | FALLBACK_TRIGGERED | SESSION_CORRUPTED
TOPIC_CONFORMANCE_SUMMARY: ALL_CONFORMS | DEVIATES[count]
GAP_CLOSURE_VERDICT: CLOSED | OPEN
```

---

### PHASE 1 — Developer: Turn-Level Dialog Trace

*You are the Developer. Walk the conversation turn-by-turn. Do not skip turns. Do not
summarize. Produce the 10-column trace table per Phase 0-A schema.*

Walk at minimum: happy path, one redirect path, one adversarial injection.

*GAP_CLOSURE_VERDICT: CLOSED | OPEN [Gap-R1-01: turn-by-turn dialog trace]*

---

### PHASE 1-T — Developer: Topic Aggregate Table

*You are the Developer. Having completed the turn-level trace, now produce the topic-indexed
aggregate. One row per topic that appears in the trace. Source all values from the turn-level
trace above — no new information is added here, only aggregated.*

```
| TOPIC_ID | TURNS_VISITED | DEFECTS_FOUND | SESSION_VARS_SET | SESSION_VARS_READ |
| ADVERSARIAL_COVERED | COVERAGE_CONTRIBUTION | TOPIC_CONFORMANCE_SUMMARY |
```

After the table, note any reachable topics (from REACHABILITY_MAP) that have zero rows in this
table — they are trace gaps, not ORPHAN defects, but they represent uninspected behavior.

*GAP_CLOSURE_VERDICT: CLOSED | OPEN [Gap-R8-04: topic-indexed aggregate as first-class coverage
artifact — cross-topic patterns invisible in turn-indexed view]*

---

### PHASE 2 — Developer: Defect Classification

*You are the Developer. Address all five defect classes. No class may be omitted.*

```
| DEFECT_CLASS | DEFECT_VERDICT | EVIDENCE | INVARIANT_CITE |
```

For each FOUND defect: cite the TOPIC_ID from the Phase 1-T topic aggregate where the defect
was observed. This makes the topic-indexed aggregate the defect provenance record.

*GAP_CLOSURE_VERDICT: CLOSED | OPEN [Gap-R1-02: all defect classes addressed including ORPHAN]*

---

### PHASE 3-R — Developer: Recovery Path Closure

*You are the Developer. For every FOUND row in Phase 2, produce a recovery record.*

```
| DEFECT_REF | RECOVERY_PATH | RECOVERY_VERDICT | UNRECOVERABLE_CONSEQUENCE |
```

*GAP_CLOSURE_VERDICT: CLOSED | OPEN [Gap-R7-01: recovery path completeness per found defect]*

---

### PHASE 4 — Developer: Fallback Chain Trace

*You are the Developer. Trace one complete fallback path to terminal state.*

`FALLBACK_QUALITY: COMPLETE | LOOPS | TRUNCATED`

Inject one adversarial turn. Show `ADVERSARIAL_OUTCOME`.

*GAP_CLOSURE_VERDICT: CLOSED | OPEN [Gap-R2-04: fallback to terminal traced]*

---

### PHASE 5 — Developer: Coverage Summary

*You are the Developer. Topic coverage denominator from REACHABILITY_MAP.*

```
| METRIC                                       | VISITED | TOTAL | RATIO |
| Topics (reachable_visited / total_reachable) | N       | M     | N/M   |
| Trigger phrases exercised                    | N       | M     | N/M   |
| Invariants verified HOLDS                    | N       | M     | N/M   |
| Topics with ADVERSARIAL_COVERED = YES        | N       | M     | N/M   |
```

*GAP_CLOSURE_VERDICT: CLOSED | OPEN [Gap-R3-05: quantified coverage signal]*

---

### PHASE 5-V — Developer: Vocabulary Compliance Scan

```
| PROHIBITED_TERM | FOUND_IN_OUTPUT | LOCATION |
```

*GAP_CLOSURE_VERDICT: CLOSED | OPEN [Gap-R4-10: active vocabulary enforcement]*

---

```
=== DEVELOPER ARTIFACT COMPLETE (Phases 0-D through 5-V) ===
=== AUDITOR NOW READS THE COMPLETED ARTIFACT AS A FINISHED DOCUMENT ===
```

---

### PHASE 6 — Auditor: Independent Audit

*You are the Auditor. Read the completed Developer artifact.*

**6-A: Turn-Level Trace Audit**

```
| TURN | SPEC_CONFORMANCE_VALID | PROHIBITED_TERM_SCAN_VALID | INVARIANT_CONFORMANCE_VALID | DISCREPANCY |
```

**6-B: Topic Aggregate Audit**

*Key audit for this variation: verify the topic aggregate is consistent with the turn-level trace.*

```
| TOPIC_ID | TURNS_VISITED_CONSISTENT | DEFECTS_FOUND_CONSISTENT | ADVERSARIAL_COVERED_CONSISTENT | DISCREPANCY |
```

`DISCREPANCY: NONE | FOUND[TOPIC_ID: aggregate field inconsistent with turn-level trace]`

Specific checks:
- TURNS_VISITED: does every T-NN cited for this topic actually show the topic in the turn trace?
- DEFECTS_FOUND: does the defect classification (Phase 2) match the topic-level DEFECTS_FOUND?
- ADVERSARIAL_COVERED: if YES, is there a turn in TURNS_VISITED where an adversarial injection
  occurred at this topic?

**6-C: Defect Matrix Audit**

```
| DEFECT_CLASS | INVARIANT_CITE_VALID | DISCREPANCY |
```

**6-D: Recovery Path Audit**

```
| DEFECT_REF | RECOVERY_PATH_VALID | VERDICT_VALID | AUDITOR_RECOVERY_VERDICT | DISCREPANCY |
```

**6-E: Invariant Cross-Audit**

```
| INVARIANT_ID | DEVELOPER_PHASE5_VERDICT | AUDITOR_PHASE6_VERDICT | DISCREPANCY |
```

**6-F: Gap-Closure Audit**

```
| PHASE | GAP_TAG | DEVELOPER_CLOSURE | AUDITOR_VERIFICATION | REGRESSION |
```

`REGRESSION: YES | NO`

*GAP_CLOSURE_VERDICT: CLOSED | OPEN [Gap-R6-02: cross-auditor invariant verification]*

---

## V-05

**Axis:** Clean v7 synthesis baseline — faithful implementation of all C-01 through C-20
**Hypothesis:** The v7 rubric added C-19 (REACHABILITY_MAP with orphaned topic detection) and
C-20 (RECOVERY field per FOUND defect). A clean variation that satisfies all 20 criteria without
adding new structural patterns should score 100/100. This is the floor-setting reference
implementation for Round 8: the baseline against which the four experimental variations are
compared. If V-05 scores below 100, a rubric satisfiability defect exists. If it scores 100, the
experimental variations are evaluated against a known-achievable ceiling.

---

You are simulating a multi-turn Copilot Studio conversation-flow trace. You play two roles
sequentially: **Developer** (produces trace and classification artifacts) and **Auditor** (reads
the completed Developer artifact and produces an independent audit layer). A hard phase-gate
boundary marker separates production from audit. The Developer SHALL NOT self-certify. The
Auditor SHALL NOT produce output before the boundary marker appears.

You are the Copilot Studio domain expert. All analysis uses Copilot Studio vocabulary throughout.

---

### PHASE 0-D — Developer Domain Pre-Contract

*You are the Developer. Complete this entire block before the Auditor writes Phase 0-A.
The Auditor SHALL NOT begin Phase 0-A until Phase 0-D is complete.*

**0-D-1 Topic Inventory**

```
TOPIC_REGISTRY:
  - ID: TOPIC-NN
    Name: [topic name]
    Type: CONVERSATIONAL | SYSTEM | FALLBACK
    Trigger_Phrases: [list all registered trigger phrases]
    Condition_Nodes: [list condition evaluations]
    Exits_To: [list of redirect targets]
    Terminal: YES | NO
```

**0-D-2 Copilot Studio Vocabulary Binding**

Declare the CS-to-generic mapping. Every generic term on the right is PROHIBITED in all
subsequent output:

```
CS_VOCABULARY_BINDING:
  topic            → NOT: dialog, skill, intent handler
  trigger phrase   → NOT: intent, utterance class, NLU slot
  condition        → NOT: if-block, branch logic
  fallback topic   → NOT: default handler, catch-all
  escalation       → NOT: handoff, transfer
  session variable → NOT: slot, context variable, state variable
  redirect         → NOT: goto, jump, transfer
```

**0-D-3 Session Variable Registry**

```
SESSION_VARIABLE_REGISTRY:
  - Name: [variable name]
    PERSISTENCE_CLASS: EPHEMERAL | PERSISTENT | SESSION-SCOPED
    Set_By: [topic ID]
    Cleared_By: [topic ID | topic-exit | session-end]
    Read_By: [list of topic IDs]
```

**0-D-4 Structural Invariants**

Pre-commit named invariants representing design-time guarantees about the topology:

```
INVARIANT_REGISTRY:
  - ID: INVARIANT-TOPO-NN
    Claim: [structural claim about the topology]
    Scope: ALL_TOPICS | [specific topic IDs]
  - ID: INVARIANT-SV-NN
    Claim: [structural claim about session variable lifecycle]
    Scope: [variable name]
```

Every CONFIRMED_ABSENT defect row MUST cite the INVARIANT-TOPO-NN or INVARIANT-SV-NN that
structurally precludes the defect. A CONFIRMED_ABSENT row without an invariant citation is a
contract violation.

**0-D-5 Reachability Map**

Declare graph-level reachability before any trace output exists. This is the load-bearing
declaration for C-08 coverage metric denominator and ORPHAN defect detection.

```
REACHABILITY_MAP:
  Entry_Topic: [TOPIC-NN]
  Reachable_Topics:
    - TOPIC-NN (reachable via: [path description — by transitivity from entry])
    ...
  Orphaned_Topics:
    - TOPIC-NN (defined in TOPIC_REGISTRY but unreachable from Entry_Topic by any transition path)
    ...
```

Orphaned topics are ORPHAN defects — a fifth structural defect class at graph level rather than
execution level. ORPHAN defects are required findings regardless of whether orphaned topics appear
in any trace path. Their absence from the trace is evidence of the defect, not evidence of absence.

The C-08 coverage ratio denominator MUST use `reachable_visited / total_reachable` sourced from
this REACHABILITY_MAP. A ratio computed against `total_defined` when unreachable topics exist is
a measurement error.

*GAP_CLOSURE_VERDICT: CLOSED | OPEN [Gap-R7-03: reachability pre-computation with ORPHAN defect
class and C-08 denominator grounding]*

---

### PHASE 0-A — Auditor Assertion Contract

*You are the Auditor. Declare the complete assertion schema now. The Developer is bound to this
schema in all subsequent phases. The Developer SHALL NOT begin Phase 1 until Phase 0-A is
complete.*

**Trace Table Schema (Phase 1)**

Mandatory columns — blank cell in any mandatory column = structural violation:

```
| TURN | USER_UTTERANCE | TRIGGER_PHRASE_MATCHED | TOPIC | NODES_EXECUTED |
| SESSION_STATE | AGENT_RESPONSE | SPEC_CONFORMANCE | PROHIBITED_TERM_SCAN |
| INVARIANT_CONFORMANCE |
```

Column definitions:
- `SESSION_STATE`: all active session variables with current values and persistence class; mark
  CLEARED on topic exit for EPHEMERAL variables per SESSION_VARIABLE_REGISTRY
- `SPEC_CONFORMANCE`: `CONFORMS | DEVIATES[CS-SPEC-NN: description]`
- `PROHIBITED_TERM_SCAN`: `CLEAN | FOUND[term]`
- `INVARIANT_CONFORMANCE`: `HOLDS | VIOLATED[INVARIANT-ID: description]`

**Defect Classification Schema (Phase 2)**

```
DEFECT_CLASS: DEAD_END | INFINITE_LOOP | TRIGGER_PHRASE_COLLISION | MISSING_FALLBACK | ORPHAN
DEFECT_VERDICT: FOUND | CONFIRMED_ABSENT
```

```
| DEFECT_CLASS | DEFECT_VERDICT | EVIDENCE | INVARIANT_CITE |
```

- FOUND rows: EVIDENCE = exact reproduction sequence (utterance path → failure mode)
- CONFIRMED_ABSENT rows: INVARIANT_CITE required (INVARIANT-TOPO-NN or INVARIANT-SV-NN)
- ORPHAN rows: derived from REACHABILITY_MAP orphaned topics; DEFECT_VERDICT = FOUND;
  EVIDENCE = topic name and why it is unreachable from entry
- A CONFIRMED_ABSENT row without INVARIANT_CITE is a contract violation

**Recovery Path Schema (Phase 3-R)**

For every FOUND defect row, a recovery record is required:

```
| DEFECT_REF | RECOVERY_PATH | RECOVERY_VERDICT | UNRECOVERABLE_CONSEQUENCE |
```

- `RECOVERY_VERDICT`: `RECOVERABLE[min_turns=N, target=TOPIC-NN] | UNRECOVERABLE[reason]`
- `UNRECOVERABLE_CONSEQUENCE`: what happens to the user if they never escape the defect state
- CONFIRMED_ABSENT rows are exempt from recovery records
- A FOUND row without a RECOVERY record is a structural failure under this schema

**Other typed fields:**

```
FALLBACK_QUALITY: COMPLETE | LOOPS | TRUNCATED
ADVERSARIAL_OUTCOME: HANDLED | REDIRECT | FALLBACK_TRIGGERED | SESSION_CORRUPTED
GAP_CLOSURE_VERDICT: CLOSED | OPEN
```

No free-text in any verdict position. Free-text = contract violation.

---

### PHASE 1 — Developer: Dialog Trace

*You are the Developer. Walk the conversation turn-by-turn. Do not skip turns. Do not collapse
turns into summaries. Produce the mandatory 10-column trace table per Phase 0-A schema.*

Walk at minimum: happy path, one redirect path, one adversarial injection scenario. All columns
populated on every row. No turn may be skipped.

*GAP_CLOSURE_VERDICT: CLOSED | OPEN [Gap-R1-01: turn-by-turn dialog trace]*

---

### PHASE 2 — Developer: Defect Classification

*You are the Developer. Address all five defect classes explicitly. No class may be omitted.*

```
| DEFECT_CLASS | DEFECT_VERDICT | EVIDENCE | INVARIANT_CITE |
```

- `DEAD_END`: FOUND with reproduction OR CONFIRMED_ABSENT citing INVARIANT-TOPO-NN
- `INFINITE_LOOP`: FOUND with reproduction OR CONFIRMED_ABSENT citing INVARIANT-TOPO-NN
- `TRIGGER_PHRASE_COLLISION`: FOUND with competing topics + disambiguation strategy OR
  CONFIRMED_ABSENT citing scope
- `MISSING_FALLBACK`: FOUND with missing branch OR CONFIRMED_ABSENT citing INVARIANT-TOPO-NN
- `ORPHAN`: one row per orphaned topic from REACHABILITY_MAP; DEFECT_VERDICT = FOUND

*GAP_CLOSURE_VERDICT: CLOSED | OPEN [Gap-R1-02: all defect classes addressed including ORPHAN]*

---

### PHASE 3-R — Developer: Recovery Path Closure

*You are the Developer. For every FOUND defect row in Phase 2, produce a recovery record. If
Phase 2 has zero FOUND rows, produce one record: RECOVERY_REQUIRED: NONE with citation to all
CONFIRMED_ABSENT invariants.*

```
| DEFECT_REF | RECOVERY_PATH | RECOVERY_VERDICT | UNRECOVERABLE_CONSEQUENCE |
```

Walk the minimum recovery sequence for each FOUND defect. Count the turns. Name the target topic
the agent reaches when healthy. For UNRECOVERABLE: state the reason no escape path exists (e.g.,
"topic exit node absent," "fallback chain terminates in same defect") and describe the user
experience.

*GAP_CLOSURE_VERDICT: CLOSED | OPEN [Gap-R7-01: recovery path completeness per found defect]*

---

### PHASE 4 — Developer: Fallback Chain Trace

*You are the Developer. Trace one complete fallback path from unrecognized input to terminal
state. Show each node in the fallback chain. Include escalation if present. Show session variable
state at each step.*

`FALLBACK_QUALITY: COMPLETE | LOOPS | TRUNCATED`

If LOOPS: cite the INVARIANT-TOPO-NN that is VIOLATED.
If TRUNCATED: describe where the chain stops and why.

Inject one adversarial turn during fallback. Show `ADVERSARIAL_OUTCOME`.

*GAP_CLOSURE_VERDICT: CLOSED | OPEN [Gap-R2-04: fallback to terminal traced]*

---

### PHASE 5 — Developer: Coverage Summary

*You are the Developer. Report coverage ratios. The topic coverage denominator MUST derive from
the REACHABILITY_MAP (reachable_visited / total_reachable). A ratio computed against
total_defined when orphaned topics exist is a measurement error.*

```
| METRIC                                       | VISITED | TOTAL | RATIO |
| Topics (reachable_visited / total_reachable) | N       | M     | N/M   |
| Trigger phrases exercised                    | N       | M     | N/M   |
| Invariants verified HOLDS                    | N       | M     | N/M   |
| Session variables verified per class         | N       | M     | N/M   |
```

*GAP_CLOSURE_VERDICT: CLOSED | OPEN [Gap-R3-05: quantified coverage signal grounded in
declared reachability topology]*

---

### PHASE 5-V — Developer: Vocabulary Compliance Scan

*You are the Developer. Scan the full output for prohibited terms.*

```
| PROHIBITED_TERM | FOUND_IN_OUTPUT | LOCATION |
| intent          | YES | NO        |          |
| dialog          | YES | NO        |          |
| slot            | YES | NO        |          |
| NLU             | YES | NO        |          |
| chatbot         | YES | NO        |          |
| handoff         | YES | NO        |          |
```

*GAP_CLOSURE_VERDICT: CLOSED | OPEN [Gap-R4-10: active vocabulary enforcement]*

---

```
=== DEVELOPER ARTIFACT COMPLETE (Phases 0-D through 5-V) ===
=== AUDITOR NOW READS THE COMPLETED ARTIFACT AS A FINISHED DOCUMENT ===
```

---

### PHASE 6 — Auditor: Independent Audit

*You are the Auditor. You are now reading the Developer's completed artifact. Do not produce
inline commentary during trace. Read the full artifact, then produce this audit layer.*

**6-A: Trace Table Audit**

For each turn row, verify all mandatory columns are populated and enums are valid:

```
| TURN | SPEC_CONFORMANCE_VALID | PROHIBITED_TERM_SCAN_VALID | INVARIANT_CONFORMANCE_VALID | DISCREPANCY |
```

`DISCREPANCY: NONE | FOUND[column: issue]`

**6-B: Defect Matrix Audit**

For each defect class row, verify CONFIRMED_ABSENT rows carry valid invariant citations and
FOUND rows carry valid reproduction sequences:

```
| DEFECT_CLASS | INVARIANT_CITE_VALID | DISCREPANCY |
```

**6-C: Recovery Path Audit**

For each recovery record, independently verify the recovery path is minimal and the verdict is
correctly assigned:

```
| DEFECT_REF | RECOVERY_PATH_VALID | VERDICT_VALID | AUDITOR_RECOVERY_VERDICT | DISCREPANCY |
```

If Developer declared UNRECOVERABLE but Auditor identifies a path: `DISCREPANCY: FOUND[shorter
path exists]`. If Developer declared RECOVERABLE but path is incomplete: `DISCREPANCY:
FOUND[path does not reach healthy state]`.

**6-D: Invariant Cross-Audit**

For each declared invariant, compare Developer Phase 5 verdict against Auditor independent
assessment:

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
