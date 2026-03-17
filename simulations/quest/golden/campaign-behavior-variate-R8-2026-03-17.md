# Quest Variations — campaign-behavior (R8)
**Skill:** campaign-behavior
**Rubric:** v6 (C-01–C-23)
**Round:** 8
**Date:** 2026-03-17

---

## Axes explored in R8

Single-axis (unexplored as of R7):
- **DEPTH asymmetry labeling** — anchor phases (Ph1, Ph2) carry inline `[ANCHOR: ...]` tags in
  their headers; execution phases (Ph3–Ph5) carry none. Targets the R7 Signal 1 excellence pattern.
- **Q6 sequence integrity gate** — adds a sixth calibration question: "Did execution order deliver
  its pre-classification guarantee? Were any blast radius values revised post-hoc?" Targets R7
  Signal 2 excellence pattern.
- **Propagation chain enumeration** — extends field 3 of each atomic finding block to name every
  census component in the propagation path as an ordered chain (A → B → C). New axis not tested
  in any prior round.

Combinations (V-04, V-05):
- **V-04:** DEPTH asymmetry + Q6 sequence integrity gate
- **V-05:** Full coverage — DEPTH asymmetry + Q6 + propagation chain + maximum structural
  reinforcement of all 15 aspirational criteria

---

## V-01 — DEPTH asymmetry labeling
**Axis:** Phase headers — anchor phases (Ph1 trace-state, Ph2 trace-permissions) carry inline
`[ANCHOR: ...]` tags naming their pre-classification guarantee; execution phases (Ph3–Ph5) carry
no such tag. The asymmetry makes the structural dependency chain scannable from headers alone.
**Hypothesis:** DEPTH asymmetry labeling was identified as a new excellence signal in R7 V-03.
All other structure is identical to R7 V-01 (which scored 90/90). If this signal contributes an
independent structural improvement, it should hold 90/90 on v6 while demonstrating a testable
pattern for a potential C-24. If not, it scores identically to R7 V-01 with no regression.

```
Simulate the technical behavior of: {{topic}}

---

## DEFINITIONS

Blast radius = how broadly a failure propagates through the system.
Wide: corrupts shared state, breaks downstream callers, or blocks multiple user roles simultaneously.
Medium: two or more components affected; no shared state surface reached.
Narrow: failure contained within one component boundary.

Severity = damage depth at the epicenter (high / med / low).
These are independent dimensions. Never merge them into a single "impact" field.
Report both as separate labeled fields in every finding.

SYSTEMIC = a finding corroborated across three or more phases.
Required format: "SYSTEMIC: yes — phases: [phase-name-1], [phase-name-2], [phase-name-3]"
Binary "SYSTEMIC: yes" without a phase list is not valid and will be rejected.

CONFIRMED = a Phase 4 or Phase 5 finding that matches a topology violation from Phases 1–3.
Match is structural: same component, same access pattern, same contract term, or same state surface.
Name the matching Phase 1–3 finding when classifying CONFIRMED.

RUNTIME ANOMALY = a Phase 4 or Phase 5 finding with no matching topology violation in Phases 1–3.

Tiebreaker protocol (applies when two or more findings share the same blast radius classification):
1. Blast radius descending (wide > medium > narrow)
2. CONFIRMED > RUNTIME ANOMALY
3. SYSTEMIC > isolated
State this protocol before the consolidated ranking. If no ties exist, state that explicitly.

---

## PHASE 0 — Topology census

Before any sub-skill runs, record the system vocabulary explicitly.

**Components in scope:** [list every named service, module, API, schema, queue from the spec]

**Shared state surfaces:** [databases, caches, event buses, configuration objects read or written by
multiple components — these are the blast-radius amplifiers]

**Downstream callers:** [every component whose behavior depends on the system under simulation]

**Role-resource inventory:** [every role and the resources it may access]

**Pre-declared contracts:** [every producer/consumer contract term the spec explicitly commits to —
these form the CONFIRMED classification baseline for Phases 4–5]

Every blast radius claim below must name a specific entry from this census.
If a finding cannot name a census item, return to the spec before recording the finding.

---

## PHASE 1 — trace-state [ANCHOR: state topology pre-classifies blast radius candidates for all downstream phases]

trace-state runs first. State topology — which states are shared, which transitions are multi-party,
which invariants span components — pre-classifies blast radius candidates before contract, access, or
flow analysis begins. Downstream sub-skills inherit this pre-built blast radius map rather than
constructing one post-hoc.

Map every state transition in scope against the shared state surfaces from Phase 0.

| From state | To state | Trigger | Invariant | Invariant holds? | Shared state surface? | Blast radius candidate |
|------------|----------|---------|-----------|------------------|-----------------------|------------------------|

For each shared state surface = yes: record blast radius candidate as wide. This classification is
locked for downstream phases — it does not require re-derivation.

If no violations: "trace-state: clean — all invariants verified."

EXIT CRITERIA: All state transitions and invariants from the spec evaluated. No transitions deferred.
State: "trace-state complete: [N] transitions evaluated, [N] violations found, [N] pre-classified wide."

---

## PHASE 2 — trace-permissions [ANCHOR: privilege boundary classification anchors flow blast radius assessment]

trace-permissions runs second, before all flow sub-skills. Privilege boundary classification must
precede flow analysis because flow violations that cross a privilege boundary are SYSTEMIC by
definition. Without this anchor, flow sub-skills may understate blast radius.

Enumerate every role-resource-action triplet in scope.

| Role | Resource | Action | Permitted? | Escalation path? | Phase 1 state surface involved? | Blast radius ceiling |
|------|----------|--------|------------|------------------|---------------------------------|----------------------|

If Phase 1 state surface involved = yes and escalation path = yes: blast radius ceiling = wide (compound anchor hit).

If no escalation paths: "trace-permissions: clean — all role-resource pairs verified, no escalation paths detected."

EXIT CRITERIA: All role-resource pairs in scope evaluated. No pairs deferred.
State: "trace-permissions complete: [N] pairs evaluated, [N] escalation paths found, [N] compound anchor hits."

---

## PHASE 3 — trace-contract

Verify what crosses role and component boundaries.
Inherit the blast radius pre-classification map from Phases 1–2.

| Producer | Consumer | Contract term | Expected | Actual | Mismatch? | Phase 1/2 topology match? |
|----------|----------|---------------|----------|--------|-----------|--------------------------|

Phase 1/2 topology match = yes if this contract involves a Phase 1 state violation surface or a
Phase 2 escalation role. If match = yes: classify CONFIRMED.

If clean: "trace-contract: clean — all contracts verified."

EXIT CRITERIA: All producer/consumer pairs in scope evaluated. No pairs deferred.
State: "trace-contract complete: [N] pairs evaluated, [N] mismatches found, [N] CONFIRMED."

---

## PHASE 4 — flow-lifecycle

Observe runtime behavior within the permission/state/contract envelope established by Phases 1–3.

| Phase | Entry contract | Exit contract | Exception path | Exception handled? | Phase tag | CONFIRMED / RUNTIME ANOMALY |
|-------|----------------|---------------|----------------|--------------------|-----------|-----------------------------|

Phase tag = the lifecycle phase in which the violation occurs (e.g., INIT, ACTIVE, SUSPENDED, TERMINAL).
CONFIRMED = this finding matches a violation from Phases 1–3. Name the matching finding.
RUNTIME ANOMALY = no matching topology violation in Phases 1–3.

If clean: "flow-lifecycle: clean — all lifecycle transitions verified."

EXIT CRITERIA: All lifecycle phases evaluated. No phases deferred.
State: "flow-lifecycle complete: [N] phases, [N] failures, [N] CONFIRMED, [N] RUNTIME ANOMALY."

---

## PHASE 5 — flow-trigger

Evaluate every trigger and every activating event in scope.

| Trigger | Expected fire order | Actual fire order | Race condition? | Phase 2 escalation role? | Phase tag | CONFIRMED / RUNTIME ANOMALY |
|---------|---------------------|-------------------|-----------------|--------------------------|-----------|------------------------------|

Phase 2 escalation role = yes if this trigger involves a role from Phase 2's escalation list.
If yes: blast radius = wide (inherits Phase 2 access surface ceiling).

If clean: "flow-trigger: clean — all triggers verified."

EXIT CRITERIA: All triggers and activating events evaluated. No triggers deferred.
State: "flow-trigger complete: [N] triggers, [N] failures, [N] CONFIRMED, [N] RUNTIME ANOMALY."

---

## CALIBRATION BLOCK

Q1: Does any finding's blast radius change when mapped against Phase 0 shared state surfaces?
For each finding with blast radius = medium or narrow: does the affected component read from or
write to a Phase 0 shared state surface? If yes, upgrade to wide. List every revision.

Q2: Do any Phase 4–5 findings match topology violations from Phases 1–3?
For each Phase 4–5 finding: identify the specific Phase 1 state violation, Phase 2 escalation path,
or Phase 3 contract mismatch it connects to. If match found: confirm CONFIRMED. If no match: confirm
RUNTIME ANOMALY. List all reclassifications.

Q3: Which findings appear in three or more phases?
List every finding corroborated across phases. Mark SYSTEMIC if three or more phases.
For every SYSTEMIC finding, enumerate the corroborating phases:
"SYSTEMIC: yes — phases: [phase-name-1], [phase-name-2], [phase-name-3]"
Do not use binary SYSTEMIC flags. The phase list is required.

Q4: Does the blast radius pre-classification map from Phases 1–2 hold throughout?
For every finding involving a Phase 2 escalation role or Phase 1 shared state surface: verify blast
radius = wide. Any finding below wide for a pre-classified component is a calibration error.
Revise and explain.

Q5: Would any finding below have shipped without this simulation?
For each wide-blast-radius finding: name the assumption it would have bypassed (undocumented
privilege, implicit contract, tacit lifecycle expectation, missing spec coverage). This is the
inertia question — what would the team have assumed?

---

## CONSOLIDATE

Write ONE report. Do not concatenate five phase outputs.

Tiebreaker protocol: (1) Blast radius descending, (2) CONFIRMED > RUNTIME ANOMALY,
(3) SYSTEMIC > isolated. State whether any ties were encountered and how they were resolved.

**Ranked findings (calibrated blast radius order, wide first):**

For each finding, use this atomic block exactly:

---
**Finding [N]**
1. Name: [finding name or short description]
2. Source phase: [phase name]
3. Blast radius: [wide | medium | narrow] — [named census components in propagation path]
4. Severity at epicenter: [high | med | low]
5. SYSTEMIC: [yes — phases: [comma-separated phase list] | no]
6. Classification: [CONFIRMED | RUNTIME ANOMALY | isolated]
7. What must change: [one concrete fix direction in spec, contract, or implementation]
---

**Spec gaps:** [list each gap with missing-clause citation, or "none detected"]

**Contract violations:** [list each with producer and consumer named, or "none detected"]

**Privilege escalation paths:** [list each, or "none detected"]

**Clean zones:** [Phase 0 census components with no findings across all five phases]

---

## VERDICT

One paragraph. Name the finding with the widest blast radius by its Phase 0 census component name.
State CONFIRMED or RUNTIME ANOMALY. If SYSTEMIC, list the corroborating phases.
State the assumption the team would have carried into implementation had this simulation not run.
Conclude: proceed, proceed with conditions, or halt.
```

---

## V-02 — Q6 sequence integrity gate
**Axis:** Calibration block extension — a sixth calibration question is added after Q5. Q6 is
self-referential: it asks whether the execution sequence (Ph1 before Ph2 before Ph3–5) actually
delivered its pre-classification guarantee. Zero post-hoc blast radius revisions = anchor held.
Any revision = anchor was violated and the sequence claim must be restated.
**Hypothesis:** Q6 is the R7 Signal 2 excellence pattern. All other structure is identical to R7
V-01. Q6 converts the C-22/C-23 structural design decisions into a runtime-verifiable assertion —
if the anchor sequence did its job, Q6 should report zero revisions. This tests whether the
self-validating question adds signal beyond what Q4 already covers (Q4 checks ceiling inheritance;
Q6 checks whether any revision happened post-hoc that would not have occurred under a different
sequence).

```
Simulate the technical behavior of: {{topic}}

---

## DEFINITIONS

Blast radius = how broadly a failure propagates through the system.
Wide: corrupts shared state, breaks downstream callers, or blocks multiple user roles simultaneously.
Medium: two or more components affected; no shared state surface reached.
Narrow: failure contained within one component boundary.

Severity = damage depth at the epicenter (high / med / low).
These are independent dimensions. Never merge them into a single "impact" field.
Report both as separate labeled fields in every finding.

SYSTEMIC = a finding corroborated across three or more phases.
Required format: "SYSTEMIC: yes — phases: [phase-name-1], [phase-name-2], [phase-name-3]"
Binary "SYSTEMIC: yes" without a phase list is not valid and will be rejected.

CONFIRMED = a Phase 4 or Phase 5 finding that matches a topology violation from Phases 1–3.
Name the matching Phase 1–3 finding when classifying CONFIRMED.

RUNTIME ANOMALY = a Phase 4 or Phase 5 finding with no matching topology violation in Phases 1–3.

Tiebreaker protocol (applies when two or more findings share the same blast radius classification):
1. Blast radius descending (wide > medium > narrow)
2. CONFIRMED > RUNTIME ANOMALY
3. SYSTEMIC > isolated
State this protocol before the consolidated ranking. If no ties exist, state that explicitly.

---

## PHASE 0 — Topology census

Before any sub-skill runs, record the system vocabulary explicitly.

**Components in scope:** [list every named service, module, API, schema, queue from the spec]

**Shared state surfaces:** [databases, caches, event buses, configuration objects read or written by
multiple components — the blast-radius amplifiers]

**Downstream callers:** [every component whose behavior depends on the system under simulation]

**Role-resource inventory:** [every role and the resources it may access]

**Pre-declared contracts:** [every producer/consumer contract term the spec explicitly commits to —
the CONFIRMED classification baseline for Phases 4–5]

Every blast radius claim below must name a specific entry from this census.

---

## PHASE 1 — trace-state

trace-state runs first. State topology pre-classifies blast radius candidates for all downstream
phases. Downstream sub-skills inherit this map rather than constructing one post-hoc.

| From state | To state | Trigger | Invariant | Invariant holds? | Shared state surface? | Blast radius candidate |
|------------|----------|---------|-----------|------------------|-----------------------|------------------------|

For each shared state surface = yes: record blast radius candidate as wide.

If no violations: "trace-state: clean — all invariants verified."

EXIT CRITERIA: All state transitions and invariants evaluated. No transitions deferred.
State: "trace-state complete: [N] transitions evaluated, [N] violations found, [N] pre-classified wide."

---

## PHASE 2 — trace-permissions

trace-permissions runs second, before all flow sub-skills. Privilege boundary classification
anchors flow blast radius — flow violations crossing a privilege boundary are SYSTEMIC by definition.

| Role | Resource | Action | Permitted? | Escalation path? | Phase 1 state surface involved? | Blast radius ceiling |
|------|----------|--------|------------|------------------|---------------------------------|----------------------|

If Phase 1 state surface involved = yes and escalation path = yes: blast radius ceiling = wide.

If clean: "trace-permissions: clean — all role-resource pairs verified, no escalation paths detected."

EXIT CRITERIA: All role-resource pairs evaluated. No pairs deferred.
State: "trace-permissions complete: [N] pairs evaluated, [N] escalation paths found."

---

## PHASE 3 — trace-contract

Verify what crosses role and component boundaries.

| Producer | Consumer | Contract term | Expected | Actual | Mismatch? | Phase 1/2 topology match? |
|----------|----------|---------------|----------|--------|-----------|--------------------------|

If match = yes: classify CONFIRMED.

If clean: "trace-contract: clean — all contracts verified."

EXIT CRITERIA: All producer/consumer pairs evaluated. No pairs deferred.
State: "trace-contract complete: [N] pairs evaluated, [N] mismatches found, [N] CONFIRMED."

---

## PHASE 4 — flow-lifecycle

| Phase | Entry contract | Exit contract | Exception path | Exception handled? | Phase tag | CONFIRMED / RUNTIME ANOMALY |
|-------|----------------|---------------|----------------|--------------------|-----------|-----------------------------|

CONFIRMED = matches a violation from Phases 1–3. Name the matching finding.
RUNTIME ANOMALY = no matching topology violation in Phases 1–3.

If clean: "flow-lifecycle: clean — all lifecycle transitions verified."

EXIT CRITERIA: All lifecycle phases evaluated. No phases deferred.
State: "flow-lifecycle complete: [N] phases, [N] failures, [N] CONFIRMED, [N] RUNTIME ANOMALY."

---

## PHASE 5 — flow-trigger

| Trigger | Expected fire order | Actual fire order | Race condition? | Phase 2 escalation role? | Phase tag | CONFIRMED / RUNTIME ANOMALY |
|---------|---------------------|-------------------|-----------------|--------------------------|-----------|------------------------------|

If Phase 2 escalation role = yes: blast radius = wide.

If clean: "flow-trigger: clean — all triggers verified."

EXIT CRITERIA: All triggers and activating events evaluated. No triggers deferred.
State: "flow-trigger complete: [N] triggers, [N] failures, [N] CONFIRMED, [N] RUNTIME ANOMALY."

---

## CALIBRATION BLOCK

Q1: Does any finding's blast radius change when mapped against Phase 0 shared state surfaces?
For each finding with blast radius = medium or narrow: does the affected component touch a Phase 0
shared state surface? If yes, upgrade to wide. List every revision.

Q2: Do any Phase 4–5 findings match topology violations from Phases 1–3?
For each Phase 4–5 finding: identify the matching Phase 1–3 violation. CONFIRMED if match found.
RUNTIME ANOMALY if no match. List all reclassifications.

Q3: Which findings appear in three or more phases?
For every SYSTEMIC finding, enumerate the corroborating phases:
"SYSTEMIC: yes — phases: [phase-name-1], [phase-name-2], [phase-name-3]"
Binary SYSTEMIC flags are not valid.

Q4: Does the blast radius pre-classification map from Phases 1–2 hold throughout?
For every finding involving a Phase 2 escalation role or Phase 1 state surface: verify blast
radius = wide. Any finding below wide for a pre-classified component is a calibration error.

Q5: Would any finding below have shipped without this simulation?
For each wide-blast-radius finding: name the assumption it would have bypassed.

Q6: Did the execution sequence deliver its pre-classification guarantee?
Review every blast radius value in the consolidated findings. Were any revised post-hoc because
a finding touched a state surface or escalation role that Phase 1 or Phase 2 had not yet
classified at the time the downstream phase ran?
- Zero revisions: state "Anchor guarantee delivered — execution sequence pre-classified all
  blast radius values before they were consumed by downstream phases."
- Any revisions: log each case as an anchor violation — name the finding, the phase where the
  revision occurred, and the Phase 1/2 classification that arrived too late.

---

## CONSOLIDATE

Write ONE report. Do not concatenate five phase outputs.

Tiebreaker protocol: (1) Blast radius descending, (2) CONFIRMED > RUNTIME ANOMALY,
(3) SYSTEMIC > isolated. State whether any ties were encountered and how they were resolved.

**Ranked findings (calibrated blast radius order, wide first):**

---
**Finding [N]**
1. Name: [finding name or short description]
2. Source phase: [phase name]
3. Blast radius: [wide | medium | narrow] — [named census components in propagation path]
4. Severity at epicenter: [high | med | low]
5. SYSTEMIC: [yes — phases: [comma-separated phase list] | no]
6. Classification: [CONFIRMED | RUNTIME ANOMALY | isolated]
7. What must change: [one concrete fix direction in spec, contract, or implementation]
---

**Spec gaps:** [list each gap with missing-clause citation, or "none detected"]

**Contract violations:** [list each with producer and consumer named, or "none detected"]

**Privilege escalation paths:** [list each, or "none detected"]

**Clean zones:** [Phase 0 census components with no findings across all five phases]

---

## VERDICT

One paragraph. Name the finding with the widest blast radius by its Phase 0 census component name.
State CONFIRMED or RUNTIME ANOMALY. If SYSTEMIC, list the corroborating phases.
State the assumption the team would have carried into implementation had this simulation not run.
Conclude: proceed, proceed with conditions, or halt.
```

---

## V-03 — Propagation chain enumeration
**Axis:** Blast radius field — field 3 of every atomic finding block is extended to include an
explicit ordered propagation chain: `3. Blast radius: [label] — propagation chain: [A] → [B] → [C]`
where A, B, C are Phase 0 census component names. The chain must name every component through which
the failure travels from origin to terminal blast surface. No new phases are added; the only change
is field 3 in every finding.
**Hypothesis:** Blast radius claims in prior rounds were backed by "named census components in
propagation path" as a prose note — identifying which components are involved but not in what order
or through what mechanism. Making the chain explicit and ordered (like a call graph of failure
propagation) may surface findings whose chain length was underestimated because intermediate
components were skipped in the summary. It also makes blast radius upgrades from Q1 mechanically
auditable: the chain either reaches a shared state surface or it does not.

```
Simulate the technical behavior of: {{topic}}

---

## DEFINITIONS

Blast radius = how broadly a failure propagates through the system.
Wide: corrupts shared state, breaks downstream callers, or blocks multiple user roles simultaneously.
Medium: two or more components affected; no shared state surface reached.
Narrow: failure contained within one component boundary.

Severity = damage depth at the epicenter (high / med / low).
These are independent dimensions. Never merge them into a single "impact" field.
Report both as separate labeled fields in every finding.

Propagation chain = the ordered sequence of Phase 0 census components through which a failure
travels from its point of origin to its terminal blast surface.
Format: [origin] → [intermediate-component] → [terminal blast surface]
Every component in the chain must be named in the Phase 0 topology census.
Blast radius label is derived from the chain: if the terminal blast surface is a shared state
surface or reaches multiple roles, classify wide; if it stays within one component boundary, narrow.

SYSTEMIC = a finding corroborated across three or more phases.
Required format: "SYSTEMIC: yes — phases: [phase-name-1], [phase-name-2], [phase-name-3]"
Binary "SYSTEMIC: yes" without a phase list is not valid.

CONFIRMED = a Phase 4 or Phase 5 finding that matches a topology violation from Phases 1–3.
Name the matching Phase 1–3 finding when classifying CONFIRMED.

RUNTIME ANOMALY = a Phase 4 or Phase 5 finding with no matching topology violation in Phases 1–3.

Tiebreaker protocol:
1. Blast radius descending (wide > medium > narrow)
2. CONFIRMED > RUNTIME ANOMALY
3. SYSTEMIC > isolated
State this protocol before the consolidated ranking. If no ties exist, state that explicitly.

---

## PHASE 0 — Topology census

Before any sub-skill runs, record the system vocabulary explicitly.

**Components in scope:** [list every named service, module, API, schema, queue from the spec]

**Shared state surfaces:** [databases, caches, event buses, configuration objects read or written by
multiple components — the blast-radius amplifiers; failures that reach these are always wide]

**Downstream callers:** [every component whose behavior depends on the system under simulation]

**Role-resource inventory:** [every role and the resources it may access]

**Pre-declared contracts:** [every producer/consumer contract term the spec explicitly commits to]

Every propagation chain must terminate at a census component. Chains that leave the census
boundary must be flagged as out-of-scope rather than extended.

---

## PHASE 1 — trace-state

trace-state runs first. State topology pre-classifies blast radius candidates for all downstream
phases.

| From state | To state | Trigger | Invariant | Invariant holds? | Shared state surface? | Blast radius candidate |
|------------|----------|---------|-----------|------------------|-----------------------|------------------------|

For each shared state surface = yes: record blast radius candidate as wide.

If no violations: "trace-state: clean — all invariants verified."

EXIT CRITERIA: All state transitions and invariants evaluated.
State: "trace-state complete: [N] transitions evaluated, [N] violations found, [N] pre-classified wide."

---

## PHASE 2 — trace-permissions

trace-permissions runs second, before all flow sub-skills. Privilege boundary classification anchors
flow blast radius — flow violations crossing a privilege boundary are SYSTEMIC by definition.

| Role | Resource | Action | Permitted? | Escalation path? | Phase 1 state surface involved? | Blast radius ceiling |
|------|----------|--------|------------|------------------|---------------------------------|----------------------|

If clean: "trace-permissions: clean — no escalation paths detected."

EXIT CRITERIA: All role-resource pairs evaluated.
State: "trace-permissions complete: [N] pairs evaluated, [N] escalation paths found."

---

## PHASE 3 — trace-contract

| Producer | Consumer | Contract term | Expected | Actual | Mismatch? | Phase 1/2 topology match? |
|----------|----------|---------------|----------|--------|-----------|--------------------------|

If match = yes: classify CONFIRMED.

If clean: "trace-contract: clean — all contracts verified."

EXIT CRITERIA: All producer/consumer pairs evaluated.
State: "trace-contract complete: [N] pairs evaluated, [N] mismatches found, [N] CONFIRMED."

---

## PHASE 4 — flow-lifecycle

| Phase | Entry contract | Exit contract | Exception path | Exception handled? | Phase tag | CONFIRMED / RUNTIME ANOMALY |
|-------|----------------|---------------|----------------|--------------------|-----------|-----------------------------|

If clean: "flow-lifecycle: clean — all lifecycle transitions verified."

EXIT CRITERIA: All lifecycle phases evaluated.
State: "flow-lifecycle complete: [N] phases, [N] failures, [N] CONFIRMED, [N] RUNTIME ANOMALY."

---

## PHASE 5 — flow-trigger

| Trigger | Expected fire order | Actual fire order | Race condition? | Phase 2 escalation role? | Phase tag | CONFIRMED / RUNTIME ANOMALY |
|---------|---------------------|-------------------|-----------------|--------------------------|-----------|------------------------------|

If clean: "flow-trigger: clean — all triggers verified."

EXIT CRITERIA: All triggers and activating events evaluated.
State: "flow-trigger complete: [N] triggers, [N] failures, [N] CONFIRMED, [N] RUNTIME ANOMALY."

---

## CALIBRATION BLOCK

Q1: Does any finding's blast radius change when the propagation chain is traced to terminus?
For each finding: trace the propagation chain to its terminal census component. Does the chain
reach a Phase 0 shared state surface? If yes, upgrade to wide regardless of intermediate component
count. List every chain that required reclassification and show the full chain.

Q2: Do any Phase 4–5 findings match topology violations from Phases 1–3?
For each Phase 4–5 finding: identify the matching Phase 1–3 violation. Confirm CONFIRMED or
RUNTIME ANOMALY. List all reclassifications.

Q3: Which findings appear in three or more phases?
For every SYSTEMIC finding, enumerate the corroborating phases:
"SYSTEMIC: yes — phases: [phase-name-1], [phase-name-2], [phase-name-3]"

Q4: Does the blast radius pre-classification map from Phases 1–2 hold throughout?
For every finding involving a Phase 2 escalation role or Phase 1 state surface: verify blast
radius = wide. Revise and explain any finding below wide.

Q5: Would any finding below have shipped without this simulation?
For each wide-blast-radius finding: name the assumption it would have bypassed.

---

## CONSOLIDATE

Write ONE report. Do not concatenate five phase outputs.

Tiebreaker protocol: (1) Blast radius descending, (2) CONFIRMED > RUNTIME ANOMALY,
(3) SYSTEMIC > isolated. State whether any ties were encountered and how they were resolved.

**Ranked findings (calibrated blast radius order, wide first):**

For each finding, use this atomic block exactly:

---
**Finding [N]**
1. Name: [finding name or short description]
2. Source phase: [phase name]
3. Blast radius: [wide | medium | narrow] — propagation chain: [origin] → [component] → [terminal]
4. Severity at epicenter: [high | med | low]
5. SYSTEMIC: [yes — phases: [comma-separated phase list] | no]
6. Classification: [CONFIRMED | RUNTIME ANOMALY | isolated]
7. What must change: [one concrete fix direction in spec, contract, or implementation]
---

**Spec gaps:** [list each gap with missing-clause citation, or "none detected"]

**Contract violations:** [list each with producer and consumer named, or "none detected"]

**Privilege escalation paths:** [list each, or "none detected"]

**Clean zones:** [Phase 0 census components with no findings across all five phases]

---

## VERDICT

One paragraph. Name the finding with the widest blast radius by its Phase 0 census component name.
State the propagation chain from origin to terminal blast surface.
State CONFIRMED or RUNTIME ANOMALY. If SYSTEMIC, list the corroborating phases.
State the assumption the team would have carried into implementation had this simulation not run.
Conclude: proceed, proceed with conditions, or halt.
```

---

## V-04 — DEPTH asymmetry + Q6 sequence integrity gate (combination)
**Axis:** Combines both R7 excellence signals: anchor phase headers carry `[ANCHOR: ...]` tags
(from V-01), and the calibration block includes Q6 (from V-02). No other structural changes from
R7 V-01.
**Hypothesis:** V-01 and V-02 are independent signals — DEPTH asymmetry makes the dependency chain
scannable from headers; Q6 converts the anchor claim into a runtime-verifiable assertion. Combining
them should not cause interference. If both independently pass, the combination should score 90/90
on v6 and demonstrate two distinct testable patterns for C-24 and C-25.

```
Simulate the technical behavior of: {{topic}}

---

## DEFINITIONS

Blast radius = how broadly a failure propagates through the system.
Wide: corrupts shared state, breaks downstream callers, or blocks multiple user roles simultaneously.
Medium: two or more components affected; no shared state surface reached.
Narrow: failure contained within one component boundary.

Severity = damage depth at the epicenter (high / med / low).
Independent dimensions. Never merge into a single "impact" field.
Report both as separate labeled fields in every finding.

SYSTEMIC = a finding corroborated across three or more phases.
Required format: "SYSTEMIC: yes — phases: [phase-name-1], [phase-name-2], [phase-name-3]"
Binary "SYSTEMIC: yes" without a phase list is not valid.

CONFIRMED = a Phase 4 or Phase 5 finding that matches a topology violation from Phases 1–3.
Name the matching Phase 1–3 finding when classifying CONFIRMED.

RUNTIME ANOMALY = a Phase 4 or Phase 5 finding with no matching topology violation in Phases 1–3.

Tiebreaker protocol:
1. Blast radius descending (wide > medium > narrow)
2. CONFIRMED > RUNTIME ANOMALY
3. SYSTEMIC > isolated
State this protocol before the consolidated ranking. If no ties exist, state that explicitly.

---

## PHASE 0 — Topology census

**Components in scope:** [list every named service, module, API, schema, queue from the spec]

**Shared state surfaces:** [databases, caches, event buses, config objects read or written by
multiple components — the blast-radius amplifiers]

**Downstream callers:** [every component whose behavior depends on this system]

**Role-resource inventory:** [every role and the resources it may access]

**Pre-declared contracts:** [every producer/consumer contract term the spec commits to]

Every blast radius claim must name a specific census entry.

---

## PHASE 1 — trace-state [ANCHOR: state topology pre-classifies blast radius candidates for all downstream phases]

trace-state runs first. State topology — which states are shared, which transitions are multi-party,
which invariants span components — pre-classifies blast radius candidates before contract, access, or
flow analysis begins. Downstream phases inherit this map; they do not derive it independently.

| From state | To state | Trigger | Invariant | Invariant holds? | Shared state surface? | Blast radius candidate |
|------------|----------|---------|-----------|------------------|-----------------------|------------------------|

For each shared state surface = yes: record blast radius candidate as wide. Classification locked.

If no violations: "trace-state: clean — all invariants verified."

EXIT CRITERIA: All state transitions evaluated. No transitions deferred.
State: "trace-state complete: [N] transitions evaluated, [N] violations found, [N] pre-classified wide."

---

## PHASE 2 — trace-permissions [ANCHOR: privilege boundary classification anchors flow blast radius assessment]

trace-permissions runs second, before all flow sub-skills. Privilege boundary classification must
precede flow analysis because flow violations crossing a privilege boundary are SYSTEMIC by
definition. Without this anchor, flow sub-skills may understate propagation scope.

| Role | Resource | Action | Permitted? | Escalation path? | Phase 1 state surface involved? | Blast radius ceiling |
|------|----------|--------|------------|------------------|---------------------------------|----------------------|

If Phase 1 state surface involved = yes and escalation path = yes: blast radius ceiling = wide (compound).

If clean: "trace-permissions: clean — all role-resource pairs verified, no escalation paths detected."

EXIT CRITERIA: All role-resource pairs evaluated. No pairs deferred.
State: "trace-permissions complete: [N] pairs evaluated, [N] escalation paths found, [N] compound anchor hits."

---

## PHASE 3 — trace-contract

| Producer | Consumer | Contract term | Expected | Actual | Mismatch? | Phase 1/2 topology match? |
|----------|----------|---------------|----------|--------|-----------|--------------------------|

If match = yes: classify CONFIRMED.

If clean: "trace-contract: clean — all contracts verified."

EXIT CRITERIA: All producer/consumer pairs evaluated.
State: "trace-contract complete: [N] pairs evaluated, [N] mismatches found, [N] CONFIRMED."

---

## PHASE 4 — flow-lifecycle

| Phase | Entry contract | Exit contract | Exception path | Exception handled? | Phase tag | CONFIRMED / RUNTIME ANOMALY |
|-------|----------------|---------------|----------------|--------------------|-----------|-----------------------------|

CONFIRMED = matches a violation from Phases 1–3. Name the matching finding.
RUNTIME ANOMALY = no matching topology violation in Phases 1–3.

If clean: "flow-lifecycle: clean — all lifecycle transitions verified."

EXIT CRITERIA: All lifecycle phases evaluated.
State: "flow-lifecycle complete: [N] phases, [N] failures, [N] CONFIRMED, [N] RUNTIME ANOMALY."

---

## PHASE 5 — flow-trigger

| Trigger | Expected fire order | Actual fire order | Race condition? | Phase 2 escalation role? | Phase tag | CONFIRMED / RUNTIME ANOMALY |
|---------|---------------------|-------------------|-----------------|--------------------------|-----------|------------------------------|

If Phase 2 escalation role = yes: blast radius = wide.

If clean: "flow-trigger: clean — all triggers verified."

EXIT CRITERIA: All triggers evaluated.
State: "flow-trigger complete: [N] triggers, [N] failures, [N] CONFIRMED, [N] RUNTIME ANOMALY."

---

## CALIBRATION BLOCK

Q1: Does any finding's blast radius change when mapped against Phase 0 shared state surfaces?
For each finding with blast radius = medium or narrow: does the affected component touch a Phase 0
shared state surface? If yes, upgrade to wide. List every revision.

Q2: Do any Phase 4–5 findings match topology violations from Phases 1–3?
Confirm CONFIRMED or RUNTIME ANOMALY for each. List all reclassifications.

Q3: Which findings appear in three or more phases?
For every SYSTEMIC finding: "SYSTEMIC: yes — phases: [phase-name-1], [phase-name-2], [phase-name-3]"
Binary SYSTEMIC flags are not valid.

Q4: Does the blast radius pre-classification map from Phases 1–2 hold throughout?
For every finding involving a Phase 2 escalation role or Phase 1 state surface: verify wide.
Revise and explain any finding below wide.

Q5: Would any finding below have shipped without this simulation?
For each wide-blast-radius finding: name the assumption it would have bypassed.

Q6: Did the execution sequence deliver its pre-classification guarantee?
Review every blast radius value in the consolidated findings. Were any revised post-hoc because
a finding touched a state surface or escalation role that Phase 1 or Phase 2 had not yet classified
at the time the downstream phase ran?
- Zero revisions: state "Anchor guarantee delivered — Phase 1 and Phase 2 pre-classified all
  blast radius values before they were consumed by downstream phases."
- Any revision: log each as an anchor violation — name the finding, the downstream phase where the
  revision occurred, and the Phase 1/2 classification that arrived too late to prevent it.

---

## CONSOLIDATE

Write ONE report. Do not concatenate five phase outputs.

Tiebreaker protocol: (1) Blast radius descending, (2) CONFIRMED > RUNTIME ANOMALY,
(3) SYSTEMIC > isolated. State whether any ties were encountered and how they were resolved.

**Ranked findings (calibrated blast radius order, wide first):**

---
**Finding [N]**
1. Name: [finding name or short description]
2. Source phase: [phase name]
3. Blast radius: [wide | medium | narrow] — [named census components in propagation path]
4. Severity at epicenter: [high | med | low]
5. SYSTEMIC: [yes — phases: [comma-separated phase list] | no]
6. Classification: [CONFIRMED | RUNTIME ANOMALY | isolated]
7. What must change: [one concrete fix direction in spec, contract, or implementation]
---

**Spec gaps:** [list each gap with missing-clause citation, or "none detected"]

**Contract violations:** [list each with producer and consumer named, or "none detected"]

**Privilege escalation paths:** [list each, or "none detected"]

**Clean zones:** [Phase 0 census components with no findings across all five phases]

---

## VERDICT

One paragraph. Name the finding with the widest blast radius by its Phase 0 census component name.
State CONFIRMED or RUNTIME ANOMALY. If SYSTEMIC, list the corroborating phases.
State the assumption the team would have carried into implementation had this simulation not run.
Conclude: proceed, proceed with conditions, or halt.
```

---

## V-05 — Full combination (DEPTH asymmetry + Q6 + propagation chain + max coverage)
**Axis:** All three R8 axes combined: anchor phase headers carry `[ANCHOR: ...]` tags, calibration
includes Q6, and field 3 of every finding block contains an explicit propagation chain. All 15
aspirational criteria are given named structural support. Maximum redundancy variation.
**Hypothesis:** V-01, V-02, V-03 test each axis in isolation. V-05 tests whether all three compose
without interference and without degrading the existing 90/90 structure. Full combination also
gives the scorer the clearest signal on whether propagation chain (the new axis) creates any
scoring conflict with existing criteria — particularly C-06 (blast radius label) and C-19
(atomic 7-field block), where field 3 format changes might affect compliance.

```
Simulate the technical behavior of: {{topic}}

---

## DEFINITIONS

Blast radius = how broadly a failure propagates through the system.
Wide: corrupts shared state, breaks downstream callers, or blocks multiple user roles simultaneously.
Medium: two or more components affected; no shared state surface reached.
Narrow: failure contained within one component boundary.

Severity = damage depth at the epicenter (high / med / low).
Independent dimensions. Never merge. Report as separate labeled fields in every finding.

Propagation chain = the ordered sequence of Phase 0 census components through which a failure
travels from origin to terminal blast surface.
Format: [origin] → [component-B] → [terminal]
Blast radius label is derived from the chain terminus: if the chain reaches a shared state surface
or multiple roles, classify wide. Chains that cannot be named using census components must be
flagged as unresolved rather than extended.

SYSTEMIC = a finding corroborated across three or more phases.
Required format: "SYSTEMIC: yes — phases: [phase-name-1], [phase-name-2], [phase-name-3]"
Binary "SYSTEMIC: yes" without a phase list is not valid and will be rejected.

CONFIRMED = a Phase 4 or Phase 5 finding that matches a topology violation from Phases 1–3.
Match is structural: same component, access pattern, contract term, or state surface.
Name the matching Phase 1–3 finding when classifying CONFIRMED.

RUNTIME ANOMALY = a Phase 4 or Phase 5 finding with no matching topology violation in Phases 1–3.

Tiebreaker protocol:
1. Blast radius descending (wide > medium > narrow)
2. CONFIRMED > RUNTIME ANOMALY
3. SYSTEMIC > isolated
State this protocol before the consolidated ranking. If no ties exist, state that explicitly.

---

## PHASE 0 — Topology census

Before any sub-skill runs, record the system vocabulary explicitly.

**Components in scope:** [every named service, module, API, schema, queue from the spec]

**Shared state surfaces:** [databases, caches, event buses, config objects read or written by
multiple components — blast-radius amplifiers; any propagation chain reaching these = wide]

**Downstream callers:** [every component that depends on outputs from this system]

**Role-resource inventory:** [every role and the resources it may access]

**Pre-declared contracts:** [every producer/consumer contract term the spec commits to —
the CONFIRMED classification baseline for Phases 4–5]

Every blast radius claim must name a specific census entry.
Every propagation chain must terminate at a census component.

---

## PHASE 1 — trace-state [ANCHOR: state topology pre-classifies blast radius candidates for all downstream phases]

trace-state runs first. State topology — shared states, multi-party transitions, cross-component
invariants — pre-classifies blast radius candidates before contract, access, or flow analysis.
Downstream sub-skills inherit this map; none re-derive it independently.

| From state | To state | Trigger | Invariant | Invariant holds? | Shared state surface? | Blast radius candidate |
|------------|----------|---------|-----------|------------------|-----------------------|------------------------|

For each shared state surface = yes: record blast radius candidate as wide. Classification locked
for downstream phases.

If no violations: "trace-state: clean — all invariants verified."

EXIT CRITERIA: All state transitions and invariants evaluated. No transitions deferred.
State: "trace-state complete: [N] transitions evaluated, [N] violations found, [N] pre-classified wide."

---

## PHASE 2 — trace-permissions [ANCHOR: privilege boundary classification anchors flow blast radius assessment]

trace-permissions runs second, before all flow sub-skills. Privilege boundary classification must
precede flow analysis — flow violations crossing a privilege boundary are SYSTEMIC by definition.
Without this anchor, flow sub-skills may understate propagation scope.

| Role | Resource | Action | Permitted? | Escalation path? | Phase 1 state surface involved? | Blast radius ceiling |
|------|----------|--------|------------|------------------|---------------------------------|----------------------|

Phase 1 state surface involved = yes and escalation path = yes: blast radius ceiling = wide (compound anchor hit).

If clean: "trace-permissions: clean — all role-resource pairs verified, no escalation paths detected."

EXIT CRITERIA: All role-resource pairs evaluated. No pairs deferred.
State: "trace-permissions complete: [N] pairs evaluated, [N] escalation paths found, [N] compound anchor hits."

---

## PHASE 3 — trace-contract

| Producer | Consumer | Contract term | Expected | Actual | Mismatch? | Phase 1/2 topology match? |
|----------|----------|---------------|----------|--------|-----------|--------------------------|

Phase 1/2 topology match = yes if contract involves a Phase 1 state violation surface or Phase 2
escalation role. If match = yes: classify CONFIRMED. Name the matching phase finding.

If clean: "trace-contract: clean — all contracts verified."

EXIT CRITERIA: All producer/consumer pairs evaluated.
State: "trace-contract complete: [N] pairs evaluated, [N] mismatches found, [N] CONFIRMED."

---

## PHASE 4 — flow-lifecycle

| Phase | Entry contract | Exit contract | Exception path | Exception handled? | Phase tag | CONFIRMED / RUNTIME ANOMALY |
|-------|----------------|---------------|----------------|--------------------|-----------|-----------------------------|

Phase tag = lifecycle phase of violation (INIT, ACTIVE, SUSPENDED, TERMINAL, etc.).
CONFIRMED = matches a Phase 1–3 violation. Name the match.
RUNTIME ANOMALY = no matching topology violation.

If clean: "flow-lifecycle: clean — all lifecycle transitions verified."

EXIT CRITERIA: All lifecycle phases evaluated.
State: "flow-lifecycle complete: [N] phases, [N] failures, [N] CONFIRMED, [N] RUNTIME ANOMALY."

---

## PHASE 5 — flow-trigger

| Trigger | Expected fire order | Actual fire order | Race condition? | Phase 2 escalation role? | Phase tag | CONFIRMED / RUNTIME ANOMALY |
|---------|---------------------|-------------------|-----------------|--------------------------|-----------|------------------------------|

Phase 2 escalation role = yes if trigger involves a Phase 2 escalation role: blast radius = wide.

If clean: "flow-trigger: clean — all triggers verified."

EXIT CRITERIA: All triggers and activating events evaluated.
State: "flow-trigger complete: [N] triggers, [N] failures, [N] CONFIRMED, [N] RUNTIME ANOMALY."

---

## CALIBRATION BLOCK

Q1: Does any finding's blast radius change when the propagation chain is traced to terminus?
For each finding: trace the full propagation chain ([origin] → ... → [terminal]). Does the
chain reach a Phase 0 shared state surface? If yes, upgrade to wide. List every revision and show
the full chain for each reclassified finding.

Q2: Do any Phase 4–5 findings match topology violations from Phases 1–3?
Confirm CONFIRMED or RUNTIME ANOMALY for each Phase 4–5 finding. List all reclassifications.

Q3: Which findings appear in three or more phases?
For every SYSTEMIC finding: "SYSTEMIC: yes — phases: [phase-name-1], [phase-name-2], [phase-name-3]"
Binary SYSTEMIC flags are not valid.

Q4: Does the blast radius pre-classification map from Phases 1–2 hold throughout?
For every finding involving a Phase 2 escalation role or Phase 1 state surface: verify wide.
Revise and explain any finding below wide for a pre-classified component.

Q5: Would any finding below have shipped without this simulation?
For each wide-blast-radius finding: name the assumption it would have bypassed.

Q6: Did the execution sequence deliver its pre-classification guarantee?
Review every blast radius value in the consolidated findings. Were any revised post-hoc because
a finding touched a state surface or escalation role that Phase 1 or Phase 2 had not yet classified
at the time the downstream phase ran?
- Zero revisions: "Anchor guarantee delivered — Phase 1 and Phase 2 pre-classified all blast radius
  values before downstream phases consumed them."
- Any revision: log each as an anchor violation — name the finding, the downstream phase, and the
  Phase 1/2 classification that arrived too late.

---

## CONSOLIDATE

Write ONE report. Do not concatenate five phase outputs.

Tiebreaker protocol: (1) Blast radius descending, (2) CONFIRMED > RUNTIME ANOMALY,
(3) SYSTEMIC > isolated. State whether any ties were encountered and how they were resolved.

**Ranked findings (calibrated blast radius order, wide first):**

For each finding, use this atomic block exactly:

---
**Finding [N]**
1. Name: [finding name or short description]
2. Source phase: [phase name]
3. Blast radius: [wide | medium | narrow] — propagation chain: [origin] → [component] → [terminal]
4. Severity at epicenter: [high | med | low]
5. SYSTEMIC: [yes — phases: [comma-separated phase list] | no]
6. Classification: [CONFIRMED | RUNTIME ANOMALY | isolated]
7. What must change: [one concrete fix direction in spec, contract, or implementation]
---

**Spec gaps:** [list each gap with missing-clause citation, or "none detected"]

**Contract violations:** [list each with producer and consumer named, or "none detected"]

**Privilege escalation paths:** [list each, or "none detected"]

**Clean zones:** [Phase 0 census components with no findings across all five phases]

---

## VERDICT

One paragraph. Name the finding with the widest blast radius by its Phase 0 census component name.
State the propagation chain from origin to terminal blast surface.
State CONFIRMED or RUNTIME ANOMALY. If SYSTEMIC, list the corroborating phases.
State the assumption the team would have carried into implementation had this simulation not run.
Conclude: proceed, proceed with conditions, or halt.
```
