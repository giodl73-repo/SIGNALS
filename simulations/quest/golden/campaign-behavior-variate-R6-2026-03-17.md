# Quest Variations -- campaign-behavior (R6)
**Skill:** campaign-behavior
**Rubric:** v5 (C-01--C-21)
**Round:** 6
**Date:** 2026-03-17

---

## Axes explored in R6

Single-axis (unexplored as of R5):
- **Q1-Qn interrogative calibration** -- targets C-18, the criterion that blocked all five R5 variations from a perfect score
- **SYSTEMIC phase enumeration** -- targets C-21, mandates phase name list in every SYSTEMIC flag
- **State-anchor role sequence** -- trace-state first establishes shared-state topology before access or contract analysis

Combinations (V-04, V-05):
- **V-04:** Q1-Qn + permissions-anchor + SYSTEMIC phase enumeration + atomic blocks + tiebreaker
- **V-05:** Full 13-criterion coverage -- permissions-anchor + DEPTH asymmetry + CONFIRMED/RUNTIME ANOMALY throughout + Q1-Qn + SYSTEMIC phase enumeration + atomic blocks + tiebreaker + all exit criteria

---

## V-01 -- Q1-Qn interrogative calibration
**Axis:** Calibration form -- structured as a numbered Q-and-A interrogative sequence (Q1-Q5) rather than step blocks or prose; each question targets a specific re-grounding concern
**Hypothesis:** C-18 (Q1-Qn calibration) blocked all five R5 variations from a perfect score. The only structural change needed is to replace the step-block calibration with numbered questions that carry explicit answers. If the base prompt structure (permissions-anchor, CONFIRMED/RUNTIME ANOMALY, atomic findings, tiebreaker) is otherwise sound, inserting Q1-Q5 should close the C-18 gap while preserving the 9/10 aspirational score from R5 V-01.

```
Simulate the technical behavior of: {{topic}}

---

## BLAST RADIUS AND SEVERITY DEFINITIONS

Blast radius = how broadly a failure propagates through the system.
Wide: corrupts shared state, breaks downstream callers, or blocks multiple user roles simultaneously.
Medium: two or more components affected; no shared state surface reached.
Narrow: failure contained within one component boundary.

Severity = damage depth at the epicenter (high / med / low).
These are independent dimensions. Never merge them into a single "impact" field.
Report both as separate labeled fields in every finding.

---

## PHASE 0 -- Topology census

Before any sub-skill runs, record the system vocabulary explicitly.

**Components in scope:** [list every named service, module, API, schema, queue from the spec]

**Shared state surfaces:** [list databases, caches, event buses, configuration objects that
multiple components read or write -- these are the blast-radius amplifiers]

**Downstream callers:** [list every component whose behavior depends on the system under simulation]

**Role-resource inventory:** [list every role and the resources it may access]

**Pre-declared contracts:** [list every producer/consumer contract term the spec explicitly
commits to -- these form the CONFIRMED classification baseline for Phases 4-5]

Every blast radius claim below must name a specific entry from this census.
If a finding cannot name a census item, return to the spec before recording the finding.

---

## PHASE 1 -- trace-permissions

Establish the access surface. Enumerate every role-resource-action triplet in scope.

| Role | Resource | Action | Permitted? | Escalation path? | Blast radius if escalated |
|------|----------|--------|------------|------------------|---------------------------|

An escalation path exists when a role can reach a resource through indirect means
(delegation, inheritance, event chain, or missing boundary check).
If escalation path = yes, the blast radius ceiling for downstream phases is wide
regardless of where the finding originates.

If no escalation paths exist:
"trace-permissions: clean -- all role-resource pairs verified, no escalation paths detected."

EXIT CRITERIA: All role-resource pairs in scope evaluated. No pairs deferred.
State: "trace-permissions complete: [N] pairs evaluated, [N] escalation paths found."

---

## PHASE 2 -- trace-state

Map state reachability through the access surface established in Phase 1.
Focus on shared state surfaces from Phase 0 -- those are the blast-radius amplifiers.

For each state transition in scope:

| From state | To state | Trigger | Invariant | Invariant holds? | Phase 1 escalation connected? |
|------------|----------|---------|-----------|------------------|-------------------------------|

If Phase 1 escalation connected = yes and invariant holds = no: classify CONFIRMED immediately.

If no state violations: "trace-state: clean -- all invariants verified."

EXIT CRITERIA: All shared state surfaces from Phase 0 evaluated. No surfaces deferred.
State: "trace-state complete: [N] transitions evaluated, [N] violations found, [N] connected to Phase 1."

---

## PHASE 3 -- trace-contract

Verify what crosses role and component boundaries.

| Producer | Consumer | Contract term | Expected | Actual | Mismatch? | Phase 1/2 topology match? |
|----------|----------|---------------|----------|--------|-----------|--------------------------|

Phase 1/2 topology match = yes if this contract involves a Phase 1 escalation role or a
Phase 2 state violation surface. If match = yes: classify CONFIRMED.

If no mismatches: "trace-contract: clean -- all contracts verified."

EXIT CRITERIA: All producer/consumer pairs in scope evaluated. No pairs deferred.
State: "trace-contract complete: [N] pairs evaluated, [N] mismatches found, [N] CONFIRMED."

---

## PHASE 4 -- flow-lifecycle

Observe runtime behavior within the permission/state/contract envelope.

| Phase | Entry contract | Exit contract | Exception path | Exception handled? | CONFIRMED / RUNTIME ANOMALY |
|-------|----------------|---------------|----------------|--------------------|-----------------------------|

CONFIRMED = this finding matches a violation from Phases 1-3. Name the matching finding.
RUNTIME ANOMALY = no matching topology violation in Phases 1-3.

If no failures: "flow-lifecycle: clean -- all lifecycle transitions verified."

EXIT CRITERIA: All lifecycle phases evaluated. No phases deferred.
State: "flow-lifecycle complete: [N] phases, [N] failures, [N] CONFIRMED, [N] RUNTIME ANOMALY."

---

## PHASE 5 -- flow-trigger

Evaluate every trigger and every activating event in scope.

| Trigger | Expected fire order | Actual fire order | Race condition? | Phase 1 escalation role? | CONFIRMED / RUNTIME ANOMALY |
|---------|---------------------|-------------------|-----------------|--------------------------|------------------------------|

Phase 1 escalation role = yes if this trigger involves a role from Phase 1's escalation list.
If yes: blast radius = wide (inherits from Phase 1 access surface ceiling).

If no failures: "flow-trigger: clean -- all triggers verified."

EXIT CRITERIA: All triggers and activating events evaluated. No triggers deferred.
State: "flow-trigger complete: [N] triggers, [N] failures, [N] CONFIRMED, [N] RUNTIME ANOMALY."

---

## CALIBRATION BLOCK

Q1: Does any finding's blast radius change when mapped against Phase 0 shared state surfaces?
For each finding with blast radius = medium or narrow: does the affected component read from
or write to a Phase 0 shared state surface? If yes, upgrade to wide. List every revision.

Q2: Do any Phase 4-5 findings match topology violations from Phases 1-3?
For each Phase 4-5 finding: identify the specific Phase 1 escalation path, Phase 2 state
violation, or Phase 3 contract mismatch it connects to. If match found: confirm CONFIRMED.
If no match: confirm RUNTIME ANOMALY. List all reclassifications.

Q3: Which findings appear in three or more phases?
List every finding corroborated across phases. Mark SYSTEMIC if three or more phases.
For every SYSTEMIC finding, enumerate the corroborating phases:
"SYSTEMIC: yes -- phases: [phase-name-1], [phase-name-2], [phase-name-3]"
Do not use binary SYSTEMIC flags. The phase list is required.

Q4: Does the blast radius ceiling from Phase 1 hold throughout?
For every finding involving a Phase 1 escalation role, verify blast radius = wide.
Any finding involving a Phase 1 escalation role with blast radius below wide is a
calibration error. Revise and explain.

Q5: Would any finding below have shipped without this simulation?
For each wide-blast-radius finding: name the assumption it would have bypassed
(undocumented privilege, implicit contract, tacit lifecycle expectation, missing spec
coverage). This is the inertia question -- what would the team have assumed?

---

## CONSOLIDATE

Write ONE report. Do not concatenate five phase outputs.

**Ranked findings (calibrated blast radius order, wide first):**

Tiebreaker protocol:
1. Blast radius descending (wide > medium > narrow)
2. CONFIRMED > RUNTIME ANOMALY
3. SYSTEMIC > isolated

For each finding, use this atomic block exactly:

---
**Finding [N]**
1. Name: [finding name or short description]
2. Source phase: [phase name]
3. Blast radius: [wide | medium | narrow] -- [named census components in propagation path]
4. Severity at epicenter: [high | med | low]
5. SYSTEMIC: [yes -- phases: [comma-separated phase list] | no]
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
State CONFIRMED or RUNTIME ANOMALY. If SYSTEMIC, list the corroborating phases.
State the assumption the team would have carried into implementation had this simulation not run.
Conclude: proceed, proceed with conditions, or halt.
```

---

## V-02 -- SYSTEMIC phase enumeration (single axis)
**Axis:** SYSTEMIC flag format -- every SYSTEMIC finding enumerates the corroborating phases by name rather than using a binary yes/no; this is enforced in the definitions block, in each phase's output format, in the calibration step, and in the consolidated finding block
**Hypothesis:** C-21 (SYSTEMIC phase enumeration) is a new criterion in v5. No R5 variation passed it. The fix is mechanical: wherever a SYSTEMIC flag appears, mandate the phase list. If the underlying base structure (V-05 R5 with CONFIRMED/RUNTIME ANOMALY and atomic blocks) is otherwise correct, adding the phase list requirement should close C-21 without disturbing other passing criteria.

```
Simulate the technical behavior of: {{topic}}

---

## DEFINITIONS

**Blast radius** = how broadly a failure propagates through the system.
Wide: corrupts shared state, breaks downstream callers, or blocks multiple user roles.
Medium: two or more components affected; no shared state surface reached.
Narrow: failure contained within one component boundary.

**Severity** = damage depth at the epicenter (high / med / low). Independent of blast radius.
Always report as a separate labeled field. Never merge into a single "impact" score.

**SYSTEMIC** = a finding that appears in three or more phases.
A SYSTEMIC finding MUST enumerate the corroborating phase names.
Required format: "SYSTEMIC: yes -- phases: [name], [name], [name]"
Binary "SYSTEMIC: yes" without a phase list is not valid and will be rejected.
A finding in exactly two phases is not SYSTEMIC.

**CONFIRMED** = a Phase 4 or Phase 5 finding that matches a topology violation from Phases 1-3.
Match is structural: same component, same access pattern, same contract term, or same state surface.

**RUNTIME ANOMALY** = a Phase 4 or Phase 5 finding with no matching topology violation in Phases 1-3.
Unexpected behavior that the static topology did not predict.

---

## PHASE 0 -- Topology census

**Components in scope:** [all named services, modules, APIs, schemas, queues from spec]

**Shared state surfaces:** [all databases, caches, event buses, config objects read/written
by multiple components -- the blast-radius amplifiers]

**Downstream callers:** [all components that depend on outputs from this system]

**Role-resource inventory:** [all roles and the resources each may access]

**Pre-declared contracts:** [all explicit producer/consumer contract terms in spec --
the CONFIRMED baseline for Phases 4-5]

Every blast radius claim must name a specific entry from this census.

---

## PHASE 1 -- trace-permissions

| Role | Resource | Action | Permitted? | Escalation path? | Shared state surface involved? |
|------|----------|--------|------------|------------------|-------------------------------|

Track which findings from this phase involve shared state surfaces -- they set the blast radius
ceiling for downstream phases.

If clean: "trace-permissions: clean -- no escalation paths detected."

EXIT CRITERIA: All role-resource pairs evaluated.
State: "trace-permissions complete: [N] pairs, [N] escalation paths, [N] involving shared state."

---

## PHASE 2 -- trace-state

| From state | To state | Trigger | Invariant | Invariant holds? | Phase 1 escalation connected? |
|------------|----------|---------|-----------|------------------|-------------------------------|

If Phase 1 escalation connected = yes: finding is CONFIRMED.
Note Phase 1 connection in each row -- this is evidence for SYSTEMIC classification later.

If clean: "trace-state: clean -- all invariants hold."

EXIT CRITERIA: All state transitions and shared state surfaces evaluated.
State: "trace-state complete: [N] transitions, [N] violations, [N] CONFIRMED from Phase 1."

---

## PHASE 3 -- trace-contract

| Producer | Consumer | Contract term | Expected | Actual | Mismatch? | Phase 1/2 connected? |
|----------|----------|---------------|----------|--------|-----------|----------------------|

If Phase 1/2 connected = yes: mark CONFIRMED.
Note Phase 1/2 connection -- evidence for SYSTEMIC classification.

If clean: "trace-contract: clean -- all contracts verified."

EXIT CRITERIA: All producer/consumer pairs evaluated.
State: "trace-contract complete: [N] pairs, [N] mismatches, [N] CONFIRMED."

---

## PHASE 4 -- flow-lifecycle

| Phase | Entry contract | Exit contract | Exception path | Exception handled? | Phase 1-3 match? | CONFIRMED / RUNTIME ANOMALY |
|-------|----------------|---------------|----------------|--------------------|-----------------|-----------------------------|

Name the specific Phase 1-3 finding that makes a CONFIRMED classification valid.
For RUNTIME ANOMALY, state why no Phase 1-3 entry predicted this.

If clean: "flow-lifecycle: clean -- all lifecycle transitions verified."

EXIT CRITERIA: All lifecycle phases evaluated.
State: "flow-lifecycle complete: [N] phases, [N] failures, [N] CONFIRMED, [N] RUNTIME ANOMALY."

---

## PHASE 5 -- flow-trigger

| Trigger | Expected fire order | Actual fire order | Race condition? | Phase 1 role? | Phase 3 contract affected? | CONFIRMED / RUNTIME ANOMALY |
|---------|---------------------|-------------------|-----------------|---------------|---------------------------|------------------------------|

Track Phase 1 and Phase 3 connections per trigger -- these will determine SYSTEMIC phase lists.

If clean: "flow-trigger: clean -- all triggers verified."

EXIT CRITERIA: All triggers and activating events evaluated.
State: "flow-trigger complete: [N] triggers, [N] failures, [N] CONFIRMED, [N] RUNTIME ANOMALY."

---

## CALIBRATION BLOCK

Step 1 -- Evidence inventory:
List every finding from Phases 1-5. Verify each names a census component in its blast radius claim.
Any finding that cannot name a census component: revise or discard.

Step 2 -- Blast radius ceiling check:
For each finding involving a Phase 1 escalation role or Phase 0 shared state surface:
verify blast radius = wide. Revise any finding that understates.

Step 3 -- CONFIRMED/RUNTIME ANOMALY review:
For every Phase 4-5 finding: trace to a specific Phase 1-3 entry or confirm RUNTIME ANOMALY.
List all reclassifications.

Step 4 -- SYSTEMIC identification with phase enumeration:
For every finding that appears in two or more phases, list the phases by name.
Apply SYSTEMIC label if three or more phases.
REQUIRED: Every SYSTEMIC finding must state the corroborating phases as a list.
Format: "SYSTEMIC: yes -- phases: [phase-name-1], [phase-name-2], [phase-name-3]"
Count is not enough. Phase names are required. Binary flag without list = invalid.

Step 5 -- Clean zones:
List every Phase 0 census component with no findings across all five phases.

---

## CONSOLIDATE

ONE unified report. No phase concatenation.

**Ranked findings (blast radius descending):**

Tiebreaker:
1. Blast radius: wide > medium > narrow
2. CONFIRMED > RUNTIME ANOMALY
3. SYSTEMIC > isolated (SYSTEMIC finding must carry phase list, not just flag)

Atomic finding block (required format for every finding):

---
**Finding [N]**
1. Name: [finding name]
2. Source phase: [phase name]
3. Blast radius: [wide | medium | narrow] -- [named census components]
4. Severity at epicenter: [high | med | low]
5. SYSTEMIC: [yes -- phases: [comma-separated corroborating phase names] | no]
6. Classification: [CONFIRMED | RUNTIME ANOMALY | isolated]
7. What must change: [one concrete targeted fix direction]
---

**Spec gaps:** [list each, or "none detected"]

**Contract violations:** [list each, or "none detected"]

**Privilege escalation paths:** [list each, or "none detected"]

**Clean zones:** [components verified clean across all phases]

---

## VERDICT

One paragraph. Name the widest-blast-radius finding by its Phase 0 census component name.
State CONFIRMED or RUNTIME ANOMALY.
If SYSTEMIC: enumerate the corroborating phases (e.g., "SYSTEMIC across trace-permissions,
trace-contract, and flow-trigger").
Name the assumption the team held that this simulation invalidated.
Conclude: proceed, proceed with conditions, or halt.
```

---

## V-03 -- State-anchor role sequence (single axis)
**Axis:** Role sequence -- trace-state runs first (Phase 1) to map shared state topology before any access control, contract, or runtime analysis; every subsequent phase inherits blast radius ceiling from Phase 1 shared state surfaces
**Hypothesis:** Shared state surfaces are the primary blast-radius amplifiers. Running trace-state first establishes the state topology -- which surfaces exist, which invariants govern them, which transitions are risky -- before any role, contract, or lifecycle analysis. This may pre-classify blast radius for downstream findings more reliably than a permissions-first or contract-first approach, because state violations are the propagation mechanism even when permissions are correctly enforced. The inertia this displaces is the assumption that access controls alone define the blast radius ceiling.

```
Simulate the technical behavior of: {{topic}}

---

## DEFINITIONS

Blast radius = how broadly a failure propagates through the system.
Wide: corrupts shared state, breaks downstream callers, or blocks multiple user roles simultaneously.
Medium: two or more components affected; no shared state surface reached.
Narrow: failure contained within one component boundary.

Severity = damage depth at the epicenter (high / med / low). Independent of blast radius.
Report as separate labeled fields. Never merge.

State-anchor rationale: shared state surfaces are the primary blast-radius amplifiers. A failure
that touches a shared state surface propagates to every downstream reader or writer of that surface.
Establishing the state topology first pre-classifies blast radius by propagation structure before any
access or contract analysis runs. Any Phase 2-5 finding involving a Phase 1 shared state surface
inherits wide blast radius by topology.

CONFIRMED = a Phase 3-5 finding that matches a state violation or shared state surface from Phase 1.
RUNTIME ANOMALY = a Phase 3-5 finding with no connection to Phase 1 state topology.

---

## PHASE 0 -- Topology census

**Components in scope:** [all named services, modules, APIs, schemas, queues from spec]

**Shared state surfaces:** [all databases, caches, event buses, config objects read/written by
multiple components -- PRIMARY FOCUS of Phase 1; these are the blast-radius amplifiers]

**Downstream callers:** [all components that depend on outputs from this system]

**Role-resource inventory:** [all roles and the resources each may access]

**Pre-declared contracts:** [all explicit producer/consumer contract terms in spec]

Every blast radius claim must name a specific entry from this census.

---

## PHASE 1 -- trace-state [HIGH DEPTH]

Map the shared state topology before any access or contract analysis runs.
Evaluate every state transition. Prioritize transitions that involve Phase 0 shared state surfaces.

| From state | To state | Trigger | Invariant | Invariant holds? | Shared state surface? | Blast radius ceiling |
|------------|----------|---------|-----------|------------------|-----------------------|---------------------|

Shared state surface = yes if this transition reads from or writes to a Phase 0 shared state entry.
If shared state surface = yes and invariant holds = no: blast radius ceiling = wide.
This ceiling propagates to all downstream phases for any finding involving this surface.

If no violations: "trace-state: clean -- all invariants hold, no shared state violations."

EXIT CRITERIA: All state transitions evaluated, all Phase 0 shared state surfaces covered.
State: "trace-state complete: [N] transitions, [N] violations, [N] involving shared state surfaces."

---

## PHASE 2 -- trace-permissions

Map which roles can reach the state surfaces and violations identified in Phase 1.

| Role | Resource | Action | Permitted? | Phase 1 shared state surface? | Escalation path? | Blast radius (Phase 1 ceiling applied?) |
|------|----------|--------|------------|-------------------------------|------------------|----------------------------------------|

Phase 1 shared state = yes if this role-resource pair involves a Phase 1 shared state surface.
If yes: blast radius ceiling = wide (inherited from Phase 1 topology).
Escalation path to a Phase 1 shared state violation: classify CONFIRMED.

If no escalation paths: "trace-permissions: clean -- no unauthorized access to state surfaces."

EXIT CRITERIA: All role-resource pairs evaluated.
State: "trace-permissions complete: [N] pairs, [N] escalation paths, [N] connecting to Phase 1 surfaces."

---

## PHASE 3 -- trace-contract

Verify what crosses component boundaries, grounded in the state-permission topology.

| Producer | Consumer | Contract term | Expected | Actual | Mismatch? | Phase 1 state surface? | Phase 2 escalation? | CONFIRMED? |
|----------|----------|---------------|----------|--------|-----------|------------------------|---------------------|------------|

Phase 1 state surface or Phase 2 escalation connection = yes: classify CONFIRMED.

If no mismatches: "trace-contract: clean -- all contracts verified."

EXIT CRITERIA: All producer/consumer pairs evaluated.
State: "trace-contract complete: [N] pairs, [N] mismatches, [N] CONFIRMED."

---

## PHASE 4 -- flow-lifecycle

Observe runtime lifecycle behavior within the state-permission-contract envelope.

| Phase | Entry contract | Exit contract | Exception path | Exception handled? | Phase 1-3 topology match? | CONFIRMED / RUNTIME ANOMALY |
|-------|----------------|---------------|----------------|--------------------|--------------------------|-----------------------------|

CONFIRMED = matches a specific Phase 1 state violation, Phase 2 escalation, or Phase 3 mismatch.
RUNTIME ANOMALY = no Phase 1-3 topology match.

If clean: "flow-lifecycle: clean -- all lifecycle transitions verified."

EXIT CRITERIA: All lifecycle phases evaluated.
State: "flow-lifecycle complete: [N] phases, [N] failures, [N] CONFIRMED, [N] RUNTIME ANOMALY."

---

## PHASE 5 -- flow-trigger [HIGH DEPTH]

Evaluate every trigger and activating event against the state topology from Phase 1.

| Trigger | Expected fire order | Actual fire order | Race condition? | Phase 1 shared state involved? | Phase 2 role involved? | CONFIRMED / RUNTIME ANOMALY |
|---------|---------------------|-------------------|-----------------|-------------------------------|------------------------|------------------------------|

Phase 1 shared state involved = yes if a race condition or out-of-order trigger corrupts a
Phase 1 shared state surface. If yes: blast radius = wide (inherits from Phase 1 ceiling).

If clean: "flow-trigger: clean -- all triggers verified."

EXIT CRITERIA: All triggers evaluated.
State: "flow-trigger complete: [N] triggers, [N] failures, [N] involving Phase 1 surfaces."

---

## CALIBRATION BLOCK

Step 1 -- Blast radius re-grounding:
For each finding: does it touch a Phase 1 shared state surface (directly or through a Phase 2 role
or Phase 3 contract)? If yes and blast radius != wide, upgrade to wide. List every revision.

Step 2 -- CONFIRMED/RUNTIME ANOMALY review:
For each Phase 3-5 finding: trace to a specific Phase 1 state violation or Phase 2 escalation path.
If match found: confirm CONFIRMED. If no match: confirm RUNTIME ANOMALY.
List all reclassifications.

Step 3 -- SYSTEMIC identification:
For every finding appearing in two or more phases, list the phases by name.
Mark SYSTEMIC if in three or more phases.
Format: "SYSTEMIC: yes -- phases: [phase-name-1], [phase-name-2], [phase-name-3]"

Step 4 -- Tiebreaker verification:
Confirm ranking order: blast radius wide > medium > narrow, then CONFIRMED > RUNTIME ANOMALY,
then SYSTEMIC > isolated.

Step 5 -- Clean zones:
List every Phase 0 census component with no findings across all five phases.

---

## CONSOLIDATE

ONE unified report. No phase concatenation.

**Ranked findings (blast radius order, Phase 1 ceiling pre-applied, wide first):**

Tiebreaker:
1. Blast radius: wide > medium > narrow (Phase 1 state-surface ceiling pre-applied)
2. CONFIRMED > RUNTIME ANOMALY
3. SYSTEMIC > isolated

---
**Finding [N]**
1. Name: [finding name]
2. Source phase: [phase name]
3. Blast radius: [wide | medium | narrow] -- [named Phase 0 census components]
4. Severity at epicenter: [high | med | low]
5. SYSTEMIC: [yes -- phases: [phase list] | no]
6. Classification: [CONFIRMED | RUNTIME ANOMALY | isolated]
7. What must change: [one concrete fix direction]
---

**Spec gaps:** [list each, or "none detected"]

**Contract violations:** [list each, or "none detected"]

**Shared state violations:** [list each, or "none detected"]

**Clean zones:** [components verified clean across all phases]

---

## VERDICT

One paragraph. Name the finding touching the widest shared state surface by its Phase 0 census name.
State CONFIRMED or RUNTIME ANOMALY. If SYSTEMIC, enumerate the corroborating phases.
Name the assumption the team held about shared state safety that this simulation invalidated.
Conclude: proceed, proceed with conditions, or halt.
```

---

## V-04 -- Q1-Qn calibration + permissions-anchor (combination)
**Axes:** Role sequence (permissions-anchor) + Calibration form (Q1-Qn interrogative) + SYSTEMIC phase enumeration (C-21) + atomic finding blocks (C-19) + tiebreaker protocol (C-20)
**Hypothesis:** V-01 R5 scored 89/90 -- the only gap was C-18 (no Q1-Qn calibration). This variation takes V-01's permissions-anchor structure verbatim and replaces the step-block calibration with Q1-Q5 interrogative form. Adding SYSTEMIC phase enumeration (C-21) in the same pass targets the second new v5 criterion. Expected result: the first variation to pass all 13 aspirational criteria, scoring 90.

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

**Permissions-anchor rationale:** Trace-permissions runs first because the access surface determines
the blast radius ceiling for all subsequent phases. Any finding involving a Phase 1 escalated role
inherits wide blast radius mechanically, before any contract or lifecycle analysis.

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

## PHASE 1 -- trace-permissions

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

## PHASE 4 -- flow-lifecycle

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

## PHASE 5 -- flow-trigger

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

Q4: Does the blast radius ceiling from Phase 1 hold throughout?
For every finding involving a Phase 1 escalation role: verify blast radius = wide.
Any finding involving a Phase 1 escalation role with blast radius below wide is a calibration
error. Revise and explain each case.

Q5: Would any finding below have shipped without this simulation?
For each wide-blast-radius finding: name the assumption it would have bypassed
(undocumented privilege, implicit contract, tacit lifecycle expectation, missing spec coverage,
assumed access boundary). This is the inertia question -- what would the team have believed?

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

## V-05 -- Full 13-criterion coverage attempt (combination)
**Axes:** Permissions-anchor + DEPTH asymmetry + CONFIRMED/RUNTIME ANOMALY throughout all runtime phases + Q1-Qn interrogative calibration + SYSTEMIC phase enumeration + atomic finding blocks + tiebreaker protocol + per-phase exit criteria
**Hypothesis:** V-04 targets C-18 and C-21 on top of the V-01 R5 base. V-05 adds DEPTH asymmetry (C-20 from prior rounds, now targeting new C-20 tiebreaker), maximizes per-phase typed schemas (C-12), and ensures every new v5 criterion (C-19 atomic blocks, C-20 tiebreaker, C-21 SYSTEMIC phase list) is structurally enforced in definitions, execution, calibration, and consolidation -- not just present in one place. The goal is to design a prompt where every aspirational criterion has at least two reinforcement points so no single omission causes a criterion to fail.

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

**Permissions-anchor rationale:** Trace-permissions runs first (Phase 1) because the access surface
determines the blast radius ceiling for all subsequent phases. A finding involving a Phase 1
escalated role inherits wide blast radius mechanically, before any lifecycle or contract analysis.
This pre-classification is structural, not retrospective.

**Tiebreaker protocol (apply in ranked findings order):**
1. Blast radius: wide > medium > narrow
2. CONFIRMED > RUNTIME ANOMALY
3. SYSTEMIC > isolated
Without explicit tiebreaker rules, ranking is arbitrary for tied findings.

---

## PHASE 0 -- Topology census

**Components in scope:** [all named services, modules, APIs, schemas, queues, event types from spec]

**Shared state surfaces:** [all databases, caches, event buses, config objects written by more than
one component -- the blast-radius amplifiers; every blast radius ceiling check uses this list]

**Downstream callers:** [all components whose behavior depends on outputs from the system under simulation]

**Role-resource inventory:** [all roles and the resources each may access -- the Phase 1 input surface]

**Pre-declared contracts:** [all explicit producer/consumer contract terms in spec -- the CONFIRMED
baseline; a Phase 4-5 finding that matches a pre-declared contract term is CONFIRMED by definition]

This census is the reference inventory for all blast radius claims throughout the campaign.
A finding that cannot name a specific census entry must be returned to the spec before recording.

---

## PHASE 1 -- trace-permissions [HIGH DEPTH]

Establish the access surface. Evaluate every role-resource-action triplet from the Phase 0 inventory.
Minimum expectation: every role and every resource in Phase 0 appears at least once in this table.

| Role | Resource | Action | Permitted? | Escalation path? | Shared state surface? | Blast radius ceiling |
|------|----------|--------|------------|------------------|----------------------|---------------------|

Escalation path = yes when a role reaches a resource through indirect means (delegation,
inheritance, event chain, missing boundary check).
Escalation path = yes AND shared state surface = yes: blast radius ceiling = wide.
This ceiling holds for all downstream findings involving this role.

If no escalation paths: "trace-permissions: clean -- no escalation paths detected."

EXIT CRITERIA: All role-resource pairs from Phase 0 inventory evaluated. No pairs deferred.
State: "trace-permissions complete: [N] pairs evaluated, [N] escalation paths, [N] involving shared state."

---

## PHASE 2 -- trace-state [AS-NEEDED DEPTH]

Map state reachability through the access surface from Phase 1. Run if Phase 0 surfaces shared state
objects with non-trivial state machines; skip with explicit statement if state is trivial.

| From state | To state | Trigger | Invariant | Invariant holds? | Phase 1 escalation connected? | Blast radius ceiling inherited? |
|------------|----------|---------|-----------|------------------|-------------------------------|--------------------------------|

Phase 1 escalation connected = yes if the trigger or state surface involves a Phase 1 escalation role.
If connected = yes: blast radius ceiling = wide (inherited from Phase 1).

If clean: "trace-state: clean -- all invariants hold."
If skipped: "trace-state: skipped -- [reason]."

EXIT CRITERIA: All shared state surfaces from Phase 0 evaluated (or skip justified).
State: "trace-state complete: [N] transitions, [N] violations, [N] connected to Phase 1."

---

## PHASE 3 -- trace-contract [MEDIUM DEPTH]

Verify what crosses role and component boundaries.

| Producer | Consumer | Contract term | Expected | Actual | Mismatch? | Phase 1/2 topology match? | CONFIRMED? |
|----------|----------|---------------|----------|--------|-----------|--------------------------|------------|

Phase 1/2 topology match = yes if this contract involves a Phase 1 escalation role or
Phase 2 state violation surface. If match = yes: mark CONFIRMED here, not waiting for calibration.

If clean: "trace-contract: clean -- all contracts verified."

EXIT CRITERIA: All producer/consumer pairs evaluated.
State: "trace-contract complete: [N] pairs, [N] mismatches, [N] CONFIRMED."

---

## PHASE 4 -- flow-lifecycle [MEDIUM DEPTH]

Observe runtime behavior within the permission/state/contract envelope.

| Phase | Entry contract | Exit contract | Exception path | Exception handled? | Phase 1-3 topology match? | CONFIRMED / RUNTIME ANOMALY |
|-------|----------------|---------------|----------------|--------------------|--------------------------|-----------------------------|

CONFIRMED = matches a specific Phase 1 escalation, Phase 2 state violation, or Phase 3 mismatch.
Name the matching finding in the CONFIRMED field.
RUNTIME ANOMALY = no matching topology entry. State explicitly why no Phase 1-3 entry predicts this.

If clean: "flow-lifecycle: clean -- all lifecycle transitions verified."

EXIT CRITERIA: All lifecycle phases evaluated.
State: "flow-lifecycle complete: [N] phases, [N] failures, [N] CONFIRMED, [N] RUNTIME ANOMALY."

---

## PHASE 5 -- flow-trigger [HIGH DEPTH]

Evaluate every trigger and every activating event. If fewer than three triggers exist, document all.
Minimum expectation: every event source, activation condition, and race condition vector is evaluated.

| Trigger | Expected fire order | Actual fire order | Race condition? | Phase 1 escalation role? | Phase 0 shared state affected? | CONFIRMED / RUNTIME ANOMALY |
|---------|---------------------|-------------------|-----------------|--------------------------|-------------------------------|------------------------------|

Phase 1 escalation role = yes if the trigger involves a role from Phase 1's escalation list.
If yes: blast radius = wide (inherits from Phase 1 access surface ceiling).

If clean: "flow-trigger: clean -- all triggers verified."

EXIT CRITERIA: All triggers and activating events evaluated. No triggers deferred.
State: "flow-trigger complete: [N] triggers, [N] failures, [N] CONFIRMED, [N] RUNTIME ANOMALY."

---

## CALIBRATION BLOCK

Q1: Does any finding's blast radius change when mapped against Phase 0 shared state surfaces?
For each finding with blast radius = medium or narrow: does the affected component read from or
write to a Phase 0 shared state surface? If yes, upgrade to wide.
Also verify: every finding involving a Phase 1 escalation role has blast radius = wide.
List every revision.

Q2: Do any Phase 4-5 findings match topology violations from Phases 1-3?
For each Phase 4-5 finding: identify the specific Phase 1, 2, or 3 entry it connects to.
If match found: confirm CONFIRMED (or reclassify if previously marked RUNTIME ANOMALY).
If no match: confirm RUNTIME ANOMALY. List all reclassifications with the topology check result.

Q3: Which findings appear in three or more phases?
List every finding corroborated across phases. Mark SYSTEMIC if three or more phases.
REQUIRED: enumerate all corroborating phase names for every SYSTEMIC finding.
Format: "SYSTEMIC: yes -- phases: [phase-name-1], [phase-name-2], [phase-name-3]"
A count of phases is not sufficient. Phase names are required. Binary flag = invalid.

Q4: Did HIGH-DEPTH phases achieve minimum expectation?
Phase 1 (trace-permissions): does every role and resource from Phase 0 appear in the table?
Phase 5 (flow-trigger): does every trigger and activating event appear?
If any item was deferred or skipped, state why and whether the omission affects ranking.

Q5: Would any finding below have shipped without this simulation?
For each wide-blast-radius finding: name the assumption it would have bypassed
(undocumented privilege, implicit contract, tacit lifecycle expectation, missing spec coverage,
assumed access boundary). This is the inertia question -- what would the team have believed
without this evidence? The verdict will name the finding with the most dangerous displaced assumption.

---

## CONSOLIDATE

Write ONE report. Do not concatenate five phase outputs. Synthesis, not a log.

**Ranked findings (blast radius descending, full tiebreaker protocol applied):**

Tiebreaker protocol (apply in order, no exceptions):
1. Blast radius: wide > medium > narrow
2. CONFIRMED > RUNTIME ANOMALY (confirmed findings rank above unconfirmed of equal blast radius)
3. SYSTEMIC > isolated (SYSTEMIC findings rank above isolated of equal blast radius and confirmation tier)

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

## Axis summary

| Variation | Axis | Key new patterns targeted | Prior best analog |
|-----------|------|--------------------------|-------------------|
| V-01 | Q1-Qn calibration (single) | C-18 | R5 V-01 base + interrogative calibration |
| V-02 | SYSTEMIC phase enumeration (single) | C-21 | R5 V-05 base + mandatory phase list |
| V-03 | State-anchor sequence (single) | unexplored execution order | none (new axis) |
| V-04 | Q1-Qn + permissions-anchor (combination) | C-18, C-21, C-20, C-19 | R5 V-01 + calibration upgrade |
| V-05 | Full 13-criterion coverage (combination) | all new v5 criteria + depth asymmetry | R5 V-05 + Q1-Qn + phase lists |

**Expected ceiling:** V-04 and V-05 are designed to pass all 13 aspirational criteria.
V-01 closes the R5 universal gap (C-18) while preserving the R5 V-01 score floor.
V-02 closes C-21 with minimal structural change.
V-03 tests whether state-anchor sequence exposes a different blast-radius topology than permissions-anchor.
