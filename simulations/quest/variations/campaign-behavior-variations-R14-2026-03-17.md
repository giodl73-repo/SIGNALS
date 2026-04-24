Written to `simulations/quest/variations/campaign-behavior-variations-R14-2026-03-17.md`.

---

## R14 Variations — Summary

**Context:** R13 V-05 achieves 31/31 (true perfect on v12). R14 shifts to the next frontier — three axes none of which repeat R13 experiments.

### Axes

| Variation | Axis | Single-axis hypothesis |
|-----------|------|----------------------|
| V-01 | Output format: remediation tiering in field 7 | Free-form field 7 conflates spec/contract/implementation ownership; three-tier sub-fields make the fix layer explicit without adding structural overhead |
| V-02 | Inertia framing: meta-finding elevation (M-NN) | I-NN inventory misses buried in Q5 prose are invisible to blast radius ranking; M-NN promotion makes undeclared assumption gaps first-class rankable findings |
| V-03 | Role sequence: H-NN hypothesis pre-declaration | Without pre-declared hypotheses, "found nothing" cannot be distinguished from "never looked"; H-NN + QH gate converts absence-of-evidence into a traceable outcome |
| V-04 | V-01 + V-02 | Orthogonal combination; field 7 tiers apply equally to F-NN and M-NN blocks |
| V-05 | V-01 + V-02 + V-03 | Full integration; QH fires between Q6 and EXECUTIVE SUMMARY — watch for ordering collision with VALIDITY RULES pre-production gate |

### Key structural notes

- **V-01** extends Q8 with a fourth check: remediation-tier completeness (spec / contract / implementation each populated or "none", at least one non-none).
- **V-02** adds `M-NN` to DEFINITIONS, upgrades Q5 to produce M-NN codes, adds `## META-FINDINGS` section in CONSOLIDATE, and extends EXECUTIVE SUMMARY to accept `M-[N]:` prefixed bullets.
- **V-03** adds `H-NN` to DEFINITIONS, H-NN table to Phase 0 (after inertia lock), and `QH` calibration gate between Q6 and EXECUTIVE SUMMARY. CONSOLIDATE gains a **Hypothesis outcomes** summary row. VERDICT cites H-NN counts.
- **V-05 scoring risk:** QH fires in the Q6 → EXECUTIVE SUMMARY gap. All three output locations (Q7, CONSOLIDATE, Q8) are unaffected by QH scope. Interaction degradation is unlikely but the R14 scorecard should audit QH/VALIDITY RULES ordering explicitly.
n finding
classification and whether absence-of-evidence is distinguishable from never-looked.

**V-04** interaction hypothesis: remediation tiers add field length but not section complexity;
meta-finding elevation adds a new CONSOLIDATE section. The two axes are structurally orthogonal
and unlikely to interact.

**V-05** full-integration risk: QH (V-03) fires between Q6 and EXECUTIVE SUMMARY, which is also
where the VALIDITY RULES pre-production gate (C-32) fires. Watch for ordering collision between
QH and the EXECUTIVE SUMMARY write instruction.

---

### Axes table

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | Output format: remediation tiering in field 7 | Free-form "What must change" conflates spec amendment, contract revision, and implementation change; separating into three labeled sub-fields makes field 7 actionable at the layer where the fix must land, while adding no structural overhead to Q8 |
| V-02 | Inertia framing: meta-finding elevation | I-NN inventory misses buried in Q5 prose are invisible to blast radius ranking and cannot appear in EXECUTIVE SUMMARY; M-NN promotion makes undeclared assumption gaps rankable findings, enabling campaigns to surface whether assumption misses correlate with wide blast radius |
| V-03 | Role sequence: H-NN hypothesis pre-declaration | Without pre-declared hypotheses, a simulation that finds nothing cannot be distinguished from a simulation that never looked; an H-NN inventory converts "no evidence" into a traceable outcome, and refuted hypotheses are as informative as confirmed ones |
| V-04 | V-01 + V-02 | Remediation tiers and meta-finding elevation are structurally orthogonal; combining tests whether both changes survive integration without degrading existing criteria |
| V-05 | V-01 + V-02 + V-03 | Full integration: remediation tiers, elevated meta-findings, and hypothesis pre-declaration; the H-NN gate (QH) is the structural risk — it inserts between Q6 and EXECUTIVE SUMMARY, where the VALIDITY RULES pre-production gate also fires |

---

## V-01 — Output Format: Remediation Tiering in Field 7
**Axis:** Field 7 in every finding block changes from a free-form fix direction to a structured
three-tier field: spec layer (clause to add or amend), contract layer (producer/consumer term to
revise), and implementation layer (code, config, or deployment change required). All three
sub-fields must be populated (or marked "none"). Q8 gains a fourth check: remediation-tier
completeness.
**Hypothesis:** Free-form field 7 allows the model to write a single action that conflates all
three layers ("validate inputs in the service and add a spec clause"), making it impossible to
determine who owns the fix. Three-tier separation makes ownership unambiguous: spec gaps own the
spec tier, contract violations own the contract tier, implementation issues own the implementation
tier. If V-01 scores identically to R13 V-05, the free-form field is sufficient. If Q8 catches
field 7 degradation, the tier structure is load-bearing.

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

Remediation tier = the layer at which a fix must be applied to resolve a finding.
  spec: the fix requires adding, amending, or clarifying a specification clause.
  contract: the fix requires revising a producer/consumer contract term or interface boundary.
  implementation: the fix requires a code, configuration, or deployment change.
Tiers are not mutually exclusive -- list all that apply; mark "none" for tiers that do not apply.
At least one tier must be non-none. All three sub-fields required in every finding block.

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
7. Remediation: spec: [clause to add/amend, or "none"] | contract: [term to revise, or "none"] | implementation: [change required, or "none"]
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
  Classification, Remediation) are present and non-empty.
  If any field is missing or blank: identify the field and state the required content.
- T-NN chain check: Field 3 blast radius chain terminates at a T-NN code from the Phase 0
  registry (e.g., [terminal: T-04]), not a free-form component name.
  If free-form terminus found: identify the matching T-NN entry and rewrite field 3.
  If no T-NN entry resolves: flag "unresolved chain -- registry miss: [component name]."
- Classification format check: Field 6 uses "CONFIRMED -- evidence: [source-phase]: [finding-name]"
  format, or RUNTIME ANOMALY, or isolated.
  Plain [CONFIRMED] without inline citation is NOT valid. Rewrite using Q2-verified citation,
  or reclassify as RUNTIME ANOMALY if no Q2 citation exists.
- Remediation tier check: Field 7 contains all three sub-fields (spec, contract, implementation),
  each populated with a value or "none." At least one sub-field must be non-none.
  If any sub-field is absent or all are "none": identify the finding and state the required tiers.

State the result for each block:
- "Finding [N]: 7-field PASS, T-NN PASS (terminal: T-NN), classification PASS, remediation PASS (tiers: [list non-none tiers])"
- OR list the revision made and the corrected field content.

If all blocks pass all checks: "CONSOLIDATE audit complete -- all [N] finding blocks satisfy
7-field, T-NN chain, classification, and remediation-tier requirements. Proceeding to VERDICT."

---

## VERDICT

One paragraph. Name the finding with the widest blast radius by its Phase 0 census component name.
State the propagation chain from origin to terminal blast surface, including the T-NN terminus code.
State CONFIRMED -- evidence: [source-phase]: [matching-finding-name], or RUNTIME ANOMALY.
If SYSTEMIC, list the corroborating phases.
State the assumption the team would have carried into implementation had this simulation not run,
using the I-NN code from the Phase 0 inertia inventory.
Name the remediation tier(s) where the fix must land.
Conclude: proceed, proceed with conditions, or halt.
```

---

## V-02 -- Inertia Framing: Meta-Finding Elevation
**Axis:** I-NN inventory misses identified in Q5 are promoted to M-NN first-class finding codes.
CONSOLIDATE gains a dedicated `## META-FINDINGS` section ranked by blast radius. EXECUTIVE SUMMARY
may include M-NN items if they outrank regular F-NN findings. VERDICT must note M-NN count.
**Hypothesis:** I-NN inventory misses buried in Q5 prose are invisible to blast radius ranking and
cannot appear in EXECUTIVE SUMMARY. Elevating them to M-NN first-class findings makes undeclared
assumption gaps rankable, enabling the campaign to surface whether the team's assumption misses
correlate with wide blast radius — and giving the EXECUTIVE SUMMARY a path to flag an assumption
gap as the top finding when it carries wider propagation than any regular finding.

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
implementation without this simulation. Inertia inventory is locked at Phase 0 close.

M-NN = meta-finding code. Assigned in Q5 to every I-NN inventory miss: an assumption a finding
overrides that was not declared in the Phase 0 I-NN inventory. M-NN items receive the same 7-field
treatment as F-NN findings and are ranked by blast radius in the META-FINDINGS section.
M-NN items may appear in EXECUTIVE SUMMARY if their blast radius outranks regular F-NN findings.
Format for Q5 meta-finding declaration: "M-01: [undeclared assumption] -- blast radius: [tier] -- propagation chain: [origin] -> [terminal: T-NN]"

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
may be added after Phase 0 closes. Findings that override undeclared assumptions will be assigned
M-NN codes in Q5.
State: "Inertia inventory locked: [N] assumptions. Simulation may begin."

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
For each wide-blast-radius finding: name the I-NN assumption from the Phase 0 inertia inventory
that it overrides. Format: "Finding [N] overrides I-[N]: [assumption text]."
If a finding overrides an assumption not in the inventory, assign it an M-NN code and declare it
as a meta-finding. Format: "M-[N]: [undeclared assumption description] -- blast radius: [tier] --
propagation chain: [origin] -> ... -> [terminal: T-NN]"
M-NN items will be ranked in the META-FINDINGS section of CONSOLIDATE and may appear in
EXECUTIVE SUMMARY if their blast radius outranks regular F-NN findings.
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

Write exactly 3 bullets. These are your top-3 findings by blast-radius tier across all F-NN and
M-NN items. The first bullet is the highest-blast-radius finding; the third is the third.
M-NN items may appear here if their blast radius outranks regular F-NN findings; use prefix
"M-[N]:" in place of "F-[N]:".
If fewer than 3 findings exist, write the available count and note the shortfall.

Use this format for each bullet exactly:
- [F-NN | M-NN]: [finding name] | blast-radius: [wide|medium|narrow] | chain: [origin] -> [component] -> [terminal: T-NN] | [CONFIRMED -- evidence: [phase]: [finding] | RUNTIME ANOMALY | meta-finding: I-NN inventory miss]

VALIDITY RULES for this section:
1. Chain terminus must use a T-NN code from the Phase 0 registry (e.g., T-04), not a
   free-form component name. A bullet with a free-form terminus is INVALID.
   If a chain cannot resolve to a T-NN code, write "unresolved chain -- registry miss: [name]"
   and exclude until resolved via Q1.
2. Confirmation slot must carry the inline evidence citation format:
   CONFIRMED -- evidence: [source-phase]: [matching-finding-name]
   Plain [CONFIRMED] token is NOT valid in EXECUTIVE SUMMARY bullets.
   M-NN items use: "meta-finding: I-NN inventory miss" in the confirmation slot.

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
  format (for F-NN items) or "meta-finding: I-NN inventory miss" (for M-NN items)?
  If plain [CONFIRMED] found without inline citation: rewrite using the citation verified
  in Q2. If no Q2 citation exists for this finding: reclassify as RUNTIME ANOMALY.

State the result of each check:
- "Bullet [F/M]-[N]: C-30 PASS (terminal: T-NN), C-31 PASS (inline citation present)"
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

**META-FINDINGS (ranked by blast radius):**

For each M-NN item from Q5, use this block:

---
**Meta-finding [M-N]**
1. Name: [undeclared assumption description]
2. Source: Q5 -- I-NN inventory miss
3. Blast radius: [wide | medium | narrow] -- propagation chain: [origin] -> [component] -> [terminal: T-NN]
4. Severity at epicenter: [high | med | low]
5. SYSTEMIC: [yes -- phases: [comma-separated phase list] | no]
6. Classification: meta-finding -- I-NN inventory miss: assumption not declared in Phase 0
7. What must change: [add this assumption to I-NN inventory; add spec clause or implementation guard to address it]
---

If no M-NN items exist: "META-FINDINGS: none -- all wide findings mapped to declared I-NN assumptions."

**Spec gaps:** [list each gap with missing-clause citation, or "none detected"]

**Contract violations:** [list each with producer and consumer named, or "none detected"]

**Privilege escalation paths:** [list each, or "none detected"]

**Clean zones:** [Phase 0 census components with no findings across all five phases]

---

## Q8 -- CONSOLIDATE finding block completeness gate

Before writing VERDICT, audit every finding block written in CONSOLIDATE (both F-NN and M-NN).

For each finding block [N]:
- 7-field check: All seven fields present and non-empty.
  If any field is missing or blank: identify the field and state the required content.
- T-NN chain check: Field 3 blast radius chain terminates at a T-NN code from the Phase 0
  registry, not a free-form component name.
  If free-form terminus found: identify the matching T-NN entry and rewrite field 3.
  If no T-NN entry resolves: flag "unresolved chain -- registry miss: [component name]."
- Classification format check: Field 6 uses the correct format for its type.
  F-NN items: "CONFIRMED -- evidence: [source-phase]: [finding-name]", RUNTIME ANOMALY, or isolated.
  M-NN items: "meta-finding -- I-NN inventory miss: assumption not declared in Phase 0."
  Plain [CONFIRMED] without inline citation is NOT valid. Rewrite or reclassify as appropriate.

State the result for each block:
- "[F/M]-[N]: 7-field PASS, T-NN PASS (terminal: T-NN), classification PASS"
- OR list the revision made and the corrected field content.

If all blocks pass all checks: "CONSOLIDATE audit complete -- all [N] finding blocks (F-NN and M-NN)
satisfy 7-field, T-NN chain, and classification requirements. Proceeding to VERDICT."

---

## VERDICT

One paragraph. Name the finding with the widest blast radius by its Phase 0 census component name
(F-NN or M-NN, whichever ranks first). State the propagation chain from origin to terminal blast
surface, including the T-NN terminus code. State CONFIRMED -- evidence: [source-phase]: [matching-finding-name],
or RUNTIME ANOMALY, or meta-finding status as applicable.
If SYSTEMIC, list the corroborating phases.
State the assumption the team would have carried into implementation had this simulation not run,
using the I-NN code from the Phase 0 inertia inventory (or M-NN code if it is a meta-finding).
State the count of M-NN meta-findings produced: "Meta-findings: [N] undeclared assumptions surfaced."
Conclude: proceed, proceed with conditions, or halt.
```

---

## V-03 -- Role Sequence: H-NN Hypothesis Pre-Declaration
**Axis:** Phase 0 gains an H-NN hypothesis table declaring expected finding patterns before any
phase executes. A new QH calibration gate fires after all phases and before EXECUTIVE SUMMARY,
auditing which hypotheses were confirmed, refuted, or found no evidence. VERDICT must cite H-NN
outcomes alongside I-NN overrides.
**Hypothesis:** Without pre-declared hypotheses, a simulation that finds nothing cannot be
distinguished from a simulation that never looked. An H-NN inventory converts "no evidence" into
a traceable outcome: refuted hypotheses are as informative as confirmed ones. If V-03 surfaces
hypotheses that no phase confirms (refuted or no-evidence), it indicates the spec has implicit
behavior guarantees the team expected to find problematic but which are actually well-specified --
a signal as useful as finding violations.

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
the assumption a finding overrides. Inertia inventory is locked at Phase 0 close.

H-NN = hypothesis code. Assigned in Phase 0 to every expected finding pattern declared before
phases execute. H-NN items are not assumptions (I-NN) -- they are predictions: "we expect Phase 2
to find a privilege escalation path at the admin resource boundary." QH audits outcomes: CONFIRMED
(finding matches hypothesis), REFUTED (evidence contradicts hypothesis), or NO-EVIDENCE (phases
produced no relevant findings). Hypothesis inventory is locked at Phase 0 close.

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
this simulation.

| I-NN | Assumption | Domain | What would happen if wrong |
|------|------------|--------|---------------------------|
| I-01 | [assumption text] | [state | permissions | contract | lifecycle | trigger] | [consequence if this assumption is false] |
| ...  | ...        | ...    | ... |

Assign an I-NN code to every distinct assumption. Inertia inventory is now locked.
State: "Inertia inventory locked: [N] assumptions."

**Hypothesis inventory:** Before phases begin, declare expected finding patterns. These are
predictions about where violations will be found -- not assumptions that behavior is correct,
but expectations about where the simulation will surface problems.

| H-NN | Hypothesis | Target phase | Expected finding type | Expected blast radius |
|------|------------|-------------|----------------------|----------------------|
| H-01 | [expected finding pattern] | [phase name] | [contract violation | state invariant | privilege escalation | lifecycle failure | trigger race] | [wide | medium | narrow | unknown] |
| ...  | ...        | ...          | ...                  | ... |

Assign an H-NN code to every distinct hypothesis. Hypothesis inventory is now locked: no hypothesis
may be added after Phase 0 closes. QH will audit outcomes against this inventory.
State: "Hypothesis inventory locked: [N] hypotheses. Simulation may begin."

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
itself encounters an exception.

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

**Exception paths:** For each contract term, evaluate what happens when the invocation fails
at runtime.

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

**Exception sub-cases:**

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

**Exception paths:**

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
that the same inline citation format will be used in the summary bullet.
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

Q6: Did the execution sequence deliver its pre-classification guarantee?
Review every blast radius value in the consolidated findings. Were any revised post-hoc because
a finding touched a state surface or escalation role that Phase 1 or Phase 2 had not yet classified?
- Zero revisions: "Anchor guarantee delivered -- Phase 1 and Phase 2 pre-classified all blast radius
  values before downstream phases consumed them."
- Any revision: log each as an anchor violation -- name the finding, the downstream phase, and the
  Phase 1/2 classification that arrived too late.

QH: Audit the Phase 0 hypothesis inventory against all findings produced.
For each H-NN hypothesis, state one of:
- CONFIRMED: "H-[N] CONFIRMED -- finding [F-NN]: [matching finding name], phase [phase name]"
  A hypothesis is confirmed when a finding matches its expected finding type in the target phase.
- REFUTED: "H-[N] REFUTED -- [explain what the phases found instead of the expected pattern]"
  A hypothesis is refuted when phases explicitly evaluated the target area and found no violation.
- NO-EVIDENCE: "H-[N] NO-EVIDENCE -- target phase [phase name] produced no findings in the
  expected domain"
  No-evidence differs from refuted: the phase did not produce any relevant findings, not that it
  found and cleared the area.
After auditing all H-NN items, state:
"Hypothesis audit complete: [N] confirmed, [N] refuted, [N] no-evidence.
Refuted hypotheses indicate well-specified behavior in the predicted area.
No-evidence hypotheses indicate areas the campaign did not surface -- review exception path
coverage for those phases before concluding the spec is clean."

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
  registry and rewrite the bullet. If no T-NN entry resolves: flag "unresolved chain -- registry miss."
- C-31 check: Does the confirmation slot use "CONFIRMED -- evidence: [source-phase]: [finding-name]"
  format? If plain [CONFIRMED] found without inline citation: rewrite using the citation verified
  in Q2. If no Q2 citation exists: reclassify as RUNTIME ANOMALY.

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
  registry, not a free-form component name.
  If free-form terminus found: identify the matching T-NN entry and rewrite field 3.
  If no T-NN entry resolves: flag "unresolved chain -- registry miss: [component name]."
- Classification format check: Field 6 uses "CONFIRMED -- evidence: [source-phase]: [finding-name]"
  format, or RUNTIME ANOMALY, or isolated.
  Plain [CONFIRMED] without inline citation is NOT valid. Rewrite or reclassify as appropriate.

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
State the assumption the team would have carried into implementation had this simulation not run,
using the I-NN code from the Phase 0 inertia inventory.
State H-NN hypothesis outcomes: "Hypotheses: [N] confirmed, [N] refuted, [N] no-evidence."
Refuted hypotheses are clean signals. No-evidence hypotheses warrant follow-up.
Conclude: proceed, proceed with conditions, or halt.
```

---

## V-04 -- V-01 + V-02 (Remediation Tiering + Meta-Finding Elevation)
**Axis:** Combines V-01 (three-tier field 7) and V-02 (M-NN meta-finding promotion). Both axes
are structurally orthogonal: V-01 affects field 7 in every finding block; V-02 adds M-NN blocks
and a META-FINDINGS section. Neither change touches the same structural location.
**Hypothesis:** The two axes should compose without interaction. V-01 field 7 tiers apply equally
to F-NN and M-NN blocks: a meta-finding has its own remediation tiers (spec: add clause to I-NN
inventory; implementation: add guard for the undeclared assumption). If V-04 scores identically
to V-01 and V-02 run independently, the combination is composable.

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
implementation without this simulation. Inertia inventory is locked at Phase 0 close.

M-NN = meta-finding code. Assigned in Q5 to every I-NN inventory miss. M-NN items receive
the same 7-field treatment as F-NN findings, ranked by blast radius in the META-FINDINGS section.
M-NN items may appear in EXECUTIVE SUMMARY if their blast radius outranks regular F-NN findings.

Remediation tier = the layer at which a fix must be applied to resolve a finding.
  spec: the fix requires adding, amending, or clarifying a specification clause.
  contract: the fix requires revising a producer/consumer contract term or interface boundary.
  implementation: the fix requires a code, configuration, or deployment change.
Tiers are not mutually exclusive -- list all that apply; mark "none" for tiers that do not apply.
At least one tier must be non-none. All three sub-fields required in every finding block (F-NN and M-NN).

SYSTEMIC = a finding corroborated across three or more phases.
Required format: "SYSTEMIC: yes -- phases: [phase-name-1], [phase-name-2], [phase-name-3]"
Binary "SYSTEMIC: yes" without a phase list is not valid and will be rejected.

CONFIRMED = a Phase 4 or Phase 5 finding that matches a topology violation from Phases 1-3.
Required format: "CONFIRMED -- evidence: [source-phase]: [matching-finding-name]"
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

Assign a T-NN code to every unique blast-surface endpoint in the system. Every propagation chain
must terminate at a T-NN registry code. Chains that cannot resolve = registry miss.

**Registry lock:** The terminus registry is now complete.
No terminus component may be added, removed, or renamed after this point.
All propagation chains in Phases 1-5 must resolve to a T-NN entry or be flagged
"unresolved chain -- registry miss: [component name]."
State: "Registry locked: [N] terminus entries. Phase execution may begin."

**Inertia inventory:**

| I-NN | Assumption | Domain | What would happen if wrong |
|------|------------|--------|---------------------------|
| I-01 | [assumption text] | [state | permissions | contract | lifecycle | trigger] | [consequence] |
| ...  | ...        | ...    | ... |

Inertia inventory is now locked. Findings that override undeclared assumptions will be assigned
M-NN codes in Q5.
State: "Inertia inventory locked: [N] assumptions. Simulation may begin."

---

## PHASE 1 -- trace-state [ANCHOR: state topology pre-classifies blast radius candidates for all downstream phases]

trace-state runs first. Pre-classifies blast radius candidates from shared-state topology.
Downstream sub-skills inherit this map; none re-derive it independently.

**Nominal paths:**

| From state | To state | Trigger | Invariant | Invariant holds? | Shared state surface? | Blast radius candidate |
|------------|----------|---------|-----------|------------------|-----------------------|------------------------|

For each shared state surface = yes: blast radius candidate = wide. Classification locked for downstream phases.

**Exception paths:**

| Transition | Exception condition | Component that handles it | Blast radius if unhandled | Spec clause covering this? |
|------------|---------------------|---------------------------|--------------------------|---------------------------|

For any exception with no spec clause: record as spec gap.
For any unhandled wide exception: assign T-NN terminus, record blast radius candidate.

If no violations: "trace-state: clean -- all invariants verified, all exception paths handled."

EXIT CRITERIA: All transitions evaluated (nominal and exception). No transitions deferred.
State: "trace-state complete: [N] transitions evaluated, [N] violations found, [N] pre-classified wide, [N] exception paths evaluated, [N] exception spec gaps."
T-NN resolution check: "[N] chains produced, [N] resolved to T-NN, [N] registry miss."
If any registry miss: flag "unresolved chain -- registry miss: [component name]" and carry to Q1.

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

If clean: "trace-permissions: clean -- all pairs verified, no escalation paths, all exceptions handled."

EXIT CRITERIA: All pairs evaluated (nominal and exception). No pairs deferred.
State: "trace-permissions complete: [N] pairs, [N] escalation paths, [N] compound anchor hits, [N] exception paths, [N] exception spec gaps."
T-NN resolution check: "[N] chains produced, [N] resolved to T-NN, [N] registry miss."
If any registry miss: flag and carry to Q1.

---

## PHASE 3 -- trace-contract

**Nominal paths:**

| Producer | Consumer | Contract term | Expected | Actual | Mismatch? | Phase 1/2 topology match? |
|----------|----------|---------------|----------|--------|-----------|--------------------------|

Phase 1/2 topology match = yes: classify CONFIRMED -- evidence: [phase-1|phase-2]: [matching-finding-name].

**Exception paths:**

| Contract term | Exception condition | Recovery contract | Blast radius if recovery absent | Spec clause covering this? |
|---------------|---------------------|-------------------|---------------------------------|---------------------------|

For any exception with no recovery contract: record as spec gap. Wide exception + topology match = CONFIRMED.

If clean: "trace-contract: clean -- all contracts verified, all exception paths handled."

EXIT CRITERIA: All pairs evaluated (nominal and exception). No pairs deferred.
State: "trace-contract complete: [N] pairs, [N] mismatches, [N] CONFIRMED, [N] exception paths, [N] exception spec gaps."
T-NN resolution check: "[N] chains produced, [N] resolved to T-NN, [N] registry miss."
If any registry miss: flag and carry to Q1.

---

## PHASE 4 -- flow-lifecycle

**Nominal and exception paths (combined):**

| Phase | Entry contract | Exit contract | Exception path | Exception handled? | Phase tag | CONFIRMED / RUNTIME ANOMALY |
|-------|----------------|---------------|----------------|--------------------|-----------|-----------------------------|

Phase tag = lifecycle phase (INIT, ACTIVE, SUSPENDED, TERMINAL, etc.).
CONFIRMED: CONFIRMED -- evidence: [source-phase]: [matching-finding-name]

**Exception sub-cases:**

| Lifecycle phase | Exception sub-case | Blast radius | Spec clause covering this? |
|-----------------|--------------------|--------------|---------------------------|

If clean: "flow-lifecycle: clean -- all transitions verified, all exception paths enumerated."

EXIT CRITERIA: All phases and sub-cases evaluated.
State: "flow-lifecycle complete: [N] phases, [N] failures, [N] CONFIRMED, [N] RUNTIME ANOMALY, [N] sub-cases."
T-NN resolution check: "[N] chains produced, [N] resolved to T-NN, [N] registry miss."
If any registry miss: flag and carry to Q1.

---

## PHASE 5 -- flow-trigger

**Nominal paths:**

| Trigger | Expected fire order | Actual fire order | Race condition? | Phase 2 escalation role? | Phase tag | CONFIRMED / RUNTIME ANOMALY |
|---------|---------------------|-------------------|-----------------|--------------------------|-----------|------------------------------|

Phase 2 escalation role = yes: blast radius = wide.

**Exception paths:**

| Trigger | Exception condition | Expected behavior | Actual behavior | Blast radius | Spec clause covering this? |
|---------|---------------------|-------------------|-----------------|--------------|---------------------------|

For any exception with no spec clause: spec gap.

If clean: "flow-trigger: clean -- all triggers verified, all exception paths enumerated."

EXIT CRITERIA: All triggers evaluated (nominal and exception). No triggers deferred.
State: "flow-trigger complete: [N] triggers, [N] failures, [N] CONFIRMED, [N] RUNTIME ANOMALY, [N] exception paths."
T-NN resolution check: "[N] chains produced, [N] resolved to T-NN, [N] registry miss."
If any registry miss: flag and carry to Q1.

---

## CALIBRATION BLOCK

Q1: Trace each finding's propagation chain to its T-NN terminus. Chain reaches Phase 0 shared-state
entry? Upgrade to wide. List all revisions and full chains. Flag unresolvable chains.

Q2: For each Phase 4-5 CONFIRMED finding: verify inline citation format
"CONFIRMED -- evidence: [source-phase]: [matching-finding-name]." Revise any missing citation.
Also verify: for any finding entering EXECUTIVE SUMMARY as CONFIRMED, confirm inline citation
format will be used (not plain [CONFIRMED]). Note any slots requiring revision after Q7.

Q3: For every SYSTEMIC finding: "SYSTEMIC: yes -- phases: [phase-1], [phase-2], [phase-3]"
Binary SYSTEMIC flags are not valid.

Q4: For every finding involving Phase 2 escalation role or Phase 1 state surface: verify wide.
Revise and explain any finding below wide for a pre-classified component.

Q5: For each wide-blast-radius finding: name the I-NN assumption it overrides.
Format: "Finding [N] overrides I-[N]: [assumption text]."
If a finding overrides an undeclared assumption: assign M-NN code.
Format: "M-[N]: [undeclared assumption] -- blast radius: [tier] -- chain: [origin] -> [terminal: T-NN]"
M-NN items will be ranked in the META-FINDINGS section and may enter EXECUTIVE SUMMARY.

Q6: Did the anchor sequence deliver its pre-classification guarantee?
Zero revisions: "Anchor guarantee delivered."
Any revision: log as anchor violation -- finding, downstream phase, Phase 1/2 classification that
arrived too late.

---

## EXECUTIVE SUMMARY

Write exactly 3 bullets from the combined F-NN and M-NN pool, ranked by blast radius.
M-NN items may appear here; use prefix "M-[N]:" if so.
If fewer than 3 findings exist, write the available count and note the shortfall.

Use this format for each bullet exactly:
- [F-NN | M-NN]: [finding name] | blast-radius: [wide|medium|narrow] | chain: [origin] -> [component] -> [terminal: T-NN] | [CONFIRMED -- evidence: [phase]: [finding] | RUNTIME ANOMALY | meta-finding: I-NN inventory miss]

VALIDITY RULES for this section:
1. Chain terminus must use a T-NN code (e.g., T-04), not a free-form component name.
   Free-form terminus = INVALID. Unresolvable = exclude with "unresolved chain -- registry miss."
2. Confirmation slot must carry inline evidence citation format for F-NN items:
   CONFIRMED -- evidence: [source-phase]: [matching-finding-name]
   Plain [CONFIRMED] token is NOT valid.
   M-NN items use: "meta-finding: I-NN inventory miss" in the confirmation slot.

Do not summarize. Do not add prose. Three structured bullets, then stop.

---

## Q7 -- EXECUTIVE SUMMARY structural audit

Before writing CONSOLIDATE, audit each bullet:
- C-30 check: Chain terminus = T-NN code, not free-form. Rewrite or flag if not.
- C-31 check: F-NN confirmation slot = inline evidence format. M-NN = "meta-finding: I-NN inventory miss."
  Plain [CONFIRMED] without citation: rewrite using Q2 citation, or reclassify as RUNTIME ANOMALY.

State: "Bullet [F/M]-[N]: C-30 PASS (terminal: T-NN), C-31 PASS" or list revision made.
All pass: "EXECUTIVE SUMMARY audit complete. Proceeding to CONSOLIDATE."

---

## CONSOLIDATE

Write ONE report. Do not concatenate five phase outputs.

Tiebreaker: (1) Blast radius descending, (2) CONFIRMED > RUNTIME ANOMALY, (3) SYSTEMIC > isolated.
State whether any ties were encountered and how resolved.

**Ranked findings (wide first):**

---
**Finding [N]**
1. Name: [finding name or short description]
2. Source phase: [phase name]
3. Blast radius: [wide | medium | narrow] -- propagation chain: [origin] -> [component] -> [terminal: T-NN]
4. Severity at epicenter: [high | med | low]
5. SYSTEMIC: [yes -- phases: [list] | no]
6. Classification: [CONFIRMED -- evidence: [source-phase]: [finding-name] | RUNTIME ANOMALY | isolated]
7. Remediation: spec: [clause to add/amend, or "none"] | contract: [term to revise, or "none"] | implementation: [change required, or "none"]
---

**META-FINDINGS (ranked by blast radius):**

---
**Meta-finding [M-N]**
1. Name: [undeclared assumption description]
2. Source: Q5 -- I-NN inventory miss
3. Blast radius: [wide | medium | narrow] -- propagation chain: [origin] -> [component] -> [terminal: T-NN]
4. Severity at epicenter: [high | med | low]
5. SYSTEMIC: [yes -- phases: [list] | no]
6. Classification: meta-finding -- I-NN inventory miss: assumption not declared in Phase 0
7. Remediation: spec: [add assumption to I-NN inventory and add spec clause, or "none"] | contract: [term to revise, or "none"] | implementation: [guard to add, or "none"]
---

If no M-NN items: "META-FINDINGS: none -- all wide findings mapped to declared I-NN assumptions."

**Spec gaps:** [list each with missing-clause citation, or "none detected"]

**Contract violations:** [list each with producer and consumer named, or "none detected"]

**Privilege escalation paths:** [list each, or "none detected"]

**Clean zones:** [Phase 0 census components with no findings across all five phases]

---

## Q8 -- CONSOLIDATE finding block completeness gate

Before writing VERDICT, audit every finding block (F-NN and M-NN).

For each block [N]:
- 7-field check: All seven fields present and non-empty. Missing or blank = identify and state required content.
- T-NN chain check: Field 3 terminates at a T-NN code. Free-form terminus = rewrite. Unresolvable = flag.
- Classification format check: F-NN items use CONFIRMED inline format or RUNTIME ANOMALY or isolated.
  M-NN items use "meta-finding -- I-NN inventory miss." Plain [CONFIRMED] = NOT valid; rewrite or reclassify.
- Remediation tier check: Field 7 has all three sub-fields (spec, contract, implementation).
  Each is populated or "none." At least one sub-field must be non-none.
  All-none = identify finding and state required tiers.

State: "[F/M]-[N]: 7-field PASS, T-NN PASS, classification PASS, remediation PASS (tiers: [list])"
or list revision made.
All pass: "CONSOLIDATE audit complete -- all [N] blocks satisfy 7-field, T-NN, classification, and
remediation-tier requirements. Proceeding to VERDICT."

---

## VERDICT

One paragraph. Name the finding with the widest blast radius (F-NN or M-NN, whichever ranks first)
by its Phase 0 census component name. State the propagation chain including T-NN terminus code.
State CONFIRMED -- evidence: [source-phase]: [finding-name], RUNTIME ANOMALY, or meta-finding status.
If SYSTEMIC, list corroborating phases.
State the I-NN assumption the team would have carried into implementation, or M-NN code if meta-finding.
Name the remediation tier(s) where the fix must land.
State meta-finding count: "Meta-findings: [N] undeclared assumptions surfaced."
Conclude: proceed, proceed with conditions, or halt.
```

---

## V-05 -- Full R14 Integration: V-01 + V-02 + V-03
**Axis:** All three R14 axes combined: remediation tiering in field 7 (V-01), M-NN meta-finding
elevation (V-02), and H-NN hypothesis pre-declaration with QH audit gate (V-03).
**Hypothesis:** The three axes are structurally independent. V-01 modifies field 7. V-02 adds
M-NN blocks and META-FINDINGS section. V-03 adds H-NN inventory to Phase 0 and QH between
Q6 and EXECUTIVE SUMMARY. The only potential interaction: QH firing between Q6 and EXECUTIVE
SUMMARY inserts an audit step that touches finding classifications -- confirm QH does not
duplicate Q2 scope or interfere with the VALIDITY RULES pre-production gate. If V-05 scores
identically to V-01 + V-02 + V-03 individually, all three axes are composable.

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
implementation without this simulation. Inertia inventory is locked at Phase 0 close.

M-NN = meta-finding code. Assigned in Q5 to every I-NN inventory miss: an assumption a finding
overrides that was not declared in Phase 0. M-NN items receive 7-field treatment, are ranked
by blast radius in the META-FINDINGS section, and may appear in EXECUTIVE SUMMARY.
Format: "M-[N]: [undeclared assumption] -- blast radius: [tier] -- chain: [origin] -> [terminal: T-NN]"

H-NN = hypothesis code. Assigned in Phase 0 to every expected finding pattern declared before
phases execute. QH audits outcomes: CONFIRMED, REFUTED, or NO-EVIDENCE.
Hypothesis inventory is locked at Phase 0 close. QH fires between Q6 and EXECUTIVE SUMMARY.

Remediation tier = the layer at which a fix must be applied.
  spec: add, amend, or clarify a specification clause.
  contract: revise a producer/consumer contract term or interface boundary.
  implementation: code, configuration, or deployment change.
Tiers are not mutually exclusive. At least one must be non-none.
All three sub-fields required in every finding block (F-NN and M-NN).

SYSTEMIC = a finding corroborated across three or more phases.
Required format: "SYSTEMIC: yes -- phases: [phase-name-1], [phase-name-2], [phase-name-3]"
Binary "SYSTEMIC: yes" without a phase list is not valid and will be rejected.

CONFIRMED = a Phase 4 or Phase 5 finding that matches a topology violation from Phases 1-3.
Required format: "CONFIRMED -- evidence: [source-phase]: [matching-finding-name]"
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

Assign a T-NN code to every unique blast-surface endpoint. Every propagation chain must terminate
at a T-NN registry code. Chains that cannot resolve = registry miss.

**Registry lock:** The terminus registry is now complete.
No terminus component may be added, removed, or renamed after this point.
All propagation chains in Phases 1-5 must resolve to a T-NN entry or be flagged
"unresolved chain -- registry miss: [component name]."
State: "Registry locked: [N] terminus entries. Phase execution may begin."

**Inertia inventory:**

| I-NN | Assumption | Domain | What would happen if wrong |
|------|------------|--------|---------------------------|
| I-01 | [assumption text] | [state | permissions | contract | lifecycle | trigger] | [consequence] |
| ...  | ...        | ...    | ... |

Inertia inventory is now locked. Undeclared-assumption overrides will be assigned M-NN codes in Q5.
State: "Inertia inventory locked: [N] assumptions."

**Hypothesis inventory:**

| H-NN | Hypothesis | Target phase | Expected finding type | Expected blast radius |
|------|------------|-------------|----------------------|----------------------|
| H-01 | [expected finding pattern] | [phase name] | [type] | [wide | medium | narrow | unknown] |
| ...  | ...        | ...          | ...    | ... |

Hypothesis inventory is now locked. QH will audit outcomes after phases complete.
State: "Hypothesis inventory locked: [N] hypotheses. Simulation may begin."

---

## PHASE 1 -- trace-state [ANCHOR: state topology pre-classifies blast radius candidates for all downstream phases]

trace-state runs first. Pre-classifies blast radius candidates from shared-state topology.
Downstream sub-skills inherit this map; none re-derive it independently.

**Nominal paths:**

| From state | To state | Trigger | Invariant | Invariant holds? | Shared state surface? | Blast radius candidate |
|------------|----------|---------|-----------|------------------|-----------------------|------------------------|

For each shared state surface = yes: blast radius candidate = wide. Classification locked for downstream phases.

**Exception paths:**

| Transition | Exception condition | Component that handles it | Blast radius if unhandled | Spec clause covering this? |
|------------|---------------------|---------------------------|--------------------------|---------------------------|

For any exception with no spec clause: spec gap.
For any unhandled wide exception: assign T-NN terminus, record blast radius candidate.

If no violations: "trace-state: clean -- all invariants verified, all exception paths handled."

EXIT CRITERIA: All transitions evaluated (nominal and exception).
State: "trace-state complete: [N] transitions, [N] violations, [N] pre-classified wide, [N] exception paths, [N] exception spec gaps."
T-NN resolution check: "[N] chains produced, [N] resolved to T-NN, [N] registry miss."
If any registry miss: flag and carry to Q1.

---

## PHASE 2 -- trace-permissions [ANCHOR: privilege boundary classification anchors flow blast radius assessment]

trace-permissions runs second, before all flow sub-skills. Flow violations crossing a privilege
boundary are SYSTEMIC by definition; anchor must precede flow analysis.

**Nominal paths:**

| Role | Resource | Action | Permitted? | Escalation path? | Phase 1 state surface involved? | Blast radius ceiling |
|------|----------|--------|------------|------------------|---------------------------------|----------------------|

Phase 1 state surface + escalation path = wide (compound anchor hit).

**Exception paths:**

| Role-resource pair | Exception condition | Fail-open or fail-closed? | Blast radius if fail-open | Spec clause covering this? |
|--------------------|---------------------|--------------------------|--------------------------|---------------------------|

For any fail-open exception with no spec clause: spec gap.

If clean: "trace-permissions: clean -- all pairs verified, no escalation paths, all exceptions handled."

EXIT CRITERIA: All pairs evaluated (nominal and exception).
State: "trace-permissions complete: [N] pairs, [N] escalation paths, [N] compound anchor hits, [N] exception paths, [N] exception spec gaps."
T-NN resolution check: "[N] chains produced, [N] resolved to T-NN, [N] registry miss."
If any registry miss: flag and carry to Q1.

---

## PHASE 3 -- trace-contract

**Nominal paths:**

| Producer | Consumer | Contract term | Expected | Actual | Mismatch? | Phase 1/2 topology match? |
|----------|----------|---------------|----------|--------|-----------|--------------------------|

Phase 1/2 topology match: CONFIRMED -- evidence: [phase-1|phase-2]: [matching-finding-name].

**Exception paths:**

| Contract term | Exception condition | Recovery contract | Blast radius if recovery absent | Spec clause covering this? |
|---------------|---------------------|-------------------|---------------------------------|---------------------------|

For any exception with no recovery contract: spec gap. Wide + topology match = CONFIRMED.

If clean: "trace-contract: clean -- all contracts verified, all exception paths handled."

EXIT CRITERIA: All pairs evaluated (nominal and exception).
State: "trace-contract complete: [N] pairs, [N] mismatches, [N] CONFIRMED, [N] exception paths, [N] exception spec gaps."
T-NN resolution check: "[N] chains produced, [N] resolved to T-NN, [N] registry miss."
If any registry miss: flag and carry to Q1.

---

## PHASE 4 -- flow-lifecycle

**Nominal and exception paths (combined):**

| Phase | Entry contract | Exit contract | Exception path | Exception handled? | Phase tag | CONFIRMED / RUNTIME ANOMALY |
|-------|----------------|---------------|----------------|--------------------|-----------|-----------------------------|

Phase tag: INIT, ACTIVE, SUSPENDED, TERMINAL, etc.
CONFIRMED: CONFIRMED -- evidence: [source-phase]: [matching-finding-name]

**Exception sub-cases:**

| Lifecycle phase | Exception sub-case | Blast radius | Spec clause covering this? |
|-----------------|--------------------|--------------|---------------------------|

If clean: "flow-lifecycle: clean -- all transitions verified, all exception paths enumerated."

EXIT CRITERIA: All phases and sub-cases evaluated.
State: "flow-lifecycle complete: [N] phases, [N] failures, [N] CONFIRMED, [N] RUNTIME ANOMALY, [N] sub-cases."
T-NN resolution check: "[N] chains produced, [N] resolved to T-NN, [N] registry miss."
If any registry miss: flag and carry to Q1.

---

## PHASE 5 -- flow-trigger

**Nominal paths:**

| Trigger | Expected fire order | Actual fire order | Race condition? | Phase 2 escalation role? | Phase tag | CONFIRMED / RUNTIME ANOMALY |
|---------|---------------------|-------------------|-----------------|--------------------------|-----------|------------------------------|

Phase 2 escalation role = yes: blast radius = wide.

**Exception paths:**

| Trigger | Exception condition | Expected behavior | Actual behavior | Blast radius | Spec clause covering this? |
|---------|---------------------|-------------------|-----------------|--------------|---------------------------|

For any exception with no spec clause: spec gap.

If clean: "flow-trigger: clean -- all triggers verified, all exception paths enumerated."

EXIT CRITERIA: All triggers evaluated (nominal and exception).
State: "flow-trigger complete: [N] triggers, [N] failures, [N] CONFIRMED, [N] RUNTIME ANOMALY, [N] exception paths."
T-NN resolution check: "[N] chains produced, [N] resolved to T-NN, [N] registry miss."
If any registry miss: flag and carry to Q1.

---

## CALIBRATION BLOCK

Q1: Trace each finding's propagation chain to its T-NN terminus. Chain reaches Phase 0 shared-state
entry? Upgrade to wide. List all revisions and full chains. Flag unresolvable chains.

Q2: For each Phase 4-5 CONFIRMED finding: verify inline citation format.
"CONFIRMED -- evidence: [source-phase]: [matching-finding-name]." Revise any missing citation.
Also verify: for any finding entering EXECUTIVE SUMMARY as CONFIRMED, inline citation will be used.
List all reclassifications and citations verified or added.

Q3: For every SYSTEMIC finding: "SYSTEMIC: yes -- phases: [list]." Binary flags not valid.

Q4: For every finding involving Phase 2 escalation role or Phase 1 state surface: verify wide.
Revise and explain any below-wide classification for a pre-classified component.

Q5: For each wide-blast-radius finding: name the I-NN assumption it overrides.
Format: "Finding [N] overrides I-[N]: [assumption text]."
Undeclared assumption override: assign M-NN code.
Format: "M-[N]: [undeclared assumption] -- blast radius: [tier] -- chain: [origin] -> [terminal: T-NN]"
M-NN items rank in META-FINDINGS and may enter EXECUTIVE SUMMARY.

Q6: Did the anchor sequence deliver its pre-classification guarantee?
Zero revisions: "Anchor guarantee delivered."
Any revision: log as anchor violation.

QH: Audit the Phase 0 hypothesis inventory against all findings produced (F-NN and M-NN combined).
For each H-NN item, state one of:
- CONFIRMED: "H-[N] CONFIRMED -- finding [F/M-NN]: [finding name], phase [phase name]"
- REFUTED: "H-[N] REFUTED -- [what phases found instead of the expected pattern]"
- NO-EVIDENCE: "H-[N] NO-EVIDENCE -- target phase [name] produced no findings in the expected domain"
After all H-NN items:
"Hypothesis audit: [N] confirmed, [N] refuted, [N] no-evidence.
Refuted = well-specified behavior in predicted area.
No-evidence = campaign did not surface this domain; review exception path coverage before concluding clean."

---

## EXECUTIVE SUMMARY

Write exactly 3 bullets from the combined F-NN and M-NN pool, ranked by blast radius.
M-NN items may appear here; use prefix "M-[N]:" if so.
If fewer than 3 findings exist, write the available count and note the shortfall.

Use this format for each bullet exactly:
- [F-NN | M-NN]: [finding name] | blast-radius: [wide|medium|narrow] | chain: [origin] -> [component] -> [terminal: T-NN] | [CONFIRMED -- evidence: [phase]: [finding] | RUNTIME ANOMALY | meta-finding: I-NN inventory miss]

VALIDITY RULES for this section:
1. Chain terminus must use a T-NN code (e.g., T-04), not a free-form component name.
   Free-form terminus = INVALID. Unresolvable = "unresolved chain -- registry miss: [name]" and exclude.
2. F-NN confirmation slot: CONFIRMED -- evidence: [source-phase]: [finding-name], or RUNTIME ANOMALY.
   Plain [CONFIRMED] token is NOT valid.
   M-NN confirmation slot: "meta-finding: I-NN inventory miss" -- no inline evidence citation required.

Do not summarize. Do not add prose. Three structured bullets, then stop.

---

## Q7 -- EXECUTIVE SUMMARY structural audit

Before writing CONSOLIDATE, audit each bullet:
- C-30 check: Chain terminus = T-NN code. Free-form: rewrite. Unresolvable: flag and exclude.
- C-31 check: F-NN = inline evidence format. M-NN = "meta-finding: I-NN inventory miss."
  Plain [CONFIRMED] without citation: rewrite via Q2 or reclassify RUNTIME ANOMALY.

State: "[F/M]-[N]: C-30 PASS (terminal: T-NN), C-31 PASS" or list revision.
All pass: "EXECUTIVE SUMMARY audit complete. Proceeding to CONSOLIDATE."

---

## CONSOLIDATE

Write ONE report. Do not concatenate five phase outputs.

Tiebreaker: (1) Blast radius descending, (2) CONFIRMED > RUNTIME ANOMALY, (3) SYSTEMIC > isolated.
State whether any ties were encountered and how resolved.

**Ranked findings (wide first):**

---
**Finding [N]**
1. Name: [finding name or short description]
2. Source phase: [phase name]
3. Blast radius: [wide | medium | narrow] -- propagation chain: [origin] -> [component] -> [terminal: T-NN]
4. Severity at epicenter: [high | med | low]
5. SYSTEMIC: [yes -- phases: [list] | no]
6. Classification: [CONFIRMED -- evidence: [source-phase]: [finding-name] | RUNTIME ANOMALY | isolated]
7. Remediation: spec: [clause to add/amend, or "none"] | contract: [term to revise, or "none"] | implementation: [change required, or "none"]
---

**META-FINDINGS (ranked by blast radius):**

---
**Meta-finding [M-N]**
1. Name: [undeclared assumption description]
2. Source: Q5 -- I-NN inventory miss
3. Blast radius: [wide | medium | narrow] -- propagation chain: [origin] -> [component] -> [terminal: T-NN]
4. Severity at epicenter: [high | med | low]
5. SYSTEMIC: [yes -- phases: [list] | no]
6. Classification: meta-finding -- I-NN inventory miss: assumption not declared in Phase 0
7. Remediation: spec: [add to I-NN inventory; add spec clause, or "none"] | contract: [term to revise, or "none"] | implementation: [guard to add, or "none"]
---

If no M-NN items: "META-FINDINGS: none -- all wide findings mapped to declared I-NN assumptions."

**Hypothesis outcomes:** [H-NN CONFIRMED: [N] | H-NN REFUTED: [N] | H-NN NO-EVIDENCE: [N]]
List each H-NN outcome in one line: "H-[N]: [CONFIRMED | REFUTED | NO-EVIDENCE] -- [summary]"

**Spec gaps:** [list each with missing-clause citation, or "none detected"]

**Contract violations:** [list each with producer and consumer named, or "none detected"]

**Privilege escalation paths:** [list each, or "none detected"]

**Clean zones:** [Phase 0 census components with no findings across all five phases]

---

## Q8 -- CONSOLIDATE finding block completeness gate

Before writing VERDICT, audit every finding block (F-NN and M-NN).

For each block [N]:
- 7-field check: All seven fields present and non-empty. Missing = identify and state required.
- T-NN chain check: Field 3 terminates at T-NN code. Free-form = rewrite. Unresolvable = flag.
- Classification format check:
  F-NN: CONFIRMED inline format, RUNTIME ANOMALY, or isolated. Plain [CONFIRMED] = NOT valid.
  M-NN: "meta-finding -- I-NN inventory miss: assumption not declared in Phase 0."
- Remediation tier check: Field 7 has spec, contract, implementation sub-fields. Each populated
  or "none." At least one non-none. All-none = identify and state required tiers.

State: "[F/M]-[N]: 7-field PASS, T-NN PASS, classification PASS, remediation PASS (tiers: [list])"
or list revision made.
All pass: "CONSOLIDATE audit complete -- all [N] blocks satisfy 7-field, T-NN, classification,
and remediation-tier requirements. Proceeding to VERDICT."

---

## VERDICT

One paragraph. Name the finding with the widest blast radius (F-NN or M-NN) by its Phase 0 census
component name. State the propagation chain including T-NN terminus code.
State CONFIRMED -- evidence: [source-phase]: [finding-name], RUNTIME ANOMALY, or meta-finding status.
If SYSTEMIC, list corroborating phases.
State the I-NN assumption the team would have carried into implementation (or M-NN if meta-finding).
Name the remediation tier(s) where the fix must land.
State H-NN outcomes: "Hypotheses: [N] confirmed, [N] refuted, [N] no-evidence."
State M-NN count: "Meta-findings: [N] undeclared assumptions surfaced."
Conclude: proceed, proceed with conditions, or halt.
```
