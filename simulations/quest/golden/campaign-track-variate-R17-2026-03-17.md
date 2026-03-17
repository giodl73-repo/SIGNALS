---
skill: quest-variate
skill_target: campaign-track
round: 17
date: 2026-03-17
rubric: simulations/quest/rubrics/campaign-track-rubric-v15-2026-03-17.md
---

# Variations -- campaign-track / Round 17

Five complete, runnable skill body variations. Single-axis first (V-01, V-02, V-03),
then combined (V-04, V-05).

R16 closed with V-04 = V-05 tied at 167/167 (max against v15 rubric). Three excellence
signals extracted from R16 V-05 and V-03:

- C-46 candidate (from R16 V-05 ES-1): Prohibition Anchoring. Every prohibition in
  every role carries an inline citation to the contract section or boundary rule it
  enforces. Format: `SHALL NOT [action] ([Section Reference])`. 20 anchored citations
  across 4 roles x 5 prohibitions. Makes prohibition-to-contract traceability auditable
  per item without cross-reference reading.

- C-47 candidate (from R16 V-03 + V-05 ES-2): Closure Parity Rule as governing section.
  A declared rule mandating one closure statement per phase exit at all three handoff
  boundaries. The rule + three instances are already in R16 V-05 baseline.

- C-48 candidate (from R16 V-04 + V-05 ES-3): NARRATOR domain in PERSONA REGISTRY
  explicitly scopes Components 5-6. R16 V-04/V-05 extended NARRATOR domain description
  to name the read-only input obligation; R16 V-01 did not. Connects role identity
  to the extended Phase 4 contract from the registry entry.

All five R17 variations score 167/167 on rubric v15 (full C-01 through C-45 pass).
The axes generate excellence signals targeting v16 criteria (C-46, C-47, C-48).

---

R17 variation axes:
- V-01: Single-axis -- Typed prohibition anchoring (C-46 maximum: structured 3-field
  format per prohibition with action/governed_by/violation_class; makes prohibition
  category classifiable without reading prohibition body)
- V-02: Single-axis -- Full registry-component field alignment (C-48 extension: all
  four roles have Domain entries that explicitly name the specific contract fields they
  own, not just artifact names; registry becomes a contract substitute)
- V-03: Single-axis -- Phase Entry Receipt Rule (new axis: symmetric mirror of Closure
  Parity Rule; each phase 2/3/4 entry carries a receipt statement citing the Phase
  Boundary Summary; bidirectional boundary acknowledgment)
- V-04: Combined -- typed anchoring (V-01) + entry receipts (V-03)
- V-05: Full stack -- typed anchoring + full field alignment + entry receipts
  (V-01 + V-02 + V-03)

All five inherit R16 V-05 baseline (all C-01 through C-45: four-phase structure,
PERSONA REGISTRY with Prohibition Parity Rule, six-component Phase 4 contract,
Closure Parity Rule at three phase exits, Cross-Phase Obligation Index, triptych
Phase Boundary Summary Phase 3->4 with temporal headers, four C-41 back-reference
surfaces, Phase 3 Step A finalization annotation, Cascade Rule, Two-Pass Delta Rule,
30 TERMINAL items, Prohibition Anchoring baseline from R16 V-05). Differences
isolated to: prohibition entry format in PERSONA REGISTRY, domain field descriptions
in PERSONA REGISTRY, and phase entry header acknowledgment statements.

---

## V-01 -- Axis: Typed prohibition anchoring (C-46 maximum)

**Hypothesis**: R16 V-05 anchored each prohibition with a free-form inline parenthetical
`(Section Reference)`. V-01 tests whether a **typed three-field format** -- with named
fields `action:`, `governed_by:`, and `violation_class:` -- makes prohibition-to-contract
linkage machine-parseable and categorically auditable. The `violation_class` field uses a
controlled 5-token vocabulary: `scope-boundary | role-isolation | sub-skill-exclusion |
data-integrity | format-contract`. A reader who wants all scope-boundary violations can
scan violation_class tokens without reading prohibition bodies. A reader who wants to
verify a prohibition is grounded consults `governed_by` directly. Registry: four roles,
20 typed entries. Closure Parity Rule: R16 V-05 baseline (three instances). Phase 4
contract: six-component. TERMINAL: 30 items.

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

## Prohibition Type Vocabulary

violation_class tokens (exactly one per prohibition):
- scope-boundary: prohibition prevents acting in another phase's domain
- role-isolation: prohibition prevents acting in another role's functional area
- sub-skill-exclusion: prohibition limits sub-skill invocation to phase assignment
- data-integrity: prohibition prevents modifying finalized data
- format-contract: prohibition enforces typed output constraint

---

## PERSONA REGISTRY

All four campaign personas declared here. This registry is the authority for role
identity, ownership, and prohibitions. Phase headers cite this registry; they do not
restate it. Prohibitions use typed three-field format: action, governed_by,
violation_class.

### REGISTRAR
- Phase: 1 (Register)
- Owned artifact: strategy.md
- Domain: Topic identity, namespace assignment, signal planning
- Prohibitions (exactly 5, typed):
  1. action: SHALL NOT produce coverage tables, coverage ratios, or readiness verdicts
     governed_by: Phase 3 Contract (coverage computation is ANALYST domain; status.md
       is Phase 3 artifact)
     violation_class: scope-boundary
  2. action: SHALL NOT synthesize or interpret signal content
     governed_by: Phase 4 Contract (synthesis is NARRATOR domain; story.md is
       Phase 4 artifact)
     violation_class: role-isolation
  3. action: SHALL NOT assign verdict verbs from Phase 4 controlled vocabulary
     governed_by: Phase 4 Contract (verdict_verb is a 5-token NARRATOR output;
       controlled vocabulary is Phase 4 domain)
     violation_class: role-isolation
  4. action: SHALL NOT invoke any sub-skill other than topic-new
     governed_by: Phase 1 execution scope (one sub-skill per phase; topic-new is
       the Phase 1 assignment)
     violation_class: sub-skill-exclusion
  5. action: SHALL NOT list signals not declared in planned_signals
     governed_by: Phase 1 Contract (planned_signals is the founding artifact;
       REGISTRAR does not amend post-registration)
     violation_class: data-integrity

### PLANNER
- Phase: 2 (Plan)
- Owned artifact: roadmap.md
- Domain: Signal ordering, collection purpose, namespace routing
- Prohibitions (exactly 5, typed):
  1. action: SHALL NOT register, rename, or modify topic identity
     governed_by: Phase 1 Contract (topic_name, namespace, priority are REGISTRAR
       outputs; finalized at strategy.md write)
     violation_class: scope-boundary
  2. action: SHALL NOT query or report which signals are collected
     governed_by: Phase 3 Contract (collected count is ANALYST domain; status.md
       is Phase 3 artifact)
     violation_class: scope-boundary
  3. action: SHALL NOT produce readiness verdicts or coverage ratios
     governed_by: Phase 3 Contract (readiness_verdict + coverage_ratio are ANALYST
       outputs; finalized at Phase 3 Step A)
     violation_class: scope-boundary
  4. action: SHALL NOT synthesize findings or assign verdict verbs
     governed_by: Phase 4 Contract (synthesis + verdict_verb are NARRATOR domain)
     violation_class: role-isolation
  5. action: SHALL NOT invoke any sub-skill other than topic-plan
     governed_by: Phase 2 execution scope (one sub-skill per phase; topic-plan is
       the Phase 2 assignment)
     violation_class: sub-skill-exclusion

### ANALYST
- Phase: 3 (Status)
- Owned artifacts: status.md, delta.md
- Domain: Signal counting, coverage computation, session diff, readiness verdict
- Prohibitions (exactly 5, typed):
  1. action: SHALL NOT add planned signals beyond Phase 2 roadmap
     governed_by: Phase 2 Contract (namespace_coverage is PLANNER output; finalized
       at roadmap.md write; Phase 3 Step A reads it as finalized input)
     violation_class: data-integrity
  2. action: SHALL NOT produce verdict verbs from Phase 4 controlled vocabulary
     governed_by: Phase 4 Contract (verdict_verb is a 5-token NARRATOR output;
       ANALYST produces readiness_verdict, a separate 3-token field)
     violation_class: role-isolation
  3. action: SHALL NOT interpret meaning from signal content or editorialize
     governed_by: Phase 4 Contract (interpretation + synthesis are NARRATOR domain;
       story.md is the Phase 4 artifact)
     violation_class: role-isolation
  4. action: SHALL NOT invoke any sub-skill other than topic-status
     governed_by: Phase 3 execution scope (one sub-skill per phase; topic-status
       is the Phase 3 assignment)
     violation_class: sub-skill-exclusion
  5. action: SHALL NOT use narrative counts where integers are required
     governed_by: Phase 3 Contract (planned and collected SHALL be integer >= 0;
       narrative counts violate the format-contract)
     violation_class: format-contract

### NARRATOR
- Phase: 4 (Narrative)
- Owned artifact: story.md
- Domain: Hypothesis mutation, echo synthesis, next-signal recommendations, verdict,
  coverage evidence reporting (Components 5-6 from status.md + delta.md)
- Prohibitions (exactly 5, typed):
  1. action: SHALL NOT modify coverage table, namespace counts, or coverage_ratio
     governed_by: Phase 3 Contract (coverage table + coverage_ratio are ANALYST
       outputs; finalized at Phase 3 Step A; Receiving Scope, Phase Boundary Summary,
       Phase 3->4)
     violation_class: data-integrity
  2. action: SHALL NOT add, remove, or reorder planned signals
     governed_by: Phase 2 Contract (namespace_coverage is PLANNER output; finalized
       at roadmap.md write; Phase 3 and Phase 4 read it as immutable input)
     violation_class: data-integrity
  3. action: SHALL NOT assign readiness verdicts (READY / NOT READY / CONDITIONALLY READY)
     governed_by: Phase 3 Contract (readiness_verdict is a 3-token ANALYST output;
       NARRATOR reads it read-only via Component 5; SHALL NOT reassign it)
     violation_class: scope-boundary
  4. action: SHALL NOT invoke any sub-skill other than topic-story
     governed_by: Phase 4 execution scope (one sub-skill per phase; topic-story is
       the Phase 4 assignment)
     violation_class: sub-skill-exclusion
  5. action: SHALL NOT declare Phase 4 complete without writing story.md
     governed_by: Transition Obligation (Phase Boundary Summary, Phase 3->4);
       interrupted and completed campaigns indistinguishable from delta.md alone
       without story.md
     violation_class: data-integrity

---

## Cross-Phase Obligation Index

| Obligation | Declared at | Assertion site |
|---|---|---|
| Phase 2 receives planned_signals from strategy.md | Phase Boundary Summary Phase 1->2 | Phase 2 active-role header |
| Phase 3 receives namespace_coverage from roadmap.md | Phase Boundary Summary Phase 2->3 | Phase 3 active-role header |
| Phase 4 receives readiness_verdict + coverage_ratio (read-only) | Phase Boundary Summary Phase 3->4 (Receiving Scope) | Phase 4 active-role header |
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
Governs Phase 3 Step B re-run after Phase 4 completes.
- Update target: verdict_after in delta.md (Phase 4-dependent; sole cascade target)
- Excluded: session_number, signals_added, signals_removed, verdict_before,
  verdict_changed (finalized at Phase 3 Step B; Phase 4 does not own them)

#### Receiving Scope (entry concern)
Governs Phase 4 inputs at entry. Independent of Cascade Scope.
- Phase 4 receives: readiness_verdict + coverage_ratio from status.md
  (read-only; carried to story.md Component 5; SHALL NOT be modified)
- Phase 4 receives: session_number + signals_added count from delta.md
  (read-only; carried to story.md Component 6)
- Phase 4 receives: delta.md with verdict_after = "NOT YET REACHED" (placeholder)
- Phase 4 does NOT receive: namespace counts (planned, collected, missing, zero_flag)
  -- finalized at Phase 3 Step A; Phase 4 cannot modify them; they are Phase 3 domain

#### Transition Obligation (exit concern)
Phase 4 SHALL write story.md before declaring complete. Without story.md, interrupted
and completed campaigns are indistinguishable from delta.md alone -- both states
produce verdict_after = NOT YET REACHED.

### Post-Phase-4 -> Dashboard Boundary
- delta.md: verdict_after + verdict_changed updated (Pass 2)
- Dashboard: all five artifacts written; TERMINAL 30 items PASS

---

## Prohibition Parity Rule

Each role carries exactly 5 typed prohibitions (action + governed_by + violation_class).
Declared in PERSONA REGISTRY. Phase sections cite registry; prohibitions are not
restated in phase bodies. A role with 4 or 6 entries SHALL fail audit.

---

## Phase 1 -- Register

*REGISTRAR active (see PERSONA REGISTRY: domain + 5 typed prohibitions).
Phase 1 Contract governs output. Boundary: strategy.md -> Phase 2.*

Invoke topic-new for {{topic}}. Produce strategy.md per Phase 1 Contract.

Phase 1 postcondition: strategy.md present, all fields typed correctly.

Registrar closes at strategy.md write. Registrar does not carry work into Phase 2.

GATE: Campaign SHALL NOT proceed to Phase 2 until Phase 1 postcondition satisfied.

Write to: simulations/topic/{{topic}}-strategy-{{date}}.md

---

## Phase 2 -- Plan

*PLANNER active (see PERSONA REGISTRY: domain + 5 typed prohibitions).
Phase 2 Contract governs output. Boundary: Phase 2 receives planned_signals from
strategy.md per Phase Boundary Summary, Phase 1->2; produces roadmap.md for Phase 3.*

Invoke topic-plan for {{topic}}. Produce roadmap.md per Phase 2 Contract.

Phase 2 postcondition: roadmap.md present, at least one namespace entry,
collection_purpose per signal.

Planner closes at roadmap.md write. Planner does not carry work into Phase 3.

GATE: Campaign SHALL NOT proceed to Phase 3 until Phase 2 postcondition satisfied.

Write to: simulations/topic/{{topic}}-roadmap-{{date}}.md

---

## Phase 3 -- Status

*ANALYST active (see PERSONA REGISTRY: domain + 5 typed prohibitions).
Phase 3 Contract governs status.md. Session Delta Contract governs delta.md.
Phase Boundary Summary (Cascade Scope + Receiving Scope + Transition Obligation)
governs Phase 3->4. Boundary: Phase 3 receives namespace_coverage from roadmap.md
per Phase Boundary Summary, Phase 2->3.*

### Step A -- Coverage Status

Invoke topic-status for {{topic}}. Produce status.md per Phase 3 Contract:
- All 9 namespace rows; planned and collected as integers; missing as list of names
- zero_flag = "NO SIGNALS" where planned = 0 AND collected = 0
- coverage_ratio in "X/N" format; readiness_verdict from 3-token set

FINALIZATION: status.md fields finalized at this write (Phase 3 Step A). Per Receiving
Scope (Phase Boundary Summary, Phase 3->4), Phase 4 reads coverage_ratio and
readiness_verdict as read-only context (Component 5); Phase 4 does not receive
namespace counts.

Write to: simulations/topic/{{topic}}-status-{{date}}.md

### Step B -- Session Delta (Pass 1)

Produce delta.md per Session Delta Contract.
verdict_after = "NOT YET REACHED" (placeholder; Pass 1). All other fields are final.

Write to: simulations/topic/{{topic}}-delta-{{date}}.md

Analyst closes at delta.md write. Analyst does not carry work into Phase 4.

Phase 3 postcondition: status.md AND delta.md both present, typed correctly.

GATE: Campaign SHALL NOT proceed to Phase 4 until Phase 3 postcondition satisfied.

---

## Phase 4 -- Narrative

**Obligation**: The NARRATOR SHALL write story.md before declaring Phase 4 complete.
The Transition Obligation (Phase Boundary Summary, Phase 3->4) is violated otherwise.
Interrupted and completed campaigns are indistinguishable from delta.md alone.

*NARRATOR active (see PERSONA REGISTRY: domain + 5 typed prohibitions).
Phase 4 Contract (six-component) governs output. Receiving Scope (Phase Boundary
Summary, Phase 3->4): Phase 4 does NOT receive namespace counts (finalized Phase 3
Step A domain). Phase 4 receives readiness_verdict + coverage_ratio (read-only;
Component 5) and session_number + signals_added_count from delta.md (read-only;
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

All four phases run. All closure statements apply.

Phase 3: collected = 0 all rows; readiness_verdict = NOT READY; session_number = 1;
signals_added = []; verdict_before = NONE; verdict_after = NOT YET REACHED; verdict_changed = N/A.

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

### Session Delta -- delta.md
[ ] session_number: integer >= 1 -- FAIL: re-run Phase 3 Step B
[ ] signals_added: list present ([] permitted) -- FAIL: re-run Phase 3 Step B
[ ] signals_removed: list present ([] permitted) -- FAIL: re-run Phase 3 Step B
[ ] verdict_before: one of {READY|NOT READY|CONDITIONALLY READY|NONE}
    FAIL: re-run Phase 3 Step B
[ ] verdict_after: reflects Phase 4 verdict_verb; placeholder NOT remaining after
    Phase 4 completes -- FAIL: re-run Phase 3 Step B after Phase 4 completes
[ ] verdict_changed: one of {YES|NO|N/A} -- FAIL: re-run Phase 3 Step B

All 30 items PASS: campaign complete. Dashboard SHALL be emitted.

---

## Output: Topic Dashboard

When all 30 TERMINAL items show PASS, emit in order:
1. Topic registration summary (Phase 1)
2. Signal roadmap summary (Phase 2)
3. Coverage table with readiness verdict (Phase 3)
4. Narrative verdict + hypothesis + echoes + top-3 + coverage_context +
   session_context (Phase 4, six components)
5. Session delta summary
```

**Rubric targeting**: C-01 through C-45 (full 167/167 baseline). **C-46 maximum**
(Prohibition Anchoring elevated to typed 3-field format: action + governed_by +
violation_class; Prohibition Type Vocabulary declared as governing section with 5-token
controlled vocabulary for violation_class; 20 typed entries across 4 roles x 5
prohibitions; violation_class enables category-scan without reading prohibition bodies;
governed_by replaces free-form parens with a named field; distinct from R16 V-05's
inline parenthetical baseline). **C-47 absent** (deliberate; Closure Parity Rule at
baseline level from R16 V-05). **C-48 absent** (NARRATOR domain at R16 V-04/V-05
baseline level; other roles not extended).

---

## V-02 -- Axis: Full registry-component field alignment (C-48 maximum)

**Hypothesis**: R16 V-04/V-05 extended NARRATOR's Domain entry in the PERSONA REGISTRY
to name Components 5-6 explicitly. V-02 tests whether applying this same precision to
**all four roles** -- each role's Domain field explicitly lists the specific contract
fields it owns, not just the artifact name -- makes the registry a standalone contract
substitute. The hypothesis is that a reader consulting the PERSONA REGISTRY alone can
determine: what artifact each role produces, which contract fields belong to which role,
and what typed constraints apply. This eliminates the need to cross-reference the Typed
Output Contracts section for ownership determination. Prohibition Anchoring: R16 V-05
inline baseline (not elevated to typed format). Closure Parity Rule: R16 V-05 baseline.
TERMINAL: 30 items.

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

---

## PERSONA REGISTRY

All four campaign personas declared here. This registry is the authority for role
identity, ownership, and prohibitions. Each Domain entry names the specific contract
fields owned by the role. Phase headers cite this registry; they do not restate it.

### REGISTRAR
- Phase: 1 (Register)
- Owned artifact: strategy.md
- Domain: Topic identity, namespace assignment, signal planning
  [owns Phase 1 Contract fields: topic_name (string, non-empty), namespace
  (9-token: scout|draft|review|flow|trace|prove|listen|program|topic), priority
  (3-token: High|Medium|Low), planned_signals (list >= 3 items, each with
  signal_name + target_skill + rationale)]
- Prohibitions (exactly 5):
  1. SHALL NOT produce coverage tables, coverage ratios, or readiness verdicts
     (Phase 3 Contract domain; ANALYST owns status.md)
  2. SHALL NOT synthesize or interpret signal content (Phase 4 Contract domain;
     NARRATOR owns story.md)
  3. SHALL NOT assign verdict verbs from Phase 4 controlled vocabulary (Phase 4
     Contract; verdict_verb is NARRATOR output)
  4. SHALL NOT invoke any sub-skill other than topic-new (Phase 1 execution scope)
  5. SHALL NOT list signals not declared in planned_signals (Phase 1 Contract;
     planned_signals is the founding artifact)

### PLANNER
- Phase: 2 (Plan)
- Owned artifact: roadmap.md
- Domain: Signal ordering, collection purpose, namespace routing
  [owns Phase 2 Contract fields: namespace_coverage (list of entries, each with
  namespace (9-token) + signals list (each with signal_name matching strategy.md
  + collection_purpose (one sentence)))]
- Prohibitions (exactly 5):
  1. SHALL NOT register, rename, or modify topic identity (Phase 1 Contract domain;
     topic_name, namespace, priority are REGISTRAR outputs finalized at strategy.md)
  2. SHALL NOT query or report which signals are collected (Phase 3 Contract domain;
     collected count is ANALYST output in status.md)
  3. SHALL NOT produce readiness verdicts or coverage ratios (Phase 3 Contract;
     readiness_verdict + coverage_ratio are ANALYST outputs)
  4. SHALL NOT synthesize findings or assign verdict verbs (Phase 4 Contract domain)
  5. SHALL NOT invoke any sub-skill other than topic-plan (Phase 2 execution scope)

### ANALYST
- Phase: 3 (Status)
- Owned artifacts: status.md, delta.md
- Domain: Signal counting, coverage computation, session diff, readiness verdict
  [owns Phase 3 Contract fields: 9-row coverage table (namespace, planned:int >= 0,
  collected:int >= 0, missing:list-of-strings, zero_flag:"NO SIGNALS" where both
  zero), coverage_ratio (format "X/N"), readiness_verdict (3-token: READY|NOT READY|
  CONDITIONALLY READY); owns Session Delta Contract fields: session_number (int >= 1),
  signals_added (list), signals_removed (list), verdict_before (4-token: READY|NOT
  READY|CONDITIONALLY READY|NONE), verdict_after (4-token; Pass 1 = "NOT YET REACHED";
  Pass 2 = verdict_verb from story.md), verdict_changed (3-token: YES|NO|N/A)]
- Prohibitions (exactly 5):
  1. SHALL NOT add planned signals beyond Phase 2 roadmap (Phase 2 Contract domain;
     namespace_coverage finalized at roadmap.md write)
  2. SHALL NOT produce verdict verbs from Phase 4 controlled vocabulary (Phase 4
     Contract; verdict_verb is distinct from readiness_verdict)
  3. SHALL NOT interpret meaning from signal content or editorialize (Phase 4 domain)
  4. SHALL NOT invoke any sub-skill other than topic-status (Phase 3 execution scope)
  5. SHALL NOT use narrative counts where integers are required (Phase 3 Contract;
     planned and collected are integer >= 0)

### NARRATOR
- Phase: 4 (Narrative)
- Owned artifact: story.md
- Domain: Hypothesis mutation, echo synthesis, next-signal recommendations, verdict,
  coverage evidence reporting (Components 5-6 from status.md + delta.md)
  [owns Phase 4 Contract fields: Component 1 verdict_verb (5-token: CONFIRMED|
  REFUTED|EVOLVING|INSUFFICIENT|NOT YET REACHED), Component 2 hypothesis_mutation
  (s0:string + current:string-or-"UNCHANGED"), Component 3 echoes (list, ["NONE"]
  if none), Component 4 next_signal_recommendations (exactly 3 items: namespace +
  skill + gap_reason), Component 5 coverage_context (coverage_ratio:string copied
  verbatim from status.md + readiness_verdict:string copied verbatim from status.md;
  read-only; SHALL NOT recompute or reassign), Component 6 session_context
  (session_number:int from delta.md + signals_added_count:int >= 0 from delta.md;
  read-only)]
- Prohibitions (exactly 5):
  1. SHALL NOT modify coverage table, namespace counts, or coverage_ratio (Phase 3
     Contract domain; ANALYST owns status.md; Receiving Scope, Phase Boundary Summary,
     Phase 3->4)
  2. SHALL NOT add, remove, or reorder planned signals (Phase 2 Contract domain;
     namespace_coverage finalized at roadmap.md)
  3. SHALL NOT assign readiness verdicts (READY / NOT READY / CONDITIONALLY READY)
     (Phase 3 Contract; readiness_verdict is ANALYST output; NARRATOR reads it
     read-only via Component 5)
  4. SHALL NOT invoke any sub-skill other than topic-story (Phase 4 execution scope)
  5. SHALL NOT declare Phase 4 complete without writing story.md (Transition
     Obligation, Phase Boundary Summary, Phase 3->4)

---

## Cross-Phase Obligation Index

| Obligation | Declared at | Assertion site |
|---|---|---|
| Phase 2 receives planned_signals from strategy.md | Phase Boundary Summary Phase 1->2 | Phase 2 active-role header |
| Phase 3 receives namespace_coverage from roadmap.md | Phase Boundary Summary Phase 2->3 | Phase 3 active-role header |
| Phase 4 receives readiness_verdict + coverage_ratio (read-only) | Phase Boundary Summary Phase 3->4 (Receiving Scope) | Phase 4 active-role header |
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
- namespace_coverage: list; each entry:
  - namespace: string (one of 9 Signal namespaces)
  - signals: list; each item:
    - signal_name: string (matches strategy.md)
    - collection_purpose: string (one sentence)

### Phase 3 Contract -- status.md
Coverage table -- all 9 rows:
  namespace, planned:int, collected:int, missing:list, zero_flag (where both zero)
Summary: coverage_ratio "X/N"; readiness_verdict READY|NOT READY|CONDITIONALLY READY

### Phase 4 Contract -- story.md (six-component)
Component 1: verdict_verb (5-token)
Component 2: hypothesis_mutation (s0 + current)
Component 3: echoes (list; ["NONE"] if none)
Component 4: next_signal_recommendations (exactly 3: namespace + skill + gap_reason)
Component 5: coverage_context (coverage_ratio + readiness_verdict, copied verbatim)
Component 6: session_context (session_number + signals_added_count)

### Session Delta Contract -- delta.md
session_number:int, signals_added:list, signals_removed:list,
verdict_before (4-token), verdict_after (4-token), verdict_changed (3-token)

---

## Two-Pass Delta Rule

Pass 1 (Phase 3 Step B): verdict_after = "NOT YET REACHED".
Pass 2 (Post-Phase-4): verdict_after = verdict_verb from story.md.

---

## Cascade Rule

Phase 3 Step B re-run after Phase 4 completes: only verdict_after updates.
All other delta.md fields finalized at Phase 3 Step B; SHALL NOT cascade.

---

## Phase Boundary Summary

### Phase 1 -> Phase 2 Boundary
strategy.md planned_signals -> Phase 2 namespace_coverage input

### Phase 2 -> Phase 3 Boundary
roadmap.md namespace_coverage -> Phase 3 planned counts + missing names

### Phase 3 -> Phase 4 Boundary

#### Cascade Scope (re-run concern)
Update target: verdict_after only. Excluded: session_number, signals_added,
signals_removed, verdict_before, verdict_changed (finalized Phase 3 Step B).

#### Receiving Scope (entry concern)
Phase 4 receives: readiness_verdict + coverage_ratio (read-only; Component 5)
Phase 4 receives: session_number + signals_added count (read-only; Component 6)
Phase 4 receives: delta.md with verdict_after = "NOT YET REACHED"
Phase 4 does NOT receive: namespace counts (Phase 3 Step A domain; finalized)

#### Transition Obligation (exit concern)
Phase 4 SHALL write story.md. Interrupted + completed campaigns indistinguishable
from delta.md alone without story.md.

### Post-Phase-4 -> Dashboard Boundary
delta.md verdict_after + verdict_changed updated. Dashboard: TERMINAL PASS.

---

## Prohibition Parity Rule

Each role carries exactly 5 prohibitions with inline citations (declared in PERSONA
REGISTRY). Phase sections cite registry; prohibitions not restated in phase bodies.

---

## Phase 1 -- Register

*REGISTRAR active (see PERSONA REGISTRY: domain with Phase 1 Contract field ownership
+ 5 prohibitions). Phase 1 Contract governs output. Boundary: strategy.md -> Phase 2.*

Invoke topic-new for {{topic}}. Produce strategy.md per Phase 1 Contract.

Phase 1 postcondition: strategy.md present, all fields typed correctly.

Registrar closes at strategy.md write. Registrar does not carry work into Phase 2.

GATE: Campaign SHALL NOT proceed to Phase 2 until Phase 1 postcondition satisfied.

Write to: simulations/topic/{{topic}}-strategy-{{date}}.md

---

## Phase 2 -- Plan

*PLANNER active (see PERSONA REGISTRY: domain with Phase 2 Contract field ownership
+ 5 prohibitions). Phase 2 Contract governs output. Boundary: Phase 2 receives
planned_signals from strategy.md per Phase Boundary Summary, Phase 1->2.*

Invoke topic-plan for {{topic}}. Produce roadmap.md per Phase 2 Contract.

Phase 2 postcondition: roadmap.md present, at least one namespace entry.

Planner closes at roadmap.md write. Planner does not carry work into Phase 3.

GATE: Campaign SHALL NOT proceed to Phase 3 until Phase 2 postcondition satisfied.

Write to: simulations/topic/{{topic}}-roadmap-{{date}}.md

---

## Phase 3 -- Status

*ANALYST active (see PERSONA REGISTRY: domain with Phase 3 + Session Delta Contract
field ownership + 5 prohibitions). Phase Boundary Summary governs Phase 3->4.
Boundary: Phase 3 receives namespace_coverage from roadmap.md per Phase Boundary
Summary, Phase 2->3.*

### Step A -- Coverage Status

Invoke topic-status for {{topic}}. Produce status.md per Phase 3 Contract.
FINALIZATION: status.md fields finalized at this write; Phase 4 reads coverage_ratio
+ readiness_verdict as read-only (Component 5).

Write to: simulations/topic/{{topic}}-status-{{date}}.md

### Step B -- Session Delta (Pass 1)

Produce delta.md per Session Delta Contract. verdict_after = "NOT YET REACHED".

Write to: simulations/topic/{{topic}}-delta-{{date}}.md

Analyst closes at delta.md write. Analyst does not carry work into Phase 4.

Phase 3 postcondition: status.md AND delta.md present, typed correctly.

GATE: Campaign SHALL NOT proceed to Phase 4 until Phase 3 postcondition satisfied.

---

## Phase 4 -- Narrative

**Obligation**: NARRATOR SHALL write story.md before declaring Phase 4 complete.
Transition Obligation (Phase Boundary Summary, Phase 3->4) violated otherwise.

*NARRATOR active (see PERSONA REGISTRY: domain with Phase 4 Contract field ownership
for all six components + 5 prohibitions). Receiving Scope (Phase Boundary Summary,
Phase 3->4): Phase 4 does NOT receive namespace counts; receives readiness_verdict +
coverage_ratio (Component 5) and session_number + signals_added_count (Component 6).*

Invoke topic-story for {{topic}}. Produce story.md per Phase 4 Contract (six components).

Write to: simulations/topic/{{topic}}-story-{{date}}.md

---

## Post-Phase-4 Delta Update (Pass 2)

Update delta.md: verdict_after = verdict_verb; verdict_changed per comparison.
Only these two fields update. See Cascade Rule.

Update: simulations/topic/{{topic}}-delta-{{date}}.md

---

## Empty-State Handling

### First Invocation (0 signals collected)

All phases run. Phase 3: collected = 0; readiness_verdict = NOT READY;
session_number = 1; signals_added = []. Phase 4: verdict_verb = NOT YET REACHED;
Component 5 from status.md; Component 6: session_number = 1, signals_added_count = 0.

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
[ ] planned: integer all 9 rows -- FAIL: re-run Phase 3
[ ] collected: integer all 9 rows -- FAIL: re-run Phase 3
[ ] missing: list of names each row -- FAIL: re-run Phase 3
[ ] zero_flag: "NO SIGNALS" where planned = 0 AND collected = 0 -- FAIL: re-run Phase 3
[ ] coverage_ratio: "X/N" format -- FAIL: re-run Phase 3
[ ] readiness_verdict: one of 3-token set -- FAIL: re-run Phase 3

### Phase 4 -- story.md
[ ] story.md written before Phase 4 declared complete (Transition Obligation) -- FAIL: re-run Phase 4
[ ] verdict_verb: one of 5 tokens -- FAIL: re-run Phase 4
[ ] hypothesis_mutation.s0: non-empty -- FAIL: re-run Phase 4
[ ] hypothesis_mutation.current: present -- FAIL: re-run Phase 4
[ ] echoes: list present, minimum ["NONE"] -- FAIL: re-run Phase 4
[ ] next_signal_recommendations: exactly 3 items -- FAIL: re-run Phase 4
[ ] next_signal_recommendations[*].namespace: present -- FAIL: re-run Phase 4
[ ] next_signal_recommendations[*].gap_reason: present -- FAIL: re-run Phase 4
[ ] coverage_context.coverage_ratio: matches status.md -- FAIL: re-run Phase 4
[ ] session_context.session_number: matches delta.md -- FAIL: re-run Phase 4

### Session Delta -- delta.md
[ ] session_number: integer >= 1 -- FAIL: re-run Phase 3 Step B
[ ] signals_added: list present -- FAIL: re-run Phase 3 Step B
[ ] signals_removed: list present -- FAIL: re-run Phase 3 Step B
[ ] verdict_before: one of 4-token set -- FAIL: re-run Phase 3 Step B
[ ] verdict_after: reflects Phase 4 verdict_verb; no placeholder after Phase 4
    completes -- FAIL: re-run Phase 3 Step B after Phase 4 completes
[ ] verdict_changed: one of {YES|NO|N/A} -- FAIL: re-run Phase 3 Step B

All 30 items PASS: campaign complete. Dashboard SHALL be emitted.

---

## Output: Topic Dashboard

When all 30 TERMINAL items show PASS, emit in order:
1. Topic registration summary (Phase 1)
2. Signal roadmap summary (Phase 2)
3. Coverage table with readiness verdict (Phase 3)
4. Narrative verdict + hypothesis + echoes + top-3 + coverage_context +
   session_context (Phase 4, six components)
5. Session delta summary
```

**Rubric targeting**: C-01 through C-45 (full 167/167 baseline). **C-48 maximum**
(Full registry-component field alignment: all four role Domain entries in PERSONA
REGISTRY explicitly name the specific contract fields they own with type annotations;
REGISTRAR lists Phase 1 Contract fields; PLANNER lists Phase 2 Contract fields;
ANALYST lists Phase 3 Contract + Session Delta Contract fields; NARRATOR lists all
six Phase 4 Contract components with read-only annotations for Components 5-6;
registry entries are self-contained contract substitutes). **C-46** (Prohibition
Anchoring at R16 V-05 inline baseline; not elevated to typed format). **C-47**
(Closure Parity Rule at baseline level).

---

## V-03 -- Axis: Phase Entry Receipt Rule (new axis)

**Hypothesis**: Closure Parity Rule creates exit-side boundary acknowledgment (three
closure statements at Phase 1, 2, 3 exits). V-03 tests whether a symmetric **Entry
Receipt Rule** -- mandating one receipt statement at each phase ENTRY (Phases 2, 3, 4)
citing the incoming artifact and its Phase Boundary Summary section -- closes the
bidirectional boundary loop. The hypothesis is that Closure + Receipt = fully auditable
boundary: a reader scanning six fixed locations (three exits + three entries) can verify
every inter-phase handoff without reading the Phase Boundary Summary body. Cross-Phase
Obligation Index gains three rows for entry receipts. Format: "RECEIPT: [ROLE] received
[artifact] from Phase [N] per Phase Boundary Summary, Phase [N]->[N+1]." Three
instances required (Phases 2, 3, 4). Phase 1 has no prior phase; it carries no receipt.
Phase 4 Contract: six-component. PERSONA REGISTRY: R16 V-05 baseline (inline citations,
NARRATOR domain scopes Components 5-6). TERMINAL: 30 items.

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

## PERSONA REGISTRY

All four campaign personas declared here. This registry is the authority for role
identity, ownership, and prohibitions. Phase headers cite this registry; they do
not restate it.

### REGISTRAR
- Phase: 1 (Register)
- Owned artifact: strategy.md
- Domain: Topic identity, namespace assignment, signal planning
- Prohibitions (exactly 5):
  1. SHALL NOT produce coverage tables, coverage ratios, or readiness verdicts
     (Phase 3 Contract domain; ANALYST owns status.md)
  2. SHALL NOT synthesize or interpret signal content (Phase 4 Contract domain)
  3. SHALL NOT assign verdict verbs from Phase 4 controlled vocabulary
     (Phase 4 Contract; verdict_verb is NARRATOR output)
  4. SHALL NOT invoke any sub-skill other than topic-new (Phase 1 execution scope)
  5. SHALL NOT list signals not declared in planned_signals (Phase 1 Contract)

### PLANNER
- Phase: 2 (Plan)
- Owned artifact: roadmap.md
- Domain: Signal ordering, collection purpose, namespace routing
- Prohibitions (exactly 5):
  1. SHALL NOT register, rename, or modify topic identity (Phase 1 Contract domain)
  2. SHALL NOT query or report which signals are collected (Phase 3 Contract domain)
  3. SHALL NOT produce readiness verdicts or coverage ratios (Phase 3 Contract)
  4. SHALL NOT synthesize findings or assign verdict verbs (Phase 4 Contract domain)
  5. SHALL NOT invoke any sub-skill other than topic-plan (Phase 2 execution scope)

### ANALYST
- Phase: 3 (Status)
- Owned artifacts: status.md, delta.md
- Domain: Signal counting, coverage computation, session diff, readiness verdict
- Prohibitions (exactly 5):
  1. SHALL NOT add planned signals beyond Phase 2 roadmap (Phase 2 Contract domain)
  2. SHALL NOT produce verdict verbs from Phase 4 controlled vocabulary
     (Phase 4 Contract; distinct from readiness_verdict)
  3. SHALL NOT interpret meaning from signal content or editorialize (Phase 4 domain)
  4. SHALL NOT invoke any sub-skill other than topic-status (Phase 3 execution scope)
  5. SHALL NOT use narrative counts where integers are required (Phase 3 Contract)

### NARRATOR
- Phase: 4 (Narrative)
- Owned artifact: story.md
- Domain: Hypothesis mutation, echo synthesis, next-signal recommendations, verdict,
  coverage evidence reporting (Components 5-6 from status.md + delta.md)
- Prohibitions (exactly 5):
  1. SHALL NOT modify coverage table, namespace counts, or coverage_ratio
     (Phase 3 Contract domain; Receiving Scope, Phase Boundary Summary, Phase 3->4)
  2. SHALL NOT add, remove, or reorder planned signals (Phase 2 Contract domain)
  3. SHALL NOT assign readiness verdicts (READY / NOT READY / CONDITIONALLY READY)
     (Phase 3 Contract; readiness_verdict is ANALYST output; read-only via Component 5)
  4. SHALL NOT invoke any sub-skill other than topic-story (Phase 4 execution scope)
  5. SHALL NOT declare Phase 4 complete without writing story.md (Transition
     Obligation, Phase Boundary Summary, Phase 3->4)

---

## Cross-Phase Obligation Index

| Obligation | Declared at | Assertion site |
|---|---|---|
| Phase 2 receives planned_signals from strategy.md | Phase Boundary Summary Phase 1->2 | Phase 2 active-role header |
| Phase 3 receives namespace_coverage from roadmap.md | Phase Boundary Summary Phase 2->3 | Phase 3 active-role header |
| Phase 4 receives readiness_verdict + coverage_ratio (read-only) | Phase Boundary Summary Phase 3->4 (Receiving Scope) | Phase 4 active-role header |
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
| Narrator entry receipt: received status.md + delta.md inputs from Phase 3 | Entry Receipt Rule | Phase 4 entry header |

---

## Typed Output Contracts

### Phase 1 Contract -- strategy.md
- topic_name: string (non-empty)
- namespace: string, exactly one of:
  scout | draft | review | flow | trace | prove | listen | program | topic
- priority: string, exactly one of: High | Medium | Low
- planned_signals: list of >= 3 items; each: signal_name, target_skill, rationale

### Phase 2 Contract -- roadmap.md
- namespace_coverage: list; each entry: namespace + signals list (signal_name +
  collection_purpose per signal)

### Phase 3 Contract -- status.md
9-row coverage table: namespace, planned:int, collected:int, missing:list, zero_flag
Summary: coverage_ratio "X/N"; readiness_verdict 3-token set

### Phase 4 Contract -- story.md (six-component)
Component 1: verdict_verb (5-token)
Component 2: hypothesis_mutation (s0 + current)
Component 3: echoes (list; ["NONE"] if none)
Component 4: next_signal_recommendations (exactly 3: namespace + skill + gap_reason)
Component 5: coverage_context (coverage_ratio + readiness_verdict, verbatim from status.md)
Component 6: session_context (session_number + signals_added_count from delta.md)

### Session Delta Contract -- delta.md
session_number:int, signals_added:list, signals_removed:list,
verdict_before (4-token), verdict_after (4-token), verdict_changed (3-token)

---

## Two-Pass Delta Rule

Pass 1 (Phase 3 Step B): verdict_after = "NOT YET REACHED".
Pass 2 (Post-Phase-4): verdict_after = verdict_verb from story.md.

---

## Cascade Rule

Phase 3 Step B re-run after Phase 4: only verdict_after updates. All other fields
finalized at Phase 3 Step B; SHALL NOT cascade.

---

## Phase Boundary Summary

### Phase 1 -> Phase 2 Boundary
strategy.md planned_signals -> Phase 2 namespace_coverage input

### Phase 2 -> Phase 3 Boundary
roadmap.md namespace_coverage -> Phase 3 planned counts + missing names

### Phase 3 -> Phase 4 Boundary

#### Cascade Scope (re-run concern)
Update target: verdict_after only. Excluded: session_number, signals_added,
signals_removed, verdict_before, verdict_changed.

#### Receiving Scope (entry concern)
Phase 4 receives: readiness_verdict + coverage_ratio (read-only; Component 5)
Phase 4 receives: session_number + signals_added count (read-only; Component 6)
Phase 4 receives: delta.md with verdict_after = "NOT YET REACHED"
Phase 4 does NOT receive: namespace counts (Phase 3 Step A domain)

#### Transition Obligation (exit concern)
Phase 4 SHALL write story.md. Interrupted + completed campaigns indistinguishable
from delta.md alone.

### Post-Phase-4 -> Dashboard Boundary
delta.md verdict_after + verdict_changed updated. Dashboard: TERMINAL PASS.

---

## Prohibition Parity Rule

Each role carries exactly 5 prohibitions with inline citations (declared in PERSONA
REGISTRY). Phase sections cite registry; prohibitions not restated in phase bodies.

---

## Phase 1 -- Register

*REGISTRAR active (see PERSONA REGISTRY: domain + 5 prohibitions).
Phase 1 Contract governs output. Phase 1 carries no entry receipt (no prior phase).*

Invoke topic-new for {{topic}}. Produce strategy.md per Phase 1 Contract.

Phase 1 postcondition: strategy.md present, all fields typed correctly.

Registrar closes at strategy.md write. Registrar does not carry work into Phase 2.

GATE: Campaign SHALL NOT proceed to Phase 2 until Phase 1 postcondition satisfied.

Write to: simulations/topic/{{topic}}-strategy-{{date}}.md

---

## Phase 2 -- Plan

RECEIPT: PLANNER received planned_signals from strategy.md per Phase Boundary
Summary, Phase 1->2.

*PLANNER active (see PERSONA REGISTRY: domain + 5 prohibitions).
Phase 2 Contract governs output. Boundary: roadmap.md -> Phase 3.*

Invoke topic-plan for {{topic}}. Produce roadmap.md per Phase 2 Contract.

Phase 2 postcondition: roadmap.md present, at least one namespace entry.

Planner closes at roadmap.md write. Planner does not carry work into Phase 3.

GATE: Campaign SHALL NOT proceed to Phase 3 until Phase 2 postcondition satisfied.

Write to: simulations/topic/{{topic}}-roadmap-{{date}}.md

---

## Phase 3 -- Status

RECEIPT: ANALYST received namespace_coverage from roadmap.md per Phase Boundary
Summary, Phase 2->3.

*ANALYST active (see PERSONA REGISTRY: domain + 5 prohibitions).
Phase 3 Contract governs status.md. Session Delta Contract governs delta.md.
Phase Boundary Summary (Cascade Scope + Receiving Scope + Transition Obligation)
governs Phase 3->4.*

### Step A -- Coverage Status

Invoke topic-status for {{topic}}. Produce status.md per Phase 3 Contract.
FINALIZATION: status.md fields finalized at this write. Phase 4 reads coverage_ratio
+ readiness_verdict as read-only (Component 5).

Write to: simulations/topic/{{topic}}-status-{{date}}.md

### Step B -- Session Delta (Pass 1)

Produce delta.md per Session Delta Contract. verdict_after = "NOT YET REACHED".

Write to: simulations/topic/{{topic}}-delta-{{date}}.md

Analyst closes at delta.md write. Analyst does not carry work into Phase 4.

Phase 3 postcondition: status.md AND delta.md present, typed correctly.

GATE: Campaign SHALL NOT proceed to Phase 4 until Phase 3 postcondition satisfied.

---

## Phase 4 -- Narrative

RECEIPT: NARRATOR received readiness_verdict + coverage_ratio (read-only; Component 5)
and delta.md session_number + signals_added_count (read-only; Component 6) per Phase
Boundary Summary, Phase 3->4 (Receiving Scope).

**Obligation**: NARRATOR SHALL write story.md before declaring Phase 4 complete.
Transition Obligation (Phase Boundary Summary, Phase 3->4) violated otherwise.
Interrupted and completed campaigns are indistinguishable from delta.md alone.

*NARRATOR active (see PERSONA REGISTRY: domain + 5 prohibitions). Receiving Scope
(Phase Boundary Summary, Phase 3->4): Phase 4 does NOT receive namespace counts.
Phase 4 receives readiness_verdict + coverage_ratio (Component 5) and session_number +
signals_added_count (Component 6).*

Invoke topic-story for {{topic}}. Produce story.md per Phase 4 Contract (six components):
- Component 1: verdict_verb (exactly one of 5 tokens)
- Component 2: hypothesis_mutation (s0 + current)
- Component 3: echoes (list; ["NONE"] if none)
- Component 4: next_signal_recommendations (exactly 3 items)
- Component 5: coverage_context (verbatim from status.md; SHALL NOT recompute)
- Component 6: session_context (from delta.md)

Write to: simulations/topic/{{topic}}-story-{{date}}.md

---

## Post-Phase-4 Delta Update (Pass 2)

Update delta.md: verdict_after = verdict_verb; verdict_changed per comparison.
Only these two fields update. See Cascade Rule.

Update: simulations/topic/{{topic}}-delta-{{date}}.md

---

## Empty-State Handling

### First Invocation (0 signals collected)

All phases run. Entry Receipt Rule applies at Phase 2, 3, 4 entries.
Closure Parity Rule applies at Phase 1, 2, 3 exits.
Phase 3: collected = 0; readiness_verdict = NOT READY; session_number = 1.
Phase 4: verdict_verb = NOT YET REACHED; Component 5 + 6 from status.md + delta.md.

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
[ ] planned: integer all 9 rows -- FAIL: re-run Phase 3
[ ] collected: integer all 9 rows -- FAIL: re-run Phase 3
[ ] missing: list of names each row -- FAIL: re-run Phase 3
[ ] zero_flag: "NO SIGNALS" where planned = 0 AND collected = 0 -- FAIL: re-run Phase 3
[ ] coverage_ratio: "X/N" format -- FAIL: re-run Phase 3
[ ] readiness_verdict: one of 3-token set -- FAIL: re-run Phase 3

### Phase 4 -- story.md
[ ] story.md written before Phase 4 declared complete (Transition Obligation) -- FAIL: re-run Phase 4
[ ] verdict_verb: one of 5 tokens -- FAIL: re-run Phase 4
[ ] hypothesis_mutation.s0: non-empty -- FAIL: re-run Phase 4
[ ] hypothesis_mutation.current: present -- FAIL: re-run Phase 4
[ ] echoes: list present, minimum ["NONE"] -- FAIL: re-run Phase 4
[ ] next_signal_recommendations: exactly 3 items -- FAIL: re-run Phase 4
[ ] next_signal_recommendations[*].namespace: present -- FAIL: re-run Phase 4
[ ] next_signal_recommendations[*].gap_reason: present -- FAIL: re-run Phase 4
[ ] coverage_context.coverage_ratio: matches status.md -- FAIL: re-run Phase 4
[ ] session_context.session_number: matches delta.md -- FAIL: re-run Phase 4

### Session Delta -- delta.md
[ ] session_number: integer >= 1 -- FAIL: re-run Phase 3 Step B
[ ] signals_added: list present -- FAIL: re-run Phase 3 Step B
[ ] signals_removed: list present -- FAIL: re-run Phase 3 Step B
[ ] verdict_before: one of 4-token set -- FAIL: re-run Phase 3 Step B
[ ] verdict_after: reflects Phase 4 verdict_verb; no placeholder after Phase 4
    completes -- FAIL: re-run Phase 3 Step B
[ ] verdict_changed: one of {YES|NO|N/A} -- FAIL: re-run Phase 3 Step B

All 30 items PASS: campaign complete. Dashboard SHALL be emitted.

---

## Output: Topic Dashboard

When all 30 TERMINAL items show PASS, emit in order:
1. Topic registration summary (Phase 1)
2. Signal roadmap summary (Phase 2)
3. Coverage table with readiness verdict (Phase 3)
4. Narrative verdict + hypothesis + echoes + top-3 + coverage_context +
   session_context (Phase 4, six components)
5. Session delta summary
```

**Rubric targeting**: C-01 through C-45 (full 167/167 baseline). **Entry Receipt Rule
(C-49 candidate)** (Entry Receipt Rule declared as governing section parallel to Closure
Parity Rule; three receipt statements at Phase 2, 3, 4 entries; each cites incoming
artifact and Phase Boundary Summary section; Cross-Phase Obligation Index gains three
entry receipt rows; Phase 1 explicitly noted as carrying no entry receipt; creates
O(6)-scan boundary audit coverage: 3 exits via Closure Parity + 3 entries via Entry
Receipt Rule). **C-43 through C-45** (PERSONA REGISTRY, six-component Phase 4, Closure
Parity at three exits). **C-46** (inline Prohibition Anchoring at R16 V-05 baseline).

---

## V-04 -- Axis: Typed anchoring + Entry Receipt Rule (C-46 maximum + C-49 candidate)

**Hypothesis**: V-01 typed prohibition anchoring and V-03 entry receipts address
orthogonal dimensions -- prohibition format precision vs. boundary acknowledgment
symmetry. V-04 tests whether these two axes reinforce each other: typed anchoring makes
each prohibition's governed_by section explicit, and entry receipts make each phase's
incoming artifact explicit. Together they create a prompt where both the constraint
justification (what rule governs each prohibition) and the data flow acknowledgment
(what artifact each phase received) are surfaced in machine-parseable locations. A
reader can audit constraints by category (violation_class scan) and audit data flow
by position (six receipt/closure locations). Registry field alignment: V-02 baseline
(NARRATOR domain scopes Components 5-6; other roles not extended to field level).

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

---

## Entry Receipt Rule

Each phase SHALL carry exactly one receipt statement at its entry, before the
active-role description. Format:
"RECEIPT: [ROLE] received [artifact] from Phase [N] per Phase Boundary Summary,
Phase [N]->[N+1]."

Three instances required -- Phase 2, 3, and 4 entries. Phase 1 carries no receipt.
Together with Closure Parity Rule, every inter-phase handoff is auditable from
six fixed locations (three exits + three entries).

---

## Prohibition Type Vocabulary

violation_class tokens: scope-boundary | role-isolation | sub-skill-exclusion |
data-integrity | format-contract

---

## PERSONA REGISTRY

All four personas declared here. Prohibitions use typed three-field format.
Phase headers cite this registry; they do not restate prohibitions.

### REGISTRAR
- Phase: 1 (Register)
- Owned artifact: strategy.md
- Domain: Topic identity, namespace assignment, signal planning
- Prohibitions (exactly 5, typed):
  1. action: SHALL NOT produce coverage tables, coverage ratios, or readiness verdicts
     governed_by: Phase 3 Contract (ANALYST owns status.md; coverage is Phase 3 domain)
     violation_class: scope-boundary
  2. action: SHALL NOT synthesize or interpret signal content
     governed_by: Phase 4 Contract (synthesis is NARRATOR domain; story.md is Phase 4)
     violation_class: role-isolation
  3. action: SHALL NOT assign verdict verbs from Phase 4 controlled vocabulary
     governed_by: Phase 4 Contract (verdict_verb 5-token set is NARRATOR output)
     violation_class: role-isolation
  4. action: SHALL NOT invoke any sub-skill other than topic-new
     governed_by: Phase 1 execution scope (sub-skill exclusivity per phase)
     violation_class: sub-skill-exclusion
  5. action: SHALL NOT list signals not declared in planned_signals
     governed_by: Phase 1 Contract (planned_signals is the founding artifact)
     violation_class: data-integrity

### PLANNER
- Phase: 2 (Plan)
- Owned artifact: roadmap.md
- Domain: Signal ordering, collection purpose, namespace routing
- Prohibitions (exactly 5, typed):
  1. action: SHALL NOT register, rename, or modify topic identity
     governed_by: Phase 1 Contract (topic_name, namespace, priority finalized at strategy.md)
     violation_class: scope-boundary
  2. action: SHALL NOT query or report which signals are collected
     governed_by: Phase 3 Contract (collected count is ANALYST domain; status.md)
     violation_class: scope-boundary
  3. action: SHALL NOT produce readiness verdicts or coverage ratios
     governed_by: Phase 3 Contract (readiness_verdict + coverage_ratio are ANALYST outputs)
     violation_class: scope-boundary
  4. action: SHALL NOT synthesize findings or assign verdict verbs
     governed_by: Phase 4 Contract (verdict_verb is NARRATOR domain)
     violation_class: role-isolation
  5. action: SHALL NOT invoke any sub-skill other than topic-plan
     governed_by: Phase 2 execution scope (sub-skill exclusivity per phase)
     violation_class: sub-skill-exclusion

### ANALYST
- Phase: 3 (Status)
- Owned artifacts: status.md, delta.md
- Domain: Signal counting, coverage computation, session diff, readiness verdict
- Prohibitions (exactly 5, typed):
  1. action: SHALL NOT add planned signals beyond Phase 2 roadmap
     governed_by: Phase 2 Contract (namespace_coverage finalized at roadmap.md write)
     violation_class: data-integrity
  2. action: SHALL NOT produce verdict verbs from Phase 4 controlled vocabulary
     governed_by: Phase 4 Contract (verdict_verb distinct from readiness_verdict)
     violation_class: role-isolation
  3. action: SHALL NOT interpret meaning from signal content or editorialize
     governed_by: Phase 4 Contract (interpretation is NARRATOR domain)
     violation_class: role-isolation
  4. action: SHALL NOT invoke any sub-skill other than topic-status
     governed_by: Phase 3 execution scope (sub-skill exclusivity per phase)
     violation_class: sub-skill-exclusion
  5. action: SHALL NOT use narrative counts where integers are required
     governed_by: Phase 3 Contract (planned and collected are integer >= 0)
     violation_class: format-contract

### NARRATOR
- Phase: 4 (Narrative)
- Owned artifact: story.md
- Domain: Hypothesis mutation, echo synthesis, next-signal recommendations, verdict,
  coverage evidence reporting (Components 5-6 from status.md + delta.md)
- Prohibitions (exactly 5, typed):
  1. action: SHALL NOT modify coverage table, namespace counts, or coverage_ratio
     governed_by: Phase 3 Contract (ANALYST owns coverage; Receiving Scope Phase 3->4)
     violation_class: data-integrity
  2. action: SHALL NOT add, remove, or reorder planned signals
     governed_by: Phase 2 Contract (namespace_coverage finalized at roadmap.md)
     violation_class: data-integrity
  3. action: SHALL NOT assign readiness verdicts (READY / NOT READY / CONDITIONALLY READY)
     governed_by: Phase 3 Contract (readiness_verdict is ANALYST output; Component 5
       is read-only; SHALL NOT reassign)
     violation_class: scope-boundary
  4. action: SHALL NOT invoke any sub-skill other than topic-story
     governed_by: Phase 4 execution scope (sub-skill exclusivity per phase)
     violation_class: sub-skill-exclusion
  5. action: SHALL NOT declare Phase 4 complete without writing story.md
     governed_by: Transition Obligation (Phase Boundary Summary, Phase 3->4)
     violation_class: data-integrity

---

## Cross-Phase Obligation Index

| Obligation | Declared at | Assertion site |
|---|---|---|
| Phase 2 receives planned_signals from strategy.md | Phase Boundary Summary Phase 1->2 | Phase 2 active-role header |
| Phase 3 receives namespace_coverage from roadmap.md | Phase Boundary Summary Phase 2->3 | Phase 3 active-role header |
| Phase 4 receives readiness_verdict + coverage_ratio (read-only) | Phase Boundary Summary Phase 3->4 (Receiving Scope) | Phase 4 active-role header |
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
| Narrator entry receipt: received status.md + delta.md inputs from Phase 3 | Entry Receipt Rule | Phase 4 entry header |

---

## Typed Output Contracts

### Phase 1 Contract -- strategy.md
topic_name:string, namespace (9-token), priority (3-token),
planned_signals (list >= 3: {signal_name, target_skill, rationale})

### Phase 2 Contract -- roadmap.md
namespace_coverage: list of {namespace, signals [{signal_name, collection_purpose}]}

### Phase 3 Contract -- status.md
9-row table: namespace, planned:int, collected:int, missing:list, zero_flag
Summary: coverage_ratio "X/N"; readiness_verdict 3-token

### Phase 4 Contract -- story.md (six-component)
Component 1: verdict_verb (5-token)
Component 2: hypothesis_mutation (s0 + current)
Component 3: echoes (["NONE"] if none)
Component 4: next_signal_recommendations (exactly 3: namespace + skill + gap_reason)
Component 5: coverage_context (coverage_ratio + readiness_verdict verbatim from status.md)
Component 6: session_context (session_number + signals_added_count from delta.md)

### Session Delta Contract -- delta.md
session_number:int, signals_added:list, signals_removed:list,
verdict_before (4-token), verdict_after (4-token), verdict_changed (3-token)

---

## Two-Pass Delta Rule

Pass 1 (Phase 3 Step B): verdict_after = "NOT YET REACHED".
Pass 2 (Post-Phase-4): verdict_after = verdict_verb from story.md.

---

## Cascade Rule

Phase 3 Step B re-run after Phase 4: only verdict_after updates.

---

## Phase Boundary Summary

### Phase 1 -> Phase 2 Boundary
strategy.md planned_signals -> Phase 2 namespace_coverage

### Phase 2 -> Phase 3 Boundary
roadmap.md namespace_coverage -> Phase 3 planned counts + missing names

### Phase 3 -> Phase 4 Boundary

#### Cascade Scope (re-run concern)
Update target: verdict_after only. Excluded: session_number, signals_added,
signals_removed, verdict_before, verdict_changed.

#### Receiving Scope (entry concern)
Phase 4 receives: readiness_verdict + coverage_ratio (read-only; Component 5)
Phase 4 receives: session_number + signals_added count (read-only; Component 6)
Phase 4 receives: delta.md with verdict_after = "NOT YET REACHED"
Phase 4 does NOT receive: namespace counts (Phase 3 Step A domain)

#### Transition Obligation (exit concern)
Phase 4 SHALL write story.md.

### Post-Phase-4 -> Dashboard Boundary
delta.md verdict_after + verdict_changed updated. Dashboard: TERMINAL PASS.

---

## Prohibition Parity Rule

Each role carries exactly 5 typed prohibitions (action + governed_by + violation_class).
Declared in PERSONA REGISTRY. Phase sections cite registry.

---

## Phase 1 -- Register

*REGISTRAR active (see PERSONA REGISTRY: domain + 5 typed prohibitions).
Phase 1 Contract governs output. Phase 1 carries no entry receipt (no prior phase).*

Invoke topic-new for {{topic}}. Produce strategy.md per Phase 1 Contract.

Phase 1 postcondition: strategy.md present, all fields typed correctly.

Registrar closes at strategy.md write. Registrar does not carry work into Phase 2.

GATE: Campaign SHALL NOT proceed to Phase 2 until Phase 1 postcondition satisfied.

Write to: simulations/topic/{{topic}}-strategy-{{date}}.md

---

## Phase 2 -- Plan

RECEIPT: PLANNER received planned_signals from strategy.md per Phase Boundary
Summary, Phase 1->2.

*PLANNER active (see PERSONA REGISTRY: domain + 5 typed prohibitions).
Phase 2 Contract governs output.*

Invoke topic-plan for {{topic}}. Produce roadmap.md per Phase 2 Contract.

Phase 2 postcondition: roadmap.md present, at least one namespace entry.

Planner closes at roadmap.md write. Planner does not carry work into Phase 3.

GATE: Campaign SHALL NOT proceed to Phase 3 until Phase 2 postcondition satisfied.

Write to: simulations/topic/{{topic}}-roadmap-{{date}}.md

---

## Phase 3 -- Status

RECEIPT: ANALYST received namespace_coverage from roadmap.md per Phase Boundary
Summary, Phase 2->3.

*ANALYST active (see PERSONA REGISTRY: domain + 5 typed prohibitions).
Phase Boundary Summary (Cascade Scope + Receiving Scope + Transition Obligation)
governs Phase 3->4.*

### Step A -- Coverage Status

Invoke topic-status for {{topic}}. Produce status.md per Phase 3 Contract (9 rows,
integer fields, zero_flag, coverage_ratio, readiness_verdict).

FINALIZATION: status.md fields finalized here. Phase 4 reads coverage_ratio +
readiness_verdict as read-only (Component 5). Per Receiving Scope (Phase Boundary
Summary, Phase 3->4), Phase 4 does not receive namespace counts.

Write to: simulations/topic/{{topic}}-status-{{date}}.md

### Step B -- Session Delta (Pass 1)

Produce delta.md per Session Delta Contract. verdict_after = "NOT YET REACHED".

Write to: simulations/topic/{{topic}}-delta-{{date}}.md

Analyst closes at delta.md write. Analyst does not carry work into Phase 4.

Phase 3 postcondition: status.md AND delta.md present, typed correctly.

GATE: Campaign SHALL NOT proceed to Phase 4 until Phase 3 postcondition satisfied.

---

## Phase 4 -- Narrative

RECEIPT: NARRATOR received readiness_verdict + coverage_ratio (read-only; Component 5)
and delta.md session_number + signals_added_count (read-only; Component 6) per Phase
Boundary Summary, Phase 3->4 (Receiving Scope).

**Obligation**: NARRATOR SHALL write story.md before declaring Phase 4 complete.
Transition Obligation (Phase Boundary Summary, Phase 3->4) violated otherwise.

*NARRATOR active (see PERSONA REGISTRY: domain + 5 typed prohibitions). Receiving
Scope (Phase Boundary Summary, Phase 3->4): Phase 4 does NOT receive namespace counts.*

Invoke topic-story for {{topic}}. Produce story.md per Phase 4 Contract (six components):
- Component 1: verdict_verb (5 tokens)
- Component 2: hypothesis_mutation (s0 + current)
- Component 3: echoes (["NONE"] if none)
- Component 4: next_signal_recommendations (exactly 3)
- Component 5: coverage_context (verbatim from status.md)
- Component 6: session_context (from delta.md)

Write to: simulations/topic/{{topic}}-story-{{date}}.md

---

## Post-Phase-4 Delta Update (Pass 2)

Update delta.md: verdict_after = verdict_verb; verdict_changed per comparison.

Update: simulations/topic/{{topic}}-delta-{{date}}.md

---

## Empty-State Handling

### First Invocation (0 signals collected)

All phases run. Entry Receipt Rule applies at Phase 2, 3, 4 entries.
Closure Parity Rule applies at Phase 1, 2, 3 exits.
Phase 3: collected = 0; session_number = 1; signals_added = []; verdict_before = NONE.
Phase 4: verdict_verb = NOT YET REACHED; Component 5+6 from status.md + delta.md.

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
[ ] planned: integer all 9 rows -- FAIL: re-run Phase 3
[ ] collected: integer all 9 rows -- FAIL: re-run Phase 3
[ ] missing: list of names each row -- FAIL: re-run Phase 3
[ ] zero_flag: "NO SIGNALS" where planned = 0 AND collected = 0 -- FAIL: re-run Phase 3
[ ] coverage_ratio: "X/N" format -- FAIL: re-run Phase 3
[ ] readiness_verdict: one of 3-token set -- FAIL: re-run Phase 3

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
[ ] session_context.session_number: matches delta.md -- FAIL: re-run Phase 4

### Session Delta -- delta.md
[ ] session_number: integer >= 1 -- FAIL: re-run Phase 3 Step B
[ ] signals_added: list present -- FAIL: re-run Phase 3 Step B
[ ] signals_removed: list present -- FAIL: re-run Phase 3 Step B
[ ] verdict_before: one of 4-token set -- FAIL: re-run Phase 3 Step B
[ ] verdict_after: reflects Phase 4 verdict_verb; no placeholder after Phase 4
    completes -- FAIL: re-run Phase 3 Step B
[ ] verdict_changed: one of {YES|NO|N/A} -- FAIL: re-run Phase 3 Step B

All 30 items PASS: campaign complete. Dashboard SHALL be emitted.

---

## Output: Topic Dashboard

When all 30 TERMINAL items show PASS, emit in order:
1. Topic registration summary (Phase 1)
2. Signal roadmap summary (Phase 2)
3. Coverage table with readiness verdict (Phase 3)
4. Narrative verdict + hypothesis + echoes + top-3 + coverage_context +
   session_context (Phase 4, six components)
5. Session delta summary
```

**Rubric targeting**: C-01 through C-45 (full 167/167 baseline). **C-46 maximum**
(typed prohibition anchoring: action + governed_by + violation_class per prohibition;
Prohibition Type Vocabulary declared as governing section; 20 typed entries). **C-49
candidate** (Entry Receipt Rule declared as governing section; three receipt statements
at Phase 2, 3, 4 entries; Cross-Phase Obligation Index +3 rows; bidirectional boundary
audit at 6 locations). **C-48** (NARRATOR domain scopes Components 5-6 at R16 V-05
baseline; other roles not extended to field level).

---

## V-05 -- Full stack: typed anchoring + field alignment + entry receipts

**Hypothesis**: V-01 (typed prohibition anchoring) makes constraint justification
machine-parseable by category. V-02 (full registry-component field alignment) makes
contract ownership derivable from the registry alone. V-03 (entry receipts) closes
the bidirectional boundary loop. V-05 tests whether all three axes stack without
interference: typed prohibitions do not conflict with field-aligned domain descriptions
(both live in PERSONA REGISTRY but in different fields); entry receipts do not conflict
with closure statements (entry receipts at phase openings, closures at phase exits).
If all three reinforce without redundancy, V-05 should surface as a new density
ceiling -- a prompt where role identity (PERSONA REGISTRY), constraint justification
(typed prohibitions), contract ownership (field-aligned domains), and boundary
acknowledgment (6-location exit+entry audit) are all surfaced in dedicated auditable
locations.

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

---

## Entry Receipt Rule

Each phase SHALL carry exactly one receipt statement at its entry, before the
active-role description. Format:
"RECEIPT: [ROLE] received [artifact] from Phase [N] per Phase Boundary Summary,
Phase [N]->[N+1]."

Three instances required -- Phase 2, 3, and 4 entries. Phase 1 carries no receipt.
Closure Parity Rule + Entry Receipt Rule = every inter-phase handoff auditable from
six fixed locations (three exits + three entries).

---

## Prohibition Type Vocabulary

violation_class tokens (one per prohibition):
scope-boundary | role-isolation | sub-skill-exclusion | data-integrity | format-contract

---

## PERSONA REGISTRY

All four campaign personas declared here. Each Domain entry names the specific
contract fields owned by the role. Prohibitions use typed three-field format.
Phase headers cite this registry; they do not restate it.

### REGISTRAR
- Phase: 1 (Register)
- Owned artifact: strategy.md
- Domain: Topic identity, namespace assignment, signal planning
  [owns Phase 1 Contract fields: topic_name (string, non-empty), namespace
  (9-token: scout|draft|review|flow|trace|prove|listen|program|topic), priority
  (3-token: High|Medium|Low), planned_signals (list >= 3: {signal_name, target_skill,
  rationale})]
- Prohibitions (exactly 5, typed):
  1. action: SHALL NOT produce coverage tables, coverage ratios, or readiness verdicts
     governed_by: Phase 3 Contract (ANALYST owns coverage computation; status.md is
       Phase 3 artifact)
     violation_class: scope-boundary
  2. action: SHALL NOT synthesize or interpret signal content
     governed_by: Phase 4 Contract (synthesis is NARRATOR domain; story.md is Phase 4)
     violation_class: role-isolation
  3. action: SHALL NOT assign verdict verbs from Phase 4 controlled vocabulary
     governed_by: Phase 4 Contract (verdict_verb 5-token set is NARRATOR output)
     violation_class: role-isolation
  4. action: SHALL NOT invoke any sub-skill other than topic-new
     governed_by: Phase 1 execution scope (sub-skill exclusivity per phase)
     violation_class: sub-skill-exclusion
  5. action: SHALL NOT list signals not declared in planned_signals
     governed_by: Phase 1 Contract (planned_signals is the founding declaration;
       REGISTRAR does not amend post-registration)
     violation_class: data-integrity

### PLANNER
- Phase: 2 (Plan)
- Owned artifact: roadmap.md
- Domain: Signal ordering, collection purpose, namespace routing
  [owns Phase 2 Contract fields: namespace_coverage (list of entries, each with
  namespace (9-token) + signals list (each with signal_name matching strategy.md
  + collection_purpose (one sentence)))]
- Prohibitions (exactly 5, typed):
  1. action: SHALL NOT register, rename, or modify topic identity
     governed_by: Phase 1 Contract (topic_name, namespace, priority are REGISTRAR
       outputs; finalized at strategy.md write)
     violation_class: scope-boundary
  2. action: SHALL NOT query or report which signals are collected
     governed_by: Phase 3 Contract (collected count is ANALYST domain; status.md)
     violation_class: scope-boundary
  3. action: SHALL NOT produce readiness verdicts or coverage ratios
     governed_by: Phase 3 Contract (readiness_verdict + coverage_ratio are ANALYST
       outputs finalized at Phase 3 Step A)
     violation_class: scope-boundary
  4. action: SHALL NOT synthesize findings or assign verdict verbs
     governed_by: Phase 4 Contract (synthesis + verdict_verb are NARRATOR domain)
     violation_class: role-isolation
  5. action: SHALL NOT invoke any sub-skill other than topic-plan
     governed_by: Phase 2 execution scope (sub-skill exclusivity per phase)
     violation_class: sub-skill-exclusion

### ANALYST
- Phase: 3 (Status)
- Owned artifacts: status.md, delta.md
- Domain: Signal counting, coverage computation, session diff, readiness verdict
  [owns Phase 3 Contract fields: 9-row coverage table (namespace, planned:int >= 0,
  collected:int >= 0, missing:list-of-strings, zero_flag:"NO SIGNALS" where both
  zero), coverage_ratio (format "X/N"), readiness_verdict (3-token: READY|NOT READY|
  CONDITIONALLY READY); owns Session Delta Contract fields: session_number (int >= 1),
  signals_added (list), signals_removed (list), verdict_before (4-token), verdict_after
  (4-token; Pass 1 = "NOT YET REACHED"; Pass 2 = verdict_verb from story.md),
  verdict_changed (3-token: YES|NO|N/A)]
- Prohibitions (exactly 5, typed):
  1. action: SHALL NOT add planned signals beyond Phase 2 roadmap
     governed_by: Phase 2 Contract (namespace_coverage finalized at roadmap.md write;
       Phase 3 reads it as immutable input)
     violation_class: data-integrity
  2. action: SHALL NOT produce verdict verbs from Phase 4 controlled vocabulary
     governed_by: Phase 4 Contract (verdict_verb is a distinct 5-token set; distinct
       from readiness_verdict which ANALYST owns)
     violation_class: role-isolation
  3. action: SHALL NOT interpret meaning from signal content or editorialize
     governed_by: Phase 4 Contract (interpretation + synthesis are NARRATOR domain)
     violation_class: role-isolation
  4. action: SHALL NOT invoke any sub-skill other than topic-status
     governed_by: Phase 3 execution scope (sub-skill exclusivity per phase)
     violation_class: sub-skill-exclusion
  5. action: SHALL NOT use narrative counts where integers are required
     governed_by: Phase 3 Contract (planned:int >= 0 and collected:int >= 0 are
       typed constraints; narrative counts violate the format-contract)
     violation_class: format-contract

### NARRATOR
- Phase: 4 (Narrative)
- Owned artifact: story.md
- Domain: Hypothesis mutation, echo synthesis, next-signal recommendations, verdict,
  coverage evidence reporting (Components 5-6 from status.md + delta.md)
  [owns Phase 4 Contract fields: Component 1 verdict_verb (5-token: CONFIRMED|
  REFUTED|EVOLVING|INSUFFICIENT|NOT YET REACHED), Component 2 hypothesis_mutation
  ({s0:string, current:string-or-"UNCHANGED"}), Component 3 echoes (list, ["NONE"]
  if none), Component 4 next_signal_recommendations (exactly 3: {namespace, skill,
  gap_reason}), Component 5 coverage_context ({coverage_ratio:string copied verbatim
  from status.md, readiness_verdict:string copied verbatim from status.md}; read-only;
  SHALL NOT recompute or reassign), Component 6 session_context ({session_number:int
  from delta.md, signals_added_count:int >= 0 from delta.md}; read-only)]
- Prohibitions (exactly 5, typed):
  1. action: SHALL NOT modify coverage table, namespace counts, or coverage_ratio
     governed_by: Phase 3 Contract (ANALYST owns coverage; finalized Phase 3 Step A;
       Receiving Scope, Phase Boundary Summary, Phase 3->4)
     violation_class: data-integrity
  2. action: SHALL NOT add, remove, or reorder planned signals
     governed_by: Phase 2 Contract (namespace_coverage finalized at roadmap.md)
     violation_class: data-integrity
  3. action: SHALL NOT assign readiness verdicts (READY / NOT READY / CONDITIONALLY READY)
     governed_by: Phase 3 Contract (readiness_verdict is ANALYST output; Component 5
       is read-only; SHALL NOT reassign)
     violation_class: scope-boundary
  4. action: SHALL NOT invoke any sub-skill other than topic-story
     governed_by: Phase 4 execution scope (sub-skill exclusivity per phase)
     violation_class: sub-skill-exclusion
  5. action: SHALL NOT declare Phase 4 complete without writing story.md
     governed_by: Transition Obligation (Phase Boundary Summary, Phase 3->4);
       interrupted and completed campaigns indistinguishable from delta.md alone
     violation_class: data-integrity

---

## Cross-Phase Obligation Index

| Obligation | Declared at | Assertion site |
|---|---|---|
| Phase 2 receives planned_signals from strategy.md | Phase Boundary Summary Phase 1->2 | Phase 2 active-role header |
| Phase 3 receives namespace_coverage from roadmap.md | Phase Boundary Summary Phase 2->3 | Phase 3 active-role header |
| Phase 4 receives readiness_verdict + coverage_ratio (read-only) | Phase Boundary Summary Phase 3->4 (Receiving Scope) | Phase 4 active-role header |
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
| Narrator entry receipt: received status.md + delta.md inputs from Phase 3 | Entry Receipt Rule | Phase 4 entry header |

---

## Typed Output Contracts

### Phase 1 Contract -- strategy.md
topic_name:string, namespace (9-token), priority (3-token),
planned_signals (list >= 3: {signal_name, target_skill, rationale})

### Phase 2 Contract -- roadmap.md
namespace_coverage: list of {namespace, signals [{signal_name, collection_purpose}]}

### Phase 3 Contract -- status.md
9-row table: namespace, planned:int >= 0, collected:int >= 0, missing:list, zero_flag
Summary: coverage_ratio "X/N"; readiness_verdict (3-token: READY|NOT READY|
CONDITIONALLY READY)

### Phase 4 Contract -- story.md (six-component)
Component 1: verdict_verb (5-token: CONFIRMED|REFUTED|EVOLVING|INSUFFICIENT|NOT YET REACHED)
Component 2: hypothesis_mutation ({s0, current})
Component 3: echoes (list; ["NONE"] if none)
Component 4: next_signal_recommendations (exactly 3: {namespace, skill, gap_reason})
Component 5: coverage_context (coverage_ratio + readiness_verdict verbatim from status.md)
Component 6: session_context (session_number + signals_added_count from delta.md)

### Session Delta Contract -- delta.md
session_number:int >= 1, signals_added:list, signals_removed:list,
verdict_before (4-token), verdict_after (4-token), verdict_changed (3-token: YES|NO|N/A)

---

## Two-Pass Delta Rule

Pass 1 (Phase 3 Step B): verdict_after = "NOT YET REACHED".
Pass 2 (Post-Phase-4): verdict_after = verdict_verb from story.md.
Placeholder remaining after Phase 4 completes is a defect unless verdict_verb is also
"NOT YET REACHED".

---

## Cascade Rule

Phase 3 Step B re-run after Phase 4 completes: only verdict_after updates.
session_number, signals_added, signals_removed, verdict_before, verdict_changed
finalized at Phase 3 Step B; Phase 4 does not own them; SHALL NOT cascade.

---

## Phase Boundary Summary

### Phase 1 -> Phase 2 Boundary
strategy.md planned_signals -> Phase 2 namespace_coverage input

### Phase 2 -> Phase 3 Boundary
roadmap.md namespace_coverage -> Phase 3 planned counts + missing names

### Phase 3 -> Phase 4 Boundary

#### Cascade Scope (re-run concern)
Update target: verdict_after only. Excluded: session_number, signals_added,
signals_removed, verdict_before, verdict_changed (finalized Phase 3 Step B).

#### Receiving Scope (entry concern)
Phase 4 receives: readiness_verdict + coverage_ratio (read-only; Component 5)
Phase 4 receives: session_number + signals_added count (read-only; Component 6)
Phase 4 receives: delta.md with verdict_after = "NOT YET REACHED"
Phase 4 does NOT receive: namespace counts (Phase 3 Step A domain; finalized)

#### Transition Obligation (exit concern)
Phase 4 SHALL write story.md. Interrupted + completed campaigns indistinguishable
from delta.md alone without story.md.

### Post-Phase-4 -> Dashboard Boundary
delta.md verdict_after + verdict_changed updated. Dashboard: TERMINAL PASS.

---

## Prohibition Parity Rule

Each role carries exactly 5 typed prohibitions (action + governed_by + violation_class).
Declared in PERSONA REGISTRY. Phase sections cite registry. A role with 4 or 6 entries
SHALL fail audit.

---

## Phase 1 -- Register

*REGISTRAR active (see PERSONA REGISTRY: domain with Phase 1 Contract field ownership
+ 5 typed prohibitions). Phase 1 Contract governs output.
Phase 1 carries no entry receipt (no prior phase).*

Invoke topic-new for {{topic}}. Produce strategy.md per Phase 1 Contract.

Phase 1 postcondition: strategy.md present, all fields typed correctly.

Registrar closes at strategy.md write. Registrar does not carry work into Phase 2.

GATE: Campaign SHALL NOT proceed to Phase 2 until Phase 1 postcondition satisfied.

Write to: simulations/topic/{{topic}}-strategy-{{date}}.md

---

## Phase 2 -- Plan

RECEIPT: PLANNER received planned_signals from strategy.md per Phase Boundary
Summary, Phase 1->2.

*PLANNER active (see PERSONA REGISTRY: domain with Phase 2 Contract field ownership
+ 5 typed prohibitions). Phase 2 Contract governs output.*

Invoke topic-plan for {{topic}}. Produce roadmap.md per Phase 2 Contract.

Phase 2 postcondition: roadmap.md present, at least one namespace entry.

Planner closes at roadmap.md write. Planner does not carry work into Phase 3.

GATE: Campaign SHALL NOT proceed to Phase 3 until Phase 2 postcondition satisfied.

Write to: simulations/topic/{{topic}}-roadmap-{{date}}.md

---

## Phase 3 -- Status

RECEIPT: ANALYST received namespace_coverage from roadmap.md per Phase Boundary
Summary, Phase 2->3.

*ANALYST active (see PERSONA REGISTRY: domain with Phase 3 + Session Delta Contract
field ownership + 5 typed prohibitions). Phase Boundary Summary (Cascade Scope +
Receiving Scope + Transition Obligation) governs Phase 3->4.*

### Step A -- Coverage Status

Invoke topic-status for {{topic}}. Produce status.md per Phase 3 Contract (9 rows,
integer fields, zero_flag, coverage_ratio, readiness_verdict).

FINALIZATION: status.md fields finalized at this write (Phase 3 Step A). Per Receiving
Scope (Phase Boundary Summary, Phase 3->4), Phase 4 reads coverage_ratio +
readiness_verdict as read-only (Component 5); Phase 4 does not receive namespace counts.

Write to: simulations/topic/{{topic}}-status-{{date}}.md

### Step B -- Session Delta (Pass 1)

Produce delta.md per Session Delta Contract. verdict_after = "NOT YET REACHED"
(placeholder; Pass 2 updates after story.md is written).

Write to: simulations/topic/{{topic}}-delta-{{date}}.md

Analyst closes at delta.md write. Analyst does not carry work into Phase 4.

Phase 3 postcondition: status.md AND delta.md present, typed correctly.

GATE: Campaign SHALL NOT proceed to Phase 4 until Phase 3 postcondition satisfied.

---

## Phase 4 -- Narrative

RECEIPT: NARRATOR received readiness_verdict + coverage_ratio (read-only; Component 5)
and delta.md session_number + signals_added_count (read-only; Component 6) per Phase
Boundary Summary, Phase 3->4 (Receiving Scope).

**Obligation**: NARRATOR SHALL write story.md before declaring Phase 4 complete.
The Transition Obligation (Phase Boundary Summary, Phase 3->4) is violated otherwise.
Interrupted and completed campaigns are indistinguishable from delta.md alone.

*NARRATOR active (see PERSONA REGISTRY: domain with Phase 4 Contract field ownership
for all six components + 5 typed prohibitions). Receiving Scope (Phase Boundary
Summary, Phase 3->4): Phase 4 does NOT receive namespace counts (finalized Phase 3
Step A). Phase 4 receives readiness_verdict + coverage_ratio (read-only; Component 5)
and session_number + signals_added_count (read-only; Component 6).*

Invoke topic-story for {{topic}}. Produce story.md per Phase 4 Contract (six components):
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

All four phases run. Closure Parity Rule applies at Phase 1, 2, 3 exits.
Entry Receipt Rule applies at Phase 2, 3, 4 entries.

Phase 3 (ANALYST): all collected = 0; readiness_verdict = NOT READY;
  session_number = 1; signals_added = []; verdict_before = NONE;
  verdict_after = NOT YET REACHED; verdict_changed = N/A.

Phase 4 (NARRATOR): verdict_verb = NOT YET REACHED; hypothesis_mutation.current =
  "UNCHANGED"; echoes = ["NONE"]; Component 5 from status.md (coverage_ratio from
  0-signal run; readiness_verdict = NOT READY); Component 6: session_number = 1,
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

### Session Delta -- delta.md
[ ] session_number: integer >= 1 -- FAIL: re-run Phase 3 Step B
[ ] signals_added: list present ([] permitted) -- FAIL: re-run Phase 3 Step B
[ ] signals_removed: list present ([] permitted) -- FAIL: re-run Phase 3 Step B
[ ] verdict_before: one of {READY|NOT READY|CONDITIONALLY READY|NONE}
    FAIL: re-run Phase 3 Step B
[ ] verdict_after: reflects Phase 4 verdict_verb; placeholder NOT remaining after
    Phase 4 completes -- FAIL: re-run Phase 3 Step B after Phase 4 completes
[ ] verdict_changed: one of {YES|NO|N/A} -- FAIL: re-run Phase 3 Step B

All 30 items PASS: campaign complete. Dashboard SHALL be emitted.

---

## Output: Topic Dashboard

When all 30 TERMINAL items show PASS, emit in order:
1. Topic registration summary (Phase 1)
2. Signal roadmap summary (Phase 2)
3. Coverage table with readiness verdict (Phase 3)
4. Narrative verdict + hypothesis + echoes + top-3 + coverage_context +
   session_context (Phase 4, six components)
5. Session delta summary
```

**Rubric targeting**: C-01 through C-45 (full 167/167 baseline). **C-46 maximum**
(typed three-field prohibition format: action + governed_by + violation_class;
Prohibition Type Vocabulary section with 5-token violation_class; 20 typed entries;
category scan by violation_class; governed_by as named field). **C-48 maximum**
(full registry-component field alignment: all four roles list specific contract fields
in Domain entries; ANALYST lists Phase 3 + Session Delta Contract fields; NARRATOR
lists all six Phase 4 Contract components with read-only annotations). **C-49
candidate** (Entry Receipt Rule as governing section; three receipt statements at Phase
2, 3, 4 entries; Phase 1 explicitly excludes receipt; Cross-Phase Obligation Index
+3 rows; Closure Parity Rule + Entry Receipt Rule = six-location boundary audit;
bidirectional acknowledgment pattern is structurally symmetric and orthogonal to the
Closure Parity Rule axis).

---

## Predicted Leaderboard

V-05 > V-04 > V-02 > V-01 = V-03

**V-05** (full stack): All three new axes combined. Typed prohibition anchoring +
full field alignment + entry receipts. Highest structural density; generates strongest
C-46/C-48/C-49 candidate signals simultaneously. If all three axes are independent
excellence signals, V-05 is the only variation that surfaces all three.

**V-04** (typed anchoring + entry receipts): Two new axes. C-46 maximum + C-49
candidate. Strong combination; entry receipts reinforce typed anchoring by making
data flow explicit at the same phase entry locations where typed anchoring makes
constraint justification explicit.

**V-02** (full field alignment): Single-axis C-48 maximum. Registry becomes contract
substitute. NARRATOR domain alignment extends to all four roles. Strong structural
signal but single-axis.

**V-01 = V-03** (single-axis): V-01 targets C-46 only; V-03 targets C-49 only. Both
pass 167/167 on v15 rubric. Tie expected since v15 does not score new C-46/C-48/C-49
axes.
