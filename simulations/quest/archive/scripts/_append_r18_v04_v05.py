content = r"""
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
"""

with open("C:/src/sim/simulations/quest/golden/campaign-track-variate-R18-2026-03-17.md", "a", encoding="utf-8") as f:
    f.write(content)

print("Done")
