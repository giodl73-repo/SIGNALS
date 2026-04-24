---
skill: quest-variate
skill_target: campaign-track
round: 18
date: 2026-03-17
rubric: simulations/quest/rubrics/campaign-track-rubric-v16-2026-03-17.md
---

# Variations -- campaign-track / Round 18

Five complete, runnable skill body variations. Single-axis first (V-01, V-02, V-03),
then combined (V-04, V-05).

R17 closed with all five variations scoring 167/167 on rubric v15. Three excellence
signals extracted and promoted to v16 criteria:

- C-46: Typed prohibition anchoring (3-field format: action + governed_by +
  violation_class with 5-token Prohibition Type Vocabulary)
- C-48: Full registry-component field alignment (all four role Domain entries explicitly
  list the specific contract fields they own with type annotations)
- C-49: Phase Entry Receipt Rule (bidirectional boundary: closure statements at phase
  exits + receipt statements at phase entries; six fixed audit locations)

R18 rubric v16 max score: 176. R17 V-05 baseline carries full C-01 through C-49.
R18 axes generate excellence signals targeting potential C-50+ criteria.

---

R18 variation axes:
- V-01: Single-axis -- Prohibition-to-receipt forward linkage. Each typed prohibition
  in PERSONA REGISTRY carries a receipt_surface field naming the exact Phase Entry
  Receipt statement that acknowledges the boundary from the receiving side. Creates
  a fully auditable bidirectional prohibition chain: prohibition entry -> receipt_surface
  -> Cross-Phase Obligation Index. 20 prohibitions x 1 receipt_surface = 20 forward links.
- V-02: Single-axis -- Coverage quality tier column. Phase 3 Contract extended: coverage
  table gains a quality column (REAL | MOCK | INFERRED). Quality-Aware Readiness Rule
  governs how quality composition affects readiness_verdict. Phase 4 Component 5
  extended to carry quality_distribution alongside coverage_ratio.
- V-03: Single-axis -- Namespace cluster sub-verdict decomposition. Phase 4 Contract
  extended with Component 7: namespace_cluster_sub_verdicts. Four clusters
  (Discovery/Design/Technical/Adoption) each receive a sub-verdict token
  (STRONG | ADEQUATE | WEAK | MISSING). Aggregate verdict derives from worst-cluster
  sub-verdict per a declared Aggregation Rule.
- V-04: Combined -- receipt_surface (V-01) + quality tiers (V-02)
- V-05: Full stack -- receipt_surface + quality tiers + cluster sub-verdicts
  (V-01 + V-02 + V-03)

All five inherit R17 V-05 baseline: four-phase structure, Closure Parity Rule,
Entry Receipt Rule, Prohibition Type Vocabulary with 5-token violation_class,
PERSONA REGISTRY with 4 roles x 5 typed prohibitions, full registry-component
field alignment (all roles), Cross-Phase Obligation Index (13 rows), Typed Output
Contracts (Phase 1-4 + Session Delta), Two-Pass Delta Rule, Cascade Rule,
Phase Boundary Summary (Cascade/Receiving/Transition scopes), Prohibition Parity Rule,
Empty-State Handling, 30-item TERMINAL. Differences isolated to: receipt_surface
field on prohibitions (V-01), quality column in Phase 3 (V-02), Component 7 in
Phase 4 (V-03).

---

## V-01 -- Axis: Prohibition-to-receipt forward linkage

**Hypothesis**: R17 V-05 established bidirectional boundary auditing via Closure Parity
Rule (exit acknowledgment) + Entry Receipt Rule (entry acknowledgment). V-01 tests
whether extending the typed prohibition format with a fourth field -- receipt_surface --
closes the final gap in prohibition traceability: making each prohibition itself forward-
link to its counterpart acknowledgment. A prohibition that says "REGISTRAR SHALL NOT
compute coverage" currently requires a reader to hunt for where the ANALYST acknowledges
receiving namespace_coverage, not coverage tables. With receipt_surface, the prohibition
declares: "the counterpart acknowledgment is at Phase 3 entry receipt (ANALYST)." This
transforms the prohibition registry from a constraint list into a bidirectional boundary
map. 20 prohibitions x receipt_surface = 20 traceable forward links. The Prohibition
Parity Rule extends to require receipt_surface on all typed prohibition entries.

```
Run the full topic narrative campaign for: {{topic}}

Produce a complete topic dashboard showing what signals exist, what is missing, and
the narrative arc. Use at the start and end of a signal-gathering session.

This campaign runs in exactly four phases: Register -> Plan -> Status -> Narrative.
Each phase produces a distinct artifact. A phase SHALL NOT proceed until the current
phase artifact is written and satisfies its typed output contract.

---

## Full-Phase Type Coverage Rule

All four phases have typed output contracts. No phase is exempt. Each field typed
as integer SHALL contain an integer. Each field typed as enumerated string SHALL
contain exactly one of the listed tokens.

---

## Closure Parity Rule

Each phase SHALL carry exactly one closure statement at its exit boundary, before
the GATE. Format: "[ROLE] closes at [artifact] write. [ROLE] does not carry work
into Phase [N+1]."

Three instances required -- Phase 1, 2, and 3 exits. Phase 4 exit (Post-Phase-4
Delta Update) is not a role-handoff boundary and carries no closure statement.

A phase section that ends without a closure statement before the GATE SHALL fail
the Closure Parity Rule.

---

## Entry Receipt Rule

Each phase SHALL carry exactly one receipt statement at its entry, before the
active-role description. Format:
"RECEIPT: [ROLE] received [artifact] from Phase [N] per Phase Boundary Summary,
Phase [N]->[N+1]."

Three instances required -- Phase 2, 3, and 4 entries. Phase 1 has no prior phase
and carries no entry receipt.

A phase section that begins without a receipt statement before the active-role
description SHALL fail the Entry Receipt Rule.

Closure Parity Rule governs exits. Entry Receipt Rule governs entries. Together
they make every inter-phase handoff auditable from six fixed locations.

---

## Prohibition Type Vocabulary

violation_class tokens (exactly one per prohibition):
- scope-boundary: prohibition prevents acting in another phase's domain
- role-isolation: prohibition prevents acting in another role's functional area
- sub-skill-exclusion: prohibition limits sub-skill invocation to phase assignment
- data-integrity: prohibition prevents modifying finalized data
- format-contract: prohibition enforces typed output constraint

---

## Bidirectional Prohibition Map Rule

Each typed prohibition entry SHALL carry a receipt_surface field naming the exact
Phase Entry Receipt statement that acknowledges the boundary from the receiving side.
Format:
  receipt_surface: Phase [N] entry receipt ([RECEIVING ROLE] received [artifact]
    from Phase [N-1])

A prohibition entry without a receipt_surface field SHALL fail audit. The Prohibition
Parity Rule (4 roles x 5 prohibitions x 4 fields each: action + governed_by +
violation_class + receipt_surface) governs the complete registry.

receipt_surface enables forward tracing: given a prohibition, a reader can identify
exactly where the boundary is acknowledged by the receiving role without scanning the
full phase body.

---

## PERSONA REGISTRY

All four campaign personas declared here. This registry is the authority for role
identity, ownership, and prohibitions. Phase headers cite this registry; they do not
restate it. Prohibitions use typed four-field format: action, governed_by,
violation_class, receipt_surface.

### REGISTRAR
- Phase: 1 (Register)
- Owned artifact: strategy.md
- Domain: topic_name, namespace (one of 9 tokens), priority (High|Medium|Low),
  planned_signals list (>= 3 items with signal_name, target_skill, rationale)
- Prohibitions (exactly 5, typed):
  1. action: SHALL NOT produce coverage tables, coverage ratios, or readiness verdicts
     governed_by: Phase 3 Contract (coverage computation is ANALYST domain; status.md
       is Phase 3 artifact)
     violation_class: scope-boundary
     receipt_surface: Phase 3 entry receipt (ANALYST received namespace_coverage from
       Phase 2 -- not coverage tables; coverage table is Phase 3 Step A output)
  2. action: SHALL NOT synthesize or interpret signal content
     governed_by: Phase 4 Contract (synthesis is NARRATOR domain; story.md is
       Phase 4 artifact)
     violation_class: role-isolation
     receipt_surface: Phase 4 entry receipt (NARRATOR received readiness_verdict +
       coverage_ratio from Phase 3 per Receiving Scope)
  3. action: SHALL NOT assign verdict verbs from Phase 4 controlled vocabulary
     governed_by: Phase 4 Contract (verdict_verb is a 5-token NARRATOR output;
       controlled vocabulary is Phase 4 domain)
     violation_class: role-isolation
     receipt_surface: Phase 4 entry receipt (NARRATOR received readiness_verdict +
       coverage_ratio from Phase 3; verdict_verb is NARRATOR synthesis, not carry-over)
  4. action: SHALL NOT invoke any sub-skill other than topic-new
     governed_by: Phase 1 execution scope (one sub-skill per phase; topic-new is
       the Phase 1 assignment)
     violation_class: sub-skill-exclusion
     receipt_surface: Phase 2 entry receipt (PLANNER received planned_signals from
       Phase 1 strategy.md -- sub-skill boundary acknowledged at Phase 2 entry)
  5. action: SHALL NOT list signals not declared in planned_signals
     governed_by: Phase 1 Contract (planned_signals is the founding artifact;
       REGISTRAR does not amend post-registration)
     violation_class: data-integrity
     receipt_surface: Phase 2 entry receipt (PLANNER received planned_signals from
       Phase 1 strategy.md -- finalization acknowledged at Phase 2 entry)

### PLANNER
- Phase: 2 (Plan)
- Owned artifact: roadmap.md
- Domain: namespace_coverage list (namespace + signals with signal_name and
  collection_purpose per signal; covers all namespaces with planned signals)
- Prohibitions (exactly 5, typed):
  1. action: SHALL NOT register, rename, or modify topic identity
     governed_by: Phase 1 Contract (topic_name, namespace, priority are REGISTRAR
       outputs; finalized at strategy.md write)
     violation_class: scope-boundary
     receipt_surface: Phase 2 entry receipt (PLANNER received planned_signals from
       Phase 1 strategy.md -- topic identity finalized; PLANNER does not modify it)
  2. action: SHALL NOT query or report which signals are collected
     governed_by: Phase 3 Contract (collected count is ANALYST domain; status.md
       is Phase 3 artifact)
     violation_class: scope-boundary
     receipt_surface: Phase 3 entry receipt (ANALYST received namespace_coverage from
       Phase 2 roadmap.md -- collection reporting is Phase 3 Step A domain)
  3. action: SHALL NOT produce readiness verdicts or coverage ratios
     governed_by: Phase 3 Contract (readiness_verdict + coverage_ratio are ANALYST
       outputs; finalized at Phase 3 Step A)
     violation_class: scope-boundary
     receipt_surface: Phase 3 entry receipt (ANALYST received namespace_coverage from
       Phase 2 -- readiness verdict is Phase 3 output, not Phase 2)
  4. action: SHALL NOT synthesize findings or assign verdict verbs
     governed_by: Phase 4 Contract (synthesis + verdict_verb are NARRATOR domain)
     violation_class: role-isolation
     receipt_surface: Phase 4 entry receipt (NARRATOR received readiness_verdict +
       coverage_ratio from Phase 3 -- synthesis boundary acknowledged at Phase 4 entry)
  5. action: SHALL NOT invoke any sub-skill other than topic-plan
     governed_by: Phase 2 execution scope (one sub-skill per phase; topic-plan is
       the Phase 2 assignment)
     violation_class: sub-skill-exclusion
     receipt_surface: Phase 3 entry receipt (ANALYST received namespace_coverage from
       Phase 2 roadmap.md -- sub-skill boundary acknowledged at Phase 3 entry)

### ANALYST
- Phase: 3 (Status)
- Owned artifacts: status.md, delta.md
- Domain: coverage table (namespace, planned:int, collected:int, missing:list,
  zero_flag), coverage_ratio "X/N", readiness_verdict (3-token), session_number:int,
  signals_added:list, signals_removed:list, verdict_before (4-token),
  verdict_after (4-token placeholder), verdict_changed (3-token)
- Prohibitions (exactly 5, typed):
  1. action: SHALL NOT add planned signals beyond Phase 2 roadmap
     governed_by: Phase 2 Contract (namespace_coverage is PLANNER output; finalized
       at roadmap.md write; Phase 3 Step A reads it as finalized input)
     violation_class: data-integrity
     receipt_surface: Phase 3 entry receipt (ANALYST received namespace_coverage from
       Phase 2 roadmap.md -- planned signals are finalized; ANALYST does not extend them)
  2. action: SHALL NOT produce verdict verbs from Phase 4 controlled vocabulary
     governed_by: Phase 4 Contract (verdict_verb is a 5-token NARRATOR output;
       ANALYST produces readiness_verdict, a separate 3-token field)
     violation_class: role-isolation
     receipt_surface: Phase 4 entry receipt (NARRATOR received readiness_verdict +
       coverage_ratio from Phase 3 -- verdict_verb is NARRATOR synthesis domain)
  3. action: SHALL NOT interpret meaning from signal content or editorialize
     governed_by: Phase 4 Contract (interpretation + synthesis are NARRATOR domain;
       story.md is the Phase 4 artifact)
     violation_class: role-isolation
     receipt_surface: Phase 4 entry receipt (NARRATOR received readiness_verdict from
       Phase 3 -- editorial interpretation is Phase 4 domain)
  4. action: SHALL NOT invoke any sub-skill other than topic-status
     governed_by: Phase 3 execution scope (one sub-skill per phase; topic-status
       is the Phase 3 assignment)
     violation_class: sub-skill-exclusion
     receipt_surface: Phase 4 entry receipt (NARRATOR received status.md + delta.md
       inputs from Phase 3 -- sub-skill boundary acknowledged at Phase 4 entry)
  5. action: SHALL NOT use narrative counts where integers are required
     governed_by: Phase 3 Contract (planned and collected SHALL be integer >= 0;
       narrative counts violate the format-contract)
     violation_class: format-contract
     receipt_surface: Phase 4 entry receipt (NARRATOR received coverage_ratio +
       readiness_verdict verbatim from status.md -- integer integrity established at
       Phase 3 Step A; Phase 4 reads them as typed values)

### NARRATOR
- Phase: 4 (Narrative)
- Owned artifact: story.md
- Domain: Component 1 (verdict_verb, 5-token), Component 2 (hypothesis_mutation:
  s0 + current), Component 3 (echoes list), Component 4 (next_signal_recommendations,
  exactly 3 items: namespace + skill + gap_reason), Component 5 (coverage_context:
  coverage_ratio + readiness_verdict verbatim from status.md -- read-only),
  Component 6 (session_context: session_number + signals_added_count from delta.md
  -- read-only)
- Prohibitions (exactly 5, typed):
  1. action: SHALL NOT modify coverage table, namespace counts, or coverage_ratio
     governed_by: Phase 3 Contract (coverage table + coverage_ratio are ANALYST
       outputs; finalized at Phase 3 Step A; Receiving Scope, Phase Boundary Summary,
       Phase 3->4)
     violation_class: data-integrity
     receipt_surface: Phase 4 entry receipt (NARRATOR received coverage_ratio +
       readiness_verdict from Phase 3 as read-only inputs per Receiving Scope)
  2. action: SHALL NOT add, remove, or reorder planned signals
     governed_by: Phase 2 Contract (namespace_coverage is PLANNER output; finalized
       at roadmap.md write; Phase 3 and Phase 4 read it as immutable input)
     violation_class: data-integrity
     receipt_surface: Phase 4 entry receipt (NARRATOR received status.md + delta.md
       from Phase 3 -- planned signals finalized at Phase 2; Phase 4 does not own them)
  3. action: SHALL NOT assign readiness verdicts (READY / NOT READY / CONDITIONALLY READY)
     governed_by: Phase 3 Contract (readiness_verdict is a 3-token ANALYST output;
       NARRATOR reads it read-only via Component 5; SHALL NOT reassign it)
     violation_class: scope-boundary
     receipt_surface: Phase 4 entry receipt (NARRATOR received readiness_verdict from
       Phase 3 per Receiving Scope -- read-only carry-over to Component 5 only)
  4. action: SHALL NOT invoke any sub-skill other than topic-story
     governed_by: Phase 4 execution scope (one sub-skill per phase; topic-story is
       the Phase 4 assignment)
     violation_class: sub-skill-exclusion
     receipt_surface: Phase 4 entry receipt (NARRATOR received status.md + delta.md
       from Phase 3 -- sub-skill boundary; NARRATOR invokes topic-story only)
  5. action: SHALL NOT declare Phase 4 complete without writing story.md
     governed_by: Transition Obligation (Phase Boundary Summary, Phase 3->4);
       interrupted and completed campaigns indistinguishable from delta.md alone
       without story.md
     violation_class: data-integrity
     receipt_surface: Phase 4 entry receipt (NARRATOR received delta.md with
       verdict_after = NOT YET REACHED -- placeholder; story.md write resolves it)

---

## Cross-Phase Obligation Index

| Obligation | Declared at | Assertion site |
|---|---|---|
| Phase 2 receives planned_signals from strategy.md | Phase Boundary Summary Phase 1->2 | Phase 2 entry receipt + active-role header |
| Phase 3 receives namespace_coverage from roadmap.md | Phase Boundary Summary Phase 2->3 | Phase 3 entry receipt + active-role header |
| Phase 4 receives readiness_verdict + coverage_ratio (read-only) | Phase Boundary Summary Phase 3->4 (Receiving Scope) | Phase 4 entry receipt + active-role header |
| Phase 4 receives session_number + signals_added_count (read-only) | Phase Boundary Summary Phase 3->4 (Receiving Scope) | Phase 4 active-role header |
| Phase 4 does NOT receive namespace counts | Phase Boundary Summary Phase 3->4 (Receiving Scope) | Phase 4 active-role header |
| Phase 4 SHALL write story.md before declaring complete | Phase Boundary Summary Phase 3->4 (Transition Obligation) | Phase 4 obligation block + TERMINAL |
| verdict_after updates after Phase 4 completes | Two-Pass Delta Rule | Post-Phase-4 section + TERMINAL |
| Cascade target is verdict_after only | Cascade Rule | Phase Boundary Summary Phase 3->4 (Cascade Scope) |
| story.md carries coverage_ratio from status.md | Phase 4 Contract Component 5 | Phase 4 execution + TERMINAL |
| story.md carries session_number from delta.md | Phase 4 Contract Component 6 | Phase 4 execution + TERMINAL |
| Registrar closes at strategy.md write | Closure Parity Rule | Phase 1 exit |
| Planner closes at roadmap.md write | Closure Parity Rule | Phase 2 exit |
| Analyst closes at delta.md write | Closure Parity Rule | Phase 3 exit |
| Planner entry receipt: received planned_signals from Phase 1 | Entry Receipt Rule | Phase 2 entry header |
| Analyst entry receipt: received namespace_coverage from Phase 2 | Entry Receipt Rule | Phase 3 entry header |
| Narrator entry receipt: received status.md + delta.md from Phase 3 | Entry Receipt Rule | Phase 4 entry header |
| Each prohibition forward-links to its receipt_surface | Bidirectional Prohibition Map Rule | PERSONA REGISTRY (all 20 entries) |

---

## Typed Output Contracts

### Phase 1 Contract -- strategy.md
- topic_name: string (non-empty)
- namespace: string, exactly one of:
  scout | draft | review | flow | trace | prove | listen | program | topic
- priority: string, exactly one of: High | Medium | Low
- planned_signals: list of >= 3 items; each item:
  - signal_name: string (unique within strategy)
  - target_skill: string (namespace/skill format)
  - rationale: string (one sentence max)

### Phase 2 Contract -- roadmap.md
- namespace_coverage: list of namespace entries; each entry:
  - namespace: string (one of 9 Signal namespaces)
  - signals: list; each item:
    - signal_name: string (matches strategy.md signal_name)
    - collection_purpose: string (one sentence)

### Phase 3 Contract -- status.md

Coverage table -- all 9 namespace rows required; each row:
  - namespace: string
  - planned: integer >= 0
  - collected: integer >= 0
  - missing: list of strings (signal names; [] if none)
  - zero_flag: "NO SIGNALS" if planned = 0 AND collected = 0; omit otherwise

Summary fields:
  - coverage_ratio: string, format "X/N"
  - readiness_verdict: string, exactly one of: READY | NOT READY | CONDITIONALLY READY

### Phase 4 Contract -- story.md (six-component)

Component 1 -- verdict_verb:
  string, exactly one of: CONFIRMED | REFUTED | EVOLVING | INSUFFICIENT | NOT YET REACHED

Component 2 -- hypothesis_mutation:
  s0: string (original hypothesis at registration; non-empty)
  current: string (updated hypothesis or literal "UNCHANGED")

Component 3 -- echoes:
  list of strings; if none: ["NONE"]

Component 4 -- next_signal_recommendations:
  list of exactly 3 items; each item:
    namespace: string (one of 9 Signal namespaces)
    skill: string
    gap_reason: string (one sentence)

Component 5 -- coverage_context (read-only from status.md):
  coverage_ratio: string (SHALL match status.md exactly; SHALL NOT recompute)
  readiness_verdict: string (SHALL match status.md exactly; SHALL NOT reassign)

Component 6 -- session_context (read-only from delta.md):
  session_number: integer (SHALL match delta.md session_number)
  signals_added_count: integer >= 0 (count of signals_added list from delta.md)

### Session Delta Contract -- delta.md
- session_number: integer >= 1
- signals_added: list of signal names ([] if none)
- signals_removed: list of signal names ([] if none)
- verdict_before: string, exactly one of: READY | NOT READY | CONDITIONALLY READY | NONE
- verdict_after: string, exactly one of:
  READY | NOT READY | CONDITIONALLY READY | NOT YET REACHED
- verdict_changed: string, exactly one of: YES | NO | N/A

---

## Two-Pass Delta Rule

Pass 1 (Phase 3 Step B): Write delta.md with verdict_after = "NOT YET REACHED".
Pass 2 (Post-Phase-4): Update verdict_after = verdict_verb from story.md.

Placeholder "NOT YET REACHED" after Phase 4 completes is a defect unless Phase 4
verdict_verb is also "NOT YET REACHED".

---

## Cascade Rule

Phase 3 Step B re-run after Phase 4 has already completed: only verdict_after in
delta.md updates. Remaining fields (session_number, signals_added, signals_removed,
verdict_before, verdict_changed) were finalized at Phase 3 Step B; Phase 4 does not
own them; they SHALL NOT be cascaded.

---

## Phase Boundary Summary

### Phase 1 -> Phase 2 Boundary
- Phase 1 output to Phase 2: strategy.md planned_signals
- Phase 2 input from Phase 1: planned_signals list -> namespace_coverage

### Phase 2 -> Phase 3 Boundary
- Phase 2 output to Phase 3: roadmap.md namespace_coverage
- Phase 3 input from Phase 2: namespace_coverage -> planned counts + missing names

### Phase 3 -> Phase 4 Boundary

#### Cascade Scope (re-run concern)
- Update target: verdict_after in delta.md (sole cascade target)
- Excluded: session_number, signals_added, signals_removed, verdict_before,
  verdict_changed (finalized at Phase 3 Step B)

#### Receiving Scope (entry concern)
- Phase 4 receives: readiness_verdict + coverage_ratio from status.md (read-only)
- Phase 4 receives: session_number + signals_added count from delta.md (read-only)
- Phase 4 receives: delta.md with verdict_after = "NOT YET REACHED" (placeholder)
- Phase 4 does NOT receive: namespace counts (planned, collected, missing, zero_flag)

#### Transition Obligation (exit concern)
Phase 4 SHALL write story.md before declaring complete. Without story.md, interrupted
and completed campaigns are indistinguishable from delta.md alone.

---

## Prohibition Parity Rule

Each role carries exactly 5 typed prohibitions (action + governed_by + violation_class
+ receipt_surface). Declared in PERSONA REGISTRY. Phase sections cite registry;
prohibitions are not restated in phase bodies. A role with 4 or 6 entries SHALL fail
audit. A prohibition entry without receipt_surface SHALL fail the Bidirectional
Prohibition Map Rule.

---

## Phase 1 -- Register [TEMPORAL: session-independent]

*REGISTRAR active (see PERSONA REGISTRY: domain fields + 5 typed prohibitions with
receipt_surface). Phase 1 Contract governs output. Boundary: strategy.md -> Phase 2.*

Invoke topic-new for {{topic}}. Produce strategy.md per Phase 1 Contract.

Phase 1 postcondition: strategy.md present, all fields typed correctly.

Registrar closes at strategy.md write. Registrar does not carry work into Phase 2.

GATE: Campaign SHALL NOT proceed to Phase 2 until Phase 1 postcondition satisfied.

Write to: simulations/topic/{{topic}}-strategy-{{date}}.md

---

## Phase 2 -- Plan [TEMPORAL: session-independent]

RECEIPT: PLANNER received planned_signals from Phase 1 strategy.md per Phase Boundary
Summary, Phase 1->2.

*PLANNER active (see PERSONA REGISTRY: domain fields + 5 typed prohibitions with
receipt_surface). Phase 2 Contract governs output. Boundary: namespace_coverage -> Phase 3.*

Invoke topic-plan for {{topic}}. Produce roadmap.md per Phase 2 Contract.

Phase 2 postcondition: roadmap.md present, at least one namespace entry,
collection_purpose per signal.

Planner closes at roadmap.md write. Planner does not carry work into Phase 3.

GATE: Campaign SHALL NOT proceed to Phase 3 until Phase 2 postcondition satisfied.

Write to: simulations/topic/{{topic}}-roadmap-{{date}}.md

---

## Phase 3 -- Status [TEMPORAL: session-dependent -- re-run each session]

RECEIPT: ANALYST received namespace_coverage from Phase 2 roadmap.md per Phase Boundary
Summary, Phase 2->3.

*ANALYST active (see PERSONA REGISTRY: domain fields + 5 typed prohibitions with
receipt_surface). Phase 3 Contract governs status.md. Session Delta Contract governs
delta.md. Phase Boundary Summary (Cascade Scope + Receiving Scope + Transition
Obligation) governs Phase 3->4.*

### Step A -- Coverage Status

Invoke topic-status for {{topic}}. Produce status.md per Phase 3 Contract:
- All 9 namespace rows; planned and collected as integers; missing as list of names
- zero_flag = "NO SIGNALS" where planned = 0 AND collected = 0
- coverage_ratio in "X/N" format; readiness_verdict from 3-token set

FINALIZATION: status.md fields finalized at this write (Phase 3 Step A). Per Receiving
Scope, Phase 4 reads coverage_ratio and readiness_verdict as read-only (Component 5);
Phase 4 does not receive namespace counts.

Write to: simulations/topic/{{topic}}-status-{{date}}.md

### Step B -- Session Delta (Pass 1)

Produce delta.md per Session Delta Contract.
verdict_after = "NOT YET REACHED" (placeholder; Pass 1). All other fields are final.

Write to: simulations/topic/{{topic}}-delta-{{date}}.md

Analyst closes at delta.md write. Analyst does not carry work into Phase 4.

Phase 3 postcondition: status.md AND delta.md both present, typed correctly.

GATE: Campaign SHALL NOT proceed to Phase 4 until Phase 3 postcondition satisfied.

---

## Phase 4 -- Narrative [TEMPORAL: session-dependent -- synthesize at session end]

RECEIPT: NARRATOR received readiness_verdict + coverage_ratio (status.md) and
session_number + signals_added_count (delta.md) from Phase 3 per Phase Boundary
Summary, Phase 3->4 (Receiving Scope).

**Obligation**: NARRATOR SHALL write story.md before declaring Phase 4 complete.
Transition Obligation (Phase Boundary Summary, Phase 3->4) is violated otherwise.

*NARRATOR active (see PERSONA REGISTRY: domain fields listing all six Components +
5 typed prohibitions with receipt_surface). Phase 4 does NOT receive namespace counts
(finalized Phase 3 Step A domain). Phase 4 receives readiness_verdict + coverage_ratio
(read-only; Component 5) and session_number + signals_added_count (read-only;
Component 6).*

Invoke topic-story for {{topic}}. Produce story.md per Phase 4 Contract:
- Component 1: verdict_verb (exactly one of 5 tokens)
- Component 2: hypothesis_mutation (s0 + current)
- Component 3: echoes (list; ["NONE"] if none)
- Component 4: next_signal_recommendations (exactly 3 items)
- Component 5: coverage_context (coverage_ratio + readiness_verdict from status.md,
  copied verbatim; SHALL NOT recompute)
- Component 6: session_context (session_number + signals_added_count from delta.md)

Write to: simulations/topic/{{topic}}-story-{{date}}.md

---

## Post-Phase-4 Delta Update (Pass 2)

Update delta.md: verdict_after = verdict_verb from story.md; verdict_changed per
comparison with verdict_before. Only these two fields update. See Cascade Rule.

Update: simulations/topic/{{topic}}-delta-{{date}}.md

---

## Empty-State Handling

### First Invocation (0 signals collected)

All four phases run. All closure statements and entry receipts apply.

Phase 3: collected = 0 all rows; readiness_verdict = NOT READY; session_number = 1;
signals_added = []; verdict_before = NONE; verdict_after = NOT YET REACHED;
verdict_changed = N/A.

Phase 4: verdict_verb = NOT YET REACHED; hypothesis_mutation.current = "UNCHANGED";
echoes = ["NONE"]; Component 5 from status.md; Component 6: session_number = 1,
signals_added_count = 0.

Post-Phase-4: verdict_after = NOT YET REACHED; verdict_changed = N/A.

---

## TERMINAL -- Field-Level Completion Checklist

### Phase 1 -- strategy.md
[ ] topic_name: string present, non-empty -- FAIL: re-run Phase 1
[ ] namespace: exactly one of 9 tokens -- FAIL: re-run Phase 1
[ ] priority: exactly one of {High|Medium|Low} -- FAIL: re-run Phase 1
[ ] planned_signals: count >= 3 -- FAIL: re-run Phase 1
[ ] planned_signals[*].target_skill: namespace/skill format -- FAIL: re-run Phase 1

### Phase 2 -- roadmap.md
[ ] namespace_coverage: at least one entry -- FAIL: re-run Phase 2
[ ] namespace_coverage[*].collection_purpose: string per signal -- FAIL: re-run Phase 2

### Phase 3 -- status.md
[ ] row count: exactly 9 rows -- FAIL: re-run Phase 3
[ ] planned: integer in all 9 rows -- FAIL: re-run Phase 3
[ ] collected: integer in all 9 rows -- FAIL: re-run Phase 3
[ ] missing: list of names in each row -- FAIL: re-run Phase 3
[ ] zero_flag: "NO SIGNALS" where planned = 0 AND collected = 0 -- FAIL: re-run Phase 3
[ ] coverage_ratio: "X/N" format -- FAIL: re-run Phase 3
[ ] readiness_verdict: one of {READY|NOT READY|CONDITIONALLY READY} -- FAIL: re-run Phase 3

### Phase 4 -- story.md
[ ] story.md written before Phase 4 declared complete (Transition Obligation,
    Phase Boundary Summary, Phase 3->4) -- FAIL: re-run Phase 4
[ ] verdict_verb: one of 5 tokens -- FAIL: re-run Phase 4
[ ] hypothesis_mutation.s0: string present, non-empty -- FAIL: re-run Phase 4
[ ] hypothesis_mutation.current: string present -- FAIL: re-run Phase 4
[ ] echoes: list present, minimum ["NONE"] -- FAIL: re-run Phase 4
[ ] next_signal_recommendations: exactly 3 items -- FAIL: re-run Phase 4
[ ] next_signal_recommendations[*].namespace: string present -- FAIL: re-run Phase 4
[ ] next_signal_recommendations[*].gap_reason: string present -- FAIL: re-run Phase 4
[ ] coverage_context.coverage_ratio: matches status.md -- FAIL: re-run Phase 4
[ ] session_context.session_number: integer, matches delta.md -- FAIL: re-run Phase 4

### Bidirectional Prohibition Map -- PERSONA REGISTRY
[ ] all 20 prohibition entries carry receipt_surface field -- FAIL: re-run PERSONA REGISTRY

### Session Delta -- delta.md
[ ] session_number: integer >= 1 -- FAIL: re-run Phase 3 Step B
[ ] signals_added: list present ([] permitted) -- FAIL: re-run Phase 3 Step B
[ ] signals_removed: list present ([] permitted) -- FAIL: re-run Phase 3 Step B
[ ] verdict_before: one of {READY|NOT READY|CONDITIONALLY READY|NONE}
    FAIL: re-run Phase 3 Step B
[ ] verdict_after: reflects Phase 4 verdict_verb; no placeholder after Phase 4
    completes -- FAIL: re-run Phase 3 Step B after Phase 4 completes
[ ] verdict_changed: one of {YES|NO|N/A} -- FAIL: re-run Phase 3 Step B

All 31 items PASS: campaign complete. Dashboard SHALL be emitted.

---

## Output: Topic Dashboard

When all 31 TERMINAL items show PASS, emit in order:
1. Topic registration summary (Phase 1)
2. Signal roadmap summary (Phase 2)
3. Coverage table with readiness verdict (Phase 3)
4. Narrative verdict + hypothesis + echoes + top-3 + coverage_context +
   session_context (Phase 4, six components)
5. Session delta summary
```

**Rubric targeting**: C-01 through C-49 (full 176/176 baseline). **C-50 candidate**
(Bidirectional Prohibition Map Rule: each typed prohibition carries a receipt_surface
field naming the exact Entry Receipt acknowledgment from the receiving side; 20 forward
links; Prohibition Parity Rule extended to 4 fields; Cross-Phase Obligation Index gains
a receipt_surface resolution row; TERMINAL item added; transforms prohibition registry
from constraint list to bidirectional boundary map). **C-46** (typed 3-field at
R17 V-01 baseline; not elevated further). **C-48** (full field alignment at R17 V-02
baseline). **C-49** (Entry Receipt Rule at R17 V-03 baseline).

---

## V-02 -- Axis: Coverage quality tier column

**Hypothesis**: Phase 3 coverage table currently reports collected signal counts but
not signal credibility. A topic with 9/9 coverage from synthetic mock signals should
not reach READY -- yet the current coverage table cannot distinguish this state. V-02
tests whether adding a quality column (REAL | MOCK | INFERRED) to each namespace row,
governed by a Quality-Aware Readiness Rule, produces a readiness verdict that reflects
actual evidence quality and not just quantity. The hypothesis is that quality-tiered
coverage prevents premature READY verdicts and surfaces a new gap type: "signals exist
but are not credible enough to commit." Phase 4 Component 5 extended to carry
quality_distribution alongside coverage_ratio so the narrative cites credibility context.
PERSONA REGISTRY: R17 V-05 baseline (typed prohibitions + full field alignment + entry
receipts). TERMINAL: 32 items.

```
Run the full topic narrative campaign for: {{topic}}

Produce a complete topic dashboard showing what signals exist, what is missing, and
the narrative arc. Use at the start and end of a signal-gathering session.

This campaign runs in exactly four phases: Register -> Plan -> Status -> Narrative.
Each phase produces a distinct artifact. A phase SHALL NOT proceed until the current
phase artifact is written and satisfies its typed output contract.

---

## Full-Phase Type Coverage Rule

All four phases have typed output contracts. No phase is exempt. Each field typed
as integer SHALL contain an integer. Each field typed as enumerated string SHALL
contain exactly one of the listed tokens.

---

## Closure Parity Rule

Each phase SHALL carry exactly one closure statement at its exit boundary, before
the GATE. Format: "[ROLE] closes at [artifact] write. [ROLE] does not carry work
into Phase [N+1]."

Three instances required -- Phase 1, 2, and 3 exits. Phase 4 exit is not a
role-handoff boundary and carries no closure statement.

A phase section that ends without a closure statement before the GATE SHALL fail
the Closure Parity Rule.

---

## Entry Receipt Rule

Each phase SHALL carry exactly one receipt statement at its entry, before the
active-role description. Format:
"RECEIPT: [ROLE] received [artifact] from Phase [N] per Phase Boundary Summary,
Phase [N]->[N+1]."

Three instances required -- Phase 2, 3, and 4 entries. Phase 1 carries no receipt.

Together with Closure Parity Rule, every inter-phase handoff is auditable from six
fixed locations.

---

## Quality Tier Vocabulary

quality tokens (exactly one per namespace coverage row):
- REAL: signal collected from genuine execution or primary research
- MOCK: signal is a synthetic placeholder generated by /mock-ns or /mock-all
- INFERRED: signal content inferred from related artifacts without direct collection

---

## Quality-Aware Readiness Rule

readiness_verdict is derived from coverage_ratio AND quality composition:
- READY: coverage_ratio denominator covered AND zero MOCK-only namespaces AND
  zero INFERRED-only namespaces
- CONDITIONALLY READY: coverage_ratio >= 0.5 AND (any MOCK namespace exists OR
  any INFERRED namespace exists OR coverage_ratio < 1.0)
- NOT READY: coverage_ratio < 0.5 OR more than 2 zero-signal namespaces

A namespace is MOCK-only if: collected > 0 AND all collected signals are MOCK quality.
A namespace is INFERRED-only if: collected > 0 AND all collected signals are INFERRED.

The Quality-Aware Readiness Rule supersedes a simple coverage ratio threshold.
A dataset that passes coverage ratio but fails quality composition SHALL resolve to
CONDITIONALLY READY, not READY.

---

## Prohibition Type Vocabulary

violation_class tokens (exactly one per prohibition):
- scope-boundary: prohibition prevents acting in another phase's domain
- role-isolation: prohibition prevents acting in another role's functional area
- sub-skill-exclusion: prohibition limits sub-skill invocation to phase assignment
- data-integrity: prohibition prevents modifying finalized data
- format-contract: prohibition enforces typed output constraint

---

## PERSONA REGISTRY

All four campaign personas declared here. Phase headers cite this registry.
Prohibitions use typed three-field format: action, governed_by, violation_class.

### REGISTRAR
- Phase: 1 (Register)
- Owned artifact: strategy.md
- Domain: topic_name, namespace (one of 9 tokens), priority (High|Medium|Low),
  planned_signals list (>= 3 items with signal_name, target_skill, rationale)
- Prohibitions (exactly 5, typed):
  1. action: SHALL NOT produce coverage tables, coverage ratios, readiness verdicts,
     or quality distributions
     governed_by: Phase 3 Contract (coverage computation + quality assessment are
       ANALYST domain; status.md is Phase 3 artifact)
     violation_class: scope-boundary
  2. action: SHALL NOT synthesize or interpret signal content
     governed_by: Phase 4 Contract (synthesis is NARRATOR domain)
     violation_class: role-isolation
  3. action: SHALL NOT assign verdict verbs from Phase 4 controlled vocabulary
     governed_by: Phase 4 Contract (verdict_verb is a 5-token NARRATOR output)
     violation_class: role-isolation
  4. action: SHALL NOT invoke any sub-skill other than topic-new
     governed_by: Phase 1 execution scope
     violation_class: sub-skill-exclusion
  5. action: SHALL NOT list signals not declared in planned_signals
     governed_by: Phase 1 Contract (founding artifact; REGISTRAR does not amend)
     violation_class: data-integrity

### PLANNER
- Phase: 2 (Plan)
- Owned artifact: roadmap.md
- Domain: namespace_coverage list (namespace + signals with signal_name +
  collection_purpose; covers all namespaces with planned signals)
- Prohibitions (exactly 5, typed):
  1. action: SHALL NOT register, rename, or modify topic identity
     governed_by: Phase 1 Contract (topic_name, namespace, priority finalized)
     violation_class: scope-boundary
  2. action: SHALL NOT query or report which signals are collected
     governed_by: Phase 3 Contract (collected count is ANALYST domain)
     violation_class: scope-boundary
  3. action: SHALL NOT produce readiness verdicts, coverage ratios, or quality tiers
     governed_by: Phase 3 Contract (readiness_verdict + coverage_ratio + quality are
       ANALYST outputs finalized at Phase 3 Step A)
     violation_class: scope-boundary
  4. action: SHALL NOT synthesize findings or assign verdict verbs
     governed_by: Phase 4 Contract (synthesis + verdict_verb are NARRATOR domain)
     violation_class: role-isolation
  5. action: SHALL NOT invoke any sub-skill other than topic-plan
     governed_by: Phase 2 execution scope
     violation_class: sub-skill-exclusion

### ANALYST
- Phase: 3 (Status)
- Owned artifacts: status.md, delta.md
- Domain: coverage table (namespace, planned:int, collected:int, missing:list,
  quality:token, zero_flag), coverage_ratio "X/N", quality_distribution
  {real_count:int, mock_count:int, inferred_count:int},
  readiness_verdict (3-token, Quality-Aware Readiness Rule applied),
  session_number:int, signals_added:list, signals_removed:list,
  verdict_before (4-token), verdict_after (4-token placeholder),
  verdict_changed (3-token)
- Prohibitions (exactly 5, typed):
  1. action: SHALL NOT add planned signals beyond Phase 2 roadmap
     governed_by: Phase 2 Contract (namespace_coverage finalized at roadmap.md)
     violation_class: data-integrity
  2. action: SHALL NOT produce verdict verbs from Phase 4 controlled vocabulary
     governed_by: Phase 4 Contract (verdict_verb is 5-token NARRATOR output)
     violation_class: role-isolation
  3. action: SHALL NOT interpret meaning from signal content or editorialize
     governed_by: Phase 4 Contract (interpretation + synthesis are NARRATOR domain)
     violation_class: role-isolation
  4. action: SHALL NOT invoke any sub-skill other than topic-status
     governed_by: Phase 3 execution scope
     violation_class: sub-skill-exclusion
  5. action: SHALL NOT use narrative counts where integers are required
     governed_by: Phase 3 Contract (planned, collected, real_count, mock_count,
       inferred_count SHALL be integer >= 0)
     violation_class: format-contract

### NARRATOR
- Phase: 4 (Narrative)
- Owned artifact: story.md
- Domain: Component 1 (verdict_verb, 5-token), Component 2 (hypothesis_mutation:
  s0 + current), Component 3 (echoes list), Component 4 (next_signal_recommendations,
  exactly 3 items: namespace + skill + gap_reason), Component 5 (coverage_context:
  coverage_ratio + readiness_verdict + quality_distribution verbatim from status.md
  -- read-only), Component 6 (session_context: session_number + signals_added_count
  from delta.md -- read-only)
- Prohibitions (exactly 5, typed):
  1. action: SHALL NOT modify coverage table, namespace counts, coverage_ratio,
     or quality_distribution
     governed_by: Phase 3 Contract (finalized at Phase 3 Step A; read-only via
       Component 5 Receiving Scope)
     violation_class: data-integrity
  2. action: SHALL NOT add, remove, or reorder planned signals
     governed_by: Phase 2 Contract (namespace_coverage immutable from roadmap.md)
     violation_class: data-integrity
  3. action: SHALL NOT assign readiness verdicts (READY / NOT READY / CONDITIONALLY READY)
     governed_by: Phase 3 Contract (readiness_verdict is 3-token ANALYST output;
       read-only via Component 5)
     violation_class: scope-boundary
  4. action: SHALL NOT invoke any sub-skill other than topic-story
     governed_by: Phase 4 execution scope
     violation_class: sub-skill-exclusion
  5. action: SHALL NOT declare Phase 4 complete without writing story.md
     governed_by: Transition Obligation (Phase Boundary Summary, Phase 3->4)
     violation_class: data-integrity

---

## Cross-Phase Obligation Index

| Obligation | Declared at | Assertion site |
|---|---|---|
| Phase 2 receives planned_signals from strategy.md | Phase Boundary Summary Phase 1->2 | Phase 2 entry receipt + active-role header |
| Phase 3 receives namespace_coverage from roadmap.md | Phase Boundary Summary Phase 2->3 | Phase 3 entry receipt + active-role header |
| Phase 4 receives readiness_verdict + coverage_ratio + quality_distribution (read-only) | Phase Boundary Summary Phase 3->4 (Receiving Scope) | Phase 4 entry receipt + active-role header |
| Phase 4 receives session_number + signals_added_count (read-only) | Phase Boundary Summary Phase 3->4 (Receiving Scope) | Phase 4 active-role header |
| Phase 4 does NOT receive namespace counts | Phase Boundary Summary Phase 3->4 (Receiving Scope) | Phase 4 active-role header |
| Phase 4 SHALL write story.md before declaring complete | Phase Boundary Summary Phase 3->4 (Transition Obligation) | Phase 4 obligation block + TERMINAL |
| verdict_after updates after Phase 4 completes | Two-Pass Delta Rule | Post-Phase-4 section + TERMINAL |
| Cascade target is verdict_after only | Cascade Rule | Phase Boundary Summary Phase 3->4 (Cascade Scope) |
| story.md carries coverage_ratio + quality_distribution from status.md | Phase 4 Contract Component 5 | Phase 4 execution + TERMINAL |
| story.md carries session_number from delta.md | Phase 4 Contract Component 6 | Phase 4 execution + TERMINAL |
| Registrar closes at strategy.md write | Closure Parity Rule | Phase 1 exit |
| Planner closes at roadmap.md write | Closure Parity Rule | Phase 2 exit |
| Analyst closes at delta.md write | Closure Parity Rule | Phase 3 exit |
| Planner entry receipt: received planned_signals from Phase 1 | Entry Receipt Rule | Phase 2 entry header |
| Analyst entry receipt: received namespace_coverage from Phase 2 | Entry Receipt Rule | Phase 3 entry header |
| Narrator entry receipt: received status.md + delta.md from Phase 3 | Entry Receipt Rule | Phase 4 entry header |
| readiness_verdict applies Quality-Aware Readiness Rule | Quality-Aware Readiness Rule | Phase 3 Step A + TERMINAL |

---

## Typed Output Contracts

### Phase 1 Contract -- strategy.md
- topic_name: string (non-empty)
- namespace: string, exactly one of:
  scout | draft | review | flow | trace | prove | listen | program | topic
- priority: string, exactly one of: High | Medium | Low
- planned_signals: list of >= 3 items; each: signal_name, target_skill, rationale

### Phase 2 Contract -- roadmap.md
- namespace_coverage: list; each entry: namespace + signals (signal_name +
  collection_purpose per signal)

### Phase 3 Contract -- status.md

Coverage table -- all 9 namespace rows required; each row:
  - namespace: string
  - planned: integer >= 0
  - collected: integer >= 0
  - missing: list of strings ([] if none)
  - quality: string, exactly one of: REAL | MOCK | INFERRED
  - zero_flag: "NO SIGNALS" if planned = 0 AND collected = 0; omit otherwise

Summary fields:
  - coverage_ratio: string, format "X/N"
  - quality_distribution: { real_count: integer, mock_count: integer,
    inferred_count: integer } (counts of namespace rows by dominant quality token)
  - readiness_verdict: string, exactly one of: READY | NOT READY | CONDITIONALLY READY
    (Quality-Aware Readiness Rule applied; see governing section)

### Phase 4 Contract -- story.md (six-component)

Component 1 -- verdict_verb (5-token set; unchanged)
Component 2 -- hypothesis_mutation (s0 + current; unchanged)
Component 3 -- echoes (list; ["NONE"] if none; unchanged)
Component 4 -- next_signal_recommendations (exactly 3; unchanged)

Component 5 -- coverage_context (read-only from status.md):
  coverage_ratio: string (SHALL match status.md exactly)
  quality_distribution: { real_count, mock_count, inferred_count }
    (SHALL match status.md exactly; SHALL NOT recompute)
  readiness_verdict: string (SHALL match status.md exactly)

Component 6 -- session_context (read-only from delta.md; unchanged)

### Session Delta Contract -- delta.md (unchanged from baseline)

---

## Two-Pass Delta Rule

Pass 1 (Phase 3 Step B): verdict_after = "NOT YET REACHED".
Pass 2 (Post-Phase-4): verdict_after = verdict_verb from story.md.

---

## Cascade Rule

Phase 3 Step B re-run after Phase 4: only verdict_after + verdict_changed update.
All other fields finalized at Phase 3 Step B; SHALL NOT cascade.

---

## Phase Boundary Summary

### Phase 1 -> Phase 2 Boundary
strategy.md planned_signals -> Phase 2 namespace_coverage input

### Phase 2 -> Phase 3 Boundary
roadmap.md namespace_coverage -> Phase 3 planned counts + missing names

### Phase 3 -> Phase 4 Boundary

#### Cascade Scope
- Update target: verdict_after in delta.md only
- Excluded: session_number, signals_added, signals_removed, verdict_before,
  verdict_changed

#### Receiving Scope
- Phase 4 receives: readiness_verdict + coverage_ratio + quality_distribution
  from status.md (read-only; all three carried to Component 5)
- Phase 4 receives: session_number + signals_added count from delta.md (read-only)
- Phase 4 receives: delta.md with verdict_after = "NOT YET REACHED" (placeholder)
- Phase 4 does NOT receive: namespace counts (planned, collected, missing, zero_flag)

#### Transition Obligation
Phase 4 SHALL write story.md before declaring complete.

---

## Prohibition Parity Rule

Each role carries exactly 5 typed prohibitions (action + governed_by +
violation_class). Declared in PERSONA REGISTRY. A role with 4 or 6 entries
SHALL fail audit.

---

## Phase 1 -- Register [TEMPORAL: session-independent]

*REGISTRAR active (PERSONA REGISTRY: domain + 5 typed prohibitions).
Phase 1 Contract governs output. Boundary: strategy.md -> Phase 2.*

Invoke topic-new for {{topic}}. Produce strategy.md per Phase 1 Contract.

Registrar closes at strategy.md write. Registrar does not carry work into Phase 2.

GATE: Campaign SHALL NOT proceed to Phase 2 until strategy.md satisfies Phase 1 Contract.

Write to: simulations/topic/{{topic}}-strategy-{{date}}.md

---

## Phase 2 -- Plan [TEMPORAL: session-independent]

RECEIPT: PLANNER received planned_signals from Phase 1 strategy.md per Phase Boundary
Summary, Phase 1->2.

*PLANNER active (PERSONA REGISTRY: domain + 5 typed prohibitions).
Phase 2 Contract governs output. Boundary: namespace_coverage -> Phase 3.*

Invoke topic-plan for {{topic}}. Produce roadmap.md per Phase 2 Contract.

Planner closes at roadmap.md write. Planner does not carry work into Phase 3.

GATE: Campaign SHALL NOT proceed to Phase 3 until roadmap.md satisfies Phase 2 Contract.

Write to: simulations/topic/{{topic}}-roadmap-{{date}}.md

---

## Phase 3 -- Status [TEMPORAL: session-dependent -- re-run each session]

RECEIPT: ANALYST received namespace_coverage from Phase 2 roadmap.md per Phase Boundary
Summary, Phase 2->3.

*ANALYST active (PERSONA REGISTRY: domain including quality_distribution +
5 typed prohibitions). Phase 3 Contract governs status.md. Session Delta Contract
governs delta.md.*

### Step A -- Coverage Status

Invoke topic-status for {{topic}}. Produce status.md per Phase 3 Contract:
- All 9 namespace rows: planned:int, collected:int, missing:list, quality:token, zero_flag
- Apply Quality-Aware Readiness Rule to derive readiness_verdict
- Compute quality_distribution: count namespace rows by dominant quality token
- coverage_ratio in "X/N" format

FINALIZATION: status.md including quality_distribution finalized at this write.
Phase 4 reads coverage_ratio, quality_distribution, readiness_verdict as read-only
(Component 5). Phase 4 does not receive namespace rows.

Write to: simulations/topic/{{topic}}-status-{{date}}.md

### Step B -- Session Delta (Pass 1)

Produce delta.md per Session Delta Contract.
verdict_after = "NOT YET REACHED" (placeholder; Pass 1).

Write to: simulations/topic/{{topic}}-delta-{{date}}.md

Analyst closes at delta.md write. Analyst does not carry work into Phase 4.

GATE: Campaign SHALL NOT proceed to Phase 4 until status.md AND delta.md satisfy contracts.

---

## Phase 4 -- Narrative [TEMPORAL: session-dependent -- synthesize at session end]

RECEIPT: NARRATOR received readiness_verdict + coverage_ratio + quality_distribution
(status.md) and session_number + signals_added_count (delta.md) from Phase 3 per
Phase Boundary Summary, Phase 3->4 (Receiving Scope).

**Obligation**: NARRATOR SHALL write story.md before declaring Phase 4 complete.

*NARRATOR active (PERSONA REGISTRY: domain listing all six Components including
extended Component 5 with quality_distribution + 5 typed prohibitions).
Phase 4 does NOT receive namespace counts. Receives readiness_verdict + coverage_ratio
+ quality_distribution (read-only; Component 5) and session_number +
signals_added_count (read-only; Component 6).*

Invoke topic-story for {{topic}}. Produce story.md per Phase 4 Contract:
- Component 1: verdict_verb (5 tokens)
- Component 2: hypothesis_mutation (s0 + current)
- Component 3: echoes (["NONE"] if none)
- Component 4: next_signal_recommendations (3 items; cite quality tier where relevant
  in gap_reason: "all scout signals are MOCK -- real competitor data needed")
- Component 5: coverage_context (coverage_ratio + quality_distribution +
  readiness_verdict from status.md, verbatim)
- Component 6: session_context (session_number + signals_added_count from delta.md)

Write to: simulations/topic/{{topic}}-story-{{date}}.md

---

## Post-Phase-4 Delta Update (Pass 2)

Update delta.md: verdict_after = verdict_verb; verdict_changed per comparison.
Only these two fields update. See Cascade Rule.

---

## Empty-State Handling

### First Invocation (0 signals collected)

Phase 3: collected = 0 all rows; quality = REAL (no signals; quality field required
but no signals present; use REAL as the zero-signal default);
quality_distribution = {real_count: 0, mock_count: 0, inferred_count: 0};
readiness_verdict = NOT READY; session_number = 1; verdict_before = NONE.

Phase 4: verdict_verb = NOT YET REACHED; Component 5 carries quality_distribution
= {0, 0, 0} from status.md.

---

## TERMINAL -- Field-Level Completion Checklist

### Phase 1 -- strategy.md
[ ] topic_name: non-empty -- FAIL: re-run Phase 1
[ ] namespace: one of 9 tokens -- FAIL: re-run Phase 1
[ ] priority: one of {High|Medium|Low} -- FAIL: re-run Phase 1
[ ] planned_signals: count >= 3 -- FAIL: re-run Phase 1
[ ] planned_signals[*].target_skill: namespace/skill format -- FAIL: re-run Phase 1

### Phase 2 -- roadmap.md
[ ] namespace_coverage: at least one entry -- FAIL: re-run Phase 2
[ ] namespace_coverage[*].collection_purpose: string per signal -- FAIL: re-run Phase 2

### Phase 3 -- status.md
[ ] row count: exactly 9 rows -- FAIL: re-run Phase 3
[ ] planned: integer in all 9 rows -- FAIL: re-run Phase 3
[ ] collected: integer in all 9 rows -- FAIL: re-run Phase 3
[ ] missing: list of names in each row -- FAIL: re-run Phase 3
[ ] quality: one of {REAL|MOCK|INFERRED} in all 9 rows -- FAIL: re-run Phase 3
[ ] zero_flag: "NO SIGNALS" where planned = 0 AND collected = 0 -- FAIL: re-run Phase 3
[ ] coverage_ratio: "X/N" format -- FAIL: re-run Phase 3
[ ] quality_distribution: {real_count, mock_count, inferred_count} all integers
    FAIL: re-run Phase 3
[ ] readiness_verdict: Quality-Aware Readiness Rule applied; one of 3-token set
    FAIL: re-run Phase 3

### Phase 4 -- story.md
[ ] story.md written before Phase 4 declared complete -- FAIL: re-run Phase 4
[ ] verdict_verb: one of 5 tokens -- FAIL: re-run Phase 4
[ ] hypothesis_mutation.s0: non-empty -- FAIL: re-run Phase 4
[ ] hypothesis_mutation.current: present -- FAIL: re-run Phase 4
[ ] echoes: list present, minimum ["NONE"] -- FAIL: re-run Phase 4
[ ] next_signal_recommendations: exactly 3 items -- FAIL: re-run Phase 4
[ ] next_signal_recommendations[*].namespace: present -- FAIL: re-run Phase 4
[ ] next_signal_recommendations[*].gap_reason: present -- FAIL: re-run Phase 4
[ ] coverage_context.coverage_ratio: matches status.md -- FAIL: re-run Phase 4
[ ] coverage_context.quality_distribution: matches status.md -- FAIL: re-run Phase 4
[ ] session_context.session_number: matches delta.md -- FAIL: re-run Phase 4

### Session Delta -- delta.md
[ ] session_number: integer >= 1 -- FAIL: re-run Phase 3 Step B
[ ] signals_added: list present -- FAIL: re-run Phase 3 Step B
[ ] signals_removed: list present -- FAIL: re-run Phase 3 Step B
[ ] verdict_before: one of 4-token set -- FAIL: re-run Phase 3 Step B
[ ] verdict_after: reflects Phase 4 verdict_verb; no placeholder remaining
    FAIL: re-run Phase 3 Step B after Phase 4 completes
[ ] verdict_changed: one of {YES|NO|N/A} -- FAIL: re-run Phase 3 Step B

All 32 items PASS: campaign complete. Dashboard SHALL be emitted.

---

## Output: Topic Dashboard

When all 32 TERMINAL items show PASS, emit in order:
1. Topic registration summary (Phase 1)
2. Signal roadmap summary (Phase 2)
3. Coverage table with quality column and readiness verdict (Phase 3)
4. Narrative verdict + hypothesis + echoes + top-3 (with quality citations in
   gap_reason where applicable) + coverage_context (with quality_distribution) +
   session_context (Phase 4, six components)
5. Session delta summary
```

**Rubric targeting**: C-01 through C-49 (full 176/176 baseline). **C-51 candidate**
(Coverage Quality Tier: quality column in 9-row coverage table with 3-token vocabulary
REAL | MOCK | INFERRED; Quality-Aware Readiness Rule governing section prevents premature
READY from synthetic signal sets; quality_distribution summary field in Phase 3 Contract;
Component 5 extended to carry quality_distribution read-only; TERMINAL gains 2 quality
items; gap_reason in Component 4 can cite quality tier; empty-state default defined).
**C-50 absent** (Bidirectional Prohibition Map Rule not present in this variation).

---

## V-03 -- Axis: Namespace cluster sub-verdict decomposition

**Hypothesis**: The current Phase 4 aggregate verdict (CONFIRMED | REFUTED | EVOLVING |
INSUFFICIENT | NOT YET REACHED) is derived from synthesis but has no declared structural
derivation path from the 9-namespace coverage table. A PM reading INSUFFICIENT cannot
determine from story.md alone which namespace cluster is the bottleneck. V-03 tests
whether adding a Phase 4 Component 7 -- namespace_cluster_sub_verdicts -- that groups
the 9 namespaces into 4 clusters (Discovery, Design, Technical, Adoption) and assigns
each a sub-verdict token (STRONG | ADEQUATE | WEAK | MISSING), then derives the
aggregate verdict from worst-cluster via a declared Aggregation Rule, produces a more
actionable narrative artifact. The hypothesis is that cluster sub-verdicts transform the
verdict from a synthesis conclusion into a traceable derivation -- and make next_signal_
recommendations in Component 4 more targeted (pointing at the weakest cluster).
PERSONA REGISTRY: R17 V-05 baseline. TERMINAL: 32 items.

```
Run the full topic narrative campaign for: {{topic}}

Produce a complete topic dashboard showing what signals exist, what is missing, and
the narrative arc. Use at the start and end of a signal-gathering session.

This campaign runs in exactly four phases: Register -> Plan -> Status -> Narrative.
Each phase produces a distinct artifact. A phase SHALL NOT proceed until the current
phase artifact is written and satisfies its typed output contract.

---

## Full-Phase Type Coverage Rule

All four phases have typed output contracts. No phase is exempt.

---

## Closure Parity Rule

Each phase SHALL carry exactly one closure statement at its exit boundary, before
the GATE. Format: "[ROLE] closes at [artifact] write. [ROLE] does not carry work
into Phase [N+1]."

Three instances required -- Phase 1, 2, and 3 exits.

---

## Entry Receipt Rule

Each phase SHALL carry one receipt statement at its entry (Phases 2, 3, 4) before
the active-role description. Format:
"RECEIPT: [ROLE] received [artifact] from Phase [N] per Phase Boundary Summary,
Phase [N]->[N+1]."

Phase 1 carries no receipt.

---

## Namespace Cluster Map

The 9 Signal namespaces group into 4 clusters for sub-verdict derivation:
- Discovery cluster:  scout, prove
- Design cluster:     draft, review
- Technical cluster:  flow, trace
- Adoption cluster:   listen, program, topic

Each cluster receives exactly one sub-verdict token (see Phase 4 Component 7).
Cluster boundaries are fixed; they do not vary by topic.

---

## Aggregation Rule

The Phase 4 aggregate verdict_verb (Component 1) SHALL derive from the worst cluster
sub-verdict per this lookup:
- All 4 clusters = STRONG -> verdict_verb = CONFIRMED
- Any cluster = MISSING -> verdict_verb = INSUFFICIENT
- Any cluster = WEAK, none MISSING -> verdict_verb = EVOLVING
- All clusters = ADEQUATE (no STRONG, no WEAK, no MISSING) -> verdict_verb = EVOLVING
- Session 1 with zero signals across all clusters -> verdict_verb = NOT YET REACHED
- Hypothesis actively contradicted by collected signals -> verdict_verb = REFUTED
  (REFUTED requires explicit evidence; cannot derive from sub-verdicts alone; ANALYST
  must flag in status.md; NARRATOR applies it over Aggregation Rule if flagged)

Aggregation Rule governs Component 1. NARRATOR SHALL state which cluster drove the
verdict in Component 7 before declaring Component 1.

---

## Sub-Verdict Vocabulary

sub_verdict tokens (exactly one per cluster):
- STRONG: all namespace rows in cluster show collected >= planned with >= 1 signal
- ADEQUATE: partial coverage across cluster (some namespaces covered, none missing)
- WEAK: at least one namespace in cluster has collected = 0 but others have signals
- MISSING: all namespaces in cluster show collected = 0

---

## Prohibition Type Vocabulary

violation_class tokens (exactly one per prohibition):
- scope-boundary | role-isolation | sub-skill-exclusion | data-integrity | format-contract

---

## PERSONA REGISTRY

All four campaign personas declared here. Phase headers cite this registry.
Prohibitions use typed three-field format: action, governed_by, violation_class.

### REGISTRAR
- Phase: 1 (Register)
- Owned artifact: strategy.md
- Domain: topic_name, namespace (one of 9 tokens), priority (High|Medium|Low),
  planned_signals list (>= 3 items with signal_name, target_skill, rationale)
- Prohibitions (exactly 5, typed):
  1. action: SHALL NOT produce coverage tables, cluster sub-verdicts, or readiness verdicts
     governed_by: Phase 3 Contract (ANALYST domain) + Phase 4 Contract (NARRATOR domain)
     violation_class: scope-boundary
  2. action: SHALL NOT synthesize or interpret signal content
     governed_by: Phase 4 Contract (synthesis is NARRATOR domain)
     violation_class: role-isolation
  3. action: SHALL NOT assign verdict verbs or sub-verdict tokens
     governed_by: Phase 4 Contract (both verdict types are NARRATOR outputs)
     violation_class: role-isolation
  4. action: SHALL NOT invoke any sub-skill other than topic-new
     governed_by: Phase 1 execution scope
     violation_class: sub-skill-exclusion
  5. action: SHALL NOT list signals not declared in planned_signals
     governed_by: Phase 1 Contract (founding artifact)
     violation_class: data-integrity

### PLANNER
- Phase: 2 (Plan)
- Owned artifact: roadmap.md
- Domain: namespace_coverage list (namespace + signals with signal_name +
  collection_purpose)
- Prohibitions (exactly 5, typed):
  1. action: SHALL NOT register, rename, or modify topic identity
     governed_by: Phase 1 Contract
     violation_class: scope-boundary
  2. action: SHALL NOT query or report which signals are collected
     governed_by: Phase 3 Contract (ANALYST domain)
     violation_class: scope-boundary
  3. action: SHALL NOT produce readiness verdicts, coverage ratios, or sub-verdicts
     governed_by: Phase 3 Contract + Phase 4 Contract
     violation_class: scope-boundary
  4. action: SHALL NOT synthesize findings or assign verdict verbs
     governed_by: Phase 4 Contract (NARRATOR domain)
     violation_class: role-isolation
  5. action: SHALL NOT invoke any sub-skill other than topic-plan
     governed_by: Phase 2 execution scope
     violation_class: sub-skill-exclusion

### ANALYST
- Phase: 3 (Status)
- Owned artifacts: status.md, delta.md
- Domain: coverage table (namespace, planned:int, collected:int, missing:list,
  zero_flag), coverage_ratio "X/N", readiness_verdict (3-token),
  refuted_flag (YES | NO -- flagged when signals actively contradict hypothesis),
  session_number:int, signals_added:list, signals_removed:list,
  verdict_before (4-token), verdict_after (4-token placeholder), verdict_changed (3-token)
- Prohibitions (exactly 5, typed):
  1. action: SHALL NOT add planned signals beyond Phase 2 roadmap
     governed_by: Phase 2 Contract
     violation_class: data-integrity
  2. action: SHALL NOT produce verdict verbs or cluster sub-verdicts
     governed_by: Phase 4 Contract (both are NARRATOR domain)
     violation_class: role-isolation
  3. action: SHALL NOT interpret meaning from signal content or editorialize
     governed_by: Phase 4 Contract
     violation_class: role-isolation
  4. action: SHALL NOT invoke any sub-skill other than topic-status
     governed_by: Phase 3 execution scope
     violation_class: sub-skill-exclusion
  5. action: SHALL NOT use narrative counts where integers are required
     governed_by: Phase 3 Contract
     violation_class: format-contract

### NARRATOR
- Phase: 4 (Narrative)
- Owned artifact: story.md
- Domain: Component 1 (verdict_verb, 5-token, Aggregation Rule applied),
  Component 2 (hypothesis_mutation: s0 + current),
  Component 3 (echoes list),
  Component 4 (next_signal_recommendations, exactly 3; SHALL target weakest cluster),
  Component 5 (coverage_context: coverage_ratio + readiness_verdict from status.md
  -- read-only),
  Component 6 (session_context: session_number + signals_added_count -- read-only),
  Component 7 (namespace_cluster_sub_verdicts: 4 clusters x sub_verdict token;
  Aggregation Rule applied before Component 1 is assigned)
- Prohibitions (exactly 5, typed):
  1. action: SHALL NOT modify coverage table, namespace counts, or coverage_ratio
     governed_by: Phase 3 Contract (finalized; read-only via Component 5)
     violation_class: data-integrity
  2. action: SHALL NOT add, remove, or reorder planned signals
     governed_by: Phase 2 Contract (immutable from roadmap.md)
     violation_class: data-integrity
  3. action: SHALL NOT assign readiness verdicts (READY / NOT READY / CONDITIONALLY READY)
     governed_by: Phase 3 Contract (readiness_verdict is ANALYST output; read-only)
     violation_class: scope-boundary
  4. action: SHALL NOT invoke any sub-skill other than topic-story
     governed_by: Phase 4 execution scope
     violation_class: sub-skill-exclusion
  5. action: SHALL NOT derive verdict_verb without first completing Component 7
     governed_by: Aggregation Rule (verdict_verb derives from worst cluster sub-verdict;
       Component 7 must be populated before Component 1 is assigned)
     violation_class: format-contract

---

## Cross-Phase Obligation Index

| Obligation | Declared at | Assertion site |
|---|---|---|
| Phase 2 receives planned_signals from strategy.md | Phase Boundary Summary Phase 1->2 | Phase 2 entry receipt |
| Phase 3 receives namespace_coverage from roadmap.md | Phase Boundary Summary Phase 2->3 | Phase 3 entry receipt |
| Phase 4 receives readiness_verdict + coverage_ratio (read-only) | Phase Boundary Summary Phase 3->4 (Receiving Scope) | Phase 4 entry receipt |
| Phase 4 receives session_number + signals_added_count (read-only) | Phase Boundary Summary Phase 3->4 | Phase 4 active-role header |
| Phase 4 does NOT receive namespace counts | Phase Boundary Summary Phase 3->4 (Receiving Scope) | Phase 4 active-role header |
| Phase 4 SHALL write story.md before declaring complete | Transition Obligation | Phase 4 obligation block + TERMINAL |
| verdict_after updates after Phase 4 completes | Two-Pass Delta Rule | Post-Phase-4 + TERMINAL |
| Cascade target is verdict_after only | Cascade Rule | Phase Boundary Summary Phase 3->4 |
| story.md carries coverage_ratio from status.md | Phase 4 Contract Component 5 | Phase 4 + TERMINAL |
| story.md carries session_number from delta.md | Phase 4 Contract Component 6 | Phase 4 + TERMINAL |
| Registrar closes at strategy.md write | Closure Parity Rule | Phase 1 exit |
| Planner closes at roadmap.md write | Closure Parity Rule | Phase 2 exit |
| Analyst closes at delta.md write | Closure Parity Rule | Phase 3 exit |
| Planner entry receipt: received planned_signals from Phase 1 | Entry Receipt Rule | Phase 2 entry |
| Analyst entry receipt: received namespace_coverage from Phase 2 | Entry Receipt Rule | Phase 3 entry |
| Narrator entry receipt: received status.md + delta.md from Phase 3 | Entry Receipt Rule | Phase 4 entry |
| Component 7 completed before Component 1 assigned | Aggregation Rule | Phase 4 execution + TERMINAL |
| next_signal_recommendations target weakest cluster | NARRATOR Domain (Component 4) | Phase 4 execution |

---

## Typed Output Contracts

### Phase 1 Contract -- strategy.md (unchanged)
topic_name:str, namespace (9-token), priority (3-token),
planned_signals list (>= 3: signal_name, target_skill, rationale)

### Phase 2 Contract -- roadmap.md (unchanged)
namespace_coverage list (namespace + signals with signal_name + collection_purpose)

### Phase 3 Contract -- status.md

Coverage table -- all 9 namespace rows:
  namespace, planned:int, collected:int, missing:list, zero_flag

Summary:
  coverage_ratio: "X/N"
  readiness_verdict: READY | NOT READY | CONDITIONALLY READY
  refuted_flag: YES | NO (YES only when signals actively contradict hypothesis)

### Phase 4 Contract -- story.md (seven-component)

Component 1 -- verdict_verb (5-token; derives from Aggregation Rule applied to
  Component 7; REFUTED overrides if refuted_flag = YES)

Component 2 -- hypothesis_mutation (s0 + current; unchanged)
Component 3 -- echoes (list; ["NONE"] if none; unchanged)

Component 4 -- next_signal_recommendations:
  list of exactly 3 items (namespace + skill + gap_reason);
  at least 1 item SHALL address the weakest cluster identified in Component 7

Component 5 -- coverage_context (read-only from status.md):
  coverage_ratio, readiness_verdict (verbatim; unchanged)

Component 6 -- session_context (read-only from delta.md; unchanged)

Component 7 -- namespace_cluster_sub_verdicts:
  Discovery:  sub_verdict (STRONG | ADEQUATE | WEAK | MISSING)
              namespaces: scout, prove
  Design:     sub_verdict (STRONG | ADEQUATE | WEAK | MISSING)
              namespaces: draft, review
  Technical:  sub_verdict (STRONG | ADEQUATE | WEAK | MISSING)
              namespaces: flow, trace
  Adoption:   sub_verdict (STRONG | ADEQUATE | WEAK | MISSING)
              namespaces: listen, program, topic
  driving_cluster: name of cluster with worst sub_verdict (or "NONE" if all STRONG)

### Session Delta Contract -- delta.md (unchanged)

---

## Two-Pass Delta Rule

Pass 1 (Phase 3 Step B): verdict_after = "NOT YET REACHED".
Pass 2 (Post-Phase-4): verdict_after = verdict_verb from story.md.

---

## Cascade Rule

Phase 3 Step B re-run after Phase 4: only verdict_after + verdict_changed update.

---

## Phase Boundary Summary

### Phase 1 -> Phase 2: strategy.md planned_signals -> Phase 2 input
### Phase 2 -> Phase 3: roadmap.md namespace_coverage -> Phase 3 planned counts

### Phase 3 -> Phase 4 Boundary

#### Cascade Scope: verdict_after in delta.md only
#### Receiving Scope:
- Phase 4 receives: readiness_verdict + coverage_ratio from status.md (read-only)
- Phase 4 receives: session_number + signals_added count from delta.md (read-only)
- Phase 4 does NOT receive: namespace counts
- Phase 4 DOES receive: refuted_flag from status.md (ANALYST flag; informs
  Aggregation Rule override; read-only)

#### Transition Obligation: Phase 4 SHALL write story.md before declaring complete.

---

## Prohibition Parity Rule

Each role: exactly 5 typed prohibitions (action + governed_by + violation_class).

---

## Phase 1 -- Register [TEMPORAL: session-independent]

*REGISTRAR active. Phase 1 Contract governs strategy.md.*

Invoke topic-new for {{topic}}. Produce strategy.md per Phase 1 Contract.

Registrar closes at strategy.md write. Registrar does not carry work into Phase 2.

GATE: Campaign SHALL NOT proceed to Phase 2 until Phase 1 postcondition satisfied.

Write to: simulations/topic/{{topic}}-strategy-{{date}}.md

---

## Phase 2 -- Plan [TEMPORAL: session-independent]

RECEIPT: PLANNER received planned_signals from Phase 1 strategy.md per Phase Boundary
Summary, Phase 1->2.

*PLANNER active. Phase 2 Contract governs roadmap.md.*

Invoke topic-plan for {{topic}}. Produce roadmap.md per Phase 2 Contract.

Planner closes at roadmap.md write. Planner does not carry work into Phase 3.

GATE: Campaign SHALL NOT proceed to Phase 3 until Phase 2 postcondition satisfied.

Write to: simulations/topic/{{topic}}-roadmap-{{date}}.md

---

## Phase 3 -- Status [TEMPORAL: session-dependent -- re-run each session]

RECEIPT: ANALYST received namespace_coverage from Phase 2 roadmap.md per Phase Boundary
Summary, Phase 2->3.

*ANALYST active. Phase 3 Contract governs status.md. Session Delta Contract governs
delta.md. Receiving Scope governs Phase 4 inputs.*

### Step A -- Coverage Status

Invoke topic-status for {{topic}}. Produce status.md per Phase 3 Contract:
- All 9 namespace rows: planned:int, collected:int, missing:list, zero_flag
- coverage_ratio "X/N"; readiness_verdict (3-token)
- refuted_flag: set YES only if collected signals actively contradict the hypothesis
  (not merely insufficient -- actively contradictory; default NO)

FINALIZATION: status.md finalized at this write. Phase 4 reads coverage_ratio,
readiness_verdict, and refuted_flag as read-only. Phase 4 does not receive
namespace row counts.

Write to: simulations/topic/{{topic}}-status-{{date}}.md

### Step B -- Session Delta (Pass 1)

Produce delta.md. verdict_after = "NOT YET REACHED".

Write to: simulations/topic/{{topic}}-delta-{{date}}.md

Analyst closes at delta.md write. Analyst does not carry work into Phase 4.

GATE: Campaign SHALL NOT proceed to Phase 4 until status.md AND delta.md satisfy contracts.

---

## Phase 4 -- Narrative [TEMPORAL: session-dependent -- synthesize at session end]

RECEIPT: NARRATOR received readiness_verdict + coverage_ratio + refuted_flag (status.md)
and session_number + signals_added_count (delta.md) from Phase 3 per Phase Boundary
Summary, Phase 3->4 (Receiving Scope).

**Obligation**: NARRATOR SHALL write story.md before declaring Phase 4 complete.

*NARRATOR active. Phase 4 Contract (seven-component) governs story.md. Phase 4 does
NOT receive namespace counts. Component 7 SHALL be completed before Component 1 is
assigned (Aggregation Rule).*

Invoke topic-story for {{topic}}. Produce story.md per Phase 4 Contract:
- Component 7 FIRST: assign sub-verdict to each of 4 clusters using Sub-Verdict
  Vocabulary; identify driving_cluster
- Component 1: apply Aggregation Rule to Component 7; override with REFUTED if
  refuted_flag = YES
- Component 2: hypothesis_mutation (s0 + current)
- Component 3: echoes (["NONE"] if none)
- Component 4: next_signal_recommendations (3 items; at least 1 targets driving_cluster)
- Component 5: coverage_context (coverage_ratio + readiness_verdict from status.md,
  verbatim)
- Component 6: session_context (session_number + signals_added_count from delta.md)

Write to: simulations/topic/{{topic}}-story-{{date}}.md

---

## Post-Phase-4 Delta Update (Pass 2)

Update delta.md: verdict_after = verdict_verb; verdict_changed per comparison.
Only these two fields update.

---

## Empty-State Handling

### First Invocation (0 signals)

Phase 3: all collected = 0; readiness_verdict = NOT READY; refuted_flag = NO.

Phase 4 Component 7: all clusters = MISSING; driving_cluster = "ALL";
verdict_verb = NOT YET REACHED (Aggregation Rule: MISSING -> INSUFFICIENT overridden
by empty-state convention NOT YET REACHED on session 1).

---

## TERMINAL -- Field-Level Completion Checklist

### Phase 1 -- strategy.md
[ ] topic_name: non-empty -- FAIL: re-run Phase 1
[ ] namespace: one of 9 tokens -- FAIL: re-run Phase 1
[ ] priority: one of 3 tokens -- FAIL: re-run Phase 1
[ ] planned_signals: count >= 3 -- FAIL: re-run Phase 1
[ ] planned_signals[*].target_skill: namespace/skill format -- FAIL: re-run Phase 1

### Phase 2 -- roadmap.md
[ ] namespace_coverage: at least one entry -- FAIL: re-run Phase 2
[ ] collection_purpose per signal -- FAIL: re-run Phase 2

### Phase 3 -- status.md
[ ] row count: exactly 9 -- FAIL: re-run Phase 3
[ ] planned: integer all 9 rows -- FAIL: re-run Phase 3
[ ] collected: integer all 9 rows -- FAIL: re-run Phase 3
[ ] missing: list each row -- FAIL: re-run Phase 3
[ ] zero_flag: "NO SIGNALS" where planned = 0 AND collected = 0 -- FAIL: re-run Phase 3
[ ] coverage_ratio: "X/N" format -- FAIL: re-run Phase 3
[ ] readiness_verdict: one of 3-token set -- FAIL: re-run Phase 3
[ ] refuted_flag: YES or NO -- FAIL: re-run Phase 3

### Phase 4 -- story.md
[ ] story.md written before Phase 4 declared complete -- FAIL: re-run Phase 4
[ ] Component 7 completed before Component 1 assigned (Aggregation Rule) -- FAIL: re-run Phase 4
[ ] Component 7: all 4 clusters have sub_verdict from 4-token set -- FAIL: re-run Phase 4
[ ] Component 7: driving_cluster named -- FAIL: re-run Phase 4
[ ] verdict_verb: one of 5 tokens; consistent with Aggregation Rule -- FAIL: re-run Phase 4
[ ] hypothesis_mutation.s0: non-empty -- FAIL: re-run Phase 4
[ ] hypothesis_mutation.current: present -- FAIL: re-run Phase 4
[ ] echoes: list present, minimum ["NONE"] -- FAIL: re-run Phase 4
[ ] next_signal_recommendations: exactly 3 items -- FAIL: re-run Phase 4
[ ] next_signal_recommendations: at least 1 targets driving_cluster -- FAIL: re-run Phase 4
[ ] coverage_context.coverage_ratio: matches status.md -- FAIL: re-run Phase 4
[ ] session_context.session_number: matches delta.md -- FAIL: re-run Phase 4

### Session Delta -- delta.md
[ ] session_number: integer >= 1 -- FAIL: re-run Phase 3 Step B
[ ] signals_added: list present -- FAIL: re-run Phase 3 Step B
[ ] signals_removed: list present -- FAIL: re-run Phase 3 Step B
[ ] verdict_before: one of 4-token set -- FAIL: re-run Phase 3 Step B
[ ] verdict_after: reflects Phase 4 verdict_verb; no placeholder remaining
    FAIL: re-run Phase 3 Step B after Phase 4
[ ] verdict_changed: one of {YES|NO|N/A} -- FAIL: re-run Phase 3 Step B

All 32 items PASS: campaign complete. Dashboard SHALL be emitted.

---

## Output: Topic Dashboard

When all 32 TERMINAL items show PASS, emit in order:
1. Topic registration summary (Phase 1)
2. Signal roadmap summary (Phase 2)
3. Coverage table with readiness verdict (Phase 3)
4. Cluster sub-verdict table (Component 7: 4 clusters x sub_verdict; driving_cluster)
5. Narrative verdict derived from Aggregation Rule + hypothesis + echoes + top-3
   (targeting driving_cluster) + coverage_context + session_context (Phase 4)
6. Session delta summary
```

**Rubric targeting**: C-01 through C-49 (full 176/176 baseline). **C-52 candidate**
(Namespace Cluster Sub-Verdict Decomposition: Component 7 in Phase 4 Contract;
Namespace Cluster Map governing section with fixed 4-cluster layout; Aggregation Rule
derives verdict_verb from worst-cluster sub-verdict; REFUTED override path from
ANALYST refuted_flag; driving_cluster field names the bottleneck cluster; Component 4
recommendations target driving_cluster; TERMINAL gains 3 cluster items; dashboard
emits cluster table before aggregate verdict; transforms verdict from opaque synthesis
into traceable derivation). **C-50 absent**. **C-51 absent**.

---

## V-04 -- Combined: receipt_surface (V-01) + quality tiers (V-02)

**Hypothesis**: V-01 closes prohibition traceability (receipt_surface on prohibitions);
V-02 closes signal credibility (quality tiers in coverage table). Combined, they address
two independent audit gaps: every prohibition forward-links to its boundary acknowledgment,
and every coverage claim carries a quality annotation. A reviewer can verify both
structural integrity (prohibition map) and evidentiary integrity (quality tiers) from
a single artifact set. Component 5 carries quality_distribution. Component 4 gap_reason
may cite quality tier. TERMINAL: 33 items.

```
Run the full topic narrative campaign for: {{topic}}

Produce a complete topic dashboard showing what signals exist, what is missing, and
the narrative arc. Use at the start and end of a signal-gathering session.

This campaign runs in exactly four phases: Register -> Plan -> Status -> Narrative.
Each phase produces a distinct artifact. A phase SHALL NOT proceed until the current
phase artifact is written and satisfies its typed output contract.

---

## Full-Phase Type Coverage Rule

All four phases have typed output contracts. No phase is exempt.

---

## Closure Parity Rule

Each phase SHALL carry one closure statement at its exit boundary, before the GATE.
Format: "[ROLE] closes at [artifact] write. [ROLE] does not carry work into Phase [N+1]."
Three instances required -- Phase 1, 2, and 3 exits.

---

## Entry Receipt Rule

Each phase SHALL carry one receipt statement at its entry (Phases 2, 3, 4). Format:
"RECEIPT: [ROLE] received [artifact] from Phase [N] per Phase Boundary Summary,
Phase [N]->[N+1]."
Phase 1 carries no receipt. Six fixed audit locations total.

---

## Quality Tier Vocabulary

quality tokens (exactly one per namespace coverage row):
- REAL: signal from genuine execution or primary research
- MOCK: synthetic placeholder from /mock-ns or /mock-all
- INFERRED: inferred from related artifacts without direct collection

---

## Quality-Aware Readiness Rule

- READY: full coverage AND zero MOCK-only namespaces AND zero INFERRED-only namespaces
- CONDITIONALLY READY: coverage >= 0.5 AND (any MOCK OR any INFERRED OR coverage < 1.0)
- NOT READY: coverage < 0.5 OR more than 2 zero-signal namespaces
MOCK-only or INFERRED-only datasets that pass coverage ratio SHALL resolve to
CONDITIONALLY READY, not READY.

---

## Prohibition Type Vocabulary

violation_class tokens: scope-boundary | role-isolation | sub-skill-exclusion |
data-integrity | format-contract

---

## Bidirectional Prohibition Map Rule

Each typed prohibition SHALL carry a receipt_surface field naming the Phase Entry
Receipt that acknowledges the boundary from the receiving side. Prohibition Parity
Rule extended: 4 roles x 5 prohibitions x 4 fields (action + governed_by +
violation_class + receipt_surface). A prohibition missing receipt_surface fails audit.

---

## PERSONA REGISTRY

### REGISTRAR
- Phase: 1 (Register)
- Owned artifact: strategy.md
- Domain: topic_name, namespace (9-token), priority (3-token),
  planned_signals (>= 3: signal_name, target_skill, rationale)
- Prohibitions (exactly 5, typed):
  1. action: SHALL NOT produce coverage tables, quality tiers, or readiness verdicts
     governed_by: Phase 3 Contract (ANALYST domain)
     violation_class: scope-boundary
     receipt_surface: Phase 3 entry receipt (ANALYST received namespace_coverage
       from Phase 2 -- quality and coverage are Phase 3 Step A outputs)
  2. action: SHALL NOT synthesize or interpret signal content
     governed_by: Phase 4 Contract (NARRATOR domain)
     violation_class: role-isolation
     receipt_surface: Phase 4 entry receipt (NARRATOR received coverage context
       from Phase 3 -- synthesis is Phase 4 domain)
  3. action: SHALL NOT assign verdict verbs from Phase 4 controlled vocabulary
     governed_by: Phase 4 Contract (5-token NARRATOR output)
     violation_class: role-isolation
     receipt_surface: Phase 4 entry receipt (NARRATOR received readiness_verdict
       from Phase 3 -- verdict_verb is NARRATOR synthesis, not carry-over)
  4. action: SHALL NOT invoke any sub-skill other than topic-new
     governed_by: Phase 1 execution scope
     violation_class: sub-skill-exclusion
     receipt_surface: Phase 2 entry receipt (PLANNER received planned_signals
       from Phase 1 -- sub-skill boundary acknowledged at Phase 2 entry)
  5. action: SHALL NOT list signals not declared in planned_signals
     governed_by: Phase 1 Contract (founding artifact)
     violation_class: data-integrity
     receipt_surface: Phase 2 entry receipt (PLANNER received planned_signals
       from strategy.md -- finalization acknowledged at Phase 2 entry)

### PLANNER
- Phase: 2 (Plan)
- Owned artifact: roadmap.md
- Domain: namespace_coverage list (namespace + signals: signal_name + collection_purpose)
- Prohibitions (exactly 5, typed):
  1. action: SHALL NOT register, rename, or modify topic identity
     governed_by: Phase 1 Contract
     violation_class: scope-boundary
     receipt_surface: Phase 2 entry receipt (PLANNER received planned_signals
       from Phase 1 -- topic identity finalized; PLANNER does not modify it)
  2. action: SHALL NOT query or report which signals are collected
     governed_by: Phase 3 Contract (ANALYST domain)
     violation_class: scope-boundary
     receipt_surface: Phase 3 entry receipt (ANALYST received namespace_coverage
       from Phase 2 -- collection reporting is Phase 3 Step A)
  3. action: SHALL NOT produce readiness verdicts, coverage ratios, or quality tiers
     governed_by: Phase 3 Contract (Quality-Aware Readiness Rule is ANALYST domain)
     violation_class: scope-boundary
     receipt_surface: Phase 3 entry receipt (ANALYST received namespace_coverage
       from Phase 2 -- readiness + quality are Phase 3 Step A outputs)
  4. action: SHALL NOT synthesize findings or assign verdict verbs
     governed_by: Phase 4 Contract (NARRATOR domain)
     violation_class: role-isolation
     receipt_surface: Phase 4 entry receipt (NARRATOR received coverage context
       from Phase 3 -- synthesis boundary at Phase 4 entry)
  5. action: SHALL NOT invoke any sub-skill other than topic-plan
     governed_by: Phase 2 execution scope
     violation_class: sub-skill-exclusion
     receipt_surface: Phase 3 entry receipt (ANALYST received namespace_coverage
       from Phase 2 roadmap.md -- sub-skill boundary acknowledged)

### ANALYST
- Phase: 3 (Status)
- Owned artifacts: status.md, delta.md
- Domain: coverage table (namespace, planned:int, collected:int, missing:list,
  quality:token, zero_flag), coverage_ratio "X/N",
  quality_distribution {real_count:int, mock_count:int, inferred_count:int},
  readiness_verdict (3-token; Quality-Aware Readiness Rule applied),
  session_number:int, signals_added:list, signals_removed:list,
  verdict_before (4-token), verdict_after (4-token placeholder), verdict_changed (3-token)
- Prohibitions (exactly 5, typed):
  1. action: SHALL NOT add planned signals beyond Phase 2 roadmap
     governed_by: Phase 2 Contract (finalized at roadmap.md)
     violation_class: data-integrity
     receipt_surface: Phase 3 entry receipt (ANALYST received namespace_coverage
       from Phase 2 -- planned signals finalized; ANALYST does not extend them)
  2. action: SHALL NOT produce verdict verbs from Phase 4 controlled vocabulary
     governed_by: Phase 4 Contract (5-token NARRATOR output)
     violation_class: role-isolation
     receipt_surface: Phase 4 entry receipt (NARRATOR received readiness_verdict
       from Phase 3 -- verdict_verb is Phase 4 synthesis domain)
  3. action: SHALL NOT interpret meaning from signal content or editorialize
     governed_by: Phase 4 Contract
     violation_class: role-isolation
     receipt_surface: Phase 4 entry receipt (NARRATOR received status.md inputs
       from Phase 3 -- editorial interpretation is Phase 4 domain)
  4. action: SHALL NOT invoke any sub-skill other than topic-status
     governed_by: Phase 3 execution scope
     violation_class: sub-skill-exclusion
     receipt_surface: Phase 4 entry receipt (NARRATOR received status.md + delta.md
       from Phase 3 -- sub-skill boundary acknowledged at Phase 4 entry)
  5. action: SHALL NOT use narrative counts where integers are required
     governed_by: Phase 3 Contract (planned, collected, quality_distribution counts
       SHALL be integer >= 0)
     violation_class: format-contract
     receipt_surface: Phase 4 entry receipt (NARRATOR received coverage_ratio verbatim
       from status.md -- integer integrity established at Phase 3 Step A)

### NARRATOR
- Phase: 4 (Narrative)
- Owned artifact: story.md
- Domain: Component 1 (verdict_verb, 5-token), Component 2 (hypothesis_mutation:
  s0 + current), Component 3 (echoes list), Component 4 (next_signal_recommendations,
  3 items: namespace + skill + gap_reason; gap_reason may cite quality tier),
  Component 5 (coverage_context: coverage_ratio + quality_distribution +
  readiness_verdict from status.md -- read-only),
  Component 6 (session_context: session_number + signals_added_count -- read-only)
- Prohibitions (exactly 5, typed):
  1. action: SHALL NOT modify coverage table, namespace counts, coverage_ratio,
     or quality_distribution
     governed_by: Phase 3 Contract (finalized at Phase 3 Step A; read-only via Component 5)
     violation_class: data-integrity
     receipt_surface: Phase 4 entry receipt (NARRATOR received coverage_ratio +
       quality_distribution + readiness_verdict from Phase 3 as read-only inputs)
  2. action: SHALL NOT add, remove, or reorder planned signals
     governed_by: Phase 2 Contract (immutable from roadmap.md)
     violation_class: data-integrity
     receipt_surface: Phase 4 entry receipt (NARRATOR received status.md + delta.md
       from Phase 3 -- planned signals finalized at Phase 2)
  3. action: SHALL NOT assign readiness verdicts
     governed_by: Phase 3 Contract (readiness_verdict is ANALYST output; read-only)
     violation_class: scope-boundary
     receipt_surface: Phase 4 entry receipt (NARRATOR received readiness_verdict
       from Phase 3 per Receiving Scope -- read-only to Component 5)
  4. action: SHALL NOT invoke any sub-skill other than topic-story
     governed_by: Phase 4 execution scope
     violation_class: sub-skill-exclusion
     receipt_surface: Phase 4 entry receipt (NARRATOR received status.md + delta.md
       from Phase 3 -- NARRATOR invokes topic-story only)
  5. action: SHALL NOT declare Phase 4 complete without writing story.md
     governed_by: Transition Obligation (Phase Boundary Summary, Phase 3->4)
     violation_class: data-integrity
     receipt_surface: Phase 4 entry receipt (NARRATOR received delta.md with
       verdict_after = NOT YET REACHED -- story.md write resolves placeholder)

---

## Cross-Phase Obligation Index

| Obligation | Declared at | Assertion site |
|---|---|---|
| Phase 2 receives planned_signals from strategy.md | Phase Boundary Summary Phase 1->2 | Phase 2 entry receipt |
| Phase 3 receives namespace_coverage from roadmap.md | Phase Boundary Summary Phase 2->3 | Phase 3 entry receipt |
| Phase 4 receives readiness_verdict + coverage_ratio + quality_distribution (read-only) | Phase Boundary Summary Phase 3->4 (Receiving Scope) | Phase 4 entry receipt |
| Phase 4 receives session_number + signals_added_count (read-only) | Phase Boundary Summary Phase 3->4 | Phase 4 active-role header |
| Phase 4 does NOT receive namespace counts | Phase Boundary Summary Phase 3->4 | Phase 4 active-role header |
| Phase 4 SHALL write story.md before declaring complete | Transition Obligation | Phase 4 obligation + TERMINAL |
| verdict_after updates after Phase 4 | Two-Pass Delta Rule | Post-Phase-4 + TERMINAL |
| Cascade target is verdict_after only | Cascade Rule | Phase Boundary Summary Phase 3->4 |
| story.md carries coverage_ratio + quality_distribution from status.md | Phase 4 Contract Component 5 | Phase 4 + TERMINAL |
| story.md carries session_number from delta.md | Phase 4 Contract Component 6 | Phase 4 + TERMINAL |
| Registrar closes at strategy.md write | Closure Parity Rule | Phase 1 exit |
| Planner closes at roadmap.md write | Closure Parity Rule | Phase 2 exit |
| Analyst closes at delta.md write | Closure Parity Rule | Phase 3 exit |
| Planner entry receipt: received planned_signals from Phase 1 | Entry Receipt Rule | Phase 2 entry |
| Analyst entry receipt: received namespace_coverage from Phase 2 | Entry Receipt Rule | Phase 3 entry |
| Narrator entry receipt: received status.md + delta.md from Phase 3 | Entry Receipt Rule | Phase 4 entry |
| Each prohibition forward-links to receipt_surface | Bidirectional Prohibition Map Rule | PERSONA REGISTRY (20 entries) |
| readiness_verdict applies Quality-Aware Readiness Rule | Quality-Aware Readiness Rule | Phase 3 Step A + TERMINAL |

---

## Typed Output Contracts

### Phase 1 Contract -- strategy.md
topic_name:str, namespace (9-token), priority (3-token),
planned_signals (>= 3: signal_name, target_skill, rationale)

### Phase 2 Contract -- roadmap.md
namespace_coverage list (namespace + signals: signal_name + collection_purpose)

### Phase 3 Contract -- status.md
Coverage table -- 9 rows: namespace, planned:int, collected:int, missing:list,
quality (REAL|MOCK|INFERRED), zero_flag
Summary: coverage_ratio "X/N",
quality_distribution {real_count:int, mock_count:int, inferred_count:int},
readiness_verdict (3-token; Quality-Aware Readiness Rule applied)

### Phase 4 Contract -- story.md (six-component)
Component 1: verdict_verb (5-token)
Component 2: hypothesis_mutation (s0 + current)
Component 3: echoes (["NONE"] if none)
Component 4: next_signal_recommendations (3 items; gap_reason may cite quality tier)
Component 5: coverage_context (coverage_ratio + quality_distribution +
  readiness_verdict from status.md; all three verbatim; SHALL NOT recompute)
Component 6: session_context (session_number + signals_added_count from delta.md)

### Session Delta Contract -- delta.md (unchanged)

---

## Two-Pass Delta Rule + Cascade Rule (unchanged from baseline)

---

## Phase Boundary Summary

### Phase 1->2: planned_signals -> namespace_coverage
### Phase 2->3: namespace_coverage -> planned counts + missing names
### Phase 3->4:
Cascade Scope: verdict_after only.
Receiving Scope: readiness_verdict + coverage_ratio + quality_distribution (read-only;
Component 5) + session_number + signals_added_count (read-only; Component 6).
Phase 4 does NOT receive namespace counts.
Transition Obligation: story.md before Phase 4 declares complete.

---

## Prohibition Parity Rule

Each role: exactly 5 typed prohibitions (action + governed_by + violation_class +
receipt_surface). Any entry missing a field SHALL fail audit.

---

## Phase 1 -- Register [TEMPORAL: session-independent]

*REGISTRAR active. Phase 1 Contract governs strategy.md.*
Invoke topic-new for {{topic}}. Produce strategy.md per Phase 1 Contract.
Registrar closes at strategy.md write. Registrar does not carry work into Phase 2.
GATE: Campaign SHALL NOT proceed to Phase 2 until Phase 1 postcondition satisfied.
Write to: simulations/topic/{{topic}}-strategy-{{date}}.md

---

## Phase 2 -- Plan [TEMPORAL: session-independent]

RECEIPT: PLANNER received planned_signals from Phase 1 strategy.md per Phase Boundary
Summary, Phase 1->2.
*PLANNER active. Phase 2 Contract governs roadmap.md.*
Invoke topic-plan for {{topic}}. Produce roadmap.md per Phase 2 Contract.
Planner closes at roadmap.md write. Planner does not carry work into Phase 3.
GATE: Campaign SHALL NOT proceed to Phase 3 until Phase 2 postcondition satisfied.
Write to: simulations/topic/{{topic}}-roadmap-{{date}}.md

---

## Phase 3 -- Status [TEMPORAL: session-dependent -- re-run each session]

RECEIPT: ANALYST received namespace_coverage from Phase 2 roadmap.md per Phase Boundary
Summary, Phase 2->3.
*ANALYST active. Phase 3 Contract governs status.md (quality column + quality_distribution).
Session Delta Contract governs delta.md.*

### Step A -- Coverage Status
Invoke topic-status for {{topic}}. Produce status.md per Phase 3 Contract:
- All 9 namespace rows: planned:int, collected:int, missing:list, quality:token, zero_flag
- Apply Quality-Aware Readiness Rule; compute quality_distribution
FINALIZATION: Phase 4 reads coverage_ratio, quality_distribution, readiness_verdict
as read-only (Component 5). Phase 4 does not receive namespace row counts.
Write to: simulations/topic/{{topic}}-status-{{date}}.md

### Step B -- Session Delta (Pass 1)
Produce delta.md. verdict_after = "NOT YET REACHED".
Write to: simulations/topic/{{topic}}-delta-{{date}}.md
Analyst closes at delta.md write. Analyst does not carry work into Phase 4.
GATE: Campaign SHALL NOT proceed to Phase 4 until status.md AND delta.md satisfy contracts.

---

## Phase 4 -- Narrative [TEMPORAL: session-dependent -- synthesize at session end]

RECEIPT: NARRATOR received readiness_verdict + coverage_ratio + quality_distribution
(status.md) and session_number + signals_added_count (delta.md) from Phase 3 per
Phase Boundary Summary, Phase 3->4 (Receiving Scope).
**Obligation**: NARRATOR SHALL write story.md before declaring Phase 4 complete.
*NARRATOR active. Phase 4 Contract (six-component) governs story.md. Phase 4 does NOT
receive namespace counts. Receives readiness_verdict + coverage_ratio +
quality_distribution (read-only; Component 5) and session_number +
signals_added_count (read-only; Component 6).*

Invoke topic-story for {{topic}}. Produce story.md per Phase 4 Contract:
- Component 1: verdict_verb (5-token)
- Component 2: hypothesis_mutation (s0 + current)
- Component 3: echoes (["NONE"] if none)
- Component 4: 3 recommendations; gap_reason may cite quality tier
- Component 5: coverage_ratio + quality_distribution + readiness_verdict (verbatim)
- Component 6: session_number + signals_added_count from delta.md
Write to: simulations/topic/{{topic}}-story-{{date}}.md

---

## Post-Phase-4 Delta Update (Pass 2)
Update delta.md: verdict_after = verdict_verb; verdict_changed per comparison.
Only these two fields update.

---

## Empty-State Handling
Phase 3: all collected = 0; quality = REAL (zero-signal default);
quality_distribution = {0, 0, 0}; readiness_verdict = NOT READY.
Phase 4: verdict_verb = NOT YET REACHED; Component 5 carries {0, 0, 0}.

---

## TERMINAL -- Field-Level Completion Checklist

### Phase 1 -- strategy.md
[ ] topic_name: non-empty -- FAIL: re-run Phase 1
[ ] namespace: one of 9 tokens -- FAIL: re-run Phase 1
[ ] priority: one of 3 tokens -- FAIL: re-run Phase 1
[ ] planned_signals: count >= 3 -- FAIL: re-run Phase 1
[ ] planned_signals[*].target_skill: namespace/skill format -- FAIL: re-run Phase 1

### Phase 2 -- roadmap.md
[ ] namespace_coverage: at least one entry -- FAIL: re-run Phase 2
[ ] collection_purpose per signal -- FAIL: re-run Phase 2

### Phase 3 -- status.md
[ ] row count: exactly 9 -- FAIL: re-run Phase 3
[ ] planned: integer all 9 rows -- FAIL: re-run Phase 3
[ ] collected: integer all 9 rows -- FAIL: re-run Phase 3
[ ] missing: list each row -- FAIL: re-run Phase 3
[ ] quality: one of {REAL|MOCK|INFERRED} all 9 rows -- FAIL: re-run Phase 3
[ ] zero_flag: "NO SIGNALS" where planned = 0 AND collected = 0 -- FAIL: re-run Phase 3
[ ] coverage_ratio: "X/N" format -- FAIL: re-run Phase 3
[ ] quality_distribution: {real_count, mock_count, inferred_count} all integers
    FAIL: re-run Phase 3
[ ] readiness_verdict: Quality-Aware Readiness Rule applied; 3-token set
    FAIL: re-run Phase 3

### PERSONA REGISTRY
[ ] all 20 prohibition entries carry receipt_surface -- FAIL: re-run PERSONA REGISTRY

### Phase 4 -- story.md
[ ] story.md written before Phase 4 declared complete -- FAIL: re-run Phase 4
[ ] verdict_verb: one of 5 tokens -- FAIL: re-run Phase 4
[ ] hypothesis_mutation.s0: non-empty -- FAIL: re-run Phase 4
[ ] hypothesis_mutation.current: present -- FAIL: re-run Phase 4
[ ] echoes: list present, minimum ["NONE"] -- FAIL: re-run Phase 4
[ ] next_signal_recommendations: exactly 3 items -- FAIL: re-run Phase 4
[ ] next_signal_recommendations[*].namespace: present -- FAIL: re-run Phase 4
[ ] next_signal_recommendations[*].gap_reason: present -- FAIL: re-run Phase 4
[ ] coverage_context.coverage_ratio: matches status.md -- FAIL: re-run Phase 4
[ ] coverage_context.quality_distribution: matches status.md -- FAIL: re-run Phase 4
[ ] session_context.session_number: matches delta.md -- FAIL: re-run Phase 4

### Session Delta -- delta.md
[ ] session_number: integer >= 1 -- FAIL: re-run Phase 3 Step B
[ ] signals_added: list present -- FAIL: re-run Phase 3 Step B
[ ] signals_removed: list present -- FAIL: re-run Phase 3 Step B
[ ] verdict_before: one of 4-token set -- FAIL: re-run Phase 3 Step B
[ ] verdict_after: reflects Phase 4; no placeholder remaining
    FAIL: re-run Phase 3 Step B after Phase 4
[ ] verdict_changed: one of {YES|NO|N/A} -- FAIL: re-run Phase 3 Step B

All 33 items PASS: campaign complete. Dashboard SHALL be emitted.

---

## Output: Topic Dashboard

When all 33 TERMINAL items PASS, emit in order:
1. Topic registration summary (Phase 1)
2. Signal roadmap summary (Phase 2)
3. Coverage table with quality column + quality_distribution + readiness verdict (Phase 3)
4. Narrative verdict + hypothesis + echoes + top-3 (gap_reason with quality citations
   where applicable) + coverage_context (with quality_distribution) + session_context
5. Session delta summary
```

**Rubric targeting**: C-01 through C-49 (176/176 baseline). **C-50 candidate**
(Bidirectional Prohibition Map Rule: receipt_surface on all 20 prohibitions).
**C-51 candidate** (Coverage Quality Tier: quality column + Quality-Aware Readiness
Rule + quality_distribution in Component 5). Combined: prohibition traceability +
signal credibility. **C-52 absent** (cluster sub-verdicts not in this variation).

---

## V-05 -- Full stack: receipt_surface + quality tiers + cluster sub-verdicts
## (V-01 + V-02 + V-03)

**Hypothesis**: All three R18 axes address non-overlapping structural gaps. V-01 closes
prohibition traceability. V-02 closes signal credibility. V-03 closes verdict derivation
transparency. Combined: (a) every prohibition is bidirectionally mapped to its receipt
acknowledgment; (b) every coverage row carries a quality annotation that governs the
readiness_verdict via a declared rule; (c) the aggregate verdict is a deterministic
derivation from per-cluster sub-verdicts rather than opaque synthesis. A PM using this
skill receives three independently auditable properties: boundary map, quality-graded
coverage, and decomposed verdict. TERMINAL: 35 items.

```
Run the full topic narrative campaign for: {{topic}}

Produce a complete topic dashboard showing what signals exist, what is missing, and
the narrative arc. Use at the start and end of a signal-gathering session.

This campaign runs in exactly four phases: Register -> Plan -> Status -> Narrative.
Each phase produces a distinct artifact. A phase SHALL NOT proceed until the current
phase artifact is written and satisfies its typed output contract.

---

## Full-Phase Type Coverage Rule

All four phases have typed output contracts. No phase is exempt.

---

## Closure Parity Rule

Each phase SHALL carry one closure statement at its exit boundary, before the GATE.
Format: "[ROLE] closes at [artifact] write. [ROLE] does not carry work into Phase [N+1]."
Three instances required -- Phase 1, 2, and 3 exits.

---

## Entry Receipt Rule

Each phase SHALL carry one receipt statement at its entry (Phases 2, 3, 4). Format:
"RECEIPT: [ROLE] received [artifact] from Phase [N] per Phase Boundary Summary,
Phase [N]->[N+1]."
Phase 1 carries no receipt. Six fixed audit locations total.

---

## Quality Tier Vocabulary

quality tokens (exactly one per namespace coverage row):
- REAL: signal from genuine execution or primary research
- MOCK: synthetic placeholder from /mock-ns or /mock-all
- INFERRED: inferred from related artifacts without direct collection

---

## Quality-Aware Readiness Rule

- READY: full coverage AND zero MOCK-only namespaces AND zero INFERRED-only namespaces
- CONDITIONALLY READY: coverage >= 0.5 AND (any MOCK OR any INFERRED OR coverage < 1.0)
- NOT READY: coverage < 0.5 OR more than 2 zero-signal namespaces
MOCK-only or INFERRED-only datasets that pass coverage ratio SHALL resolve to
CONDITIONALLY READY, not READY.

---

## Namespace Cluster Map

Fixed 4-cluster layout for Component 7:
- Discovery cluster:  scout, prove
- Design cluster:     draft, review
- Technical cluster:  flow, trace
- Adoption cluster:   listen, program, topic

---

## Sub-Verdict Vocabulary

sub_verdict tokens (exactly one per cluster):
- STRONG: all cluster namespaces have collected >= planned with >= 1 signal
- ADEQUATE: partial cluster coverage (some covered, none fully missing)
- WEAK: at least one namespace in cluster has collected = 0 but others have signals
- MISSING: all cluster namespaces have collected = 0

---

## Aggregation Rule

verdict_verb (Component 1) derives from worst cluster sub-verdict in Component 7:
- All 4 STRONG -> CONFIRMED
- Any MISSING -> INSUFFICIENT
- Any WEAK, none MISSING -> EVOLVING
- All ADEQUATE -> EVOLVING
- Session 1, all MISSING -> NOT YET REACHED (empty-state override)
- refuted_flag = YES -> REFUTED (overrides all other rules)

Component 7 SHALL be completed before Component 1 is assigned.

---

## Prohibition Type Vocabulary

violation_class tokens: scope-boundary | role-isolation | sub-skill-exclusion |
data-integrity | format-contract

---

## Bidirectional Prohibition Map Rule

Each typed prohibition SHALL carry receipt_surface naming the entry receipt that
acknowledges the boundary from the receiving side. Prohibition Parity Rule: 4 roles
x 5 prohibitions x 4 fields (action + governed_by + violation_class + receipt_surface).
Missing receipt_surface fails audit.

---

## PERSONA REGISTRY

### REGISTRAR
- Phase: 1 (Register)
- Owned artifact: strategy.md
- Domain: topic_name, namespace (9-token), priority (3-token),
  planned_signals (>= 3: signal_name, target_skill, rationale)
- Prohibitions (exactly 5, typed):
  1. action: SHALL NOT produce coverage tables, quality tiers, quality_distribution,
     cluster sub-verdicts, or readiness verdicts
     governed_by: Phase 3 Contract (ANALYST) + Phase 4 Contract (NARRATOR)
     violation_class: scope-boundary
     receipt_surface: Phase 3 entry receipt (ANALYST received namespace_coverage
       from Phase 2 -- quality, coverage, sub-verdicts are Phase 3/4 outputs)
  2. action: SHALL NOT synthesize or interpret signal content
     governed_by: Phase 4 Contract (NARRATOR)
     violation_class: role-isolation
     receipt_surface: Phase 4 entry receipt (NARRATOR received coverage context
       from Phase 3 -- synthesis is Phase 4 domain)
  3. action: SHALL NOT assign verdict verbs or cluster sub-verdict tokens
     governed_by: Phase 4 Contract (both are NARRATOR outputs)
     violation_class: role-isolation
     receipt_surface: Phase 4 entry receipt (NARRATOR received readiness_verdict
       from Phase 3 -- both verdict types are NARRATOR synthesis)
  4. action: SHALL NOT invoke any sub-skill other than topic-new
     governed_by: Phase 1 execution scope
     violation_class: sub-skill-exclusion
     receipt_surface: Phase 2 entry receipt (PLANNER received planned_signals
       from Phase 1 -- sub-skill boundary acknowledged at Phase 2 entry)
  5. action: SHALL NOT list signals not declared in planned_signals
     governed_by: Phase 1 Contract (founding artifact)
     violation_class: data-integrity
     receipt_surface: Phase 2 entry receipt (PLANNER received planned_signals
       from strategy.md -- finalization acknowledged at Phase 2 entry)

### PLANNER
- Phase: 2 (Plan)
- Owned artifact: roadmap.md
- Domain: namespace_coverage list (namespace + signals: signal_name + collection_purpose)
- Prohibitions (exactly 5, typed):
  1. action: SHALL NOT register, rename, or modify topic identity
     governed_by: Phase 1 Contract
     violation_class: scope-boundary
     receipt_surface: Phase 2 entry receipt (PLANNER received planned_signals
       from Phase 1 -- topic identity finalized)
  2. action: SHALL NOT query or report which signals are collected
     governed_by: Phase 3 Contract (ANALYST)
     violation_class: scope-boundary
     receipt_surface: Phase 3 entry receipt (ANALYST received namespace_coverage
       from Phase 2 -- collection reporting is Phase 3 Step A)
  3. action: SHALL NOT produce readiness verdicts, coverage ratios, quality tiers,
     or cluster sub-verdicts
     governed_by: Phase 3 Contract + Phase 4 Contract
     violation_class: scope-boundary
     receipt_surface: Phase 3 entry receipt (ANALYST received namespace_coverage
       from Phase 2 -- quality and readiness are Phase 3 outputs)
  4. action: SHALL NOT synthesize findings or assign verdict verbs
     governed_by: Phase 4 Contract (NARRATOR)
     violation_class: role-isolation
     receipt_surface: Phase 4 entry receipt (NARRATOR received coverage context
       from Phase 3 -- synthesis boundary at Phase 4 entry)
  5. action: SHALL NOT invoke any sub-skill other than topic-plan
     governed_by: Phase 2 execution scope
     violation_class: sub-skill-exclusion
     receipt_surface: Phase 3 entry receipt (ANALYST received namespace_coverage
       from Phase 2 roadmap.md -- sub-skill boundary acknowledged)

### ANALYST
- Phase: 3 (Status)
- Owned artifacts: status.md, delta.md
- Domain: coverage table (namespace, planned:int, collected:int, missing:list,
  quality:token, zero_flag), coverage_ratio "X/N",
  quality_distribution {real_count:int, mock_count:int, inferred_count:int},
  readiness_verdict (3-token; Quality-Aware Readiness Rule),
  refuted_flag (YES | NO),
  session_number:int, signals_added:list, signals_removed:list,
  verdict_before (4-token), verdict_after (4-token placeholder), verdict_changed (3-token)
- Prohibitions (exactly 5, typed):
  1. action: SHALL NOT add planned signals beyond Phase 2 roadmap
     governed_by: Phase 2 Contract
     violation_class: data-integrity
     receipt_surface: Phase 3 entry receipt (ANALYST received namespace_coverage
       from Phase 2 -- planned signals finalized; ANALYST does not extend them)
  2. action: SHALL NOT produce verdict verbs or cluster sub-verdict tokens
     governed_by: Phase 4 Contract (both are NARRATOR domain)
     violation_class: role-isolation
     receipt_surface: Phase 4 entry receipt (NARRATOR received readiness_verdict
       from Phase 3 -- verdict_verb and sub-verdicts are Phase 4 domain)
  3. action: SHALL NOT interpret meaning from signal content or editorialize
     governed_by: Phase 4 Contract
     violation_class: role-isolation
     receipt_surface: Phase 4 entry receipt (NARRATOR received status.md from Phase 3
       -- editorial interpretation is Phase 4 domain)
  4. action: SHALL NOT invoke any sub-skill other than topic-status
     governed_by: Phase 3 execution scope
     violation_class: sub-skill-exclusion
     receipt_surface: Phase 4 entry receipt (NARRATOR received status.md + delta.md
       from Phase 3 -- sub-skill boundary acknowledged at Phase 4 entry)
  5. action: SHALL NOT use narrative counts where integers are required
     governed_by: Phase 3 Contract (planned, collected, quality_distribution:int)
     violation_class: format-contract
     receipt_surface: Phase 4 entry receipt (NARRATOR received coverage_ratio verbatim
       from status.md -- integer integrity established at Phase 3 Step A)

### NARRATOR
- Phase: 4 (Narrative)
- Owned artifact: story.md
- Domain: Component 1 (verdict_verb, 5-token; Aggregation Rule from Component 7),
  Component 2 (hypothesis_mutation: s0 + current),
  Component 3 (echoes list),
  Component 4 (next_signal_recommendations, 3: namespace + skill + gap_reason;
  >= 1 targets driving_cluster; gap_reason may cite quality tier),
  Component 5 (coverage_context: coverage_ratio + quality_distribution +
  readiness_verdict from status.md -- read-only),
  Component 6 (session_context: session_number + signals_added_count -- read-only),
  Component 7 (namespace_cluster_sub_verdicts: 4 clusters x sub_verdict; driving_cluster;
  completed before Component 1)
- Prohibitions (exactly 5, typed):
  1. action: SHALL NOT modify coverage table, namespace counts, coverage_ratio,
     or quality_distribution
     governed_by: Phase 3 Contract (finalized; read-only via Component 5)
     violation_class: data-integrity
     receipt_surface: Phase 4 entry receipt (NARRATOR received coverage_ratio +
       quality_distribution + readiness_verdict from Phase 3 as read-only)
  2. action: SHALL NOT add, remove, or reorder planned signals
     governed_by: Phase 2 Contract (immutable from roadmap.md)
     violation_class: data-integrity
     receipt_surface: Phase 4 entry receipt (NARRATOR received status.md + delta.md
       from Phase 3 -- planned signals finalized at Phase 2)
  3. action: SHALL NOT assign readiness verdicts
     governed_by: Phase 3 Contract (readiness_verdict is ANALYST output; read-only)
     violation_class: scope-boundary
     receipt_surface: Phase 4 entry receipt (NARRATOR received readiness_verdict
       from Phase 3 per Receiving Scope -- read-only to Component 5)
  4. action: SHALL NOT invoke any sub-skill other than topic-story
     governed_by: Phase 4 execution scope
     violation_class: sub-skill-exclusion
     receipt_surface: Phase 4 entry receipt (NARRATOR received status.md + delta.md
       from Phase 3 -- NARRATOR invokes topic-story only)
  5. action: SHALL NOT derive verdict_verb without first completing Component 7
     governed_by: Aggregation Rule
     violation_class: format-contract
     receipt_surface: Phase 4 entry receipt (NARRATOR received status.md coverage
       from Phase 3 -- Component 7 sub-verdict derivation precedes Component 1)

---

## Cross-Phase Obligation Index

| Obligation | Declared at | Assertion site |
|---|---|---|
| Phase 2 receives planned_signals from strategy.md | Phase Boundary Summary Phase 1->2 | Phase 2 entry receipt |
| Phase 3 receives namespace_coverage from roadmap.md | Phase Boundary Summary Phase 2->3 | Phase 3 entry receipt |
| Phase 4 receives readiness_verdict + coverage_ratio + quality_distribution (read-only) | Phase Boundary Summary Phase 3->4 (Receiving Scope) | Phase 4 entry receipt |
| Phase 4 receives session_number + signals_added_count (read-only) | Phase Boundary Summary Phase 3->4 | Phase 4 active-role header |
| Phase 4 receives refuted_flag (read-only; Aggregation Rule override) | Phase Boundary Summary Phase 3->4 | Phase 4 active-role header |
| Phase 4 does NOT receive namespace counts | Phase Boundary Summary Phase 3->4 | Phase 4 active-role header |
| Phase 4 SHALL write story.md before declaring complete | Transition Obligation | Phase 4 obligation + TERMINAL |
| verdict_after updates after Phase 4 | Two-Pass Delta Rule | Post-Phase-4 + TERMINAL |
| Cascade target is verdict_after only | Cascade Rule | Phase Boundary Summary Phase 3->4 |
| story.md carries coverage_ratio + quality_distribution from status.md | Phase 4 Contract Component 5 | Phase 4 + TERMINAL |
| story.md carries session_number from delta.md | Phase 4 Contract Component 6 | Phase 4 + TERMINAL |
| Registrar closes at strategy.md write | Closure Parity Rule | Phase 1 exit |
| Planner closes at roadmap.md write | Closure Parity Rule | Phase 2 exit |
| Analyst closes at delta.md write | Closure Parity Rule | Phase 3 exit |
| Planner entry receipt: received planned_signals from Phase 1 | Entry Receipt Rule | Phase 2 entry |
| Analyst entry receipt: received namespace_coverage from Phase 2 | Entry Receipt Rule | Phase 3 entry |
| Narrator entry receipt: received status.md + delta.md from Phase 3 | Entry Receipt Rule | Phase 4 entry |
| Each prohibition forward-links to receipt_surface | Bidirectional Prohibition Map Rule | PERSONA REGISTRY (20 entries) |
| readiness_verdict applies Quality-Aware Readiness Rule | Quality-Aware Readiness Rule | Phase 3 Step A + TERMINAL |
| Component 7 completed before Component 1 assigned | Aggregation Rule | Phase 4 + TERMINAL |
| next_signal_recommendations target driving_cluster | NARRATOR Domain (Component 4) | Phase 4 |

---

## Typed Output Contracts

### Phase 1 Contract -- strategy.md
topic_name:str, namespace (9-token), priority (3-token),
planned_signals (>= 3: signal_name, target_skill, rationale)

### Phase 2 Contract -- roadmap.md
namespace_coverage list (namespace + signals: signal_name + collection_purpose)

### Phase 3 Contract -- status.md
Coverage table -- 9 rows: namespace, planned:int, collected:int, missing:list,
quality (REAL|MOCK|INFERRED), zero_flag
Summary: coverage_ratio "X/N",
quality_distribution {real_count:int, mock_count:int, inferred_count:int},
readiness_verdict (3-token; Quality-Aware Readiness Rule applied),
refuted_flag (YES | NO)

### Phase 4 Contract -- story.md (seven-component)
Component 1: verdict_verb (5-token; Aggregation Rule from Component 7;
  REFUTED overrides if refuted_flag = YES)
Component 2: hypothesis_mutation (s0 + current)
Component 3: echoes (["NONE"] if none)
Component 4: next_signal_recommendations (3 items; >= 1 targets driving_cluster;
  gap_reason may cite quality tier)
Component 5: coverage_context (coverage_ratio + quality_distribution +
  readiness_verdict from status.md; all three verbatim; SHALL NOT recompute)
Component 6: session_context (session_number + signals_added_count from delta.md)
Component 7: namespace_cluster_sub_verdicts
  Discovery: sub_verdict (STRONG|ADEQUATE|WEAK|MISSING); namespaces: scout, prove
  Design:    sub_verdict; namespaces: draft, review
  Technical: sub_verdict; namespaces: flow, trace
  Adoption:  sub_verdict; namespaces: listen, program, topic
  driving_cluster: cluster with worst sub_verdict (or "NONE" if all STRONG)

### Session Delta Contract -- delta.md (unchanged)

---

## Two-Pass Delta Rule

Pass 1 (Phase 3 Step B): verdict_after = "NOT YET REACHED".
Pass 2 (Post-Phase-4): verdict_after = verdict_verb from story.md.

---

## Cascade Rule

Phase 3 Step B re-run after Phase 4: only verdict_after + verdict_changed update.

---

## Phase Boundary Summary

### Phase 1->2: planned_signals -> namespace_coverage
### Phase 2->3: namespace_coverage -> planned counts + missing names

### Phase 3->4:
Cascade Scope: verdict_after only.
Receiving Scope: readiness_verdict + coverage_ratio + quality_distribution +
refuted_flag (all from status.md; read-only) + session_number +
signals_added_count (from delta.md; read-only). Phase 4 does NOT receive namespace counts.
Transition Obligation: story.md before Phase 4 declares complete.

---

## Prohibition Parity Rule

Each role: exactly 5 typed prohibitions (action + governed_by + violation_class +
receipt_surface). Any entry missing a field fails audit.

---

## Phase 1 -- Register [TEMPORAL: session-independent]

*REGISTRAR active. Phase 1 Contract governs strategy.md.*
Invoke topic-new for {{topic}}. Produce strategy.md per Phase 1 Contract.
Registrar closes at strategy.md write. Registrar does not carry work into Phase 2.
GATE: Campaign SHALL NOT proceed to Phase 2 until Phase 1 postcondition satisfied.
Write to: simulations/topic/{{topic}}-strategy-{{date}}.md

---

## Phase 2 -- Plan [TEMPORAL: session-independent]

RECEIPT: PLANNER received planned_signals from Phase 1 strategy.md per Phase Boundary
Summary, Phase 1->2.
*PLANNER active. Phase 2 Contract governs roadmap.md.*
Invoke topic-plan for {{topic}}. Produce roadmap.md per Phase 2 Contract.
Planner closes at roadmap.md write. Planner does not carry work into Phase 3.
GATE: Campaign SHALL NOT proceed to Phase 3 until Phase 2 postcondition satisfied.
Write to: simulations/topic/{{topic}}-roadmap-{{date}}.md

---

## Phase 3 -- Status [TEMPORAL: session-dependent -- re-run each session]

RECEIPT: ANALYST received namespace_coverage from Phase 2 roadmap.md per Phase Boundary
Summary, Phase 2->3.
*ANALYST active. Phase 3 Contract governs status.md (quality column + quality_distribution
+ refuted_flag). Session Delta Contract governs delta.md.*

### Step A -- Coverage Status
Invoke topic-status for {{topic}}. Produce status.md per Phase 3 Contract:
- All 9 namespace rows: planned:int, collected:int, missing:list, quality:token, zero_flag
- Apply Quality-Aware Readiness Rule to derive readiness_verdict
- Compute quality_distribution; set refuted_flag (default NO)
FINALIZATION: all fields finalized at this write. Phase 4 reads coverage_ratio,
quality_distribution, readiness_verdict, refuted_flag as read-only. Phase 4 does
not receive namespace row counts.
Write to: simulations/topic/{{topic}}-status-{{date}}.md

### Step B -- Session Delta (Pass 1)
Produce delta.md. verdict_after = "NOT YET REACHED".
Write to: simulations/topic/{{topic}}-delta-{{date}}.md
Analyst closes at delta.md write. Analyst does not carry work into Phase 4.
GATE: Campaign SHALL NOT proceed to Phase 4 until status.md AND delta.md satisfy contracts.

---

## Phase 4 -- Narrative [TEMPORAL: session-dependent -- synthesize at session end]

RECEIPT: NARRATOR received readiness_verdict + coverage_ratio + quality_distribution +
refuted_flag (status.md) and session_number + signals_added_count (delta.md) from
Phase 3 per Phase Boundary Summary, Phase 3->4 (Receiving Scope).
**Obligation**: NARRATOR SHALL write story.md before declaring Phase 4 complete.
*NARRATOR active. Phase 4 Contract (seven-component). Phase 4 does NOT receive
namespace counts. Component 7 completed before Component 1 (Aggregation Rule).*

Invoke topic-story for {{topic}}. Produce story.md per Phase 4 Contract:
- Component 7 FIRST: assign sub_verdict to each cluster; identify driving_cluster
- Component 1: Aggregation Rule from Component 7; REFUTED overrides if refuted_flag = YES
- Component 2: hypothesis_mutation (s0 + current)
- Component 3: echoes (["NONE"] if none)
- Component 4: 3 recommendations; >= 1 targets driving_cluster; gap_reason may cite quality
- Component 5: coverage_ratio + quality_distribution + readiness_verdict (verbatim)
- Component 6: session_number + signals_added_count from delta.md
Write to: simulations/topic/{{topic}}-story-{{date}}.md

---

## Post-Phase-4 Delta Update (Pass 2)
Update delta.md: verdict_after = verdict_verb; verdict_changed per comparison.
Only these two fields update.

---

## Empty-State Handling

Phase 3: all collected = 0; quality = REAL (zero-signal default);
quality_distribution = {0, 0, 0}; readiness_verdict = NOT READY; refuted_flag = NO.
Phase 4 Component 7: all clusters = MISSING; driving_cluster = "ALL".
Aggregation Rule: session 1 + all MISSING -> NOT YET REACHED (empty-state override).

---

## TERMINAL -- Field-Level Completion Checklist

### Phase 1 -- strategy.md
[ ] topic_name: non-empty -- FAIL: re-run Phase 1
[ ] namespace: one of 9 tokens -- FAIL: re-run Phase 1
[ ] priority: one of 3 tokens -- FAIL: re-run Phase 1
[ ] planned_signals: count >= 3 -- FAIL: re-run Phase 1
[ ] planned_signals[*].target_skill: namespace/skill format -- FAIL: re-run Phase 1

### Phase 2 -- roadmap.md
[ ] namespace_coverage: at least one entry -- FAIL: re-run Phase 2
[ ] collection_purpose per signal -- FAIL: re-run Phase 2

### Phase 3 -- status.md
[ ] row count: exactly 9 -- FAIL: re-run Phase 3
[ ] planned: integer all 9 rows -- FAIL: re-run Phase 3
[ ] collected: integer all 9 rows -- FAIL: re-run Phase 3
[ ] missing: list each row -- FAIL: re-run Phase 3
[ ] quality: one of {REAL|MOCK|INFERRED} all 9 rows -- FAIL: re-run Phase 3
[ ] zero_flag: "NO SIGNALS" where planned = 0 AND collected = 0 -- FAIL: re-run Phase 3
[ ] coverage_ratio: "X/N" format -- FAIL: re-run Phase 3
[ ] quality_distribution: {real_count, mock_count, inferred_count} all integers
    FAIL: re-run Phase 3
[ ] readiness_verdict: Quality-Aware Readiness Rule applied; 3-token set
    FAIL: re-run Phase 3
[ ] refuted_flag: YES or NO -- FAIL: re-run Phase 3

### PERSONA REGISTRY
[ ] all 20 prohibition entries carry receipt_surface -- FAIL: re-run PERSONA REGISTRY

### Phase 4 -- story.md
[ ] story.md written before Phase 4 declared complete -- FAIL: re-run Phase 4
[ ] Component 7 completed before Component 1 assigned -- FAIL: re-run Phase 4
[ ] Component 7: all 4 clusters have sub_verdict from 4-token set -- FAIL: re-run Phase 4
[ ] Component 7: driving_cluster named -- FAIL: re-run Phase 4
[ ] verdict_verb: 5-token; consistent with Aggregation Rule -- FAIL: re-run Phase 4
[ ] REFUTED applied if refuted_flag = YES -- FAIL: re-run Phase 4
[ ] hypothesis_mutation.s0: non-empty -- FAIL: re-run Phase 4
[ ] hypothesis_mutation.current: present -- FAIL: re-run Phase 4
[ ] echoes: list present, minimum ["NONE"] -- FAIL: re-run Phase 4
[ ] next_signal_recommendations: exactly 3 items -- FAIL: re-run Phase 4
[ ] next_signal_recommendations: >= 1 targets driving_cluster -- FAIL: re-run Phase 4
[ ] coverage_context.coverage_ratio: matches status.md -- FAIL: re-run Phase 4
[ ] coverage_context.quality_distribution: matches status.md -- FAIL: re-run Phase 4
[ ] session_context.session_number: matches delta.md -- FAIL: re-run Phase 4

### Session Delta -- delta.md
[ ] session_number: integer >= 1 -- FAIL: re-run Phase 3 Step B
[ ] signals_added: list present -- FAIL: re-run Phase 3 Step B
[ ] signals_removed: list present -- FAIL: re-run Phase 3 Step B
[ ] verdict_before: one of 4-token set -- FAIL: re-run Phase 3 Step B
[ ] verdict_after: reflects Phase 4; no placeholder remaining
    FAIL: re-run Phase 3 Step B after Phase 4
[ ] verdict_changed: one of {YES|NO|N/A} -- FAIL: re-run Phase 3 Step B

All 35 items PASS: campaign complete. Dashboard SHALL be emitted.

---

## Output: Topic Dashboard

When all 35 TERMINAL items PASS, emit in order:
1. Topic registration summary (Phase 1)
2. Signal roadmap summary (Phase 2)
3. Coverage table with quality column + quality_distribution + readiness verdict (Phase 3)
4. Cluster sub-verdict table (Component 7: 4 rows; driving_cluster identified)
5. Narrative verdict (Aggregation Rule derivation shown) + hypothesis + echoes +
   top-3 recommendations (driving_cluster targeted; quality citations in gap_reason
   where applicable) + coverage_context (with quality_distribution) + session_context
6. Session delta summary
```

**Rubric targeting**: C-01 through C-49 (176/176 baseline). **C-50 candidate**
(Bidirectional Prohibition Map Rule: receipt_surface on all 20 prohibitions; 4-field
Prohibition Parity Rule; Cross-Phase Obligation Index receipt_surface row; TERMINAL item).
**C-51 candidate** (Coverage Quality Tier: quality column + Quality-Aware Readiness Rule
+ quality_distribution; prevents premature READY from synthetic datasets; gap_reason
may cite quality; 2 new TERMINAL items). **C-52 candidate** (Namespace Cluster Sub-Verdict
Decomposition: Component 7 seven-component contract; Namespace Cluster Map; Sub-Verdict
Vocabulary; Aggregation Rule; REFUTED override; driving_cluster; Component 4 targeting;
35 TERMINAL items; cluster table in dashboard). Full-stack R18: three new excellence
signals, three new candidate criteria, maximum structural coverage.
