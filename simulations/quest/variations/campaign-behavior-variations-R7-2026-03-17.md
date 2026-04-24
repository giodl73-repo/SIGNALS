**campaign-behavior R7 — 5 variations written.**

---

## Axes explored in R7

| Variation | Axis | New criteria targeted | Expected score |
|-----------|------|-----------------------|----------------|
| **V-01** | State-anchor sequence (single) | C-22 + C-23 (sequence swap delivers both) | 15/15 → **90/90** |
| **V-02** | Permissions-anchor rationale reinforcement (single) | C-23 isolation test only | 14/15 → **89/90** |
| **V-03** | DEPTH asymmetry on state-anchor sequence (single) | C-22 + C-23 + depth labels | 15/15 → **90/90** |
| **V-04** | Dual-anchor + Q6 sequence integrity (combination) | C-22, C-23 + Q6 verification | 15/15 → **90/90** |
| **V-05** | Full 15-criterion coverage (combination) | All C-01–C-23, double reinforcement | 15/15 → **90/90** |

---

## Key structural decisions

**Optimal sequence for both C-22 and C-23:**
`trace-state (Ph1) → trace-permissions (Ph2) → trace-contract (Ph3) → flow-lifecycle (Ph4) → flow-trigger (Ph5)`

- C-22 requires trace-state *first* with state-topology-pre-classifies rationale
- C-23 requires trace-permissions *before flow sub-skills* — Phase 2 satisfies this even after the swap
- The two criteria are structurally linked: satisfying C-22 by moving trace-state to Phase 1 simultaneously preserves C-23 (permissions still precedes Phases 4–5)

**V-02 is the diagnostic variation** — it keeps R6 V-04's sequence unchanged (permissions at Phase 1) and only adds explicit "before flow sub-skills" language for C-23. If V-02 scores 90/90, it means C-23 was already satisfied in R6 V-04 and the rubric merely formalized an existing pattern. If it scores 89/90, C-23 requires the standalone declaration.

**V-04's Q6** is the new structural contribution: a self-referential calibration question that verifies the execution sequence delivered its pre-classification guarantee (zero post-hoc blast radius revisions). This becomes the canonical pattern for future rounds where sequencing order is a rubric criterion.
es simultaneously.
Medium: two or more components affected; no shared state surface reached.
Narrow: failure contained within one component boundary.

**Severity** = damage depth at the epicenter (high / med / low). Independent of blast radius.
Always report as a separate labeled field. Never merge into a combined "impact" score.

**CONFIRMED** = a Phase 4-5 runtime finding that matches a specific topology violation from
Phases 1-3. The match must be structural: same component, role, state surface, or contract term.

**RUNTIME ANOMALY** = a Phase 4-5 finding with no matching topology violation in Phases 1-3.
Unexpected behavior not predicted by the static topology.

**SYSTEMIC** = a finding corroborated in three or more phases. Must enumerate corroborating phase
names. Format: "SYSTEMIC: yes -- phases: [name], [name], [name]." Binary flag = invalid.

**State-anchor rationale:** Trace-state runs first (Phase 1) because shared-state topology
pre-classifies blast radius candidates for all downstream sub-skills. A state surface shared
across multiple components carries wide blast radius by definition. Identifying these surfaces
before access or contract analysis means every subsequent finding inherits a pre-built blast
radius map rather than constructing one post-hoc. Running any other sub-skill first risks
underestimating blast radius for findings that touch shared state.

**Permissions-anchor rationale:** Trace-permissions runs second (Phase 2), before flow-lifecycle
and flow-trigger, because the access surface ceiling must be established before flow behavior
is evaluated. A flow finding involving an escalated role inherits wide blast radius mechanically
from Phase 2. Running trace-permissions after the flow sub-skills would require retroactive blast
radius revision -- an unreliable post-hoc correction.

---

## PHASE 0 -- Topology census

**Components in scope:** [all named services, modules, APIs, schemas, queues from spec]

**Shared state surfaces:** [all databases, caches, event buses, config objects read/written by
multiple components -- the blast-radius amplifiers; every blast radius ceiling check uses this list]

**Downstream callers:** [all components that depend on outputs from this system]

**Role-resource inventory:** [all roles and the resources each may access -- Phase 2 input surface]

**Pre-declared contracts:** [all explicit producer/consumer contract terms in spec --
the CONFIRMED baseline for Phases 4-5]

Every blast radius claim must name a specific entry from this census. A finding that cannot name
a census item is not a finding -- return to the spec.

---

## PHASE 1 -- trace-state [ANCHOR: state topology pre-classifies blast radius for Phases 2-5]

Map shared state topology. Identify every shared state surface, its consumers, and its invariants.
This topology becomes the blast radius pre-classification map for all downstream sub-skills.

| From state | To state | Trigger | Invariant | Invariant holds? | Shared state surfaces affected | Blast radius pre-classification |
|------------|----------|---------|-----------|------------------|-------------------------------|--------------------------------|

Shared state surface = any state object from Phase 0 written by more than one component.
If a transition touches a shared state surface: blast radius pre-classification = wide.
This classification is structural and propagates to all findings involving this surface in Phases 2-5.

If clean: "trace-state: clean -- all invariants hold; blast radius map built from Phase 0 census."

EXIT CRITERIA: All shared state surfaces from Phase 0 evaluated.
State: "trace-state complete: [N] transitions, [N] violations, [N] wide-pre-classified surfaces."

---

## PHASE 2 -- trace-permissions [ANCHOR: access surface ceiling before flow sub-skills]

Establish the access surface. Evaluate every role-resource-action triplet from Phase 0 inventory.
Cross-reference Phase 1: any role that accesses a Phase 1 wide-pre-classified state surface
inherits wide blast radius ceiling mechanically.

| Role | Resource | Action | Permitted? | Escalation path? | Phase 1 shared state surface? | Blast radius ceiling |
|------|----------|--------|------------|------------------|------------------------------|---------------------|

Escalation path = yes when a role reaches a resource through indirect means (delegation,
inheritance, event chain, missing boundary check).
Escalation path = yes AND Phase 1 shared state surface = yes: blast radius ceiling = wide.
This ceiling holds for all downstream findings involving this role in Phases 3-5.

If no escalation paths: "trace-permissions: clean -- no escalation paths detected."

EXIT CRITERIA: All role-resource pairs from Phase 0 inventory evaluated. No pairs deferred.
State: "trace-permissions complete: [N] pairs evaluated, [N] escalation paths, [N] involving Phase 1 shared state."

---

## PHASE 3 -- trace-contract

Verify what crosses role and component boundaries.
Phase 1 match = this contract involves a Phase 1 state transition or invariant violation surface.
Phase 2 match = this contract involves a Phase 2 escalation role.
If either match = yes: classify CONFIRMED here, not waiting for calibration.

| Producer | Consumer | Contract term | Expected | Actual | Mismatch? | Phase 1 state match? | Phase 2 role match? | CONFIRMED? |
|----------|----------|---------------|----------|--------|-----------|---------------------|---------------------|------------|

If clean: "trace-contract: clean -- all contracts verified."

EXIT CRITERIA: All producer/consumer pairs evaluated.
State: "trace-contract complete: [N] pairs, [N] mismatches, [N] CONFIRMED."

---

## PHASE 4 -- flow-lifecycle

Observe runtime behavior within the state/permission/contract envelope from Phases 1-3.

| Phase | Entry contract | Exit contract | Exception path | Exception handled? | Phase 1-3 topology match? | CONFIRMED / RUNTIME ANOMALY |
|-------|----------------|---------------|----------------|--------------------|--------------------------|-----------------------------|

CONFIRMED = matches a specific Phase 1 state violation, Phase 2 escalation path, or Phase 3 mismatch.
Name the matching finding.
RUNTIME ANOMALY = no matching topology entry. Document the absence explicitly.

If clean: "flow-lifecycle: clean -- all lifecycle transitions verified."

EXIT CRITERIA: All lifecycle phases evaluated.
State: "flow-lifecycle complete: [N] phases, [N] failures, [N] CONFIRMED, [N] RUNTIME ANOMALY."

---

## PHASE 5 -- flow-trigger

Evaluate every trigger and every activating event in scope.

| Trigger | Expected fire order | Actual fire order | Race condition? | Phase 2 escalation role? | Phase 1 shared state affected? | CONFIRMED / RUNTIME ANOMALY |
|---------|---------------------|-------------------|-----------------|--------------------------|-------------------------------|------------------------------|

Phase 2 escalation role = yes if the trigger involves a role from Phase 2's escalation list.
If yes: blast radius = wide (inherits from Phase 2 access surface ceiling).

If clean: "flow-trigger: clean -- all triggers verified."

EXIT CRITERIA: All triggers and activating events evaluated. No triggers deferred.
State: "flow-trigger complete: [N] triggers, [N] failures, [N] CONFIRMED, [N] RUNTIME ANOMALY."

---

## CALIBRATION BLOCK

Q1: Does any finding's blast radius change when mapped against Phase 0 shared state surfaces?
For each finding with blast radius = medium or narrow: does the affected component read from or
write to a Phase 0 shared state surface? If yes, upgrade to wide. List every revision explicitly.

Q2: Do any Phase 4-5 findings match topology violations from Phases 1-3?
For each Phase 4-5 finding: identify the specific Phase 1 state surface, Phase 2 escalation path,
or Phase 3 contract mismatch it connects to. If match found: confirm CONFIRMED
(or reclassify if marked RUNTIME ANOMALY). If no match: confirm RUNTIME ANOMALY.
List all reclassifications.

Q3: Which findings appear in three or more phases?
List every finding corroborated across phases. Mark SYSTEMIC if three or more phases.
REQUIRED: enumerate the corroborating phase names for every SYSTEMIC finding.
Format: "SYSTEMIC: yes -- phases: [phase-name-1], [phase-name-2], [phase-name-3]"
A finding in exactly two phases is not SYSTEMIC. Binary flags without phase lists are not valid.

Q4: Does the blast radius pre-classification from Phase 1 hold throughout?
For every finding involving a Phase 1 wide-pre-classified state surface: verify blast radius = wide.
For every finding involving a Phase 2 escalation role: verify blast radius = wide.
Any deviation is a calibration error. Revise and explain each case.

Q5: Would any finding below have shipped without this simulation?
For each wide-blast-radius finding: name the assumption it would have bypassed
(undocumented privilege, implicit contract, tacit lifecycle expectation, missing spec coverage,
assumed state boundary). This is the inertia question -- what would the team have believed?

---

## CONSOLIDATE

Write ONE report. Do not concatenate five phase outputs. Synthesis, not a log.

**Ranked findings (calibrated blast radius descending, tiebreaker protocol applied):**

Tiebreaker protocol (apply in order):
1. Blast radius: wide > medium > narrow
2. CONFIRMED > RUNTIME ANOMALY
3. SYSTEMIC > isolated

For each finding, use this atomic block exactly:

---
**Finding [N]**
1. Name: [finding name or short description]
2. Source phase: [phase name that produced this finding]
3. Blast radius: [wide | medium | narrow] -- [named census components in propagation path]
4. Severity at epicenter: [high | med | low]
5. SYSTEMIC: [yes -- phases: [comma-separated corroborating phase names] | no]
6. Classification: [CONFIRMED | RUNTIME ANOMALY | isolated]
7. What must change: [one concrete fix direction in spec, contract, or implementation]
---

**Spec gaps:** [list each gap, or "none detected"]

**Contract violations:** [list each violation, or "none detected"]

**Privilege escalation paths:** [list each path, or "none detected"]

**Clean zones:** [Phase 0 census components with no findings across all five phases]

---

## VERDICT

One paragraph. Name the finding with the widest blast radius by its Phase 0 census component name.
State CONFIRMED or RUNTIME ANOMALY. If SYSTEMIC, enumerate the corroborating phases.
Name the assumption the team would have carried into implementation had this simulation not run.
Conclude: proceed, proceed with conditions, or halt.
```

---

## V-02 -- Permissions-anchor rationale reinforcement (single-axis)
**Axis:** Permissions-anchor rationale -- keep R6 V-04 sequence unchanged (trace-permissions = Phase 1, before flow sub-skills); add an explicit before-flow declaration as a labeled criterion section in DEFINITIONS and as a standalone statement in the CONSOLIDATE section. Tests whether C-23 was already satisfied by R6 V-04 structurally (in which case this single-axis change adds C-23 without affecting anything else) or whether the before-flow rationale must be independently declared.
**Hypothesis:** R6 V-04 scored 13/13 under v5, leaving C-22 and C-23 unscored. If R6 V-04's existing permissions-anchor rationale ("Trace-permissions runs first because...") already satisfies C-23, then this V-02 is only an incremental refinement. If C-23 requires a distinct "before flow sub-skills" declaration rather than just "runs first," this variation fills the gap. Expected: C-22 FAIL (no state-anchor), C-23 PASS, score 14/15 → 9 pts → 89/90.

```
Simulate the technical behavior of: {{topic}}

---

## DEFINITIONS

**Blast radius** = how broadly a failure propagates through the system.
Wide: corrupts shared state, breaks downstream callers, or blocks multiple user roles simultaneously.
Medium: two or more components affected; no shared state surface reached.
Narrow: failure contained within one component boundary.

**Severity** = damage depth at the epicenter (high / med / low). Independent of blast radius.
Always report as a separate labeled field. Never merge into a combined "impact" score.

**CONFIRMED** = a Phase 4-5 runtime finding that matches a specific topology violation from
Phases 1-3. The match must be structural: same component, role, state surface, or contract term.

**RUNTIME ANOMALY** = a Phase 4-5 finding with no matching topology violation in Phases 1-3.
Unexpected behavior not predicted by the static topology.

**SYSTEMIC** = a finding corroborated in three or more phases. Must enumerate corroborating phase
names. Format: "SYSTEMIC: yes -- phases: [name], [name], [name]." Binary flag = invalid.

**Permissions-anchor rationale (C-23 compliance):** Trace-permissions is positioned as Phase 1,
explicitly BEFORE flow-lifecycle (Phase 4) and flow-trigger (Phase 5). This ordering is not
arbitrary. Privilege boundary classification must precede flow analysis because a flow that
triggers across a permission boundary carries elevated blast radius -- SYSTEMIC by definition.
Without permissions-anchor ordering, flow sub-skills may classify blast radius without visibility
into the privilege scope, understating propagation. The access surface ceiling set in Phase 1
propagates to all flow findings in Phases 4-5 without re-analysis.

---

## PHASE 0 -- Topology census

**Components in scope:** [all named services, modules, APIs, schemas, queues from spec]

**Shared state surfaces:** [all databases, caches, event buses, config objects read/written by
multiple components -- the blast-radius amplifiers]

**Downstream callers:** [all components that depend on outputs from this system]

**Role-resource inventory:** [all roles and the resources each may access -- the Phase 1 input surface]

**Pre-declared contracts:** [all explicit producer/consumer contract terms in spec --
the CONFIRMED baseline for Phases 4-5]

Every blast radius claim must name a specific entry from this census. A finding that cannot name
a census item is not a finding -- return to the spec.

---

## PHASE 1 -- trace-permissions [RUNS BEFORE FLOW SUB-SKILLS -- see permissions-anchor rationale]

Establish the access surface ceiling. Evaluate every role-resource-action triplet from Phase 0.

| Role | Resource | Action | Permitted? | Escalation path? | Blast radius if escalated | Shared state surface? |
|------|----------|--------|------------|------------------|--------------------------|----------------------|

Escalation path = yes when a role reaches a resource through indirect means (delegation,
inheritance, event chain, missing boundary check).
Escalation path = yes AND shared state surface = yes: blast radius ceiling = wide for all
downstream findings involving this role.

If no escalation paths: "trace-permissions: clean -- no escalation paths detected."

EXIT CRITERIA: All role-resource pairs from Phase 0 inventory evaluated. No pairs deferred.
State: "trace-permissions complete: [N] pairs evaluated, [N] escalation paths, [N] involving shared state."

---

## PHASE 2 -- trace-state

Map state reachability through the access surface from Phase 1.

| From state | To state | Trigger | Invariant | Invariant holds? | Phase 1 escalation role involved? |
|------------|----------|---------|-----------|------------------|-----------------------------------|

If Phase 1 escalation role = yes and invariant = no: classify CONFIRMED immediately
(topology match: role escalation enables state violation).

If clean: "trace-state: clean -- all invariants hold."

EXIT CRITERIA: All shared state surfaces from Phase 0 evaluated.
State: "trace-state complete: [N] transitions, [N] violations, [N] CONFIRMED from Phase 1."

---

## PHASE 3 -- trace-contract

Verify what crosses role and component boundaries.

| Producer | Consumer | Contract term | Expected | Actual | Mismatch? | Phase 1/2 topology match? |
|----------|----------|---------------|----------|--------|-----------|--------------------------|

Phase 1/2 topology match = yes if this contract involves a Phase 1 escalation role or
Phase 2 state violation surface. If match = yes: classify CONFIRMED.

If clean: "trace-contract: clean -- all contracts verified."

EXIT CRITERIA: All producer/consumer pairs evaluated.
State: "trace-contract complete: [N] pairs, [N] mismatches, [N] CONFIRMED."

---

## PHASE 4 -- flow-lifecycle [RUNS AFTER trace-permissions -- blast radius ceiling inherited from Phase 1]

Observe runtime behavior within the permission/state/contract envelope.

| Phase | Entry contract | Exit contract | Exception path | Exception handled? | Phase 1-3 topology match? | CONFIRMED / RUNTIME ANOMALY |
|-------|----------------|---------------|----------------|--------------------|--------------------------|-----------------------------|

CONFIRMED = matches a specific Phase 1 escalation, Phase 2 state violation, or Phase 3 mismatch.
Name the matching finding.
RUNTIME ANOMALY = no matching topology entry. Document the absence explicitly.

If clean: "flow-lifecycle: clean -- all lifecycle transitions verified."

EXIT CRITERIA: All lifecycle phases evaluated.
State: "flow-lifecycle complete: [N] phases, [N] failures, [N] CONFIRMED, [N] RUNTIME ANOMALY."

---

## PHASE 5 -- flow-trigger [RUNS AFTER trace-permissions -- blast radius ceiling inherited from Phase 1]

Evaluate every trigger and every activating event in scope.

| Trigger | Expected fire order | Actual fire order | Race condition? | Phase 1 escalation role? | Phase 0 shared state affected? | CONFIRMED / RUNTIME ANOMALY |
|---------|---------------------|-------------------|-----------------|--------------------------|-------------------------------|------------------------------|

Phase 1 escalation role = yes if the trigger involves a role from Phase 1's escalation list.
If yes: blast radius = wide (inherited from Phase 1 access surface ceiling).

If clean: "flow-trigger: clean -- all triggers verified."

EXIT CRITERIA: All triggers and activating events evaluated. No triggers deferred.
State: "flow-trigger complete: [N] triggers, [N] failures, [N] CONFIRMED, [N] RUNTIME ANOMALY."

---

## CALIBRATION BLOCK

Q1: Does any finding's blast radius change when mapped against Phase 0 shared state surfaces?
For each finding with blast radius = medium or narrow: does the affected component read from or
write to a Phase 0 shared state surface? If yes, upgrade to wide. List every revision explicitly.

Q2: Do any Phase 4-5 findings match topology violations from Phases 1-3?
For each Phase 4-5 finding: identify the specific Phase 1 escalation path, Phase 2 state
violation, or Phase 3 contract mismatch it connects to. If match found: confirm CONFIRMED
(or reclassify if marked RUNTIME ANOMALY). If no match: confirm RUNTIME ANOMALY.
List all reclassifications.

Q3: Which findings appear in three or more phases?
List every finding corroborated across phases. Mark SYSTEMIC if three or more phases.
REQUIRED: enumerate the corroborating phase names for every SYSTEMIC finding.
Format: "SYSTEMIC: yes -- phases: [phase-name-1], [phase-name-2], [phase-name-3]"
A finding in exactly two phases is not SYSTEMIC. Binary flags without phase lists are not valid.

Q4: Does the blast radius ceiling from Phase 1 hold throughout Phases 4-5?
Phase 1 ran before the flow sub-skills specifically to prevent retroactive blast radius revision.
For every flow finding involving a Phase 1 escalation role: verify blast radius = wide.
Any deviation undermines the permissions-anchor ordering guarantee. Revise and explain each case.

Q5: Would any finding below have shipped without this simulation?
For each wide-blast-radius finding: name the assumption it would have bypassed
(undocumented privilege, implicit contract, tacit lifecycle expectation, missing spec coverage,
assumed access boundary). This is the inertia question -- what would the team have believed?

---

## CONSOLIDATE

Write ONE report. Do not concatenate five phase outputs. Synthesis, not a log.

**Permissions-anchor compliance declaration:** trace-permissions (Phase 1) executed before
flow-lifecycle (Phase 4) and flow-trigger (Phase 5). All flow blast radius claims inherit the
Phase 1 access surface ceiling. No retroactive revision applied.

**Ranked findings (calibrated blast radius descending, tiebreaker protocol applied):**

Tiebreaker protocol (apply in order):
1. Blast radius: wide > medium > narrow
2. CONFIRMED > RUNTIME ANOMALY
3. SYSTEMIC > isolated

For each finding, use this atomic block exactly:

---
**Finding [N]**
1. Name: [finding name or short description]
2. Source phase: [phase name that produced this finding]
3. Blast radius: [wide | medium | narrow] -- [named census components in propagation path]
4. Severity at epicenter: [high | med | low]
5. SYSTEMIC: [yes -- phases: [comma-separated corroborating phase names] | no]
6. Classification: [CONFIRMED | RUNTIME ANOMALY | isolated]
7. What must change: [one concrete fix direction in spec, contract, or implementation]
---

**Spec gaps:** [list each gap, or "none detected"]

**Contract violations:** [list each violation, or "none detected"]

**Privilege escalation paths:** [list each path, or "none detected"]

**Clean zones:** [Phase 0 census components with no findings across all five phases]

---

## VERDICT

One paragraph. Name the finding with the widest blast radius by its Phase 0 census component name.
State CONFIRMED or RUNTIME ANOMALY. If SYSTEMIC, enumerate the corroborating phases.
Name the assumption the team would have carried into implementation had this simulation not run.
Conclude: proceed, proceed with conditions, or halt.
```

---

## V-03 -- DEPTH asymmetry on state-anchor sequence (single-axis)
**Axis:** DEPTH labels applied to the V-01 resequencing -- each phase receives HIGH, MEDIUM, or AS-NEEDED depth classification; trace-state (Phase 1) and flow-trigger (Phase 5) get HIGH because state topology and trigger coverage are the primary blast radius amplifiers; trace-permissions (Phase 2) and flow-lifecycle (Phase 4) get MEDIUM; trace-contract (Phase 3) gets AS-NEEDED if contract terms are explicitly declared in spec
**Hypothesis:** V-01 introduces state-anchor sequencing but does not differentiate depth by phase. V-03 tests whether adding DEPTH labels to the resequenced structure strengthens C-22 and C-23 (by making the anchor rationale structurally prominent in phase headers) while preserving all 13 prior criteria from R6 V-04. DEPTH labels appeared in R6 V-05 (which scored 90/90 under v5); combining them with V-01's new sequence should satisfy all 15 aspirational criteria. Expected: 15/15 → 90/90.

```
Simulate the technical behavior of: {{topic}}

---

## CORE DEFINITIONS

**Blast radius** = propagation width across the system when a failure occurs.
Wide: corrupts shared state, breaks downstream callers, or blocks multiple user roles simultaneously.
Medium: two or more components affected; no shared state surface reached.
Narrow: failure contained within one component boundary.

**Severity** = local damage intensity at the epicenter (high / med / low). Independent of blast
radius. Always a separate labeled field. Never merge into a combined "impact" score.

**CONFIRMED** = a Phase 4-5 runtime finding that matches a specific topology violation from
Phases 1-3. Match is structural: same component, role, state surface, or contract term.
Name the matching Phase 1-3 finding explicitly.

**RUNTIME ANOMALY** = a Phase 4-5 finding with no matching topology violation in Phases 1-3.
Unexpected behavior that the static topology did not predict. Document the absence explicitly.

**SYSTEMIC** = a finding corroborated in three or more phases.
REQUIRED: every SYSTEMIC finding must enumerate the corroborating phase names.
Format: "SYSTEMIC: yes -- phases: [name], [name], [name]"
Binary "SYSTEMIC: yes" without a phase list is invalid. A finding in two phases is not SYSTEMIC.

**DEPTH labels:**
HIGH = exhaustive depth -- every item in scope must be evaluated; calibration verifies HIGH phases
produced at least one finding or an explicit "clean" declaration.
MEDIUM = standard coverage of primary paths and known risk vectors.
AS-NEEDED = run only if Phase 0 surfaces items warranting evaluation; skip with explicit statement.

**State-anchor rationale (C-22):** Trace-state runs first (Phase 1, HIGH DEPTH) because shared
state topology is the primary blast radius amplifier in any multi-component system. Pre-classifying
which state surfaces are shared, which transitions are multi-party, and which invariants span
components gives every downstream sub-skill a structural blast radius map. Running trace-state
first is not optional -- it is the prerequisite for correct blast radius classification downstream.

**Permissions-anchor rationale (C-23):** Trace-permissions runs second (Phase 2, MEDIUM DEPTH),
before flow-lifecycle (Phase 4) and flow-trigger (Phase 5). Privilege boundary classification must
precede flow analysis. A flow violation that crosses a permission boundary is SYSTEMIC by
definition. Without Phase 2 preceding the flow sub-skills, blast radius for cross-boundary flow
findings cannot be correctly assigned without retroactive revision.

**Tiebreaker protocol (apply in ranked findings order):**
1. Blast radius: wide > medium > narrow
2. CONFIRMED > RUNTIME ANOMALY
3. SYSTEMIC > isolated

---

## PHASE 0 -- Topology census

**Components in scope:** [all named services, modules, APIs, schemas, queues, event types from spec]

**Shared state surfaces:** [all databases, caches, event buses, config objects written by more than
one component -- the blast-radius amplifiers; every blast radius ceiling check uses this list]

**Downstream callers:** [all components whose behavior depends on outputs from the system under simulation]

**Role-resource inventory:** [all roles and the resources each may access -- Phase 2 input surface]

**Pre-declared contracts:** [all explicit producer/consumer contract terms in spec -- the CONFIRMED
baseline; a Phase 4-5 finding that matches a pre-declared contract term is CONFIRMED by definition]

This census is the reference inventory for all blast radius claims throughout the campaign.
A finding that cannot name a specific census entry must be returned to the spec before recording.

---

## PHASE 1 -- trace-state [HIGH DEPTH | ANCHOR: state topology pre-classifies blast radius for Phases 2-5]

Map shared state topology exhaustively. Every shared state surface from Phase 0 must appear.
Minimum expectation: every Phase 0 shared state surface is classified (multi-party or single-owner)
and every invariant is evaluated. Phase 1 output is the blast radius pre-classification map.

| From state | To state | Trigger | Invariant | Invariant holds? | Shared state surfaces affected | Blast radius pre-classification | Components in propagation path |
|------------|----------|---------|-----------|------------------|-------------------------------|--------------------------------|-------------------------------|

Shared state surface = any state object written by more than one component (from Phase 0 census).
If transition touches shared state: blast radius pre-classification = wide.
This pre-classification propagates to all downstream findings involving this surface.

If clean: "trace-state: clean -- all invariants hold; no shared state violations."

EXIT CRITERIA: All shared state surfaces from Phase 0 evaluated. No surfaces deferred.
State: "trace-state complete: [N] transitions, [N] violations, [N] wide-pre-classified surfaces."

---

## PHASE 2 -- trace-permissions [MEDIUM DEPTH | ANCHOR: privilege ceiling before flow sub-skills]

Establish the access surface. Evaluate every role-resource-action triplet from the Phase 0 inventory.
Cross-reference Phase 1: any role accessing a Phase 1 wide-pre-classified state surface inherits
wide blast radius mechanically.
Minimum expectation: every role and every resource from Phase 0 appears at least once.

| Role | Resource | Action | Permitted? | Escalation path? | Phase 1 shared state surface? | Blast radius ceiling |
|------|----------|--------|------------|------------------|------------------------------|---------------------|

Escalation path = yes when a role reaches a resource through indirect means (delegation,
inheritance, event chain, missing boundary check).
Escalation path = yes AND Phase 1 shared state surface = yes: blast radius ceiling = wide.
This ceiling holds for all downstream findings involving this role in Phases 3-5.

If no escalation paths: "trace-permissions: clean -- no escalation paths detected."

EXIT CRITERIA: All role-resource pairs from Phase 0 inventory evaluated. No pairs deferred.
State: "trace-permissions complete: [N] pairs evaluated, [N] escalation paths, [N] involving Phase 1 shared state."

---

## PHASE 3 -- trace-contract [AS-NEEDED DEPTH]

Verify what crosses role and component boundaries. Run if Phase 0 surfaces explicit contract terms;
skip with explicit statement if all interactions are implicit.

| Producer | Consumer | Contract term | Expected | Actual | Mismatch? | Phase 1 state match? | Phase 2 role match? | CONFIRMED? |
|----------|----------|---------------|----------|--------|-----------|---------------------|---------------------|------------|

Phase 1 state match = involves a Phase 1 state transition or invariant violation surface.
Phase 2 role match = involves a Phase 2 escalation role.
If either match = yes: mark CONFIRMED here, not waiting for calibration.

If clean: "trace-contract: clean -- all contracts verified."
If skipped: "trace-contract: skipped -- [reason]."

EXIT CRITERIA: All producer/consumer pairs evaluated (or skip justified).
State: "trace-contract complete: [N] pairs, [N] mismatches, [N] CONFIRMED."

---

## PHASE 4 -- flow-lifecycle [MEDIUM DEPTH]

Observe runtime behavior within the state/permission/contract envelope from Phases 1-3.

| Phase | Entry contract | Exit contract | Exception path | Exception handled? | Phase 1-3 topology match? | CONFIRMED / RUNTIME ANOMALY |
|-------|----------------|---------------|----------------|--------------------|--------------------------|-----------------------------|

CONFIRMED = matches a specific Phase 1 state violation, Phase 2 escalation, or Phase 3 mismatch.
Name the matching finding in the CONFIRMED field.
RUNTIME ANOMALY = no matching topology entry. State explicitly why no Phase 1-3 entry predicts this.

If clean: "flow-lifecycle: clean -- all lifecycle transitions verified."

EXIT CRITERIA: All lifecycle phases evaluated.
State: "flow-lifecycle complete: [N] phases, [N] failures, [N] CONFIRMED, [N] RUNTIME ANOMALY."

---

## PHASE 5 -- flow-trigger [HIGH DEPTH]

Evaluate every trigger and every activating event. Minimum expectation: every event source,
activation condition, and race condition vector is evaluated; no triggers deferred.

| Trigger | Expected fire order | Actual fire order | Race condition? | Phase 2 escalation role? | Phase 1 shared state affected? | CONFIRMED / RUNTIME ANOMALY |
|---------|---------------------|-------------------|-----------------|--------------------------|-------------------------------|------------------------------|

Phase 2 escalation role = yes if the trigger involves a role from Phase 2's escalation list.
If yes: blast radius = wide (inherits Phase 2 access surface ceiling).

If clean: "flow-trigger: clean -- all triggers verified."

EXIT CRITERIA: All triggers and activating events evaluated. No triggers deferred.
State: "flow-trigger complete: [N] triggers, [N] failures, [N] CONFIRMED, [N] RUNTIME ANOMALY."

---

## CALIBRATION BLOCK

Q1: Does any finding's blast radius change when mapped against Phase 0 shared state surfaces?
For each finding with blast radius = medium or narrow: does the affected component read from or
write to a Phase 0 shared state surface? If yes, upgrade to wide.
Also verify: every finding involving a Phase 1 wide-pre-classified surface or Phase 2 escalation
role has blast radius = wide. List every revision.

Q2: Do any Phase 4-5 findings match topology violations from Phases 1-3?
For each Phase 4-5 finding: identify the specific Phase 1, 2, or 3 entry it connects to.
If match found: confirm CONFIRMED. If no match: confirm RUNTIME ANOMALY.
List all reclassifications with the topology check result.

Q3: Which findings appear in three or more phases?
List every finding corroborated across phases. Mark SYSTEMIC if three or more phases.
REQUIRED: enumerate all corroborating phase names for every SYSTEMIC finding.
Format: "SYSTEMIC: yes -- phases: [phase-name-1], [phase-name-2], [phase-name-3]"
A count of phases is not sufficient. Phase names are required. Binary flag = invalid.

Q4: Did HIGH-DEPTH phases achieve minimum expectation?
Phase 1 (trace-state): does every Phase 0 shared state surface appear in the table?
Phase 5 (flow-trigger): does every trigger and activating event appear?
If any item was deferred or skipped, state why and whether the omission affects ranking.

Q5: Would any finding below have shipped without this simulation?
For each wide-blast-radius finding: name the assumption it would have bypassed
(undocumented privilege, implicit contract, tacit lifecycle expectation, missing spec coverage,
assumed state boundary). This is the inertia question -- what would the team have believed
without this evidence?

---

## CONSOLIDATE

Write ONE report. Do not concatenate five phase outputs. Synthesis, not a log.

**Ranked findings (blast radius descending, full tiebreaker protocol applied):**

Tiebreaker protocol (apply in order, no exceptions):
1. Blast radius: wide > medium > narrow
2. CONFIRMED > RUNTIME ANOMALY
3. SYSTEMIC > isolated

For each finding, use this atomic block without modification or omission:

---
**Finding [N]**
1. Name: [finding name or short description]
2. Source phase: [phase name that produced this finding]
3. Blast radius: [wide | medium | narrow] -- [named Phase 0 census components in propagation path]
4. Severity at epicenter: [high | med | low]
5. SYSTEMIC: [yes -- phases: [comma-separated corroborating phase names] | no]
6. Classification: [CONFIRMED | RUNTIME ANOMALY | isolated]
7. What must change: [one concrete fix direction in spec, contract, or implementation]
---

Prose findings, partial field sets, and inline annotations are not valid replacements for this block.
Every finding must use all seven fields.

**Spec gaps:** [list each gap, or "none detected"]

**Contract violations:** [list each violation, or "none detected"]

**Privilege escalation paths:** [list each path, or "none detected"]

**Clean zones:** [all Phase 0 census components with no findings across all five phases]

---

## VERDICT

One paragraph. Name the finding with the widest blast radius by its Phase 0 census component name.
If SYSTEMIC: enumerate the corroborating phases by name.
If CONFIRMED: name the Phase 1-3 topology finding that predicted it.
Name the assumption the team would have carried into implementation without this simulation --
the displaced belief from Q5 with the widest potential damage.
Conclude with a clear recommendation: proceed, proceed with conditions, or halt.
```

---

## V-04 -- State-anchor + permissions-anchor + Q6 sequence integrity (combination)
**Axes:** Role sequence (state-anchor Phase 1 + permissions-anchor Phase 2) + Calibration form (Q6 sequencing integrity question) + explicit C-22/C-23 anchor declarations at phase headers
**Hypothesis:** V-01 establishes the dual-anchor sequence; the Q1-Q5 calibration block does not explicitly verify that the sequencing contract held throughout execution. A sixth question -- "Did the execution sequence deliver the pre-classification guarantee?" -- adds a self-referential integrity check that makes C-22 and C-23 compliance visible as a named output, not just as a structural property. Expected: all 15 aspirational criteria satisfied; 90/90. The Q6 addition distinguishes this from V-01 and may become the canonical combination for future rubric versions.

```
Simulate the technical behavior of: {{topic}}

---

## DEFINITIONS

**Blast radius** = how broadly a failure propagates through the system.
Wide: corrupts shared state, breaks downstream callers, or blocks multiple user roles simultaneously.
Medium: two or more components affected; no shared state surface reached.
Narrow: failure contained within one component boundary.

**Severity** = damage depth at the epicenter (high / med / low). Independent of blast radius.
Always report as a separate labeled field. Never merge into a combined "impact" score.

**CONFIRMED** = a Phase 4-5 runtime finding that matches a specific topology violation from
Phases 1-3. The match must be structural: same component, role, state surface, or contract term.

**RUNTIME ANOMALY** = a Phase 4-5 finding with no matching topology violation in Phases 1-3.
Unexpected behavior not predicted by the static topology.

**SYSTEMIC** = a finding corroborated in three or more phases. Must enumerate corroborating phase
names. Format: "SYSTEMIC: yes -- phases: [name], [name], [name]." Binary flag = invalid.

**State-anchor rationale (C-22):** Trace-state runs first (Phase 1) because state topology
pre-classifies blast radius candidates for all downstream sub-skills. Shared state surfaces are
the primary blast radius amplifiers: a failure that touches a shared state object propagates to
every component that reads or writes it. Running trace-state first builds the blast radius map
that every subsequent phase inherits. Any other execution order defers this classification to
post-hoc analysis, introducing blast radius underestimation risk.

**Permissions-anchor rationale (C-23):** Trace-permissions runs second (Phase 2), before
flow-lifecycle (Phase 4) and flow-trigger (Phase 5). Privilege boundaries determine the blast
radius ceiling for flow findings: a trigger that fires across a permission boundary reaches
whatever the role's access surface allows. Establishing the access surface ceiling in Phase 2
means flow findings inherit it structurally, without retroactive revision.

**Tiebreaker protocol (apply in order):**
1. Blast radius: wide > medium > narrow
2. CONFIRMED > RUNTIME ANOMALY
3. SYSTEMIC > isolated

---

## PHASE 0 -- Topology census

**Components in scope:** [all named services, modules, APIs, schemas, queues from spec]

**Shared state surfaces:** [all databases, caches, event buses, config objects read/written by
multiple components -- the blast-radius amplifiers]

**Downstream callers:** [all components that depend on outputs from this system]

**Role-resource inventory:** [all roles and the resources each may access -- Phase 2 input surface]

**Pre-declared contracts:** [all explicit producer/consumer contract terms in spec --
the CONFIRMED baseline for Phases 4-5]

Every blast radius claim must name a specific entry from this census.

---

## PHASE 1 -- trace-state [ANCHOR: runs first; state topology pre-classifies blast radius for Phases 2-5]

Map shared state topology and build the blast radius pre-classification map.

| From state | To state | Trigger | Invariant | Invariant holds? | Shared state surfaces affected | Blast radius pre-classification | Downstream phase inheritance |
|------------|----------|---------|-----------|------------------|-------------------------------|--------------------------------|-----------------------------|

Shared state surface = any state object from Phase 0 written by more than one component.
Invariant violation on a shared state surface: blast radius pre-classification = wide.
Wide pre-classification propagates to Phases 2-5 for any finding involving this surface.

If clean: "trace-state: clean -- all invariants hold; Phase 0 state surfaces catalogued."

EXIT CRITERIA: All shared state surfaces from Phase 0 evaluated.
State: "trace-state complete: [N] transitions, [N] violations, [N] wide-pre-classified surfaces."

---

## PHASE 2 -- trace-permissions [ANCHOR: runs before flow-lifecycle and flow-trigger; access ceiling set here]

Establish the access surface ceiling. All flow findings in Phases 4-5 inherit this ceiling.
Cross-reference Phase 1: role accessing a Phase 1 wide-pre-classified surface = wide ceiling.

| Role | Resource | Action | Permitted? | Escalation path? | Phase 1 shared state surface? | Blast radius ceiling |
|------|----------|--------|------------|------------------|------------------------------|---------------------|

Escalation path = yes when a role reaches a resource through indirect means.
If escalation = yes AND Phase 1 shared state = yes: blast radius ceiling = wide.

If no escalation paths: "trace-permissions: clean -- no escalation paths detected."

EXIT CRITERIA: All role-resource pairs evaluated.
State: "trace-permissions complete: [N] pairs, [N] escalation paths, [N] involving Phase 1 shared state."

---

## PHASE 3 -- trace-contract

Verify what crosses role and component boundaries.

| Producer | Consumer | Contract term | Expected | Actual | Mismatch? | Phase 1 state match? | Phase 2 role match? | CONFIRMED? |
|----------|----------|---------------|----------|--------|-----------|---------------------|---------------------|------------|

Phase 1 state match = involves a Phase 1 state violation surface.
Phase 2 role match = involves a Phase 2 escalation role.
Either match = CONFIRMED.

If clean: "trace-contract: clean -- all contracts verified."

EXIT CRITERIA: All producer/consumer pairs evaluated.
State: "trace-contract complete: [N] pairs, [N] mismatches, [N] CONFIRMED."

---

## PHASE 4 -- flow-lifecycle [inherits Phase 1 state map + Phase 2 access ceiling]

Observe runtime behavior within the state/permission/contract envelope.

| Phase | Entry contract | Exit contract | Exception path | Exception handled? | Phase 1-3 topology match? | CONFIRMED / RUNTIME ANOMALY |
|-------|----------------|---------------|----------------|--------------------|--------------------------|-----------------------------|

CONFIRMED = matches Phase 1 state violation, Phase 2 escalation, or Phase 3 mismatch.
RUNTIME ANOMALY = no Phase 1-3 entry predicts this finding. Document the absence explicitly.

If clean: "flow-lifecycle: clean -- all lifecycle transitions verified."

EXIT CRITERIA: All lifecycle phases evaluated.
State: "flow-lifecycle complete: [N] phases, [N] failures, [N] CONFIRMED, [N] RUNTIME ANOMALY."

---

## PHASE 5 -- flow-trigger [inherits Phase 1 state map + Phase 2 access ceiling]

Evaluate every trigger and every activating event in scope.

| Trigger | Expected fire order | Actual fire order | Race condition? | Phase 2 escalation role? | Phase 1 shared state affected? | CONFIRMED / RUNTIME ANOMALY |
|---------|---------------------|-------------------|-----------------|--------------------------|-------------------------------|------------------------------|

Phase 2 escalation role = yes: blast radius = wide (inherits Phase 2 ceiling).

If clean: "flow-trigger: clean -- all triggers verified."

EXIT CRITERIA: All triggers and activating events evaluated. No triggers deferred.
State: "flow-trigger complete: [N] triggers, [N] failures, [N] CONFIRMED, [N] RUNTIME ANOMALY."

---

## CALIBRATION BLOCK

Q1: Does any finding's blast radius change when mapped against Phase 0 shared state surfaces?
For each finding with blast radius = medium or narrow: does the affected component read from or
write to a Phase 0 shared state surface? If yes, upgrade to wide. List every revision explicitly.

Q2: Do any Phase 4-5 findings match topology violations from Phases 1-3?
For each Phase 4-5 finding: identify the specific Phase 1, 2, or 3 entry it connects to.
If match: confirm CONFIRMED. If no match: confirm RUNTIME ANOMALY. List all reclassifications.

Q3: Which findings appear in three or more phases?
List every finding corroborated across phases. Mark SYSTEMIC if three or more phases.
REQUIRED: enumerate the corroborating phase names for every SYSTEMIC finding.
Format: "SYSTEMIC: yes -- phases: [phase-name-1], [phase-name-2], [phase-name-3]"
Binary flags without phase lists are not valid.

Q4: Does the blast radius pre-classification from Phase 1 hold throughout?
For every finding involving a Phase 1 wide-pre-classified surface: verify blast radius = wide.
For every finding involving a Phase 2 escalation role: verify blast radius = wide.
Any deviation is a calibration error. Revise and explain each case.

Q5: Would any finding below have shipped without this simulation?
For each wide-blast-radius finding: name the assumption it would have bypassed.
This is the inertia question -- what would the team have believed?

Q6: Did the execution sequence deliver its pre-classification guarantee?
State the sequence used: trace-state (Phase 1) → trace-permissions (Phase 2) → trace-contract
(Phase 3) → flow-lifecycle (Phase 4) → flow-trigger (Phase 5).
For each Phase 4-5 finding: confirm that its blast radius classification used the Phase 1 state
topology map and Phase 2 access surface ceiling, not a post-hoc reconstruction.
If any finding's classification was constructed after the fact rather than inherited from Phase 1
or Phase 2, identify it and explain the remediation.

---

## CONSOLIDATE

Write ONE report. Do not concatenate five phase outputs. Synthesis, not a log.

**Ranked findings (calibrated blast radius descending, tiebreaker protocol applied):**

Tiebreaker protocol (apply in order):
1. Blast radius: wide > medium > narrow
2. CONFIRMED > RUNTIME ANOMALY
3. SYSTEMIC > isolated

For each finding, use this atomic block exactly:

---
**Finding [N]**
1. Name: [finding name or short description]
2. Source phase: [phase name that produced this finding]
3. Blast radius: [wide | medium | narrow] -- [named census components in propagation path]
4. Severity at epicenter: [high | med | low]
5. SYSTEMIC: [yes -- phases: [comma-separated corroborating phase names] | no]
6. Classification: [CONFIRMED | RUNTIME ANOMALY | isolated]
7. What must change: [one concrete fix direction in spec, contract, or implementation]
---

**Spec gaps:** [list each gap, or "none detected"]

**Contract violations:** [list each violation, or "none detected"]

**Privilege escalation paths:** [list each path, or "none detected"]

**Clean zones:** [Phase 0 census components with no findings across all five phases]

---

## VERDICT

One paragraph. Name the finding with the widest blast radius by its Phase 0 census component name.
State CONFIRMED or RUNTIME ANOMALY. If SYSTEMIC, enumerate the corroborating phases.
Name the assumption the team would have carried into implementation had this simulation not run.
Conclude: proceed, proceed with conditions, or halt.
```

---

## V-05 -- Full 15-criterion coverage (combination)
**Axes:** All prior axes combined -- state-anchor Phase 1 + permissions-anchor Phase 2 + DEPTH asymmetry + CONFIRMED/RUNTIME ANOMALY throughout + Q1-Q6 calibration + SYSTEMIC phase enumeration + atomic 7-field blocks + tiebreaker protocol + per-phase exit criteria + double-reinforcement for C-22/C-23
**Hypothesis:** V-05 is the maximum coverage variation. It takes R6 V-05 (double-reinforcement strategy, 90/90 under v5) and applies the dual-anchor resequencing from V-01 plus the Q6 sequence integrity question from V-04. Every criterion in v6 rubric (C-01 through C-23) has at least two reinforcement points: once in CORE DEFINITIONS and once in the execution section. C-22 and C-23 each have three reinforcement points: CORE DEFINITIONS, phase header label, and Q6 verification. Expected: 15/15 aspirational → 90/90. Most durable scaffold for future rubric versions.

```
Simulate the technical behavior of: {{topic}}

---

## CORE DEFINITIONS

**Blast radius** = propagation width across the system when a failure occurs.
Wide: corrupts shared state, breaks downstream callers, or blocks multiple user roles simultaneously.
Medium: two or more components affected; no shared state surface reached.
Narrow: failure contained within one component boundary.

**Severity** = local damage intensity at the epicenter (high / med / low). Independent of blast
radius. Always a separate labeled field. Never merge into a combined "impact" score.
Do not merge blast radius and severity. They are separate fields. Always.

**CONFIRMED** = a Phase 4-5 runtime finding that matches a specific topology violation from
Phases 1-3. Match is structural: same component, role, state surface, or contract term.
Name the matching Phase 1-3 finding explicitly.

**RUNTIME ANOMALY** = a Phase 4-5 finding with no matching topology violation in Phases 1-3.
Unexpected behavior that the static topology did not predict. Document the absence explicitly.

**SYSTEMIC** = a finding corroborated in three or more phases.
REQUIRED: every SYSTEMIC finding must enumerate the corroborating phase names.
Format: "SYSTEMIC: yes -- phases: [name], [name], [name]"
Binary "SYSTEMIC: yes" without a phase list is invalid. A finding in two phases is not SYSTEMIC.

**DEPTH labels:**
HIGH = exhaustive depth -- every item in scope must be evaluated; calibration verifies HIGH phases
produced at least one finding or an explicit "clean" declaration.
MEDIUM = standard coverage of primary paths and known risk vectors.
AS-NEEDED = run only if Phase 0 surfaces items warranting evaluation; skip with explicit statement.

**State-anchor rationale (C-22 -- first reinforcement):** Trace-state runs first (Phase 1) because
shared state topology is the structural source of blast radius amplification. A finding touching
a shared state surface propagates to every component that reads or writes it -- blast radius = wide
by construction. Pre-building this topology map in Phase 1 means Phases 2-5 inherit it without
reconstruction. Running trace-state first is not optional; it is the prerequisite for correct blast
radius classification across the entire campaign.

**Permissions-anchor rationale (C-23 -- first reinforcement):** Trace-permissions runs second
(Phase 2), explicitly before flow-lifecycle (Phase 4) and flow-trigger (Phase 5). Privilege
boundary classification determines the blast radius ceiling for flow findings: a flow that crosses
a permission boundary is SYSTEMIC by definition. Without the Phase 2 ceiling established before
flow analysis, blast radius classification for flow sub-skills cannot be reliably assigned.

**Tiebreaker protocol (apply in ranked findings order -- first reinforcement):**
1. Blast radius: wide > medium > narrow
2. CONFIRMED > RUNTIME ANOMALY (confirmed findings rank above unconfirmed at equal blast radius)
3. SYSTEMIC > isolated (SYSTEMIC findings rank above isolated at equal blast radius and confirmation)
Without explicit tiebreaker rules, ranking is arbitrary for tied findings.

---

## PHASE 0 -- Topology census

**Components in scope:** [all named services, modules, APIs, schemas, queues, event types from spec]

**Shared state surfaces:** [all databases, caches, event buses, config objects written by more than
one component -- the blast-radius amplifiers; every blast radius ceiling check uses this list]

**Downstream callers:** [all components whose behavior depends on outputs from the system under simulation]

**Role-resource inventory:** [all roles and the resources each may access -- Phase 2 input surface]

**Pre-declared contracts:** [all explicit producer/consumer contract terms in spec -- the CONFIRMED
baseline; a Phase 4-5 finding matching a pre-declared contract term is CONFIRMED by definition]

This census is the reference inventory for all blast radius claims throughout the campaign.
A finding that cannot name a specific census entry must be returned to the spec before recording.

---

## PHASE 1 -- trace-state [HIGH DEPTH | C-22 ANCHOR: state topology pre-classifies blast radius for Phases 2-5]

Map shared state topology exhaustively. This is the blast radius pre-classification phase.
Every shared state surface from Phase 0 must appear in this table.
Minimum expectation: every Phase 0 shared state surface is classified and every invariant evaluated.

| From state | To state | Trigger | Invariant | Invariant holds? | Shared state surfaces affected | Blast radius pre-classification | Components in propagation path |
|------------|----------|---------|-----------|------------------|-------------------------------|--------------------------------|-------------------------------|

Shared state surface = any state object from Phase 0 written by more than one component.
Violation on shared state surface: blast radius pre-classification = wide.
This wide pre-classification propagates structurally to all findings involving this surface in Phases 2-5.
No downstream phase needs to reconstruct this classification -- it is inherited.

If clean: "trace-state: clean -- all invariants hold; blast radius map established from Phase 0."

EXIT CRITERIA: All shared state surfaces from Phase 0 evaluated. No surfaces deferred.
State: "trace-state complete: [N] transitions, [N] violations, [N] wide-pre-classified surfaces."

---

## PHASE 2 -- trace-permissions [MEDIUM DEPTH | C-23 ANCHOR: access ceiling before flow-lifecycle and flow-trigger]

Establish the access surface ceiling. All flow findings in Phases 4-5 inherit this ceiling.
Evaluate every role-resource-action triplet from Phase 0. Cross-reference Phase 1: any role
accessing a Phase 1 wide-pre-classified state surface inherits wide blast radius mechanically.
Minimum expectation: every role and every resource from Phase 0 appears at least once.

| Role | Resource | Action | Permitted? | Escalation path? | Phase 1 shared state surface? | Blast radius ceiling |
|------|----------|--------|------------|------------------|------------------------------|---------------------|

Escalation path = yes when a role reaches a resource through indirect means (delegation,
inheritance, event chain, missing boundary check).
Escalation path = yes AND Phase 1 shared state surface = yes: blast radius ceiling = wide.
This ceiling holds for all downstream findings involving this role in Phases 3-5.

If no escalation paths: "trace-permissions: clean -- no escalation paths detected."

EXIT CRITERIA: All role-resource pairs from Phase 0 inventory evaluated. No pairs deferred.
State: "trace-permissions complete: [N] pairs evaluated, [N] escalation paths, [N] involving Phase 1 shared state."

---

## PHASE 3 -- trace-contract [AS-NEEDED DEPTH]

Verify what crosses role and component boundaries. Run if Phase 0 surfaces explicit contract terms;
skip with explicit statement if all interactions are implicit.

| Producer | Consumer | Contract term | Expected | Actual | Mismatch? | Phase 1 state match? | Phase 2 role match? | CONFIRMED? |
|----------|----------|---------------|----------|--------|-----------|---------------------|---------------------|------------|

Phase 1 state match = involves a Phase 1 state violation or shared state surface.
Phase 2 role match = involves a Phase 2 escalation role.
Either match = mark CONFIRMED here, not waiting for calibration.

If clean: "trace-contract: clean -- all contracts verified."
If skipped: "trace-contract: skipped -- [reason]."

EXIT CRITERIA: All producer/consumer pairs evaluated (or skip justified).
State: "trace-contract complete: [N] pairs, [N] mismatches, [N] CONFIRMED."

---

## PHASE 4 -- flow-lifecycle [MEDIUM DEPTH | inherits Phase 1 state map + Phase 2 access ceiling]

Observe runtime behavior within the state/permission/contract envelope from Phases 1-3.
Blast radius ceiling for any finding involving a Phase 2 escalation role = wide (inherited, not computed).

| Phase | Entry contract | Exit contract | Exception path | Exception handled? | Phase 1-3 topology match? | CONFIRMED / RUNTIME ANOMALY |
|-------|----------------|---------------|----------------|--------------------|--------------------------|-----------------------------|

CONFIRMED = matches a specific Phase 1 state violation, Phase 2 escalation, or Phase 3 mismatch.
Name the matching finding in the CONFIRMED field.
RUNTIME ANOMALY = no matching topology entry. State explicitly why no Phase 1-3 entry predicts this.

If clean: "flow-lifecycle: clean -- all lifecycle transitions verified."

EXIT CRITERIA: All lifecycle phases evaluated.
State: "flow-lifecycle complete: [N] phases, [N] failures, [N] CONFIRMED, [N] RUNTIME ANOMALY."

---

## PHASE 5 -- flow-trigger [HIGH DEPTH | inherits Phase 1 state map + Phase 2 access ceiling]

Evaluate every trigger and every activating event. Minimum expectation: every event source,
activation condition, and race condition vector is evaluated; no triggers deferred.
Blast radius ceiling for any finding involving a Phase 2 escalation role = wide (inherited, not computed).

| Trigger | Expected fire order | Actual fire order | Race condition? | Phase 2 escalation role? | Phase 1 shared state affected? | CONFIRMED / RUNTIME ANOMALY |
|---------|---------------------|-------------------|-----------------|--------------------------|-------------------------------|------------------------------|

Phase 2 escalation role = yes: blast radius = wide (inherits Phase 2 ceiling).

If clean: "flow-trigger: clean -- all triggers verified."

EXIT CRITERIA: All triggers and activating events evaluated. No triggers deferred.
State: "flow-trigger complete: [N] triggers, [N] failures, [N] CONFIRMED, [N] RUNTIME ANOMALY."

---

## CALIBRATION BLOCK

Q1: Does any finding's blast radius change when mapped against Phase 0 shared state surfaces?
For each finding with blast radius = medium or narrow: does the affected component read from or
write to a Phase 0 shared state surface? If yes, upgrade to wide.
Also verify: every finding involving a Phase 1 wide-pre-classified surface has blast radius = wide.
Every finding involving a Phase 2 escalation role has blast radius = wide.
List every revision.

Q2: Do any Phase 4-5 findings match topology violations from Phases 1-3?
For each Phase 4-5 finding: identify the specific Phase 1, 2, or 3 entry it connects to.
If match: confirm CONFIRMED. If no match: confirm RUNTIME ANOMALY.
List all reclassifications with the topology check result.

Q3: Which findings appear in three or more phases?
List every finding corroborated across phases. Mark SYSTEMIC if three or more phases.
REQUIRED: enumerate all corroborating phase names for every SYSTEMIC finding.
Format: "SYSTEMIC: yes -- phases: [phase-name-1], [phase-name-2], [phase-name-3]"
A count of phases is not sufficient. Phase names are required. Binary flag = invalid.

Q4: Did HIGH-DEPTH phases achieve minimum expectation?
Phase 1 (trace-state): does every Phase 0 shared state surface appear in the table?
Phase 5 (flow-trigger): does every trigger and activating event appear?
If any item was deferred or skipped, state why and whether the omission affects ranking.

Q5: Would any finding below have shipped without this simulation?
For each wide-blast-radius finding: name the assumption it would have bypassed
(undocumented privilege, implicit contract, tacit lifecycle expectation, missing spec coverage,
assumed state or access boundary). The verdict will name the finding with the most dangerous
displaced assumption.

Q6: Did the execution sequence deliver the pre-classification guarantee?
The prescribed sequence is: trace-state (Phase 1) → trace-permissions (Phase 2) →
trace-contract (Phase 3) → flow-lifecycle (Phase 4) → flow-trigger (Phase 5).
For each Phase 4-5 finding: confirm that blast radius classification was inherited from Phase 1
state topology and Phase 2 access surface ceiling -- not constructed post-hoc.
If any finding required post-hoc blast radius revision (i.e., the pre-classification from Phase 1
or Phase 2 was unavailable when the finding was recorded), identify it and explain why.
The goal of the sequence is zero post-hoc blast radius revisions.

---

## CONSOLIDATE

Write ONE report. Do not concatenate five phase outputs. Synthesis, not a log.

**Ranked findings (blast radius descending, full tiebreaker protocol applied -- second reinforcement):**

Tiebreaker protocol (apply in order, no exceptions):
1. Blast radius: wide > medium > narrow
2. CONFIRMED > RUNTIME ANOMALY (confirmed findings rank above unconfirmed at equal blast radius)
3. SYSTEMIC > isolated (SYSTEMIC findings rank above isolated at equal blast radius and confirmation tier)

For each finding, use this atomic block without modification or omission:

---
**Finding [N]**
1. Name: [finding name or short description]
2. Source phase: [phase name that produced this finding]
3. Blast radius: [wide | medium | narrow] -- [named Phase 0 census components in propagation path]
4. Severity at epicenter: [high | med | low]
5. SYSTEMIC: [yes -- phases: [comma-separated corroborating phase names] | no]
6. Classification: [CONFIRMED | RUNTIME ANOMALY | isolated]
7. What must change: [one concrete fix direction in spec, contract, or implementation]
---

Prose findings, partial field sets, and inline annotations are not valid replacements for this block.
Every finding must use all seven fields.

**Spec gaps:** [list each gap, or "none detected"]

**Contract violations:** [list each violation, or "none detected"]

**Privilege escalation paths:** [list each path, or "none detected"]

**Clean zones:** [all Phase 0 census components with no findings across all five phases]

---

## VERDICT

One paragraph. Name the finding with the widest blast radius by its Phase 0 census component name.
If SYSTEMIC: enumerate the corroborating phases by name (second reinforcement for SYSTEMIC format).
If CONFIRMED: name the Phase 1-3 topology finding that predicted it.
Name the assumption the team would have carried into implementation without this simulation --
the displaced belief from Q5 with the widest potential damage.
Conclude with a clear recommendation: proceed, proceed with conditions, or halt.
```

---

## Axis summary

| Variation | Axis | New criteria targeted | Prior best analog |
|-----------|------|-----------------------|-------------------|
| V-01 | State-anchor sequence (single) | C-22, C-23 (sequence delivers both) | R6 V-04 base + Phase 1/2 swap |
| V-02 | Permissions-anchor rationale reinforcement (single) | C-23 isolation test | R6 V-04 unchanged sequence + explicit before-flow declarations |
| V-03 | DEPTH asymmetry on state-anchor sequence (single) | C-22, C-23 + depth labels | R6 V-05 base + Phase 1/2 swap |
| V-04 | Dual-anchor sequence + Q6 (combination) | C-22, C-23 + sequence integrity calibration | V-01 + Q6 addition |
| V-05 | Full 15-criterion coverage (combination) | All C-01--C-23 + double reinforcement | R6 V-05 + dual-anchor resequencing + Q6 |

**Expected ceiling:** V-01 and V-03 through V-05 should pass all 15 aspirational criteria (90/90).
V-02 tests whether C-23 was already structurally satisfied by R6 V-04 (expected: 14/15, 89/90).
If V-02 also reaches 90/90, it confirms C-23 was implicit in R6 V-04 and the rubric formalized an already-passing pattern.
