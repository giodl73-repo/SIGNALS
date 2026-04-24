Written to `simulations/quest/variations/campaign-behavior-variations-R13-2026-03-17.md`.

---

## R13 Variations — Summary

**Context:** R12 V-05 already achieves 29/29. R13 shifts from enforcement-structure experiments to prompt engineering experiments — three stylistic/framing axes that test what can change without breaking existing criteria.

### Axes

| Variation | Axis | Key change |
|-----------|------|------------|
| V-01 | Phrasing register: condensed-imperative | Rationale paragraphs stripped to one-liner minimum; all structural elements preserved |
| V-02 | Lifecycle emphasis: exception path in all phases | Exception path sub-table added to every phase (1-5), not just flow-lifecycle |
| V-03 | Inertia framing: I-NN assumption inventory | Phase 0 gains a locked I-NN inventory; Q5 cross-references I-NN codes; VERDICT cites the overridden assumption |
| V-04 | V-01 + V-02 | Condensed register + exception expansion combined |
| V-05 | V-01 + V-02 + V-03 | Full integration — all three axes |

### Key structural decisions

**V-01** keeps the [ANCHOR:...] tags and one-liner rationale for C-22/C-23 — strips everything beyond the minimum-viable stated-rationale. Tests whether verbose rationale is load-bearing or redundant.

**V-02** adds exception path sub-tables to Phases 1–3 and 5 (Phase 4 already had exception path columns). EXIT CRITERIA in each phase gains an exception path enumeration count. All T-NN exit gates still fire on both nominal and exception chains.

**V-03** introduces I-NN namespace (parallel to T-NN). Inertia inventory locks at Phase 0 close. If a finding overrides an undeclared assumption, it becomes a meta-finding — the simulation discovered an assumption the team did not know it held. Candidate v12 criterion pattern.

**V-05** is the full integration candidate. The interaction hypothesis: condensed rationale prose + expanded phase bodies may degrade C-22/C-23 if the anchor ordering rationale becomes hard to locate amid exception sub-tables. This is the scoring risk to watch in the R13 scorecard.
tia framing)

---

### Axes table

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | Phrasing register: condensed-imperative | Minimal rationale prose still satisfies C-22/C-23 stated-rationale pass conditions; all 37 criteria hold with lower token overhead |
| V-02 | Lifecycle emphasis: exception path in all phases | Exception path sub-tables in Phases 1-3 surface spec gaps missed by the nominal-path table format; finding density increases |
| V-03 | Inertia framing: I-NN assumption inventory | Explicit I-NN inertia codes in Phase 0 make Q5 mechanical and VERDICT assumption field traceable to a Phase 0 record rather than reconstructed from memory |
| V-04 | V-01 + V-02 | Condensed prose + exception depth: tests whether minimal phrasing survives when phase bodies grow due to exception sub-tables |
| V-05 | V-01 + V-02 + V-03 | Full integration: minimal register, full exception coverage, explicit inertia — tests whether combining all three axes preserves enforcement architecture or reveals interaction degradation |

---

## V-01 — Phrasing Register: Condensed-Imperative
**Axis:** Strip rationale paragraphs from phase bodies and DEFINITIONS elaborations to their
minimum viable form. Structural elements — [ANCHOR:...] tags, T-NN notation, exit gate statements,
all calibration questions, VALIDITY RULES, Q7, Q8 — are preserved verbatim. Only discursive
rationale prose is condensed.
**Hypothesis:** The v11 rubric requires "stated rationale" for C-22 and C-23 (anchor ordering
justification) but does not require verbose rationale. A one-clause rationale that links execution
order to the pre-classification benefit should satisfy the pass condition while reducing prompt
surface area. If V-01 scores identically to R12 V-05 under v11, the rationale paragraphs are
redundant. If C-22 or C-23 degrade to PARTIAL, the one-liner rationale is insufficient for those
pass conditions.

```
Simulate the technical behavior of: {{topic}}

---

## DEFINITIONS

Blast radius = propagation scope of a failure.
Wide: corrupts shared state, breaks downstream callers, or blocks multiple user roles simultaneously.
Medium: two or more components affected; no shared state surface reached.
Narrow: failure contained within one component boundary.

Severity = damage depth at the epicenter (high / med / low). Independent of blast radius. Never merge.
Report as separate labeled fields in every finding.

Propagation chain = ordered sequence of Phase 0 census components from origin to terminal blast surface.
Format: [origin] -> [component-B] -> [terminal: T-NN]
Terminal must resolve to a T-NN entry. Chains that cannot resolve: flag "unresolved chain -- registry miss."

T-NN = terminus registry code. Phase 0 registry is the single source of truth. No entry may be added,
removed, or renamed after Phase 0 is locked. Referenced in field 3, EXECUTIVE SUMMARY bullets, and Q1.

SYSTEMIC = finding corroborated across three or more phases.
Required format: "SYSTEMIC: yes -- phases: [phase-name-1], [phase-name-2], [phase-name-3]"
Binary "SYSTEMIC: yes" without a phase list is not valid and will be rejected.

CONFIRMED = Phase 4 or Phase 5 finding matching a topology violation from Phases 1-3.
Required format: "CONFIRMED -- evidence: [source-phase]: [matching-finding-name]"
Omitting the evidence citation invalidates the CONFIRMED classification.

RUNTIME ANOMALY = Phase 4 or Phase 5 finding with no matching topology violation in Phases 1-3.

Tiebreaker protocol:
1. Blast radius descending (wide > medium > narrow)
2. CONFIRMED > RUNTIME ANOMALY
3. SYSTEMIC > isolated
State this protocol before the consolidated ranking. If no ties exist, state that explicitly.

---

## PHASE 0 -- Topology census

Record the system vocabulary before any sub-skill runs.

**Components in scope:** [every named service, module, API, schema, queue from the spec]

**Shared state surfaces:** [databases, caches, event buses, config objects read or written by
multiple components -- any propagation chain reaching these = wide]

**Downstream callers:** [every component that depends on outputs from this system]

**Role-resource inventory:** [every role and the resources it may access]

**Pre-declared contracts:** [every producer/consumer contract term the spec commits to --
the CONFIRMED classification baseline for Phases 4-5]

**Terminus registry:**

| T-NN | Terminus component | Type |
|------|--------------------|------|
| T-01 | [component name]   | [shared-state | downstream-caller | role-boundary] |
| ...  | ...                | ... |

Assign a T-NN code to every unique blast-surface endpoint. Propagation chains must terminate at
a T-NN entry. Chains that cannot resolve = registry miss.

**Registry lock:** Terminus registry is complete.
No terminus component may be added, removed, or renamed after this point.
All chains in Phases 1-5 must resolve to a T-NN entry or be flagged "unresolved chain -- registry
miss: [component name]." Components not in this registry encountered during phases = spec gap
(undeclared blast surface); do not silently add.
State: "Registry locked: [N] terminus entries. Phase execution may begin."

---

## PHASE 1 -- trace-state [ANCHOR: state topology pre-classifies blast radius candidates for downstream phases]

trace-state runs first. Pre-classifies blast radius from shared-state topology; downstream phases
inherit this map and do not re-derive it.

| From state | To state | Trigger | Invariant | Invariant holds? | Shared state surface? | Blast radius candidate |
|------------|----------|---------|-----------|------------------|-----------------------|------------------------|

For each shared state surface = yes: blast radius candidate = wide. Classification locked for
downstream phases.

If no violations: "trace-state: clean -- all invariants verified."

EXIT CRITERIA: All state transitions and invariants evaluated. No transitions deferred.
State: "trace-state complete: [N] transitions evaluated, [N] violations found, [N] pre-classified wide."
T-NN resolution check: All propagation chains produced in this phase resolve to T-NN registry entries.
State: "[N] chains produced, [N] resolved to T-NN, [N] registry miss."
If any registry miss: flag "unresolved chain -- registry miss: [component name]" and carry forward to Q1.

---

## PHASE 2 -- trace-permissions [ANCHOR: privilege boundary classification anchors flow blast radius assessment]

trace-permissions runs second, before all flow sub-skills. Flow violations crossing a privilege
boundary are SYSTEMIC by definition; anchor must precede flow analysis.

| Role | Resource | Action | Permitted? | Escalation path? | Phase 1 state surface involved? | Blast radius ceiling |
|------|----------|--------|------------|------------------|---------------------------------|----------------------|

Phase 1 state surface involved = yes and escalation path = yes: blast radius ceiling = wide
(compound anchor hit).

If clean: "trace-permissions: clean -- all role-resource pairs verified, no escalation paths detected."

EXIT CRITERIA: All role-resource pairs evaluated. No pairs deferred.
State: "trace-permissions complete: [N] pairs evaluated, [N] escalation paths found, [N] compound anchor hits."
T-NN resolution check: All propagation chains produced in this phase resolve to T-NN registry entries.
State: "[N] chains produced, [N] resolved to T-NN, [N] registry miss."
If any registry miss: flag "unresolved chain -- registry miss: [component name]" and carry forward to Q1.

---

## PHASE 3 -- trace-contract

| Producer | Consumer | Contract term | Expected | Actual | Mismatch? | Phase 1/2 topology match? |
|----------|----------|---------------|----------|--------|-----------|--------------------------|

Phase 1/2 topology match = yes if contract involves a Phase 1 state violation surface or Phase 2
escalation role. If match = yes: classify CONFIRMED -- evidence: [phase-1|phase-2]: [matching-finding-name].

If clean: "trace-contract: clean -- all contracts verified."

EXIT CRITERIA: All producer/consumer pairs evaluated.
State: "trace-contract complete: [N] pairs evaluated, [N] mismatches found, [N] CONFIRMED."
T-NN resolution check: All propagation chains produced in this phase resolve to T-NN registry entries.
State: "[N] chains produced, [N] resolved to T-NN, [N] registry miss."
If any registry miss: flag "unresolved chain -- registry miss: [component name]" and carry forward to Q1.

---

## PHASE 4 -- flow-lifecycle

| Phase | Entry contract | Exit contract | Exception path | Exception handled? | Phase tag | CONFIRMED / RUNTIME ANOMALY |
|-------|----------------|---------------|----------------|--------------------|-----------|-----------------------------|

Phase tag = lifecycle phase of violation (INIT, ACTIVE, SUSPENDED, TERMINAL, etc.).
CONFIRMED = matches a Phase 1-3 violation: CONFIRMED -- evidence: [source-phase]: [matching-finding-name]
RUNTIME ANOMALY = no matching topology violation.

If clean: "flow-lifecycle: clean -- all lifecycle transitions verified."

EXIT CRITERIA: All lifecycle phases evaluated.
State: "flow-lifecycle complete: [N] phases, [N] failures, [N] CONFIRMED, [N] RUNTIME ANOMALY."
T-NN resolution check: All propagation chains produced in this phase resolve to T-NN registry entries.
State: "[N] chains produced, [N] resolved to T-NN, [N] registry miss."
If any registry miss: flag "unresolved chain -- registry miss: [component name]" and carry forward to Q1.

---

## PHASE 5 -- flow-trigger

| Trigger | Expected fire order | Actual fire order | Race condition? | Phase 2 escalation role? | Phase tag | CONFIRMED / RUNTIME ANOMALY |
|---------|---------------------|-------------------|-----------------|--------------------------|-----------|------------------------------|

Phase 2 escalation role = yes: blast radius = wide.
CONFIRMED -- evidence: [source-phase]: [matching-finding-name] | RUNTIME ANOMALY

If clean: "flow-trigger: clean -- all triggers verified."

EXIT CRITERIA: All triggers and activating events evaluated.
State: "flow-trigger complete: [N] triggers, [N] failures, [N] CONFIRMED, [N] RUNTIME ANOMALY."
T-NN resolution check: All propagation chains produced in this phase resolve to T-NN registry entries.
State: "[N] chains produced, [N] resolved to T-NN, [N] registry miss."
If any registry miss: flag "unresolved chain -- registry miss: [component name]" and carry forward to Q1.

---

## CALIBRATION BLOCK

Q1: Trace each finding's propagation chain to its T-NN terminus. Does the chain reach a Phase 0
shared-state entry? If yes, upgrade to wide. List every revision and full chain. Flag any chain
that cannot resolve: "unresolved chain -- registry miss."

Q2: For each Phase 4-5 finding classified CONFIRMED: verify inline citation format
"CONFIRMED -- evidence: [source-phase]: [matching-finding-name]." Revise any CONFIRMED
classification missing this citation. Also verify: for any finding entering EXECUTIVE SUMMARY as
CONFIRMED, confirm the same inline citation format will be used (not a plain [CONFIRMED] token).
Note any summary slots that would use plain tokens -- revise after Q7.

Q3: For every SYSTEMIC finding: "SYSTEMIC: yes -- phases: [phase-name-1], [phase-name-2], [phase-name-3]"
Binary SYSTEMIC flags are not valid.

Q4: For every finding involving a Phase 2 escalation role or Phase 1 state surface: verify wide.
Revise and explain any finding below wide for a pre-classified component.

Q5: For each wide-blast-radius finding: name the assumption it would have bypassed had this
simulation not run.

Q6: Did the execution sequence deliver its pre-classification guarantee?
Review blast radius values. Were any revised post-hoc because a finding touched a state surface or
escalation role that Phase 1 or Phase 2 had not yet classified?
- Zero revisions: "Anchor guarantee delivered -- Phase 1 and Phase 2 pre-classified all blast radius
  values before downstream phases consumed them."
- Any revision: log each as an anchor violation -- name the finding, the downstream phase, and the
  Phase 1/2 classification that arrived too late.

---

## EXECUTIVE SUMMARY

Write exactly 3 bullets. First bullet = highest blast radius; third = third.
If fewer than 3 findings exist, write the available count and note the shortfall.

Format for each bullet exactly:
- F-[N]: [finding name] | blast-radius: [wide|medium|narrow] | chain: [origin] -> [component] -> [terminal: T-NN] | [CONFIRMED -- evidence: [phase]: [finding] | RUNTIME ANOMALY]

VALIDITY RULES for this section:
1. Chain terminus must use a T-NN code from the Phase 0 registry (e.g., T-04), not a free-form
   component name. A bullet with a free-form terminus is INVALID.
   If a chain cannot resolve to a T-NN code, write "unresolved chain -- registry miss: [name]"
   and exclude until resolved via Q1.
2. Confirmation slot must carry the inline evidence citation format:
   CONFIRMED -- evidence: [source-phase]: [matching-finding-name]
   Plain [CONFIRMED] token is NOT valid in EXECUTIVE SUMMARY bullets.

Do not summarize. Do not add prose. Three structured bullets, then stop.

---

## Q7 -- EXECUTIVE SUMMARY structural audit

Before writing CONSOLIDATE, audit the EXECUTIVE SUMMARY bullets you just wrote.

For each bullet:
- C-30 check: Does the chain field terminate at a T-NN code (e.g., -> T-04), not a free-form
  component name? If free-form name found: identify the matching T-NN entry from the Phase 0
  registry and rewrite the bullet with the T-NN code. If no T-NN entry resolves: flag
  "unresolved chain -- registry miss" and exclude from ranking.
- C-31 check: Does the confirmation slot use "CONFIRMED -- evidence: [source-phase]: [finding-name]"
  format? If plain [CONFIRMED] found without inline citation: rewrite using the citation verified
  in Q2. If no Q2 citation exists for this finding: reclassify as RUNTIME ANOMALY.

State the result of each check:
- "Bullet F-[N]: C-30 PASS (terminal: T-NN), C-31 PASS (inline citation present)"
- OR list the revision made and the corrected bullet text.

If all three bullets pass both checks: "EXECUTIVE SUMMARY audit complete -- C-30 and C-31 satisfied
for all three bullets. Proceeding to CONSOLIDATE."

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
3. Blast radius: [wide | medium | narrow] -- propagation chain: [origin] -> [component] -> [terminal: T-NN]
4. Severity at epicenter: [high | med | low]
5. SYSTEMIC: [yes -- phases: [comma-separated phase list] | no]
6. Classification: [CONFIRMED -- evidence: [source-phase]: [matching-finding-name] | RUNTIME ANOMALY | isolated]
7. What must change: [one concrete fix direction in spec, contract, or implementation]
---

**Spec gaps:** [list each gap with missing-clause citation, or "none detected"]

**Contract violations:** [list each with producer and consumer named, or "none detected"]

**Privilege escalation paths:** [list each, or "none detected"]

**Clean zones:** [Phase 0 census components with no findings across all five phases]

---

## Q8 -- CONSOLIDATE finding block completeness gate

Before writing VERDICT, audit every finding block written in CONSOLIDATE.

For each finding block [N]:
- 7-field check: All seven fields (Name, Source phase, Blast radius, Severity, SYSTEMIC,
  Classification, What must change) are present and non-empty.
  If any field is missing or blank: identify the field and state the required content.
- T-NN chain check: Field 3 blast radius chain terminates at a T-NN code from the Phase 0
  registry (e.g., [terminal: T-04]), not a free-form component name.
  If free-form terminus found: identify the matching T-NN entry and rewrite field 3.
  If no T-NN entry resolves: flag "unresolved chain -- registry miss: [component name]."
- Classification format check: Field 6 uses "CONFIRMED -- evidence: [source-phase]: [finding-name]"
  format, or RUNTIME ANOMALY, or isolated.
  Plain [CONFIRMED] without inline citation is NOT valid. Rewrite using Q2-verified citation,
  or reclassify as RUNTIME ANOMALY if no Q2 citation exists.

State the result for each block:
- "Finding [N]: 7-field PASS, T-NN PASS (terminal: T-NN), classification PASS"
- OR list the revision made and the corrected field content.

If all blocks pass all checks: "CONSOLIDATE audit complete -- all [N] finding blocks satisfy
7-field, T-NN chain, and classification requirements. Proceeding to VERDICT."

---

## VERDICT

One paragraph. Name the finding with the widest blast radius by its Phase 0 census component name.
State the propagation chain from origin to terminal blast surface, including the T-NN terminus code.
State CONFIRMED -- evidence: [source-phase]: [matching-finding-name], or RUNTIME ANOMALY.
If SYSTEMIC, list the corroborating phases.
State the assumption the team would have carried into implementation had this simulation not run.
Conclude: proceed, proceed with conditions, or halt.
```

---

## V-02 -- Lifecycle Emphasis: Exception Path Sub-Table in Every Phase
**Axis:** Every phase (1-5) gains a mandatory exception path sub-table after the nominal-path table.
Each exception condition must be enumerated, assigned a blast radius, and evaluated for T-NN chain
resolution. Phase EXIT CRITERIA require both nominal and exception path completion statements.
**Hypothesis:** The v11 rubric (C-05) requires flow-lifecycle to evaluate exception paths. Trace
phases (1-3) currently evaluate only nominal paths. Adding exception path sub-tables to Phases 1-3
tests whether state transition failures, permission check failures, and contract invocation failures
under exception conditions produce findings the nominal table misses. If V-02 scores higher finding
density than R12 V-05 on real topics, exception path expansion in trace phases is a v12 candidate.

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
Format: [origin] -> [component-B] -> [terminal: T-NN]
The terminal must resolve to a T-NN entry in the Phase 0 terminus registry.
Chains that cannot resolve to a T-NN entry must be flagged: "unresolved chain -- registry miss."

T-NN = terminus registry code. Assigned in Phase 0 to every unique propagation chain endpoint
(shared state surface, downstream caller boundary, or role-boundary that terminates blast).
The Phase 0 registry is the single source of truth. No T-NN entry may be added, removed, or
renamed after Phase 0 is locked. Referenced in field 3 of every finding, in EXECUTIVE SUMMARY
bullets, and in chain-to-terminus tracing during Q1.

SYSTEMIC = a finding corroborated across three or more phases.
Required format: "SYSTEMIC: yes -- phases: [phase-name-1], [phase-name-2], [phase-name-3]"
Binary "SYSTEMIC: yes" without a phase list is not valid and will be rejected.

CONFIRMED = a Phase 4 or Phase 5 finding that matches a topology violation from Phases 1-3.
Match is structural: same component, access pattern, contract term, or state surface.
Required format when classifying CONFIRMED:
  "CONFIRMED -- evidence: [source-phase]: [matching-finding-name]"
Omitting the evidence citation invalidates the CONFIRMED classification.

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

**Terminus registry:**

| T-NN | Terminus component | Type |
|------|--------------------|------|
| T-01 | [component name]   | [shared-state | downstream-caller | role-boundary] |
| ...  | ...                | ... |

Assign a T-NN code to every unique blast-surface endpoint in the system. Propagation chains
in findings below must terminate at a T-NN entry. Chains that cannot resolve = registry miss.

Every blast radius claim must name a specific census entry.
Every propagation chain must terminate at a T-NN registry code.

**Registry lock:** The terminus registry is now complete.
No terminus component may be added, removed, or renamed after this point.
All propagation chains in Phases 1-5 must resolve to a T-NN entry from this registry or be
flagged "unresolved chain -- registry miss: [component name]."
Any component encountered in Phases 1-5 that is not in this registry must be recorded as a
spec gap (undeclared blast surface) -- it may not be silently added to the registry.
State: "Registry locked: [N] terminus entries. Phase execution may begin."

---

## PHASE 1 -- trace-state [ANCHOR: state topology pre-classifies blast radius candidates for all downstream phases]

trace-state runs first. State topology -- shared states, multi-party transitions, cross-component
invariants -- pre-classifies blast radius candidates before contract, access, or flow analysis.
Downstream sub-skills inherit this map; none re-derive it independently.

**Nominal paths:**

| From state | To state | Trigger | Invariant | Invariant holds? | Shared state surface? | Blast radius candidate |
|------------|----------|---------|-----------|------------------|-----------------------|------------------------|

For each shared state surface = yes: record blast radius candidate as wide. Classification locked
for downstream phases.

**Exception paths:** For each state transition above, evaluate what happens when the transition
fails, is interrupted, or encounters an unexpected input. Enumerate every exception condition.

| Transition | Exception condition | Component that handles it | Blast radius if unhandled | Spec clause covering this? |
|------------|---------------------|---------------------------|--------------------------|---------------------------|

For any exception condition with no spec clause covering it: record as spec gap.
For any exception condition whose unhandled blast radius = wide: assign T-NN terminus, record
blast radius candidate.

If no violations (nominal or exception): "trace-state: clean -- all invariants verified, all
exception paths handled."

EXIT CRITERIA: All state transitions and invariants evaluated on nominal paths. No transitions
deferred. All exception paths enumerated for each transition.
State: "trace-state complete: [N] transitions evaluated, [N] violations found, [N] pre-classified wide, [N] exception paths evaluated, [N] exception spec gaps."
T-NN resolution check: All propagation chains produced in this phase (nominal and exception) resolve
to T-NN registry entries.
State: "[N] chains produced, [N] resolved to T-NN, [N] registry miss."
If any registry miss: flag "unresolved chain -- registry miss: [component name]" and carry forward to Q1.

---

## PHASE 2 -- trace-permissions [ANCHOR: privilege boundary classification anchors flow blast radius assessment]

trace-permissions runs second, before all flow sub-skills. Privilege boundary classification must
precede flow analysis -- flow violations crossing a privilege boundary are SYSTEMIC by definition.
Without this anchor, flow sub-skills may understate propagation scope.

**Nominal paths:**

| Role | Resource | Action | Permitted? | Escalation path? | Phase 1 state surface involved? | Blast radius ceiling |
|------|----------|--------|------------|------------------|---------------------------------|----------------------|

Phase 1 state surface involved = yes and escalation path = yes: blast radius ceiling = wide
(compound anchor hit).

**Exception paths:** For each role-resource pair, evaluate what happens when the permission check
itself encounters an exception -- e.g., the permission service is unavailable, the role assertion
is stale, or the resource boundary is ambiguous at runtime.

| Role-resource pair | Exception condition | Fail-open or fail-closed? | Blast radius if fail-open | Spec clause covering this? |
|--------------------|---------------------|--------------------------|--------------------------|---------------------------|

For any fail-open exception with no spec clause: record as spec gap.
For any fail-open exception whose blast radius = wide: assign T-NN terminus, record blast radius candidate.

If clean (nominal and exception): "trace-permissions: clean -- all role-resource pairs verified,
no escalation paths detected, all exception conditions handled."

EXIT CRITERIA: All role-resource pairs evaluated (nominal and exception). No pairs deferred.
State: "trace-permissions complete: [N] pairs evaluated, [N] escalation paths found, [N] compound anchor hits, [N] exception paths evaluated, [N] exception spec gaps."
T-NN resolution check: All propagation chains produced in this phase (nominal and exception) resolve
to T-NN registry entries.
State: "[N] chains produced, [N] resolved to T-NN, [N] registry miss."
If any registry miss: flag "unresolved chain -- registry miss: [component name]" and carry forward to Q1.

---

## PHASE 3 -- trace-contract

**Nominal paths:**

| Producer | Consumer | Contract term | Expected | Actual | Mismatch? | Phase 1/2 topology match? |
|----------|----------|---------------|----------|--------|-----------|--------------------------|

Phase 1/2 topology match = yes if contract involves a Phase 1 state violation surface or Phase 2
escalation role. If match = yes: classify CONFIRMED -- evidence: [phase-1|phase-2]: [matching-finding-name].
Name the matching finding from Phase 1 or Phase 2.

**Exception paths:** For each contract term, evaluate what happens when the invocation fails
at runtime -- e.g., the producer is unavailable, the payload schema is violated, or the consumer
receives a partial response.

| Contract term | Exception condition | Recovery contract | Blast radius if recovery absent | Spec clause covering this? |
|---------------|---------------------|-------------------|---------------------------------|---------------------------|

For any exception with no recovery contract in the spec: record as spec gap with the missing clause.
For any exception whose blast radius = wide and Phase 1/2 topology match = yes: classify CONFIRMED.

If clean: "trace-contract: clean -- all contracts verified, all exception paths handled."

EXIT CRITERIA: All producer/consumer pairs evaluated (nominal and exception). No pairs deferred.
State: "trace-contract complete: [N] pairs evaluated, [N] mismatches found, [N] CONFIRMED, [N] exception paths evaluated, [N] exception spec gaps."
T-NN resolution check: All propagation chains produced in this phase (nominal and exception) resolve
to T-NN registry entries.
State: "[N] chains produced, [N] resolved to T-NN, [N] registry miss."
If any registry miss: flag "unresolved chain -- registry miss: [component name]" and carry forward to Q1.

---

## PHASE 4 -- flow-lifecycle

**Nominal and exception paths (combined):**

| Phase | Entry contract | Exit contract | Exception path | Exception handled? | Phase tag | CONFIRMED / RUNTIME ANOMALY |
|-------|----------------|---------------|----------------|--------------------|-----------|-----------------------------|

Phase tag = lifecycle phase of violation (INIT, ACTIVE, SUSPENDED, TERMINAL, etc.).
CONFIRMED = matches a Phase 1-3 violation. Use format:
  CONFIRMED -- evidence: [source-phase]: [matching-finding-name]
RUNTIME ANOMALY = no matching topology violation.

**Exception sub-cases:** For each exception path in the table above, enumerate sub-cases
(concurrent exception conditions, recovery failures, re-entry during exception handling).

| Lifecycle phase | Exception sub-case | Blast radius | Spec clause covering this? |
|-----------------|--------------------|--------------|---------------------------|

If clean: "flow-lifecycle: clean -- all lifecycle transitions verified, all exception paths enumerated."

EXIT CRITERIA: All lifecycle phases evaluated. All exception paths and sub-cases enumerated.
State: "flow-lifecycle complete: [N] phases, [N] failures, [N] CONFIRMED, [N] RUNTIME ANOMALY, [N] exception sub-cases evaluated."
T-NN resolution check: All propagation chains produced in this phase resolve to T-NN registry entries.
State: "[N] chains produced, [N] resolved to T-NN, [N] registry miss."
If any registry miss: flag "unresolved chain -- registry miss: [component name]" and carry forward to Q1.

---

## PHASE 5 -- flow-trigger

**Nominal paths:**

| Trigger | Expected fire order | Actual fire order | Race condition? | Phase 2 escalation role? | Phase tag | CONFIRMED / RUNTIME ANOMALY |
|---------|---------------------|-------------------|-----------------|--------------------------|-----------|------------------------------|

Phase 2 escalation role = yes if trigger involves a Phase 2 escalation role: blast radius = wide.
CONFIRMED = matches a Phase 1-3 violation. Use format:
  CONFIRMED -- evidence: [source-phase]: [matching-finding-name]

**Exception paths:** For each trigger, evaluate what happens when it fires under exceptional
conditions -- duplicate fires, suppressed fires, fires with stale context, or fires during
phase-transition state.

| Trigger | Exception condition | Expected behavior | Actual behavior | Blast radius | Spec clause covering this? |
|---------|---------------------|-------------------|-----------------|--------------|---------------------------|

For any exception with no spec clause: record as spec gap. Phase 2 escalation role involved = wide.

If clean: "flow-trigger: clean -- all triggers verified, all exception paths enumerated."

EXIT CRITERIA: All triggers and activating events evaluated. All exception paths enumerated.
State: "flow-trigger complete: [N] triggers, [N] failures, [N] CONFIRMED, [N] RUNTIME ANOMALY, [N] exception paths evaluated."
T-NN resolution check: All propagation chains produced in this phase resolve to T-NN registry entries.
State: "[N] chains produced, [N] resolved to T-NN, [N] registry miss."
If any registry miss: flag "unresolved chain -- registry miss: [component name]" and carry forward to Q1.

---

## CALIBRATION BLOCK

Q1: Does any finding's blast radius change when the propagation chain is traced to its T-NN terminus?
For each finding: trace the full chain ([origin] -> ... -> [terminal: T-NN]). Does the chain reach
a Phase 0 shared-state T-NN entry? If yes, upgrade to wide. List every revision and the full chain.
Flag any finding whose chain cannot resolve to a T-NN entry: "unresolved chain -- registry miss."

Q2: Do any Phase 4-5 findings match topology violations from Phases 1-3?
For each Phase 4-5 finding classified as CONFIRMED: verify the inline citation is present using
format "CONFIRMED -- evidence: [source-phase]: [matching-finding-name]."
Any CONFIRMED classification missing this citation must be revised before consolidation.
Also verify: for any finding that will appear in the EXECUTIVE SUMMARY as CONFIRMED, confirm
that the same inline citation format will be used in the summary bullet (not a plain [CONFIRMED]
token). Note any summary slots that would use plain tokens -- revise those bullets after Q7.
List all reclassifications and citations verified or added.

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

## EXECUTIVE SUMMARY

Write exactly 3 bullets. These are your top-3 findings by blast-radius tier, identified by position
in this section. The first bullet is the highest-blast-radius finding; the third is the third.
If fewer than 3 findings exist, write the available count and note the shortfall.

Use this format for each bullet exactly:
- F-[N]: [finding name] | blast-radius: [wide|medium|narrow] | chain: [origin] -> [component] -> [terminal: T-NN] | [CONFIRMED -- evidence: [phase]: [finding] | RUNTIME ANOMALY]

VALIDITY RULES for this section:
1. Chain terminus must use a T-NN code from the Phase 0 registry (e.g., T-04), not a
   free-form component name. A bullet with a free-form terminus is INVALID.
   If a chain cannot resolve to a T-NN code, write "unresolved chain -- registry miss: [name]"
   and exclude until resolved via Q1.
2. Confirmation slot must carry the inline evidence citation format:
   CONFIRMED -- evidence: [source-phase]: [matching-finding-name]
   Plain [CONFIRMED] token is NOT valid in EXECUTIVE SUMMARY bullets.

Do not summarize. Do not add prose. Three structured bullets, then stop.

---

## Q7 -- EXECUTIVE SUMMARY structural audit

Before writing CONSOLIDATE, audit the EXECUTIVE SUMMARY bullets you just wrote.

For each bullet:
- C-30 check: Does the chain field terminate at a T-NN code (e.g., -> T-04), not a free-form
  component name? If free-form name found: identify the matching T-NN entry from the Phase 0
  registry and rewrite the bullet with the T-NN code. If no T-NN entry resolves: flag
  "unresolved chain -- registry miss" and exclude from ranking.
- C-31 check: Does the confirmation slot use "CONFIRMED -- evidence: [source-phase]: [finding-name]"
  format? If plain [CONFIRMED] found without inline citation: rewrite using the citation verified
  in Q2. If no Q2 citation exists for this finding: reclassify as RUNTIME ANOMALY.

State the result of each check:
- "Bullet F-[N]: C-30 PASS (terminal: T-NN), C-31 PASS (inline citation present)"
- OR list the revision made and the corrected bullet text.

If all three bullets pass both checks: "EXECUTIVE SUMMARY audit complete -- C-30 and C-31 satisfied
for all three bullets. Proceeding to CONSOLIDATE."

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
3. Blast radius: [wide | medium | narrow] -- propagation chain: [origin] -> [component] -> [terminal: T-NN]
4. Severity at epicenter: [high | med | low]
5. SYSTEMIC: [yes -- phases: [comma-separated phase list] | no]
6. Classification: [CONFIRMED -- evidence: [source-phase]: [matching-finding-name] | RUNTIME ANOMALY | isolated]
7. What must change: [one concrete fix direction in spec, contract, or implementation]
---

**Spec gaps:** [list each gap with missing-clause citation, or "none detected"]

**Contract violations:** [list each with producer and consumer named, or "none detected"]

**Privilege escalation paths:** [list each, or "none detected"]

**Clean zones:** [Phase 0 census components with no findings across all five phases]

---

## Q8 -- CONSOLIDATE finding block completeness gate

Before writing VERDICT, audit every finding block written in CONSOLIDATE.

For each finding block [N]:
- 7-field check: All seven fields (Name, Source phase, Blast radius, Severity, SYSTEMIC,
  Classification, What must change) are present and non-empty.
  If any field is missing or blank: identify the field and state the required content.
- T-NN chain check: Field 3 blast radius chain terminates at a T-NN code from the Phase 0
  registry (e.g., [terminal: T-04]), not a free-form component name.
  If free-form terminus found: identify the matching T-NN entry and rewrite field 3.
  If no T-NN entry resolves: flag "unresolved chain -- registry miss: [component name]."
- Classification format check: Field 6 uses "CONFIRMED -- evidence: [source-phase]: [finding-name]"
  format, or RUNTIME ANOMALY, or isolated.
  Plain [CONFIRMED] without inline citation is NOT valid. Rewrite using Q2-verified citation,
  or reclassify as RUNTIME ANOMALY if no Q2 citation exists.

State the result for each block:
- "Finding [N]: 7-field PASS, T-NN PASS (terminal: T-NN), classification PASS"
- OR list the revision made and the corrected field content.

If all blocks pass all checks: "CONSOLIDATE audit complete -- all [N] finding blocks satisfy
7-field, T-NN chain, and classification requirements. Proceeding to VERDICT."

---

## VERDICT

One paragraph. Name the finding with the widest blast radius by its Phase 0 census component name.
State the propagation chain from origin to terminal blast surface, including the T-NN terminus code.
State CONFIRMED -- evidence: [source-phase]: [matching-finding-name], or RUNTIME ANOMALY.
If SYSTEMIC, list the corroborating phases.
State the assumption the team would have carried into implementation had this simulation not run.
Conclude: proceed, proceed with conditions, or halt.
```

---

## V-03 -- Inertia Framing: I-NN Assumption Inventory
**Axis:** Phase 0 gains an inertia model -- a numbered I-NN inventory of the assumptions the team
would carry into implementation without this simulation. Q5 cross-references I-NN codes: every wide
finding must name the I-NN assumption it overrides. VERDICT must cite the I-NN assumption most
endangered by the campaign's top finding.
**Hypothesis:** Q5 currently asks for a free-form assumption description reconstructed backward from
findings. An I-NN inventory built before phases execute forces commitment to assumptions before
seeing findings, making Q5 a verification step (does this finding override I-NN?) rather than a
generation step (what assumption does this finding expose?). If this produces more precise Q5
outputs, inertia framing is a v12 candidate. The meta-finding pattern -- "assumption not in
inventory" -- tests whether simulation surfaces implicit beliefs the team did not know it held.

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
Format: [origin] -> [component-B] -> [terminal: T-NN]
The terminal must resolve to a T-NN entry in the Phase 0 terminus registry.
Chains that cannot resolve to a T-NN entry must be flagged: "unresolved chain -- registry miss."

T-NN = terminus registry code. Assigned in Phase 0 to every unique propagation chain endpoint
(shared state surface, downstream caller boundary, or role-boundary that terminates blast).
The Phase 0 registry is the single source of truth. No T-NN entry may be added, removed, or
renamed after Phase 0 is locked. Referenced in field 3 of every finding, in EXECUTIVE SUMMARY
bullets, and in chain-to-terminus tracing during Q1.

I-NN = inertia code. Assigned in Phase 0 to every assumption the team would carry into
implementation without this simulation. I-NN codes are referenced in Q5 and VERDICT to name
the assumption a finding overrides. Inertia inventory is locked at Phase 0 close: no new
assumptions may be added post-hoc. If a finding overrides an assumption not in the inventory,
that is a meta-finding: the simulation discovered an assumption the team did not know it held.

SYSTEMIC = a finding corroborated across three or more phases.
Required format: "SYSTEMIC: yes -- phases: [phase-name-1], [phase-name-2], [phase-name-3]"
Binary "SYSTEMIC: yes" without a phase list is not valid and will be rejected.

CONFIRMED = a Phase 4 or Phase 5 finding that matches a topology violation from Phases 1-3.
Match is structural: same component, access pattern, contract term, or state surface.
Required format when classifying CONFIRMED:
  "CONFIRMED -- evidence: [source-phase]: [matching-finding-name]"
Omitting the evidence citation invalidates the CONFIRMED classification.

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

**Terminus registry:**

| T-NN | Terminus component | Type |
|------|--------------------|------|
| T-01 | [component name]   | [shared-state | downstream-caller | role-boundary] |
| ...  | ...                | ... |

Assign a T-NN code to every unique blast-surface endpoint in the system. Propagation chains
in findings below must terminate at a T-NN entry. Chains that cannot resolve = registry miss.

Every blast radius claim must name a specific census entry.
Every propagation chain must terminate at a T-NN registry code.

**Registry lock:** The terminus registry is now complete.
No terminus component may be added, removed, or renamed after this point.
All propagation chains in Phases 1-5 must resolve to a T-NN entry from this registry or be
flagged "unresolved chain -- registry miss: [component name]."
Any component encountered in Phases 1-5 that is not in this registry must be recorded as a
spec gap (undeclared blast surface) -- it may not be silently added to the registry.
State: "Registry locked: [N] terminus entries. Phase execution may begin."

**Inertia inventory:** Before phases begin, enumerate the assumptions that would ship without
this simulation. These are implicit beliefs about safe defaults, handled edge cases, and
acceptable failure modes that the team holds prior to running the campaign.

| I-NN | Assumption | Domain | What would happen if wrong |
|------|------------|--------|---------------------------|
| I-01 | [assumption text] | [state | permissions | contract | lifecycle | trigger] | [consequence if this assumption is false] |
| ...  | ...        | ...    | ... |

Assign an I-NN code to every distinct assumption. Inertia inventory is now locked: no assumption
may be added after Phase 0 closes. If a phase finding overrides an assumption not listed here,
record it as a meta-finding: "I-NN inventory miss -- assumption not declared: [description]."
State: "Inertia inventory locked: [N] assumptions. Simulation may begin."

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
T-NN resolution check: All propagation chains produced in this phase resolve to T-NN registry entries.
State: "[N] chains produced, [N] resolved to T-NN, [N] registry miss."
If any registry miss: flag "unresolved chain -- registry miss: [component name]" and carry forward to Q1.

---

## PHASE 2 -- trace-permissions [ANCHOR: privilege boundary classification anchors flow blast radius assessment]

trace-permissions runs second, before all flow sub-skills. Privilege boundary classification must
precede flow analysis -- flow violations crossing a privilege boundary are SYSTEMIC by definition.
Without this anchor, flow sub-skills may understate propagation scope.

| Role | Resource | Action | Permitted? | Escalation path? | Phase 1 state surface involved? | Blast radius ceiling |
|------|----------|--------|------------|------------------|---------------------------------|----------------------|

Phase 1 state surface involved = yes and escalation path = yes: blast radius ceiling = wide
(compound anchor hit).

If clean: "trace-permissions: clean -- all role-resource pairs verified, no escalation paths detected."

EXIT CRITERIA: All role-resource pairs evaluated. No pairs deferred.
State: "trace-permissions complete: [N] pairs evaluated, [N] escalation paths found, [N] compound anchor hits."
T-NN resolution check: All propagation chains produced in this phase resolve to T-NN registry entries.
State: "[N] chains produced, [N] resolved to T-NN, [N] registry miss."
If any registry miss: flag "unresolved chain -- registry miss: [component name]" and carry forward to Q1.

---

## PHASE 3 -- trace-contract

| Producer | Consumer | Contract term | Expected | Actual | Mismatch? | Phase 1/2 topology match? |
|----------|----------|---------------|----------|--------|-----------|--------------------------|

Phase 1/2 topology match = yes if contract involves a Phase 1 state violation surface or Phase 2
escalation role. If match = yes: classify CONFIRMED -- evidence: [phase-1|phase-2]: [matching-finding-name].
Name the matching finding from Phase 1 or Phase 2.

If clean: "trace-contract: clean -- all contracts verified."

EXIT CRITERIA: All producer/consumer pairs evaluated.
State: "trace-contract complete: [N] pairs evaluated, [N] mismatches found, [N] CONFIRMED."
T-NN resolution check: All propagation chains produced in this phase resolve to T-NN registry entries.
State: "[N] chains produced, [N] resolved to T-NN, [N] registry miss."
If any registry miss: flag "unresolved chain -- registry miss: [component name]" and carry forward to Q1.

---

## PHASE 4 -- flow-lifecycle

| Phase | Entry contract | Exit contract | Exception path | Exception handled? | Phase tag | CONFIRMED / RUNTIME ANOMALY |
|-------|----------------|---------------|----------------|--------------------|-----------|-----------------------------|

Phase tag = lifecycle phase of violation (INIT, ACTIVE, SUSPENDED, TERMINAL, etc.).
CONFIRMED = matches a Phase 1-3 violation. Use format:
  CONFIRMED -- evidence: [source-phase]: [matching-finding-name]
RUNTIME ANOMALY = no matching topology violation.

If clean: "flow-lifecycle: clean -- all lifecycle transitions verified."

EXIT CRITERIA: All lifecycle phases evaluated.
State: "flow-lifecycle complete: [N] phases, [N] failures, [N] CONFIRMED, [N] RUNTIME ANOMALY."
T-NN resolution check: All propagation chains produced in this phase resolve to T-NN registry entries.
State: "[N] chains produced, [N] resolved to T-NN, [N] registry miss."
If any registry miss: flag "unresolved chain -- registry miss: [component name]" and carry forward to Q1.

---

## PHASE 5 -- flow-trigger

| Trigger | Expected fire order | Actual fire order | Race condition? | Phase 2 escalation role? | Phase tag | CONFIRMED / RUNTIME ANOMALY |
|---------|---------------------|-------------------|-----------------|--------------------------|-----------|------------------------------|

Phase 2 escalation role = yes if trigger involves a Phase 2 escalation role: blast radius = wide.
CONFIRMED = matches a Phase 1-3 violation. Use format:
  CONFIRMED -- evidence: [source-phase]: [matching-finding-name]

If clean: "flow-trigger: clean -- all triggers verified."

EXIT CRITERIA: All triggers and activating events evaluated.
State: "flow-trigger complete: [N] triggers, [N] failures, [N] CONFIRMED, [N] RUNTIME ANOMALY."
T-NN resolution check: All propagation chains produced in this phase resolve to T-NN registry entries.
State: "[N] chains produced, [N] resolved to T-NN, [N] registry miss."
If any registry miss: flag "unresolved chain -- registry miss: [component name]" and carry forward to Q1.

---

## CALIBRATION BLOCK

Q1: Does any finding's blast radius change when the propagation chain is traced to its T-NN terminus?
For each finding: trace the full chain ([origin] -> ... -> [terminal: T-NN]). Does the chain reach
a Phase 0 shared-state T-NN entry? If yes, upgrade to wide. List every revision and the full chain.
Flag any finding whose chain cannot resolve to a T-NN entry: "unresolved chain -- registry miss."

Q2: Do any Phase 4-5 findings match topology violations from Phases 1-3?
For each Phase 4-5 finding classified as CONFIRMED: verify the inline citation is present using
format "CONFIRMED -- evidence: [source-phase]: [matching-finding-name]."
Any CONFIRMED classification missing this citation must be revised before consolidation.
Also verify: for any finding that will appear in the EXECUTIVE SUMMARY as CONFIRMED, confirm
that the same inline citation format will be used in the summary bullet (not a plain [CONFIRMED]
token). Note any summary slots that would use plain tokens -- revise those bullets after Q7.
List all reclassifications and citations verified or added.

Q3: Which findings appear in three or more phases?
For every SYSTEMIC finding: "SYSTEMIC: yes -- phases: [phase-name-1], [phase-name-2], [phase-name-3]"
Binary SYSTEMIC flags are not valid.

Q4: Does the blast radius pre-classification map from Phases 1-2 hold throughout?
For every finding involving a Phase 2 escalation role or Phase 1 state surface: verify wide.
Revise and explain any finding below wide for a pre-classified component.

Q5: Would any finding below have shipped without this simulation?
For each wide-blast-radius finding: name the I-NN assumption from the Phase 0 inertia inventory
that it overrides. Format: "Finding [N] overrides I-[N]: [assumption text]."
If a finding overrides an assumption not in the inventory: record as a meta-finding:
"I-NN inventory miss -- assumption not declared: [describe the undeclared assumption]."
If no wide findings exist: state "no wide findings -- inertia inventory not overridden."

Q6: Did the execution sequence deliver its pre-classification guarantee?
Review every blast radius value in the consolidated findings. Were any revised post-hoc because
a finding touched a state surface or escalation role that Phase 1 or Phase 2 had not yet classified
at the time the downstream phase ran?
- Zero revisions: "Anchor guarantee delivered -- Phase 1 and Phase 2 pre-classified all blast radius
  values before downstream phases consumed them."
- Any revision: log each as an anchor violation -- name the finding, the downstream phase, and the
  Phase 1/2 classification that arrived too late.

---

## EXECUTIVE SUMMARY

Write exactly 3 bullets. These are your top-3 findings by blast-radius tier, identified by position
in this section. The first bullet is the highest-blast-radius finding; the third is the third.
If fewer than 3 findings exist, write the available count and note the shortfall.

Use this format for each bullet exactly:
- F-[N]: [finding name] | blast-radius: [wide|medium|narrow] | chain: [origin] -> [component] -> [terminal: T-NN] | [CONFIRMED -- evidence: [phase]: [finding] | RUNTIME ANOMALY]

VALIDITY RULES for this section:
1. Chain terminus must use a T-NN code from the Phase 0 registry (e.g., T-04), not a
   free-form component name. A bullet with a free-form terminus is INVALID.
   If a chain cannot resolve to a T-NN code, write "unresolved chain -- registry miss: [name]"
   and exclude until resolved via Q1.
2. Confirmation slot must carry the inline evidence citation format:
   CONFIRMED -- evidence: [source-phase]: [matching-finding-name]
   Plain [CONFIRMED] token is NOT valid in EXECUTIVE SUMMARY bullets.

Do not summarize. Do not add prose. Three structured bullets, then stop.

---

## Q7 -- EXECUTIVE SUMMARY structural audit

Before writing CONSOLIDATE, audit the EXECUTIVE SUMMARY bullets you just wrote.

For each bullet:
- C-30 check: Does the chain field terminate at a T-NN code (e.g., -> T-04), not a free-form
  component name? If free-form name found: identify the matching T-NN entry from the Phase 0
  registry and rewrite the bullet with the T-NN code. If no T-NN entry resolves: flag
  "unresolved chain -- registry miss" and exclude from ranking.
- C-31 check: Does the confirmation slot use "CONFIRMED -- evidence: [source-phase]: [finding-name]"
  format? If plain [CONFIRMED] found without inline citation: rewrite using the citation verified
  in Q2. If no Q2 citation exists for this finding: reclassify as RUNTIME ANOMALY.

State the result of each check:
- "Bullet F-[N]: C-30 PASS (terminal: T-NN), C-31 PASS (inline citation present)"
- OR list the revision made and the corrected bullet text.

If all three bullets pass both checks: "EXECUTIVE SUMMARY audit complete -- C-30 and C-31 satisfied
for all three bullets. Proceeding to CONSOLIDATE."

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
3. Blast radius: [wide | medium | narrow] -- propagation chain: [origin] -> [component] -> [terminal: T-NN]
4. Severity at epicenter: [high | med | low]
5. SYSTEMIC: [yes -- phases: [comma-separated phase list] | no]
6. Classification: [CONFIRMED -- evidence: [source-phase]: [matching-finding-name] | RUNTIME ANOMALY | isolated]
7. What must change: [one concrete fix direction in spec, contract, or implementation]
---

**Spec gaps:** [list each gap with missing-clause citation, or "none detected"]

**Contract violations:** [list each with producer and consumer named, or "none detected"]

**Privilege escalation paths:** [list each, or "none detected"]

**Clean zones:** [Phase 0 census components with no findings across all five phases]

---

## Q8 -- CONSOLIDATE finding block completeness gate

Before writing VERDICT, audit every finding block written in CONSOLIDATE.

For each finding block [N]:
- 7-field check: All seven fields (Name, Source phase, Blast radius, Severity, SYSTEMIC,
  Classification, What must change) are present and non-empty.
  If any field is missing or blank: identify the field and state the required content.
- T-NN chain check: Field 3 blast radius chain terminates at a T-NN code from the Phase 0
  registry (e.g., [terminal: T-04]), not a free-form component name.
  If free-form terminus found: identify the matching T-NN entry and rewrite field 3.
  If no T-NN entry resolves: flag "unresolved chain -- registry miss: [component name]."
- Classification format check: Field 6 uses "CONFIRMED -- evidence: [source-phase]: [finding-name]"
  format, or RUNTIME ANOMALY, or isolated.
  Plain [CONFIRMED] without inline citation is NOT valid. Rewrite using Q2-verified citation,
  or reclassify as RUNTIME ANOMALY if no Q2 citation exists.

State the result for each block:
- "Finding [N]: 7-field PASS, T-NN PASS (terminal: T-NN), classification PASS"
- OR list the revision made and the corrected field content.

If all blocks pass all checks: "CONSOLIDATE audit complete -- all [N] finding blocks satisfy
7-field, T-NN chain, and classification requirements. Proceeding to VERDICT."

---

## VERDICT

One paragraph. Name the finding with the widest blast radius by its Phase 0 census component name.
State the propagation chain from origin to terminal blast surface, including the T-NN terminus code.
State CONFIRMED -- evidence: [source-phase]: [matching-finding-name], or RUNTIME ANOMALY.
If SYSTEMIC, list the corroborating phases.
Name the I-NN assumption from the Phase 0 inertia inventory that this finding overrides. Format:
"This finding overrides I-[N]: [assumption text]." If the assumption was not in the inventory,
state: "Assumption not declared in inertia inventory -- I-NN inventory miss."
Conclude: proceed, proceed with conditions, or halt.
```

---

## V-04 -- Combination: Condensed Register + Exception Path Expansion (V-01 + V-02)
**Axis:** V-01 phrasing register (condensed-imperative) combined with V-02 lifecycle emphasis
(exception path sub-tables in every phase). Rationale paragraphs are stripped to minimum viable
form while every phase body expands to include an explicit exception path sub-table.
**Hypothesis:** V-01 reduces token overhead; V-02 increases phase body volume. Combined: tests
whether compressed DEFINITIONS and minimal calibration phrasing still carry C-22/C-23
stated-rationale pass conditions when phase bodies grow in the other direction. Also tests whether
exception coverage from V-02 is preserved at condensed-register verbosity.

```
Simulate the technical behavior of: {{topic}}

---

## DEFINITIONS

Blast radius = propagation scope of a failure.
Wide: corrupts shared state, breaks downstream callers, or blocks multiple user roles simultaneously.
Medium: two or more components affected; no shared state surface reached.
Narrow: failure contained within one component boundary.

Severity = damage depth at the epicenter (high / med / low). Independent of blast radius. Never merge.
Report as separate labeled fields in every finding.

Propagation chain = ordered sequence of Phase 0 census components from origin to terminal blast surface.
Format: [origin] -> [component-B] -> [terminal: T-NN]
Terminal must resolve to a T-NN entry. Chains that cannot resolve: flag "unresolved chain -- registry miss."

T-NN = terminus registry code. Phase 0 registry is the single source of truth. No entry may be added,
removed, or renamed after Phase 0 is locked. Referenced in field 3, EXECUTIVE SUMMARY bullets, and Q1.

SYSTEMIC = finding corroborated across three or more phases.
Required format: "SYSTEMIC: yes -- phases: [phase-name-1], [phase-name-2], [phase-name-3]"
Binary "SYSTEMIC: yes" without a phase list is not valid and will be rejected.

CONFIRMED = Phase 4 or Phase 5 finding matching a topology violation from Phases 1-3.
Required format: "CONFIRMED -- evidence: [source-phase]: [matching-finding-name]"
Omitting the evidence citation invalidates the CONFIRMED classification.

RUNTIME ANOMALY = Phase 4 or Phase 5 finding with no matching topology violation in Phases 1-3.

Tiebreaker protocol:
1. Blast radius descending (wide > medium > narrow)
2. CONFIRMED > RUNTIME ANOMALY
3. SYSTEMIC > isolated
State this protocol before the consolidated ranking. If no ties exist, state that explicitly.

---

## PHASE 0 -- Topology census

Record the system vocabulary before any sub-skill runs.

**Components in scope:** [every named service, module, API, schema, queue from the spec]

**Shared state surfaces:** [databases, caches, event buses, config objects read or written by
multiple components -- any propagation chain reaching these = wide]

**Downstream callers:** [every component that depends on outputs from this system]

**Role-resource inventory:** [every role and the resources it may access]

**Pre-declared contracts:** [every producer/consumer contract term the spec commits to --
the CONFIRMED classification baseline for Phases 4-5]

**Terminus registry:**

| T-NN | Terminus component | Type |
|------|--------------------|------|
| T-01 | [component name]   | [shared-state | downstream-caller | role-boundary] |
| ...  | ...                | ... |

Assign a T-NN code to every unique blast-surface endpoint. Propagation chains must terminate at
a T-NN entry. Chains that cannot resolve = registry miss.

**Registry lock:** Terminus registry is complete.
No terminus component may be added, removed, or renamed after this point.
All chains in Phases 1-5 must resolve to a T-NN entry or be flagged "unresolved chain -- registry
miss: [component name]." Components not in this registry = spec gap; do not add silently.
State: "Registry locked: [N] terminus entries. Phase execution may begin."

---

## PHASE 1 -- trace-state [ANCHOR: state topology pre-classifies blast radius candidates for downstream phases]

trace-state runs first. Pre-classifies blast radius from shared-state topology; downstream phases
inherit this map and do not re-derive it.

**Nominal paths:**

| From state | To state | Trigger | Invariant | Invariant holds? | Shared state surface? | Blast radius candidate |
|------------|----------|---------|-----------|------------------|-----------------------|------------------------|

For each shared state surface = yes: blast radius candidate = wide. Classification locked.

**Exception paths:**

| Transition | Exception condition | Component that handles it | Blast radius if unhandled | Spec clause covering this? |
|------------|---------------------|---------------------------|--------------------------|---------------------------|

For any exception with no spec clause: record as spec gap. For any exception with blast radius = wide:
assign T-NN terminus.

If no violations (nominal or exception): "trace-state: clean -- all invariants verified, all exception paths handled."

EXIT CRITERIA: All transitions evaluated (nominal and exception). No transitions deferred.
State: "trace-state complete: [N] transitions evaluated, [N] violations found, [N] pre-classified wide, [N] exception paths evaluated, [N] exception spec gaps."
T-NN resolution check: All propagation chains produced in this phase resolve to T-NN registry entries.
State: "[N] chains produced, [N] resolved to T-NN, [N] registry miss."
If any registry miss: flag "unresolved chain -- registry miss: [component name]" and carry forward to Q1.

---

## PHASE 2 -- trace-permissions [ANCHOR: privilege boundary classification anchors flow blast radius assessment]

trace-permissions runs second, before all flow sub-skills. Flow violations crossing a privilege
boundary are SYSTEMIC by definition; anchor must precede flow analysis.

**Nominal paths:**

| Role | Resource | Action | Permitted? | Escalation path? | Phase 1 state surface involved? | Blast radius ceiling |
|------|----------|--------|------------|------------------|---------------------------------|----------------------|

Phase 1 state surface involved = yes and escalation path = yes: blast radius ceiling = wide (compound anchor hit).

**Exception paths:**

| Role-resource pair | Exception condition | Fail-open or fail-closed? | Blast radius if fail-open | Spec clause covering this? |
|--------------------|---------------------|--------------------------|--------------------------|---------------------------|

For any fail-open exception with no spec clause: record as spec gap.

If clean (nominal and exception): "trace-permissions: clean -- all pairs verified, no escalation paths, all exception conditions handled."

EXIT CRITERIA: All role-resource pairs evaluated (nominal and exception). No pairs deferred.
State: "trace-permissions complete: [N] pairs evaluated, [N] escalation paths found, [N] compound anchor hits, [N] exception paths evaluated, [N] exception spec gaps."
T-NN resolution check: All propagation chains produced in this phase resolve to T-NN registry entries.
State: "[N] chains produced, [N] resolved to T-NN, [N] registry miss."
If any registry miss: flag "unresolved chain -- registry miss: [component name]" and carry forward to Q1.

---

## PHASE 3 -- trace-contract

**Nominal paths:**

| Producer | Consumer | Contract term | Expected | Actual | Mismatch? | Phase 1/2 topology match? |
|----------|----------|---------------|----------|--------|-----------|--------------------------|

Phase 1/2 topology match = yes if contract involves a Phase 1 state violation surface or Phase 2
escalation role. If match = yes: classify CONFIRMED -- evidence: [phase-1|phase-2]: [matching-finding-name].

**Exception paths:**

| Contract term | Exception condition | Recovery contract | Blast radius if recovery absent | Spec clause covering this? |
|---------------|---------------------|-------------------|---------------------------------|---------------------------|

For any exception with no recovery contract in spec: record as spec gap with missing clause.
For any exception with Phase 1/2 topology match = yes: classify CONFIRMED.

If clean: "trace-contract: clean -- all contracts verified, all exception paths handled."

EXIT CRITERIA: All producer/consumer pairs evaluated (nominal and exception). No pairs deferred.
State: "trace-contract complete: [N] pairs evaluated, [N] mismatches found, [N] CONFIRMED, [N] exception paths evaluated, [N] exception spec gaps."
T-NN resolution check: All propagation chains produced in this phase resolve to T-NN registry entries.
State: "[N] chains produced, [N] resolved to T-NN, [N] registry miss."
If any registry miss: flag "unresolved chain -- registry miss: [component name]" and carry forward to Q1.

---

## PHASE 4 -- flow-lifecycle

**Nominal and exception paths:**

| Phase | Entry contract | Exit contract | Exception path | Exception handled? | Phase tag | CONFIRMED / RUNTIME ANOMALY |
|-------|----------------|---------------|----------------|--------------------|-----------|-----------------------------|

Phase tag = lifecycle phase (INIT, ACTIVE, SUSPENDED, TERMINAL, etc.).
CONFIRMED -- evidence: [source-phase]: [matching-finding-name] | RUNTIME ANOMALY

**Exception sub-cases:**

| Lifecycle phase | Exception sub-case | Blast radius | Spec clause covering this? |
|-----------------|--------------------|--------------|---------------------------|

If clean: "flow-lifecycle: clean -- all transitions verified, all exception paths enumerated."

EXIT CRITERIA: All phases evaluated. All exception paths enumerated.
State: "flow-lifecycle complete: [N] phases, [N] failures, [N] CONFIRMED, [N] RUNTIME ANOMALY, [N] exception sub-cases evaluated."
T-NN resolution check: All propagation chains produced in this phase resolve to T-NN registry entries.
State: "[N] chains produced, [N] resolved to T-NN, [N] registry miss."
If any registry miss: flag "unresolved chain -- registry miss: [component name]" and carry forward to Q1.

---

## PHASE 5 -- flow-trigger

**Nominal paths:**

| Trigger | Expected fire order | Actual fire order | Race condition? | Phase 2 escalation role? | Phase tag | CONFIRMED / RUNTIME ANOMALY |
|---------|---------------------|-------------------|-----------------|--------------------------|-----------|------------------------------|

Phase 2 escalation role = yes: blast radius = wide.
CONFIRMED -- evidence: [source-phase]: [matching-finding-name] | RUNTIME ANOMALY

**Exception paths:**

| Trigger | Exception condition | Expected behavior | Actual behavior | Blast radius | Spec clause covering this? |
|---------|---------------------|-------------------|-----------------|--------------|---------------------------|

For any exception with no spec clause: record as spec gap. Phase 2 escalation role involved = wide.

If clean: "flow-trigger: clean -- all triggers verified, all exception paths enumerated."

EXIT CRITERIA: All triggers evaluated. All exception paths enumerated.
State: "flow-trigger complete: [N] triggers, [N] failures, [N] CONFIRMED, [N] RUNTIME ANOMALY, [N] exception paths evaluated."
T-NN resolution check: All propagation chains produced in this phase resolve to T-NN registry entries.
State: "[N] chains produced, [N] resolved to T-NN, [N] registry miss."
If any registry miss: flag "unresolved chain -- registry miss: [component name]" and carry forward to Q1.

---

## CALIBRATION BLOCK

Q1: Trace each finding's propagation chain to its T-NN terminus. Does the chain reach a Phase 0
shared-state entry? If yes, upgrade to wide. List every revision and full chain. Flag any chain
that cannot resolve: "unresolved chain -- registry miss."

Q2: For each Phase 4-5 finding classified CONFIRMED: verify inline citation format
"CONFIRMED -- evidence: [source-phase]: [matching-finding-name]." Revise any CONFIRMED
classification missing this citation. Also verify: for any finding entering EXECUTIVE SUMMARY as
CONFIRMED, confirm the same inline citation format will be used (not a plain [CONFIRMED] token).
Note any summary slots that would use plain tokens -- revise after Q7.

Q3: For every SYSTEMIC finding: "SYSTEMIC: yes -- phases: [phase-name-1], [phase-name-2], [phase-name-3]"
Binary SYSTEMIC flags are not valid.

Q4: For every finding involving a Phase 2 escalation role or Phase 1 state surface: verify wide.
Revise and explain any finding below wide for a pre-classified component.

Q5: For each wide-blast-radius finding: name the assumption it would have bypassed had this
simulation not run.

Q6: Did the execution sequence deliver its pre-classification guarantee?
Review blast radius values. Were any revised post-hoc because a finding touched a state surface or
escalation role that Phase 1 or Phase 2 had not yet classified?
- Zero revisions: "Anchor guarantee delivered -- Phase 1 and Phase 2 pre-classified all blast radius
  values before downstream phases consumed them."
- Any revision: log each as an anchor violation -- name the finding, the downstream phase, and the
  Phase 1/2 classification that arrived too late.

---

## EXECUTIVE SUMMARY

Write exactly 3 bullets. First bullet = highest blast radius; third = third.
If fewer than 3 findings exist, write the available count and note the shortfall.

Format for each bullet exactly:
- F-[N]: [finding name] | blast-radius: [wide|medium|narrow] | chain: [origin] -> [component] -> [terminal: T-NN] | [CONFIRMED -- evidence: [phase]: [finding] | RUNTIME ANOMALY]

VALIDITY RULES for this section:
1. Chain terminus must use a T-NN code from the Phase 0 registry (e.g., T-04), not a free-form
   component name. A bullet with a free-form terminus is INVALID.
   If a chain cannot resolve to a T-NN code, write "unresolved chain -- registry miss: [name]"
   and exclude until resolved via Q1.
2. Confirmation slot must carry the inline evidence citation format:
   CONFIRMED -- evidence: [source-phase]: [matching-finding-name]
   Plain [CONFIRMED] token is NOT valid in EXECUTIVE SUMMARY bullets.

Do not summarize. Do not add prose. Three structured bullets, then stop.

---

## Q7 -- EXECUTIVE SUMMARY structural audit

Before writing CONSOLIDATE, audit the EXECUTIVE SUMMARY bullets you just wrote.

For each bullet:
- C-30 check: Does the chain field terminate at a T-NN code (e.g., -> T-04), not a free-form
  component name? If free-form name found: identify the matching T-NN entry and rewrite with T-NN
  code. If no T-NN entry resolves: flag "unresolved chain -- registry miss" and exclude.
- C-31 check: Does the confirmation slot use "CONFIRMED -- evidence: [source-phase]: [finding-name]"
  format? If plain [CONFIRMED] found: rewrite using Q2 citation or reclassify as RUNTIME ANOMALY.

State the result of each check:
- "Bullet F-[N]: C-30 PASS (terminal: T-NN), C-31 PASS (inline citation present)"
- OR list the revision made and the corrected bullet text.

If all three bullets pass both checks: "EXECUTIVE SUMMARY audit complete -- C-30 and C-31 satisfied
for all three bullets. Proceeding to CONSOLIDATE."

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
3. Blast radius: [wide | medium | narrow] -- propagation chain: [origin] -> [component] -> [terminal: T-NN]
4. Severity at epicenter: [high | med | low]
5. SYSTEMIC: [yes -- phases: [comma-separated phase list] | no]
6. Classification: [CONFIRMED -- evidence: [source-phase]: [matching-finding-name] | RUNTIME ANOMALY | isolated]
7. What must change: [one concrete fix direction in spec, contract, or implementation]
---

**Spec gaps:** [list each gap with missing-clause citation, or "none detected"]

**Contract violations:** [list each with producer and consumer named, or "none detected"]

**Privilege escalation paths:** [list each, or "none detected"]

**Clean zones:** [Phase 0 census components with no findings across all five phases]

---

## Q8 -- CONSOLIDATE finding block completeness gate

Before writing VERDICT, audit every finding block written in CONSOLIDATE.

For each finding block [N]:
- 7-field check: All seven fields (Name, Source phase, Blast radius, Severity, SYSTEMIC,
  Classification, What must change) are present and non-empty.
  If any field is missing or blank: identify the field and state the required content.
- T-NN chain check: Field 3 blast radius chain terminates at a T-NN code from the Phase 0
  registry (e.g., [terminal: T-04]), not a free-form component name.
  If free-form terminus found: identify the matching T-NN entry and rewrite field 3.
  If no T-NN entry resolves: flag "unresolved chain -- registry miss: [component name]."
- Classification format check: Field 6 uses "CONFIRMED -- evidence: [source-phase]: [finding-name]"
  format, or RUNTIME ANOMALY, or isolated.
  Plain [CONFIRMED] without inline citation is NOT valid. Rewrite using Q2-verified citation,
  or reclassify as RUNTIME ANOMALY if no Q2 citation exists.

State the result for each block:
- "Finding [N]: 7-field PASS, T-NN PASS (terminal: T-NN), classification PASS"
- OR list the revision made and the corrected field content.

If all blocks pass all checks: "CONSOLIDATE audit complete -- all [N] finding blocks satisfy
7-field, T-NN chain, and classification requirements. Proceeding to VERDICT."

---

## VERDICT

One paragraph. Name the finding with the widest blast radius by its Phase 0 census component name.
State the propagation chain from origin to terminal blast surface, including the T-NN terminus code.
State CONFIRMED -- evidence: [source-phase]: [matching-finding-name], or RUNTIME ANOMALY.
If SYSTEMIC, list the corroborating phases.
State the assumption the team would have carried into implementation had this simulation not run.
Conclude: proceed, proceed with conditions, or halt.
```

---

## V-05 -- Full Integration: Condensed Register + Exception Path Expansion + Inertia Framing (V-01 + V-02 + V-03)
**Axis:** All three R13 axes combined: V-01 condensed phrasing register, V-02 exception path
sub-tables in every phase, and V-03 I-NN inertia inventory in Phase 0.
**Hypothesis:** The three axes are structurally independent: condensed register reduces token
overhead (no structural change), exception sub-tables increase analysis depth per phase (structural
addition), inertia inventory adds a Phase 0 declaration (structural addition). Combined, they test
whether both enforcement pipelines -- EXECUTIVE SUMMARY (C-32/C-33/C-34) and CONSOLIDATE
(C-35/C-36/C-37) -- hold with minimal rationale prose, expanded phase bodies, and an additional
Phase 0 element. Interaction risk: expanded phase bodies with condensed headers may reduce C-22/C-23
rationale clarity. If V-05 scores below R12 V-05 on C-22/C-23, the axes are not independently
composable and rationale cannot be condensed when phase bodies are simultaneously expanded.

```
Simulate the technical behavior of: {{topic}}

---

## DEFINITIONS

Blast radius = propagation scope of a failure.
Wide: corrupts shared state, breaks downstream callers, or blocks multiple user roles simultaneously.
Medium: two or more components affected; no shared state surface reached.
Narrow: failure contained within one component boundary.

Severity = damage depth at the epicenter (high / med / low). Independent of blast radius. Never merge.
Report as separate labeled fields in every finding.

Propagation chain = ordered sequence of Phase 0 census components from origin to terminal blast surface.
Format: [origin] -> [component-B] -> [terminal: T-NN]
Terminal must resolve to a T-NN entry. Chains that cannot resolve: flag "unresolved chain -- registry miss."

T-NN = terminus registry code. Phase 0 registry is the single source of truth. No entry may be added,
removed, or renamed after Phase 0 is locked. Referenced in field 3, EXECUTIVE SUMMARY bullets, and Q1.

I-NN = inertia code. Assigned in Phase 0 to every assumption the team would carry into implementation
without this simulation. Referenced in Q5 and VERDICT. Inertia inventory is locked at Phase 0 close.
If a finding overrides an assumption not in the inventory: meta-finding
"I-NN inventory miss -- assumption not declared: [description]."

SYSTEMIC = finding corroborated across three or more phases.
Required format: "SYSTEMIC: yes -- phases: [phase-name-1], [phase-name-2], [phase-name-3]"
Binary "SYSTEMIC: yes" without a phase list is not valid and will be rejected.

CONFIRMED = Phase 4 or Phase 5 finding matching a topology violation from Phases 1-3.
Required format: "CONFIRMED -- evidence: [source-phase]: [matching-finding-name]"
Omitting the evidence citation invalidates the CONFIRMED classification.

RUNTIME ANOMALY = Phase 4 or Phase 5 finding with no matching topology violation in Phases 1-3.

Tiebreaker protocol:
1. Blast radius descending (wide > medium > narrow)
2. CONFIRMED > RUNTIME ANOMALY
3. SYSTEMIC > isolated
State this protocol before the consolidated ranking. If no ties exist, state that explicitly.

---

## PHASE 0 -- Topology census

Record the system vocabulary before any sub-skill runs.

**Components in scope:** [every named service, module, API, schema, queue from the spec]

**Shared state surfaces:** [databases, caches, event buses, config objects read or written by
multiple components -- any propagation chain reaching these = wide]

**Downstream callers:** [every component that depends on outputs from this system]

**Role-resource inventory:** [every role and the resources it may access]

**Pre-declared contracts:** [every producer/consumer contract term the spec commits to --
the CONFIRMED classification baseline for Phases 4-5]

**Terminus registry:**

| T-NN | Terminus component | Type |
|------|--------------------|------|
| T-01 | [component name]   | [shared-state | downstream-caller | role-boundary] |
| ...  | ...                | ... |

Assign a T-NN code to every unique blast-surface endpoint. Propagation chains must terminate at
a T-NN entry. Chains that cannot resolve = registry miss.

**Registry lock:** Terminus registry is complete.
No terminus component may be added, removed, or renamed after this point.
All chains in Phases 1-5 must resolve to a T-NN entry or be flagged "unresolved chain -- registry
miss: [component name]." Components not in this registry = spec gap; do not add silently.
State: "Registry locked: [N] terminus entries. Phase execution may begin."

**Inertia inventory:** Enumerate the assumptions that would ship without this simulation.

| I-NN | Assumption | Domain | What would happen if wrong |
|------|------------|--------|---------------------------|
| I-01 | [assumption text] | [state | permissions | contract | lifecycle | trigger] | [consequence if false] |
| ...  | ...        | ...    | ... |

Inertia inventory is now locked. No assumption may be added after Phase 0 closes.
If a finding overrides an assumption not listed here: meta-finding
"I-NN inventory miss -- assumption not declared: [description]."
State: "Inertia inventory locked: [N] assumptions. Simulation may begin."

---

## PHASE 1 -- trace-state [ANCHOR: state topology pre-classifies blast radius candidates for downstream phases]

trace-state runs first. Pre-classifies blast radius from shared-state topology; downstream phases
inherit this map and do not re-derive it.

**Nominal paths:**

| From state | To state | Trigger | Invariant | Invariant holds? | Shared state surface? | Blast radius candidate |
|------------|----------|---------|-----------|------------------|-----------------------|------------------------|

For each shared state surface = yes: blast radius candidate = wide. Classification locked.

**Exception paths:**

| Transition | Exception condition | Component that handles it | Blast radius if unhandled | Spec clause covering this? |
|------------|---------------------|---------------------------|--------------------------|---------------------------|

For any exception with no spec clause: record as spec gap. For any exception with blast radius = wide:
assign T-NN terminus.

If no violations (nominal or exception): "trace-state: clean -- all invariants verified, all exception paths handled."

EXIT CRITERIA: All transitions evaluated (nominal and exception). No transitions deferred.
State: "trace-state complete: [N] transitions evaluated, [N] violations found, [N] pre-classified wide, [N] exception paths evaluated, [N] exception spec gaps."
T-NN resolution check: All propagation chains produced in this phase resolve to T-NN registry entries.
State: "[N] chains produced, [N] resolved to T-NN, [N] registry miss."
If any registry miss: flag "unresolved chain -- registry miss: [component name]" and carry forward to Q1.

---

## PHASE 2 -- trace-permissions [ANCHOR: privilege boundary classification anchors flow blast radius assessment]

trace-permissions runs second, before all flow sub-skills. Flow violations crossing a privilege
boundary are SYSTEMIC by definition; anchor must precede flow analysis.

**Nominal paths:**

| Role | Resource | Action | Permitted? | Escalation path? | Phase 1 state surface involved? | Blast radius ceiling |
|------|----------|--------|------------|------------------|---------------------------------|----------------------|

Phase 1 state surface involved = yes and escalation path = yes: blast radius ceiling = wide (compound anchor hit).

**Exception paths:**

| Role-resource pair | Exception condition | Fail-open or fail-closed? | Blast radius if fail-open | Spec clause covering this? |
|--------------------|---------------------|--------------------------|--------------------------|---------------------------|

For any fail-open exception with no spec clause: record as spec gap.

If clean (nominal and exception): "trace-permissions: clean -- all pairs verified, no escalation paths, all exception conditions handled."

EXIT CRITERIA: All role-resource pairs evaluated (nominal and exception). No pairs deferred.
State: "trace-permissions complete: [N] pairs evaluated, [N] escalation paths found, [N] compound anchor hits, [N] exception paths evaluated, [N] exception spec gaps."
T-NN resolution check: All propagation chains produced in this phase resolve to T-NN registry entries.
State: "[N] chains produced, [N] resolved to T-NN, [N] registry miss."
If any registry miss: flag "unresolved chain -- registry miss: [component name]" and carry forward to Q1.

---

## PHASE 3 -- trace-contract

**Nominal paths:**

| Producer | Consumer | Contract term | Expected | Actual | Mismatch? | Phase 1/2 topology match? |
|----------|----------|---------------|----------|--------|-----------|--------------------------|

Phase 1/2 topology match = yes if contract involves a Phase 1 state violation surface or Phase 2
escalation role. If match = yes: classify CONFIRMED -- evidence: [phase-1|phase-2]: [matching-finding-name].

**Exception paths:**

| Contract term | Exception condition | Recovery contract | Blast radius if recovery absent | Spec clause covering this? |
|---------------|---------------------|-------------------|---------------------------------|---------------------------|

For any exception with no recovery contract in spec: record as spec gap with missing clause.
For any exception with Phase 1/2 topology match = yes: classify CONFIRMED.

If clean: "trace-contract: clean -- all contracts verified, all exception paths handled."

EXIT CRITERIA: All producer/consumer pairs evaluated (nominal and exception). No pairs deferred.
State: "trace-contract complete: [N] pairs evaluated, [N] mismatches found, [N] CONFIRMED, [N] exception paths evaluated, [N] exception spec gaps."
T-NN resolution check: All propagation chains produced in this phase resolve to T-NN registry entries.
State: "[N] chains produced, [N] resolved to T-NN, [N] registry miss."
If any registry miss: flag "unresolved chain -- registry miss: [component name]" and carry forward to Q1.

---

## PHASE 4 -- flow-lifecycle

**Nominal and exception paths:**

| Phase | Entry contract | Exit contract | Exception path | Exception handled? | Phase tag | CONFIRMED / RUNTIME ANOMALY |
|-------|----------------|---------------|----------------|--------------------|-----------|-----------------------------|

Phase tag = lifecycle phase (INIT, ACTIVE, SUSPENDED, TERMINAL, etc.).
CONFIRMED -- evidence: [source-phase]: [matching-finding-name] | RUNTIME ANOMALY

**Exception sub-cases:**

| Lifecycle phase | Exception sub-case | Blast radius | Spec clause covering this? |
|-----------------|--------------------|--------------|---------------------------|

If clean: "flow-lifecycle: clean -- all transitions verified, all exception paths enumerated."

EXIT CRITERIA: All phases evaluated. All exception paths enumerated.
State: "flow-lifecycle complete: [N] phases, [N] failures, [N] CONFIRMED, [N] RUNTIME ANOMALY, [N] exception sub-cases evaluated."
T-NN resolution check: All propagation chains produced in this phase resolve to T-NN registry entries.
State: "[N] chains produced, [N] resolved to T-NN, [N] registry miss."
If any registry miss: flag "unresolved chain -- registry miss: [component name]" and carry forward to Q1.

---

## PHASE 5 -- flow-trigger

**Nominal paths:**

| Trigger | Expected fire order | Actual fire order | Race condition? | Phase 2 escalation role? | Phase tag | CONFIRMED / RUNTIME ANOMALY |
|---------|---------------------|-------------------|-----------------|--------------------------|-----------|------------------------------|

Phase 2 escalation role = yes: blast radius = wide.
CONFIRMED -- evidence: [source-phase]: [matching-finding-name] | RUNTIME ANOMALY

**Exception paths:**

| Trigger | Exception condition | Expected behavior | Actual behavior | Blast radius | Spec clause covering this? |
|---------|---------------------|-------------------|-----------------|--------------|---------------------------|

For any exception with no spec clause: record as spec gap. Phase 2 escalation role involved = wide.

If clean: "flow-trigger: clean -- all triggers verified, all exception paths enumerated."

EXIT CRITERIA: All triggers evaluated. All exception paths enumerated.
State: "flow-trigger complete: [N] triggers, [N] failures, [N] CONFIRMED, [N] RUNTIME ANOMALY, [N] exception paths evaluated."
T-NN resolution check: All propagation chains produced in this phase resolve to T-NN registry entries.
State: "[N] chains produced, [N] resolved to T-NN, [N] registry miss."
If any registry miss: flag "unresolved chain -- registry miss: [component name]" and carry forward to Q1.

---

## CALIBRATION BLOCK

Q1: Trace each finding's propagation chain to its T-NN terminus. Does the chain reach a Phase 0
shared-state entry? If yes, upgrade to wide. List every revision and full chain. Flag any chain
that cannot resolve: "unresolved chain -- registry miss."

Q2: For each Phase 4-5 finding classified CONFIRMED: verify inline citation format
"CONFIRMED -- evidence: [source-phase]: [matching-finding-name]." Revise any CONFIRMED
classification missing this citation. Also verify: for any finding entering EXECUTIVE SUMMARY as
CONFIRMED, confirm the same inline citation format will be used (not a plain [CONFIRMED] token).
Note any summary slots that would use plain tokens -- revise after Q7.

Q3: For every SYSTEMIC finding: "SYSTEMIC: yes -- phases: [phase-name-1], [phase-name-2], [phase-name-3]"
Binary SYSTEMIC flags are not valid.

Q4: For every finding involving a Phase 2 escalation role or Phase 1 state surface: verify wide.
Revise and explain any finding below wide for a pre-classified component.

Q5: For each wide-blast-radius finding: name the I-NN assumption from the Phase 0 inertia inventory
that it overrides. Format: "Finding [N] overrides I-[N]: [assumption text]."
If a finding overrides an assumption not in the inventory: meta-finding:
"I-NN inventory miss -- assumption not declared: [describe the undeclared assumption]."
If no wide findings: state "no wide findings -- inertia inventory not overridden."

Q6: Did the execution sequence deliver its pre-classification guarantee?
Review blast radius values. Were any revised post-hoc because a finding touched a state surface or
escalation role that Phase 1 or Phase 2 had not yet classified?
- Zero revisions: "Anchor guarantee delivered -- Phase 1 and Phase 2 pre-classified all blast radius
  values before downstream phases consumed them."
- Any revision: log each as an anchor violation -- name the finding, the downstream phase, and the
  Phase 1/2 classification that arrived too late.

---

## EXECUTIVE SUMMARY

Write exactly 3 bullets. First bullet = highest blast radius; third = third.
If fewer than 3 findings exist, write the available count and note the shortfall.

Format for each bullet exactly:
- F-[N]: [finding name] | blast-radius: [wide|medium|narrow] | chain: [origin] -> [component] -> [terminal: T-NN] | [CONFIRMED -- evidence: [phase]: [finding] | RUNTIME ANOMALY]

VALIDITY RULES for this section:
1. Chain terminus must use a T-NN code from the Phase 0 registry (e.g., T-04), not a free-form
   component name. A bullet with a free-form terminus is INVALID.
   If a chain cannot resolve to a T-NN code, write "unresolved chain -- registry miss: [name]"
   and exclude until resolved via Q1.
2. Confirmation slot must carry the inline evidence citation format:
   CONFIRMED -- evidence: [source-phase]: [matching-finding-name]
   Plain [CONFIRMED] token is NOT valid in EXECUTIVE SUMMARY bullets.

Do not summarize. Do not add prose. Three structured bullets, then stop.

---

## Q7 -- EXECUTIVE SUMMARY structural audit

Before writing CONSOLIDATE, audit the EXECUTIVE SUMMARY bullets you just wrote.

For each bullet:
- C-30 check: Does the chain field terminate at a T-NN code (e.g., -> T-04), not a free-form
  component name? If free-form name found: identify the matching T-NN entry and rewrite with T-NN
  code. If no T-NN entry resolves: flag "unresolved chain -- registry miss" and exclude.
- C-31 check: Does the confirmation slot use "CONFIRMED -- evidence: [source-phase]: [finding-name]"
  format? If plain [CONFIRMED] found: rewrite using Q2 citation or reclassify as RUNTIME ANOMALY.

State the result of each check:
- "Bullet F-[N]: C-30 PASS (terminal: T-NN), C-31 PASS (inline citation present)"
- OR list the revision made and the corrected bullet text.

If all three bullets pass both checks: "EXECUTIVE SUMMARY audit complete -- C-30 and C-31 satisfied
for all three bullets. Proceeding to CONSOLIDATE."

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
3. Blast radius: [wide | medium | narrow] -- propagation chain: [origin] -> [component] -> [terminal: T-NN]
4. Severity at epicenter: [high | med | low]
5. SYSTEMIC: [yes -- phases: [comma-separated phase list] | no]
6. Classification: [CONFIRMED -- evidence: [source-phase]: [matching-finding-name] | RUNTIME ANOMALY | isolated]
7. What must change: [one concrete fix direction in spec, contract, or implementation]
---

**Spec gaps:** [list each gap with missing-clause citation, or "none detected"]

**Contract violations:** [list each with producer and consumer named, or "none detected"]

**Privilege escalation paths:** [list each, or "none detected"]

**Clean zones:** [Phase 0 census components with no findings across all five phases]

---

## Q8 -- CONSOLIDATE finding block completeness gate

Before writing VERDICT, audit every finding block written in CONSOLIDATE.

For each finding block [N]:
- 7-field check: All seven fields (Name, Source phase, Blast radius, Severity, SYSTEMIC,
  Classification, What must change) are present and non-empty.
  If any field is missing or blank: identify the field and state the required content.
- T-NN chain check: Field 3 blast radius chain terminates at a T-NN code from the Phase 0
  registry (e.g., [terminal: T-04]), not a free-form component name.
  If free-form terminus found: identify the matching T-NN entry and rewrite field 3.
  If no T-NN entry resolves: flag "unresolved chain -- registry miss: [component name]."
- Classification format check: Field 6 uses "CONFIRMED -- evidence: [source-phase]: [finding-name]"
  format, or RUNTIME ANOMALY, or isolated.
  Plain [CONFIRMED] without inline citation is NOT valid. Rewrite using Q2-verified citation,
  or reclassify as RUNTIME ANOMALY if no Q2 citation exists.

State the result for each block:
- "Finding [N]: 7-field PASS, T-NN PASS (terminal: T-NN), classification PASS"
- OR list the revision made and the corrected field content.

If all blocks pass all checks: "CONSOLIDATE audit complete -- all [N] finding blocks satisfy
7-field, T-NN chain, and classification requirements. Proceeding to VERDICT."

---

## VERDICT

One paragraph. Name the finding with the widest blast radius by its Phase 0 census component name.
State the propagation chain from origin to terminal blast surface, including the T-NN terminus code.
State CONFIRMED -- evidence: [source-phase]: [matching-finding-name], or RUNTIME ANOMALY.
If SYSTEMIC, list the corroborating phases.
Name the I-NN assumption from the Phase 0 inertia inventory that this finding overrides. Format:
"This finding overrides I-[N]: [assumption text]." If the assumption was not in the inventory,
state: "Assumption not declared in inertia inventory -- I-NN inventory miss."
Conclude: proceed, proceed with conditions, or halt.
```

---

## R13 Summary

### Axes and what they test

| Variation | C-22/C-23 risk | C-05 coverage | Q5 depth | New structural element |
|-----------|---------------|---------------|----------|----------------------|
| V-01 | Minimal rationale -- tests PARTIAL boundary | Identical to R12 V-05 | Identical | None |
| V-02 | No change | Extended to all phases | Identical | Exception sub-tables in Phases 1-3, 5 |
| V-03 | No change | Identical | I-NN overrides | I-NN inventory + inertia lock |
| V-04 | Minimal rationale + exception expansion | Extended to all phases | Identical | Exception sub-tables under condensed headers |
| V-05 | Minimal rationale + exception expansion | Extended to all phases | I-NN overrides | All: exception sub-tables + I-NN inventory |

### Expected scoring under v11 (all 29 existing criteria)

All five variations preserve:
- Full dual-pipeline enforcement: C-32/C-33/C-34 (EXECUTIVE SUMMARY) + C-35/C-36/C-37 (CONSOLIDATE)
- T-NN registry with lock (C-27, C-35)
- Per-phase T-NN exit gates (C-36)
- Q8 post-CONSOLIDATE gate (C-37)
- 7-field atomic finding blocks (C-19)
- [ANCHOR:...] tags on Phase 1 and Phase 2 headers (C-24)

Risk: V-01, V-04, V-05 reduce rationale prose. If C-22/C-23 require verbosity above the
condensed one-liner, those three variations score PARTIAL on C-22 or C-23.

### Candidate v12 criteria (if V-05 scores surface-level equivalent to R12 V-05)

| Element | Source variation | Candidate criterion |
|---------|-----------------|---------------------|
| Exception path sub-tables in trace phases | V-02 | Every phase (1-5) evaluates exception paths in addition to nominal paths; EXIT CRITERIA requires enumeration count |
| I-NN inertia inventory in Phase 0 | V-03 | Phase 0 includes an I-NN inertia inventory locked at close; Q5 cross-references I-NN codes; VERDICT cites the overridden assumption |
| I-NN meta-finding (assumption not declared) | V-03 | If a finding overrides an assumption not in the inventory, it is flagged as an I-NN inventory miss -- undeclared assumption surfaced by simulation |
