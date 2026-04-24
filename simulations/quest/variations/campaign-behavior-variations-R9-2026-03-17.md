R9 variations written. Here's the summary:

---

## Round 9 — campaign-behavior variations

**Baseline:** R8 V-05 (90/90 under v6; all three new v7 criteria C-24/C-25/C-26 already present)

### Three new single axes

| Variation | Axis | What it adds | C-27/28 candidate |
|-----------|------|--------------|-------------------|
| **V-01** | Chain Terminus Registry | Phase 0 gets a T-NN numbered table of valid chain termini; every propagation chain in field 3 must resolve to a T-NN entry or be flagged "unresolved chain" | C-27: converts terminus requirement from DEFINITIONS prose to structural lookup |
| **V-02** | Dedicated Executive Summary | `## EXECUTIVE SUMMARY` heading with exactly 3 structured bullets appears before ranked findings | C-28: makes C-16 satisfiable by section position, not list-order inference |
| **V-03** | Inline CONFIRMED evidence citation | Field 6 format changes to `CONFIRMED -- evidence: [phase]: [finding]` inline — promotes C-17 from a DEFINITIONS instruction into a structural field requirement | C-27 (alt): evidence basis becomes mechanically verifiable within the field itself |

### Two combinations

- **V-04:** V-01 + V-02 — tests whether Phase 0 vocab layer and CONSOLIDATE output layer compose without interference (specific risk: T-NN notation in EXECUTIVE SUMMARY bullets)
- **V-05:** All three axes + R8 V-05 max coverage — three interference risks flagged: T-NN in field 3 vs C-26, EXECUTIVE SUMMARY with T-NN vs C-16, inline field 6 vs C-07/C-19

File written to `simulations/quest/variations/campaign-behavior-variations-R9-2026-03-17.md`.
ry entry. Chains that reach a component
not in the registry are flagged "unresolved chain — registry miss: [component name]." The registry
is declared before any phase runs.
**Hypothesis:** Phase 0 already lists shared state surfaces informally. Making them a named,
numbered registry converts the terminus requirement from a prose instruction (in DEFINITIONS) into
a structural lookup. Findings become independently verifiable: a reviewer checks the chain terminus
against the registry list rather than re-reading DEFINITIONS prose. All other structure is identical
to R8 V-05. If the registry adds structural clarity without changing any criterion-level compliance,
R9 V-01 should score 90/90 on v7.

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
Format: [origin] -> [component-B] -> [T-NN terminal]
The terminal must be a named entry in the Phase 0 Chain Terminus Registry (T-NN).
Blast radius label is derived from the chain terminus: if T-NN is classified as a shared state
surface or multi-role access point, classify wide. Chains that cannot resolve to a T-NN entry
must be flagged: "unresolved chain -- registry miss: [component name not in registry]."

SYSTEMIC = a finding corroborated across three or more phases.
Required format: "SYSTEMIC: yes -- phases: [phase-name-1], [phase-name-2], [phase-name-3]"
Binary "SYSTEMIC: yes" without a phase list is not valid and will be rejected.

CONFIRMED = a Phase 4 or Phase 5 finding that matches a topology violation from Phases 1-3.
Match is structural: same component, access pattern, contract term, or state surface.
Name the matching Phase 1-3 finding when classifying CONFIRMED.

RUNTIME ANOMALY = a Phase 4 or Phase 5 finding with no matching topology violation in Phases 1-3.

Tiebreaker protocol:
1. Blast radius descending (wide > medium > narrow)
2. CONFIRMED > RUNTIME ANOMALY
3. SYSTEMIC > isolated
State this protocol before the consolidated ranking. If no ties exist, state that explicitly.

---

## PHASE 0 -- Topology census

Before any sub-skill runs, record the system vocabulary explicitly.

**Components in scope:** [every named service, module, API, schema, queue from the spec]

**Shared state surfaces:** [databases, caches, event buses, config objects read or written by
multiple components -- blast-radius amplifiers; any propagation chain reaching these = wide]

**Downstream callers:** [every component that depends on outputs from this system]

**Role-resource inventory:** [every role and the resources it may access]

**Pre-declared contracts:** [every producer/consumer contract term the spec commits to --
the CONFIRMED classification baseline for Phases 4-5]

**Chain Terminus Registry:**
List every valid blast-radius terminus point in numbered form. Every propagation chain in the
CONSOLIDATE block must terminate at a named entry here.

| T-NN | Terminus name | Type | Blast radius floor |
|------|---------------|------|--------------------|
| T-01 | [component name] | [shared state surface / downstream caller / multi-role access point] | [wide / medium] |
| ...  | ...             | ...  | ... |

Every blast radius claim must name a specific census entry.
Every propagation chain must terminate at a T-NN registry entry. Chains that exit the registry
are flagged "unresolved chain" and excluded from ranking until the registry is updated.

---

## PHASE 1 -- trace-state [ANCHOR: state topology pre-classifies blast radius candidates for all downstream phases]

trace-state runs first. State topology -- shared states, multi-party transitions, cross-component
invariants -- pre-classifies blast radius candidates before contract, access, or flow analysis.
Downstream sub-skills inherit this map; none re-derive it independently.

| From state | To state | Trigger | Invariant | Invariant holds? | Shared state surface? | Blast radius candidate |
|------------|----------|---------|-----------|------------------|-----------------------|------------------------|

For each shared state surface = yes: record blast radius candidate as wide. Classification locked
for downstream phases.

If no violations: "trace-state: clean -- all invariants verified."

EXIT CRITERIA: All state transitions and invariants evaluated. No transitions deferred.
State: "trace-state complete: [N] transitions evaluated, [N] violations found, [N] pre-classified wide."

---

## PHASE 2 -- trace-permissions [ANCHOR: privilege boundary classification anchors flow blast radius assessment]

trace-permissions runs second, before all flow sub-skills. Privilege boundary classification must
precede flow analysis -- flow violations crossing a privilege boundary are SYSTEMIC by definition.
Without this anchor, flow sub-skills may understate propagation scope.

| Role | Resource | Action | Permitted? | Escalation path? | Phase 1 state surface involved? | Blast radius ceiling |
|------|----------|--------|------------|------------------|---------------------------------|----------------------|

Phase 1 state surface involved = yes and escalation path = yes: blast radius ceiling = wide (compound anchor hit).

If clean: "trace-permissions: clean -- all role-resource pairs verified, no escalation paths detected."

EXIT CRITERIA: All role-resource pairs evaluated. No pairs deferred.
State: "trace-permissions complete: [N] pairs evaluated, [N] escalation paths found, [N] compound anchor hits."

---

## PHASE 3 -- trace-contract

| Producer | Consumer | Contract term | Expected | Actual | Mismatch? | Phase 1/2 topology match? |
|----------|----------|---------------|----------|--------|-----------|--------------------------|

Phase 1/2 topology match = yes if contract involves a Phase 1 state violation surface or Phase 2
escalation role. If match = yes: classify CONFIRMED. Name the matching phase finding.

If clean: "trace-contract: clean -- all contracts verified."

EXIT CRITERIA: All producer/consumer pairs evaluated.
State: "trace-contract complete: [N] pairs evaluated, [N] mismatches found, [N] CONFIRMED."

---

## PHASE 4 -- flow-lifecycle

| Phase | Entry contract | Exit contract | Exception path | Exception handled? | Phase tag | CONFIRMED / RUNTIME ANOMALY |
|-------|----------------|---------------|----------------|--------------------|-----------|-----------------------------|

Phase tag = lifecycle phase of violation (INIT, ACTIVE, SUSPENDED, TERMINAL, etc.).
CONFIRMED = matches a Phase 1-3 violation. Name the match.
RUNTIME ANOMALY = no matching topology violation.

If clean: "flow-lifecycle: clean -- all lifecycle transitions verified."

EXIT CRITERIA: All lifecycle phases evaluated.
State: "flow-lifecycle complete: [N] phases, [N] failures, [N] CONFIRMED, [N] RUNTIME ANOMALY."

---

## PHASE 5 -- flow-trigger

| Trigger | Expected fire order | Actual fire order | Race condition? | Phase 2 escalation role? | Phase tag | CONFIRMED / RUNTIME ANOMALY |
|---------|---------------------|-------------------|-----------------|--------------------------|-----------|------------------------------|

Phase 2 escalation role = yes if trigger involves a Phase 2 escalation role: blast radius = wide.

If clean: "flow-trigger: clean -- all triggers verified."

EXIT CRITERIA: All triggers and activating events evaluated.
State: "flow-trigger complete: [N] triggers, [N] failures, [N] CONFIRMED, [N] RUNTIME ANOMALY."

---

## CALIBRATION BLOCK

Q1: Does any finding's blast radius change when the propagation chain is traced to terminus?
For each finding: trace the full propagation chain ([origin] -> ... -> [T-NN terminal]). Does the
T-NN registry entry carry blast radius floor = wide? If yes, upgrade to wide. List every revision
and show the full chain for each reclassified finding. Flag any chain that cannot resolve to a
T-NN entry as "unresolved chain."

Q2: Do any Phase 4-5 findings match topology violations from Phases 1-3?
Confirm CONFIRMED or RUNTIME ANOMALY for each Phase 4-5 finding. List all reclassifications.

Q3: Which findings appear in three or more phases?
For every SYSTEMIC finding: "SYSTEMIC: yes -- phases: [phase-name-1], [phase-name-2], [phase-name-3]"
Binary SYSTEMIC flags are not valid.

Q4: Does the blast radius pre-classification map from Phases 1-2 hold throughout?
For every finding involving a Phase 2 escalation role or Phase 1 state surface: verify wide.
Revise and explain any finding below wide for a pre-classified component.

Q5: Would any finding below have shipped without this simulation?
For each wide-blast-radius finding: name the assumption it would have bypassed.

Q6: Did the execution sequence deliver its pre-classification guarantee?
Review every blast radius value in the consolidated findings. Were any revised post-hoc because
a finding touched a state surface or escalation role that Phase 1 or Phase 2 had not yet classified
at the time the downstream phase ran?
- Zero revisions: "Anchor guarantee delivered -- Phase 1 and Phase 2 pre-classified all blast radius
  values before downstream phases consumed them."
- Any revision: log each as an anchor violation -- name the finding, the downstream phase, and the
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
3. Blast radius: [wide | medium | narrow] -- propagation chain: [origin] -> [component] -> [T-NN terminal]
4. Severity at epicenter: [high | med | low]
5. SYSTEMIC: [yes -- phases: [comma-separated phase list] | no]
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
State the propagation chain from origin to T-NN terminal blast surface.
State CONFIRMED or RUNTIME ANOMALY. If SYSTEMIC, list the corroborating phases.
State the assumption the team would have carried into implementation had this simulation not run.
Conclude: proceed, proceed with conditions, or halt.
```

---

## V-02 -- Dedicated Executive Summary section
**Axis:** A `## EXECUTIVE SUMMARY` heading is inserted immediately after the CONSOLIDATE
tiebreaker protocol statement and before the ranked findings list. It contains exactly three
structured bullet points -- one per top-ranked finding -- each formatted as:
`[F-NN] [blast-radius tier] -- [origin] -> [terminal] -- [CONFIRMED/RUNTIME ANOMALY]`.
The Executive Summary is written before the full findings list. All other structure is identical
to R8 V-05.
**Hypothesis:** C-16 (executive summary top-3) currently passes by inferring top-3 from ranked
list position. A dedicated `## EXECUTIVE SUMMARY` heading makes the pass condition unambiguous --
there is no inference required. If the dedicated section adds no scoring value beyond what ranked
list position already delivers, V-02 should match 90/90. If it improves mechanical auditability
of C-16, it becomes a candidate for C-27.

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
Format: [origin] -> [component-B] -> [terminal]
Blast radius label is derived from the chain terminus: if the chain reaches a shared state surface
or multiple roles, classify wide. Chains that cannot be named using census components must be
flagged as unresolved rather than extended.

SYSTEMIC = a finding corroborated across three or more phases.
Required format: "SYSTEMIC: yes -- phases: [phase-name-1], [phase-name-2], [phase-name-3]"
Binary "SYSTEMIC: yes" without a phase list is not valid and will be rejected.

CONFIRMED = a Phase 4 or Phase 5 finding that matches a topology violation from Phases 1-3.
Match is structural: same component, access pattern, contract term, or state surface.
Name the matching Phase 1-3 finding when classifying CONFIRMED.

RUNTIME ANOMALY = a Phase 4 or Phase 5 finding with no matching topology violation in Phases 1-3.

Tiebreaker protocol:
1. Blast radius descending (wide > medium > narrow)
2. CONFIRMED > RUNTIME ANOMALY
3. SYSTEMIC > isolated
State this protocol before the consolidated ranking. If no ties exist, state that explicitly.

---

## PHASE 0 -- Topology census

Before any sub-skill runs, record the system vocabulary explicitly.

**Components in scope:** [every named service, module, API, schema, queue from the spec]

**Shared state surfaces:** [databases, caches, event buses, config objects read or written by
multiple components -- blast-radius amplifiers; any propagation chain reaching these = wide]

**Downstream callers:** [every component that depends on outputs from this system]

**Role-resource inventory:** [every role and the resources it may access]

**Pre-declared contracts:** [every producer/consumer contract term the spec commits to --
the CONFIRMED classification baseline for Phases 4-5]

Every blast radius claim must name a specific census entry.
Every propagation chain must terminate at a census component.

---

## PHASE 1 -- trace-state [ANCHOR: state topology pre-classifies blast radius candidates for all downstream phases]

trace-state runs first. State topology -- shared states, multi-party transitions, cross-component
invariants -- pre-classifies blast radius candidates before contract, access, or flow analysis.
Downstream sub-skills inherit this map; none re-derive it independently.

| From state | To state | Trigger | Invariant | Invariant holds? | Shared state surface? | Blast radius candidate |
|------------|----------|---------|-----------|------------------|-----------------------|------------------------|

For each shared state surface = yes: record blast radius candidate as wide. Classification locked
for downstream phases.

If no violations: "trace-state: clean -- all invariants verified."

EXIT CRITERIA: All state transitions and invariants evaluated. No transitions deferred.
State: "trace-state complete: [N] transitions evaluated, [N] violations found, [N] pre-classified wide."

---

## PHASE 2 -- trace-permissions [ANCHOR: privilege boundary classification anchors flow blast radius assessment]

trace-permissions runs second, before all flow sub-skills. Privilege boundary classification must
precede flow analysis -- flow violations crossing a privilege boundary are SYSTEMIC by definition.
Without this anchor, flow sub-skills may understate propagation scope.

| Role | Resource | Action | Permitted? | Escalation path? | Phase 1 state surface involved? | Blast radius ceiling |
|------|----------|--------|------------|------------------|---------------------------------|----------------------|

Phase 1 state surface involved = yes and escalation path = yes: blast radius ceiling = wide (compound anchor hit).

If clean: "trace-permissions: clean -- all role-resource pairs verified, no escalation paths detected."

EXIT CRITERIA: All role-resource pairs evaluated. No pairs deferred.
State: "trace-permissions complete: [N] pairs evaluated, [N] escalation paths found, [N] compound anchor hits."

---

## PHASE 3 -- trace-contract

| Producer | Consumer | Contract term | Expected | Actual | Mismatch? | Phase 1/2 topology match? |
|----------|----------|---------------|----------|--------|-----------|--------------------------|

Phase 1/2 topology match = yes if contract involves a Phase 1 state violation surface or Phase 2
escalation role. If match = yes: classify CONFIRMED. Name the matching phase finding.

If clean: "trace-contract: clean -- all contracts verified."

EXIT CRITERIA: All producer/consumer pairs evaluated.
State: "trace-contract complete: [N] pairs evaluated, [N] mismatches found, [N] CONFIRMED."

---

## PHASE 4 -- flow-lifecycle

| Phase | Entry contract | Exit contract | Exception path | Exception handled? | Phase tag | CONFIRMED / RUNTIME ANOMALY |
|-------|----------------|---------------|----------------|--------------------|-----------|-----------------------------|

Phase tag = lifecycle phase of violation (INIT, ACTIVE, SUSPENDED, TERMINAL, etc.).
CONFIRMED = matches a Phase 1-3 violation. Name the match.
RUNTIME ANOMALY = no matching topology violation.

If clean: "flow-lifecycle: clean -- all lifecycle transitions verified."

EXIT CRITERIA: All lifecycle phases evaluated.
State: "flow-lifecycle complete: [N] phases, [N] failures, [N] CONFIRMED, [N] RUNTIME ANOMALY."

---

## PHASE 5 -- flow-trigger

| Trigger | Expected fire order | Actual fire order | Race condition? | Phase 2 escalation role? | Phase tag | CONFIRMED / RUNTIME ANOMALY |
|---------|---------------------|-------------------|-----------------|--------------------------|-----------|------------------------------|

Phase 2 escalation role = yes if trigger involves a Phase 2 escalation role: blast radius = wide.

If clean: "flow-trigger: clean -- all triggers verified."

EXIT CRITERIA: All triggers and activating events evaluated.
State: "flow-trigger complete: [N] triggers, [N] failures, [N] CONFIRMED, [N] RUNTIME ANOMALY."

---

## CALIBRATION BLOCK

Q1: Does any finding's blast radius change when the propagation chain is traced to terminus?
For each finding: trace the full propagation chain ([origin] -> ... -> [terminal]). Does the
chain reach a Phase 0 shared state surface? If yes, upgrade to wide. List every revision and show
the full chain for each reclassified finding.

Q2: Do any Phase 4-5 findings match topology violations from Phases 1-3?
Confirm CONFIRMED or RUNTIME ANOMALY for each Phase 4-5 finding. List all reclassifications.

Q3: Which findings appear in three or more phases?
For every SYSTEMIC finding: "SYSTEMIC: yes -- phases: [phase-name-1], [phase-name-2], [phase-name-3]"
Binary SYSTEMIC flags are not valid.

Q4: Does the blast radius pre-classification map from Phases 1-2 hold throughout?
For every finding involving a Phase 2 escalation role or Phase 1 state surface: verify wide.
Revise and explain any finding below wide for a pre-classified component.

Q5: Would any finding below have shipped without this simulation?
For each wide-blast-radius finding: name the assumption it would have bypassed.

Q6: Did the execution sequence deliver its pre-classification guarantee?
Review every blast radius value in the consolidated findings. Were any revised post-hoc because
a finding touched a state surface or escalation role that Phase 1 or Phase 2 had not yet classified
at the time the downstream phase ran?
- Zero revisions: "Anchor guarantee delivered -- Phase 1 and Phase 2 pre-classified all blast radius
  values before downstream phases consumed them."
- Any revision: log each as an anchor violation -- name the finding, the downstream phase, and the
  Phase 1/2 classification that arrived too late.

---

## CONSOLIDATE

Write ONE report. Do not concatenate five phase outputs.

Tiebreaker protocol: (1) Blast radius descending, (2) CONFIRMED > RUNTIME ANOMALY,
(3) SYSTEMIC > isolated. State whether any ties were encountered and how they were resolved.

## EXECUTIVE SUMMARY

Three bullet points. One per top-ranked finding. Write this section before the full findings list.
Each bullet uses this format: [F-NN] [blast-radius tier] -- [origin] -> [terminal] -- [CONFIRMED/RUNTIME ANOMALY]
A reader assessing campaign risk reads these three lines and has the full risk signal.

- [F-01] [blast-radius tier] -- [propagation chain abbreviated] -- [CONFIRMED/RUNTIME ANOMALY]
- [F-02] [blast-radius tier] -- [propagation chain abbreviated] -- [CONFIRMED/RUNTIME ANOMALY]
- [F-03] [blast-radius tier] -- [propagation chain abbreviated] -- [CONFIRMED/RUNTIME ANOMALY]

**Ranked findings (calibrated blast radius order, wide first):**

For each finding, use this atomic block exactly:

---
**Finding [N]**
1. Name: [finding name or short description]
2. Source phase: [phase name]
3. Blast radius: [wide | medium | narrow] -- propagation chain: [origin] -> [component] -> [terminal]
4. Severity at epicenter: [high | med | low]
5. SYSTEMIC: [yes -- phases: [comma-separated phase list] | no]
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

## V-03 -- Inline CONFIRMED evidence citation in field 6
**Axis:** Field 6 of the atomic finding block is restructured from a bare classification label to
an inline evidence citation. For CONFIRMED findings the format becomes:
"CONFIRMED -- evidence: [phase name]: [matching finding description]". For RUNTIME ANOMALY:
"RUNTIME ANOMALY -- no topology match in Phases 1-3". The DEFINITIONS instruction "Name the
matching Phase 1-3 finding when classifying CONFIRMED" is promoted into the field format itself,
making C-17 (evidence basis per CONFIRMED finding) a structural requirement within every block
rather than a prose expectation in DEFINITIONS. All other structure is identical to R8 V-05.
**Hypothesis:** C-17 currently passes because DEFINITIONS instructs citation and field 6 carries
the classification. Embedding the citation format into field 6 removes the gap between instruction
location (DEFINITIONS) and compliance surface (finding block). If inline evidence citation adds
structural clarity without breaking C-07 (confirmation status per finding) or C-19 (atomic 7-field
block), V-03 should score 90/90. The citation format is a candidate for C-27.

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
Format: [origin] -> [component-B] -> [terminal]
Blast radius label is derived from the chain terminus: if the chain reaches a shared state surface
or multiple roles, classify wide. Chains that cannot be named using census components must be
flagged as unresolved rather than extended.

SYSTEMIC = a finding corroborated across three or more phases.
Required format: "SYSTEMIC: yes -- phases: [phase-name-1], [phase-name-2], [phase-name-3]"
Binary "SYSTEMIC: yes" without a phase list is not valid and will be rejected.

CONFIRMED = a Phase 4 or Phase 5 finding that matches a topology violation from Phases 1-3.
Match is structural: same component, access pattern, contract term, or state surface.
Field 6 format for CONFIRMED: "CONFIRMED -- evidence: [matching phase name]: [matching finding description]"
This citation is required. CONFIRMED without an inline evidence citation = incomplete block.

RUNTIME ANOMALY = a Phase 4 or Phase 5 finding with no matching topology violation in Phases 1-3.
Field 6 format for RUNTIME ANOMALY: "RUNTIME ANOMALY -- no topology match in Phases 1-3"

Tiebreaker protocol:
1. Blast radius descending (wide > medium > narrow)
2. CONFIRMED > RUNTIME ANOMALY
3. SYSTEMIC > isolated
State this protocol before the consolidated ranking. If no ties exist, state that explicitly.

---

## PHASE 0 -- Topology census

Before any sub-skill runs, record the system vocabulary explicitly.

**Components in scope:** [every named service, module, API, schema, queue from the spec]

**Shared state surfaces:** [databases, caches, event buses, config objects read or written by
multiple components -- blast-radius amplifiers; any propagation chain reaching these = wide]

**Downstream callers:** [every component that depends on outputs from this system]

**Role-resource inventory:** [every role and the resources it may access]

**Pre-declared contracts:** [every producer/consumer contract term the spec commits to --
the CONFIRMED classification baseline for Phases 4-5]

Every blast radius claim must name a specific census entry.
Every propagation chain must terminate at a census component.

---

## PHASE 1 -- trace-state [ANCHOR: state topology pre-classifies blast radius candidates for all downstream phases]

trace-state runs first. State topology -- shared states, multi-party transitions, cross-component
invariants -- pre-classifies blast radius candidates before contract, access, or flow analysis.
Downstream sub-skills inherit this map; none re-derive it independently.

| From state | To state | Trigger | Invariant | Invariant holds? | Shared state surface? | Blast radius candidate |
|------------|----------|---------|-----------|------------------|-----------------------|------------------------|

For each shared state surface = yes: record blast radius candidate as wide. Classification locked
for downstream phases.

If no violations: "trace-state: clean -- all invariants verified."

EXIT CRITERIA: All state transitions and invariants evaluated. No transitions deferred.
State: "trace-state complete: [N] transitions evaluated, [N] violations found, [N] pre-classified wide."

---

## PHASE 2 -- trace-permissions [ANCHOR: privilege boundary classification anchors flow blast radius assessment]

trace-permissions runs second, before all flow sub-skills. Privilege boundary classification must
precede flow analysis -- flow violations crossing a privilege boundary are SYSTEMIC by definition.
Without this anchor, flow sub-skills may understate propagation scope.

| Role | Resource | Action | Permitted? | Escalation path? | Phase 1 state surface involved? | Blast radius ceiling |
|------|----------|--------|------------|------------------|---------------------------------|----------------------|

Phase 1 state surface involved = yes and escalation path = yes: blast radius ceiling = wide (compound anchor hit).

If clean: "trace-permissions: clean -- all role-resource pairs verified, no escalation paths detected."

EXIT CRITERIA: All role-resource pairs evaluated. No pairs deferred.
State: "trace-permissions complete: [N] pairs evaluated, [N] escalation paths found, [N] compound anchor hits."

---

## PHASE 3 -- trace-contract

| Producer | Consumer | Contract term | Expected | Actual | Mismatch? | Phase 1/2 topology match? |
|----------|----------|---------------|----------|--------|-----------|--------------------------|

Phase 1/2 topology match = yes if contract involves a Phase 1 state violation surface or Phase 2
escalation role. If match = yes: classify CONFIRMED. Name the matching phase finding.

If clean: "trace-contract: clean -- all contracts verified."

EXIT CRITERIA: All producer/consumer pairs evaluated.
State: "trace-contract complete: [N] pairs evaluated, [N] mismatches found, [N] CONFIRMED."

---

## PHASE 4 -- flow-lifecycle

| Phase | Entry contract | Exit contract | Exception path | Exception handled? | Phase tag | CONFIRMED / RUNTIME ANOMALY |
|-------|----------------|---------------|----------------|--------------------|-----------|-----------------------------|

Phase tag = lifecycle phase of violation (INIT, ACTIVE, SUSPENDED, TERMINAL, etc.).
CONFIRMED = matches a Phase 1-3 violation. Use field 6 inline citation format. Name the match.
RUNTIME ANOMALY = no matching topology violation.

If clean: "flow-lifecycle: clean -- all lifecycle transitions verified."

EXIT CRITERIA: All lifecycle phases evaluated.
State: "flow-lifecycle complete: [N] phases, [N] failures, [N] CONFIRMED, [N] RUNTIME ANOMALY."

---

## PHASE 5 -- flow-trigger

| Trigger | Expected fire order | Actual fire order | Race condition? | Phase 2 escalation role? | Phase tag | CONFIRMED / RUNTIME ANOMALY |
|---------|---------------------|-------------------|-----------------|--------------------------|-----------|------------------------------|

Phase 2 escalation role = yes if trigger involves a Phase 2 escalation role: blast radius = wide.

If clean: "flow-trigger: clean -- all triggers verified."

EXIT CRITERIA: All triggers and activating events evaluated.
State: "flow-trigger complete: [N] triggers, [N] failures, [N] CONFIRMED, [N] RUNTIME ANOMALY."

---

## CALIBRATION BLOCK

Q1: Does any finding's blast radius change when the propagation chain is traced to terminus?
For each finding: trace the full propagation chain ([origin] -> ... -> [terminal]). Does the
chain reach a Phase 0 shared state surface? If yes, upgrade to wide. List every revision and show
the full chain for each reclassified finding.

Q2: Do any Phase 4-5 findings match topology violations from Phases 1-3?
Confirm CONFIRMED or RUNTIME ANOMALY for each Phase 4-5 finding. Verify that every CONFIRMED
finding includes the inline evidence citation in field 6. List all reclassifications.

Q3: Which findings appear in three or more phases?
For every SYSTEMIC finding: "SYSTEMIC: yes -- phases: [phase-name-1], [phase-name-2], [phase-name-3]"
Binary SYSTEMIC flags are not valid.

Q4: Does the blast radius pre-classification map from Phases 1-2 hold throughout?
For every finding involving a Phase 2 escalation role or Phase 1 state surface: verify wide.
Revise and explain any finding below wide for a pre-classified component.

Q5: Would any finding below have shipped without this simulation?
For each wide-blast-radius finding: name the assumption it would have bypassed.

Q6: Did the execution sequence deliver its pre-classification guarantee?
Review every blast radius value in the consolidated findings. Were any revised post-hoc because
a finding touched a state surface or escalation role that Phase 1 or Phase 2 had not yet classified
at the time the downstream phase ran?
- Zero revisions: "Anchor guarantee delivered -- Phase 1 and Phase 2 pre-classified all blast radius
  values before downstream phases consumed them."
- Any revision: log each as an anchor violation -- name the finding, the downstream phase, and the
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
3. Blast radius: [wide | medium | narrow] -- propagation chain: [origin] -> [component] -> [terminal]
4. Severity at epicenter: [high | med | low]
5. SYSTEMIC: [yes -- phases: [comma-separated phase list] | no]
6. Classification: [CONFIRMED -- evidence: [matching phase name]: [matching finding description] | RUNTIME ANOMALY -- no topology match in Phases 1-3 | isolated]
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
State CONFIRMED (with evidence: [phase]: [finding]) or RUNTIME ANOMALY. If SYSTEMIC, list the
corroborating phases.
State the assumption the team would have carried into implementation had this simulation not run.
Conclude: proceed, proceed with conditions, or halt.
```

---

## V-04 -- Chain Terminus Registry + Dedicated Executive Summary (combination)
**Axis:** Combines V-01 (Chain Terminus Registry in Phase 0) and V-02 (Dedicated Executive Summary
before ranked findings). No other structural changes from R8 V-05.
**Hypothesis:** V-01 and V-02 are structurally independent -- V-01 adds a lookup table in Phase 0
that validates chain termini; V-02 adds a heading in CONSOLIDATE that surfaces top-3 before the
full list. They operate at different structural layers (input vocabulary vs output communication)
and should not interfere. If both independently pass at 90/90, combination should hold 90/90
under v7. The combination also tests whether two C-27 candidates can be introduced simultaneously
without the EXECUTIVE SUMMARY bullets conflicting with the T-NN registry citation format in
field 3.

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
Format: [origin] -> [component-B] -> [T-NN terminal]
The terminal must be a named entry in the Phase 0 Chain Terminus Registry (T-NN).
Blast radius label is derived from the chain terminus: if T-NN is classified as a shared state
surface or multi-role access point, classify wide. Chains that cannot resolve to a T-NN entry
must be flagged: "unresolved chain -- registry miss: [component name not in registry]."

SYSTEMIC = a finding corroborated across three or more phases.
Required format: "SYSTEMIC: yes -- phases: [phase-name-1], [phase-name-2], [phase-name-3]"
Binary "SYSTEMIC: yes" without a phase list is not valid and will be rejected.

CONFIRMED = a Phase 4 or Phase 5 finding that matches a topology violation from Phases 1-3.
Match is structural: same component, access pattern, contract term, or state surface.
Name the matching Phase 1-3 finding when classifying CONFIRMED.

RUNTIME ANOMALY = a Phase 4 or Phase 5 finding with no matching topology violation in Phases 1-3.

Tiebreaker protocol:
1. Blast radius descending (wide > medium > narrow)
2. CONFIRMED > RUNTIME ANOMALY
3. SYSTEMIC > isolated
State this protocol before the consolidated ranking. If no ties exist, state that explicitly.

---

## PHASE 0 -- Topology census

Before any sub-skill runs, record the system vocabulary explicitly.

**Components in scope:** [every named service, module, API, schema, queue from the spec]

**Shared state surfaces:** [databases, caches, event buses, config objects read or written by
multiple components -- blast-radius amplifiers; any propagation chain reaching these = wide]

**Downstream callers:** [every component that depends on outputs from this system]

**Role-resource inventory:** [every role and the resources it may access]

**Pre-declared contracts:** [every producer/consumer contract term the spec commits to --
the CONFIRMED classification baseline for Phases 4-5]

**Chain Terminus Registry:**
List every valid blast-radius terminus point in numbered form. Every propagation chain in the
CONSOLIDATE block must terminate at a named entry here.

| T-NN | Terminus name | Type | Blast radius floor |
|------|---------------|------|--------------------|
| T-01 | [component name] | [shared state surface / downstream caller / multi-role access point] | [wide / medium] |
| ...  | ...             | ...  | ... |

Every blast radius claim must name a specific census entry.
Every propagation chain must terminate at a T-NN registry entry. Chains that exit the registry
are flagged "unresolved chain" and excluded from ranking until the registry is updated.

---

## PHASE 1 -- trace-state [ANCHOR: state topology pre-classifies blast radius candidates for all downstream phases]

trace-state runs first. State topology -- shared states, multi-party transitions, cross-component
invariants -- pre-classifies blast radius candidates before contract, access, or flow analysis.
Downstream sub-skills inherit this map; none re-derive it independently.

| From state | To state | Trigger | Invariant | Invariant holds? | Shared state surface? | Blast radius candidate |
|------------|----------|---------|-----------|------------------|-----------------------|------------------------|

For each shared state surface = yes: record blast radius candidate as wide. Classification locked
for downstream phases.

If no violations: "trace-state: clean -- all invariants verified."

EXIT CRITERIA: All state transitions and invariants evaluated. No transitions deferred.
State: "trace-state complete: [N] transitions evaluated, [N] violations found, [N] pre-classified wide."

---

## PHASE 2 -- trace-permissions [ANCHOR: privilege boundary classification anchors flow blast radius assessment]

trace-permissions runs second, before all flow sub-skills. Privilege boundary classification must
precede flow analysis -- flow violations crossing a privilege boundary are SYSTEMIC by definition.
Without this anchor, flow sub-skills may understate propagation scope.

| Role | Resource | Action | Permitted? | Escalation path? | Phase 1 state surface involved? | Blast radius ceiling |
|------|----------|--------|------------|------------------|---------------------------------|----------------------|

Phase 1 state surface involved = yes and escalation path = yes: blast radius ceiling = wide (compound anchor hit).

If clean: "trace-permissions: clean -- all role-resource pairs verified, no escalation paths detected."

EXIT CRITERIA: All role-resource pairs evaluated. No pairs deferred.
State: "trace-permissions complete: [N] pairs evaluated, [N] escalation paths found, [N] compound anchor hits."

---

## PHASE 3 -- trace-contract

| Producer | Consumer | Contract term | Expected | Actual | Mismatch? | Phase 1/2 topology match? |
|----------|----------|---------------|----------|--------|-----------|--------------------------|

Phase 1/2 topology match = yes if contract involves a Phase 1 state violation surface or Phase 2
escalation role. If match = yes: classify CONFIRMED. Name the matching phase finding.

If clean: "trace-contract: clean -- all contracts verified."

EXIT CRITERIA: All producer/consumer pairs evaluated.
State: "trace-contract complete: [N] pairs evaluated, [N] mismatches found, [N] CONFIRMED."

---

## PHASE 4 -- flow-lifecycle

| Phase | Entry contract | Exit contract | Exception path | Exception handled? | Phase tag | CONFIRMED / RUNTIME ANOMALY |
|-------|----------------|---------------|----------------|--------------------|-----------|-----------------------------|

Phase tag = lifecycle phase of violation (INIT, ACTIVE, SUSPENDED, TERMINAL, etc.).
CONFIRMED = matches a Phase 1-3 violation. Name the match.
RUNTIME ANOMALY = no matching topology violation.

If clean: "flow-lifecycle: clean -- all lifecycle transitions verified."

EXIT CRITERIA: All lifecycle phases evaluated.
State: "flow-lifecycle complete: [N] phases, [N] failures, [N] CONFIRMED, [N] RUNTIME ANOMALY."

---

## PHASE 5 -- flow-trigger

| Trigger | Expected fire order | Actual fire order | Race condition? | Phase 2 escalation role? | Phase tag | CONFIRMED / RUNTIME ANOMALY |
|---------|---------------------|-------------------|-----------------|--------------------------|-----------|------------------------------|

Phase 2 escalation role = yes if trigger involves a Phase 2 escalation role: blast radius = wide.

If clean: "flow-trigger: clean -- all triggers verified."

EXIT CRITERIA: All triggers and activating events evaluated.
State: "flow-trigger complete: [N] triggers, [N] failures, [N] CONFIRMED, [N] RUNTIME ANOMALY."

---

## CALIBRATION BLOCK

Q1: Does any finding's blast radius change when the propagation chain is traced to terminus?
For each finding: trace the full propagation chain ([origin] -> ... -> [T-NN terminal]). Does the
T-NN registry entry carry blast radius floor = wide? If yes, upgrade to wide. List every revision
and show the full chain for each reclassified finding. Flag any chain that cannot resolve to a
T-NN entry as "unresolved chain."

Q2: Do any Phase 4-5 findings match topology violations from Phases 1-3?
Confirm CONFIRMED or RUNTIME ANOMALY for each Phase 4-5 finding. List all reclassifications.

Q3: Which findings appear in three or more phases?
For every SYSTEMIC finding: "SYSTEMIC: yes -- phases: [phase-name-1], [phase-name-2], [phase-name-3]"
Binary SYSTEMIC flags are not valid.

Q4: Does the blast radius pre-classification map from Phases 1-2 hold throughout?
For every finding involving a Phase 2 escalation role or Phase 1 state surface: verify wide.
Revise and explain any finding below wide for a pre-classified component.

Q5: Would any finding below have shipped without this simulation?
For each wide-blast-radius finding: name the assumption it would have bypassed.

Q6: Did the execution sequence deliver its pre-classification guarantee?
Review every blast radius value in the consolidated findings. Were any revised post-hoc because
a finding touched a state surface or escalation role that Phase 1 or Phase 2 had not yet classified
at the time the downstream phase ran?
- Zero revisions: "Anchor guarantee delivered -- Phase 1 and Phase 2 pre-classified all blast radius
  values before downstream phases consumed them."
- Any revision: log each as an anchor violation -- name the finding, the downstream phase, and the
  Phase 1/2 classification that arrived too late.

---

## CONSOLIDATE

Write ONE report. Do not concatenate five phase outputs.

Tiebreaker protocol: (1) Blast radius descending, (2) CONFIRMED > RUNTIME ANOMALY,
(3) SYSTEMIC > isolated. State whether any ties were encountered and how they were resolved.

## EXECUTIVE SUMMARY

Three bullet points. One per top-ranked finding. Write this section before the full findings list.
Each bullet: [F-NN] [blast-radius tier] -- [origin] -> [T-NN terminal] -- [CONFIRMED/RUNTIME ANOMALY]
A reader assessing campaign risk reads these three lines and has the full risk signal.

- [F-01] [blast-radius tier] -- [origin] -> [T-NN terminal] -- [CONFIRMED/RUNTIME ANOMALY]
- [F-02] [blast-radius tier] -- [origin] -> [T-NN terminal] -- [CONFIRMED/RUNTIME ANOMALY]
- [F-03] [blast-radius tier] -- [origin] -> [T-NN terminal] -- [CONFIRMED/RUNTIME ANOMALY]

**Ranked findings (calibrated blast radius order, wide first):**

For each finding, use this atomic block exactly:

---
**Finding [N]**
1. Name: [finding name or short description]
2. Source phase: [phase name]
3. Blast radius: [wide | medium | narrow] -- propagation chain: [origin] -> [component] -> [T-NN terminal]
4. Severity at epicenter: [high | med | low]
5. SYSTEMIC: [yes -- phases: [comma-separated phase list] | no]
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
State the propagation chain from origin to T-NN terminal blast surface.
State CONFIRMED or RUNTIME ANOMALY. If SYSTEMIC, list the corroborating phases.
State the assumption the team would have carried into implementation had this simulation not run.
Conclude: proceed, proceed with conditions, or halt.
```

---

## V-05 -- Full combination (Chain Terminus Registry + Executive Summary + inline CONFIRMED citation + R8 V-05 max coverage)
**Axis:** All three R9 axes combined with the full R8 V-05 baseline: (1) Phase 0 Chain Terminus
Registry with T-NN numbering scheme, (2) dedicated EXECUTIVE SUMMARY section with T-NN chain
references before ranked findings, (3) field 6 inline CONFIRMED evidence citation. All R8 V-05
structural features retained: [ANCHOR:] tags on Ph1/Ph2 headers, Q6 sequence integrity gate,
propagation chain in field 3, DEFINITIONS, VERDICT.
**Hypothesis:** V-01, V-02, V-03 test each R9 axis in isolation. V-05 tests whether all three
compose without interference and without disturbing the R8 V-05 baseline. Three specific
interference risks: (a) T-NN notation in field 3 vs C-26 propagation chain format, (b) EXECUTIVE
SUMMARY bullet format with T-NN vs C-16 pass condition, (c) inline field 6 citation format vs
C-07 (confirmation status field) and C-19 (7-field block). V-05 is the maximum redundancy target.

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
Format: [origin] -> [component-B] -> [T-NN terminal]
The terminal must be a named entry in the Phase 0 Chain Terminus Registry (T-NN).
Blast radius label is derived from the chain terminus: if T-NN is classified as a shared state
surface or multi-role access point, classify wide. Chains that cannot resolve to a T-NN entry
must be flagged: "unresolved chain -- registry miss: [component name not in registry]."

SYSTEMIC = a finding corroborated across three or more phases.
Required format: "SYSTEMIC: yes -- phases: [phase-name-1], [phase-name-2], [phase-name-3]"
Binary "SYSTEMIC: yes" without a phase list is not valid and will be rejected.

CONFIRMED = a Phase 4 or Phase 5 finding that matches a topology violation from Phases 1-3.
Match is structural: same component, access pattern, contract term, or state surface.
Field 6 format for CONFIRMED: "CONFIRMED -- evidence: [matching phase name]: [matching finding description]"
This citation is required. CONFIRMED without an inline evidence citation = incomplete block.

RUNTIME ANOMALY = a Phase 4 or Phase 5 finding with no matching topology violation in Phases 1-3.
Field 6 format for RUNTIME ANOMALY: "RUNTIME ANOMALY -- no topology match in Phases 1-3"

Tiebreaker protocol:
1. Blast radius descending (wide > medium > narrow)
2. CONFIRMED > RUNTIME ANOMALY
3. SYSTEMIC > isolated
State this protocol before the consolidated ranking. If no ties exist, state that explicitly.

---

## PHASE 0 -- Topology census

Before any sub-skill runs, record the system vocabulary explicitly.

**Components in scope:** [every named service, module, API, schema, queue from the spec]

**Shared state surfaces:** [databases, caches, event buses, config objects read or written by
multiple components -- blast-radius amplifiers; any propagation chain reaching these = wide]

**Downstream callers:** [every component that depends on outputs from this system]

**Role-resource inventory:** [every role and the resources it may access]

**Pre-declared contracts:** [every producer/consumer contract term the spec commits to --
the CONFIRMED classification baseline for Phases 4-5]

**Chain Terminus Registry:**
List every valid blast-radius terminus point in numbered form. Every propagation chain in the
CONSOLIDATE block must terminate at a named entry here. Chains that exit the registry are
flagged "unresolved chain" and excluded from ranking until the registry is updated.

| T-NN | Terminus name | Type | Blast radius floor |
|------|---------------|------|--------------------|
| T-01 | [component name] | [shared state surface / downstream caller / multi-role access point] | [wide / medium] |
| ...  | ...             | ...  | ... |

Every blast radius claim must name a specific census entry.
Every propagation chain must terminate at a T-NN registry entry.

---

## PHASE 1 -- trace-state [ANCHOR: state topology pre-classifies blast radius candidates for all downstream phases]

trace-state runs first. State topology -- shared states, multi-party transitions, cross-component
invariants -- pre-classifies blast radius candidates before contract, access, or flow analysis.
Downstream sub-skills inherit this map; none re-derive it independently.

| From state | To state | Trigger | Invariant | Invariant holds? | Shared state surface? | Blast radius candidate |
|------------|----------|---------|-----------|------------------|-----------------------|------------------------|

For each shared state surface = yes: record blast radius candidate as wide. Classification locked
for downstream phases.

If no violations: "trace-state: clean -- all invariants verified."

EXIT CRITERIA: All state transitions and invariants evaluated. No transitions deferred.
State: "trace-state complete: [N] transitions evaluated, [N] violations found, [N] pre-classified wide."

---

## PHASE 2 -- trace-permissions [ANCHOR: privilege boundary classification anchors flow blast radius assessment]

trace-permissions runs second, before all flow sub-skills. Privilege boundary classification must
precede flow analysis -- flow violations crossing a privilege boundary are SYSTEMIC by definition.
Without this anchor, flow sub-skills may understate propagation scope.

| Role | Resource | Action | Permitted? | Escalation path? | Phase 1 state surface involved? | Blast radius ceiling |
|------|----------|--------|------------|------------------|---------------------------------|----------------------|

Phase 1 state surface involved = yes and escalation path = yes: blast radius ceiling = wide (compound anchor hit).

If clean: "trace-permissions: clean -- all role-resource pairs verified, no escalation paths detected."

EXIT CRITERIA: All role-resource pairs evaluated. No pairs deferred.
State: "trace-permissions complete: [N] pairs evaluated, [N] escalation paths found, [N] compound anchor hits."

---

## PHASE 3 -- trace-contract

| Producer | Consumer | Contract term | Expected | Actual | Mismatch? | Phase 1/2 topology match? |
|----------|----------|---------------|----------|--------|-----------|--------------------------|

Phase 1/2 topology match = yes if contract involves a Phase 1 state violation surface or Phase 2
escalation role. If match = yes: classify CONFIRMED. Name the matching phase finding.

If clean: "trace-contract: clean -- all contracts verified."

EXIT CRITERIA: All producer/consumer pairs evaluated.
State: "trace-contract complete: [N] pairs evaluated, [N] mismatches found, [N] CONFIRMED."

---

## PHASE 4 -- flow-lifecycle

| Phase | Entry contract | Exit contract | Exception path | Exception handled? | Phase tag | CONFIRMED / RUNTIME ANOMALY |
|-------|----------------|---------------|----------------|--------------------|-----------|-----------------------------|

Phase tag = lifecycle phase of violation (INIT, ACTIVE, SUSPENDED, TERMINAL, etc.).
CONFIRMED = matches a Phase 1-3 violation. Use field 6 inline citation format. Name the match.
RUNTIME ANOMALY = no matching topology violation.

If clean: "flow-lifecycle: clean -- all lifecycle transitions verified."

EXIT CRITERIA: All lifecycle phases evaluated.
State: "flow-lifecycle complete: [N] phases, [N] failures, [N] CONFIRMED, [N] RUNTIME ANOMALY."

---

## PHASE 5 -- flow-trigger

| Trigger | Expected fire order | Actual fire order | Race condition? | Phase 2 escalation role? | Phase tag | CONFIRMED / RUNTIME ANOMALY |
|---------|---------------------|-------------------|-----------------|--------------------------|-----------|------------------------------|

Phase 2 escalation role = yes if trigger involves a Phase 2 escalation role: blast radius = wide.

If clean: "flow-trigger: clean -- all triggers verified."

EXIT CRITERIA: All triggers and activating events evaluated.
State: "flow-trigger complete: [N] triggers, [N] failures, [N] CONFIRMED, [N] RUNTIME ANOMALY."

---

## CALIBRATION BLOCK

Q1: Does any finding's blast radius change when the propagation chain is traced to terminus?
For each finding: trace the full propagation chain ([origin] -> ... -> [T-NN terminal]). Does the
T-NN registry entry carry blast radius floor = wide? If yes, upgrade to wide regardless of
intermediate component count. List every revision and show the full chain for each reclassified
finding. Flag any chain that cannot resolve to a T-NN entry as "unresolved chain."

Q2: Do any Phase 4-5 findings match topology violations from Phases 1-3?
Confirm CONFIRMED or RUNTIME ANOMALY for each Phase 4-5 finding. Verify that every CONFIRMED
finding includes the inline evidence citation in field 6 format. List all reclassifications.

Q3: Which findings appear in three or more phases?
For every SYSTEMIC finding: "SYSTEMIC: yes -- phases: [phase-name-1], [phase-name-2], [phase-name-3]"
Binary SYSTEMIC flags are not valid.

Q4: Does the blast radius pre-classification map from Phases 1-2 hold throughout?
For every finding involving a Phase 2 escalation role or Phase 1 state surface: verify wide.
Revise and explain any finding below wide for a pre-classified component.

Q5: Would any finding below have shipped without this simulation?
For each wide-blast-radius finding: name the assumption it would have bypassed.

Q6: Did the execution sequence deliver its pre-classification guarantee?
Review every blast radius value in the consolidated findings. Were any revised post-hoc because
a finding touched a state surface or escalation role that Phase 1 or Phase 2 had not yet classified
at the time the downstream phase ran?
- Zero revisions: "Anchor guarantee delivered -- Phase 1 and Phase 2 pre-classified all blast radius
  values before downstream phases consumed them."
- Any revision: log each as an anchor violation -- name the finding, the downstream phase, and the
  Phase 1/2 classification that arrived too late.

---

## CONSOLIDATE

Write ONE report. Do not concatenate five phase outputs.

Tiebreaker protocol: (1) Blast radius descending, (2) CONFIRMED > RUNTIME ANOMALY,
(3) SYSTEMIC > isolated. State whether any ties were encountered and how they were resolved.

## EXECUTIVE SUMMARY

Three bullet points. One per top-ranked finding. Write this section before the full findings list.
Each bullet: [F-NN] [blast-radius tier] -- [origin] -> [T-NN terminal] -- [CONFIRMED -- evidence: [phase]: [match] | RUNTIME ANOMALY]
A reader assessing campaign risk reads these three lines and has blast radius, propagation chain,
and confirmation evidence without opening the full findings list.

- [F-01] [blast-radius tier] -- [origin] -> [T-NN terminal] -- [CONFIRMED -- evidence: [phase]: [match] | RUNTIME ANOMALY]
- [F-02] [blast-radius tier] -- [origin] -> [T-NN terminal] -- [CONFIRMED -- evidence: [phase]: [match] | RUNTIME ANOMALY]
- [F-03] [blast-radius tier] -- [origin] -> [T-NN terminal] -- [CONFIRMED -- evidence: [phase]: [match] | RUNTIME ANOMALY]

**Ranked findings (calibrated blast radius order, wide first):**

For each finding, use this atomic block exactly:

---
**Finding [N]**
1. Name: [finding name or short description]
2. Source phase: [phase name]
3. Blast radius: [wide | medium | narrow] -- propagation chain: [origin] -> [component] -> [T-NN terminal]
4. Severity at epicenter: [high | med | low]
5. SYSTEMIC: [yes -- phases: [comma-separated phase list] | no]
6. Classification: [CONFIRMED -- evidence: [matching phase name]: [matching finding description] | RUNTIME ANOMALY -- no topology match in Phases 1-3 | isolated]
7. What must change: [one concrete fix direction in spec, contract, or implementation]
---

**Spec gaps:** [list each gap with missing-clause citation, or "none detected"]

**Contract violations:** [list each with producer and consumer named, or "none detected"]

**Privilege escalation paths:** [list each, or "none detected"]

**Clean zones:** [Phase 0 census components with no findings across all five phases]

---

## VERDICT

One paragraph. Name the finding with the widest blast radius by its Phase 0 census component name.
State the propagation chain from origin to T-NN terminal blast surface.
State CONFIRMED (with evidence: [phase]: [matching finding]) or RUNTIME ANOMALY. If SYSTEMIC,
list the corroborating phases.
State the assumption the team would have carried into implementation had this simulation not run.
Conclude: proceed, proceed with conditions, or halt.
```

---

## Axis summary

| Variation | Axis | New candidate |
|-----------|------|---------------|
| V-01 | Chain Terminus Registry (Phase 0 T-NN table) | C-27 candidate: terminus lookup replaces DEFINITIONS prose for chain validation |
| V-02 | Dedicated Executive Summary section | C-28 candidate: unambiguous C-16 surface by explicit heading |
| V-03 | Inline CONFIRMED evidence citation (field 6) | C-27 candidate (alternative): evidence citation becomes structural field requirement |
| V-04 | V-01 + V-02 | Tests T-NN in EXECUTIVE SUMMARY bullets; checks for interference between Phase 0 vocab extension and CONSOLIDATE output layer |
| V-05 | All three axes + R8 V-05 max coverage | Interference test: T-NN in field 3 (C-26), EXECUTIVE SUMMARY with T-NN (C-16), inline field 6 (C-07/C-19) |
