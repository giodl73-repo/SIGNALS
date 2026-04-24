# Quest Variations -- campaign-behavior (R4)
**Skill:** campaign-behavior
**Rubric:** v4 (C-01--C-18, adds C-15 EXIT CRITERIA, C-16 CONFIRMED, C-17 interrogative calibration, C-18 Phase 0 census)
**Round:** 4
**Date:** 2026-03-17

---

## V-01 -- Prose-block output format (no markdown tables)
**Axis:** Output format -- all findings rendered as labeled-field prose blocks; zero markdown tables anywhere in execution or consolidation
**Hypothesis:** Removing tables forces explicit causal articulation in every blast radius assessment. If the rubric criteria are structure-dependent (not format-dependent), prose blocks should pass the same criteria as tables. If table format is load-bearing for rubric detection, prose will fail specific criteria despite satisfying their intent.

```
Simulate the technical behavior of: {{topic}}

---

## BLAST RADIUS DEFINITION

Blast radius = how broadly a failure propagates through the system.
Wide: corrupts shared state, breaks downstream callers, or blocks multiple user roles simultaneously.
Medium: two or more components affected; no shared state surface reached.
Narrow: failure contained within one component boundary.

Severity = damage depth at the epicenter (high / med / low).
These are independent dimensions. A wide blast radius with low severity is possible.
A narrow blast radius with high severity is possible. Report both as separate labeled fields.
Never merge them into a single "impact" field.

---

## PHASE 0 -- Topology census

Before any sub-skill runs, record the system vocabulary explicitly.

Components in scope: [list every named service, module, API, schema, queue from the spec or codebase]

Shared state surfaces: [list databases, caches, event buses, configuration objects that multiple
components read or write -- these are the blast-radius amplifiers]

Downstream callers: [list every component whose behavior depends on the system under simulation]

Role-resource inventory: [list every role and the resources it is permitted to access]

Every blast radius assessment below must name a specific item from this census.
If a finding cannot name a census item, return to the spec and identify the component
before recording the finding.

---

## PHASE 1 -- trace-contract

For each producer/consumer pairing in scope, write one finding block using this structure exactly:

---
Finding TC-[N]
Producer: [component name from census]
Consumer: [component name from census]
Contract term: [what the producer promises to deliver]
Expected: [what the consumer receives when the contract holds]
Actual: [what the consumer receives when this finding occurs]
Mismatch: [yes | no] -- if yes, describe the divergence in one sentence
Severity at epicenter: [high | med | low]
Blast radius: [wide | medium | narrow] -- name the census component and explain
  the propagation path in one sentence
Spec gap: [yes | no] -- if yes, state what the spec does not address in one sentence
---

If no producer/consumer mismatches are found:
"trace-contract: clean -- all contracts verified, no violations detected."

EXIT CRITERIA: All producer/consumer pairs in scope have been evaluated. No pairs deferred.

---

## PHASE 2 -- trace-state

For each state transition in the system, write one finding block using this structure exactly:

---
Finding TS-[N]
From state: [state name]
Trigger: [event or action that initiates the transition]
To state: [state name]
Preconditions: [what must hold before this transition is valid]
Postcondition: [what holds after the transition completes]
Invariant: [what must hold throughout this state]
Violated: [yes | no] -- if yes, describe the violation in one sentence
Blast radius: [wide | medium | narrow] -- name the census component; invariant violations
  on shared state surfaces are wide
Spec gap: [yes | no] -- if yes, state what the spec does not address
---

If no violations are found:
"trace-state: clean -- all transitions verified, no invariant violations detected."

EXIT CRITERIA: All states and all transitions in scope have been evaluated.

---

## PHASE 3 -- trace-permissions

For each role-resource-action combination in scope, write one finding block using this structure exactly:

---
Finding TP-[N]
Role: [role name from census]
Resource: [resource name from census]
Action: [read | write | delete | execute | escalate | other]
Expected access: [what the spec says should happen]
Actual access: [what the permission model delivers]
Privilege escalation: [yes | no] -- if yes, describe the escalation path in one sentence
Blast radius: [wide | medium | narrow] -- privilege escalation is wide by default;
  name the census component
Spec gap: [yes | no]
---

If no violations are found:
"trace-permissions: clean -- all role-resource pairs verified, no escalation paths detected."

EXIT CRITERIA: All role-resource pairs in the census have been evaluated.

---

## PHASE 4 -- flow-lifecycle

For each lifecycle phase from creation to terminal state, write one finding block using this structure exactly:

---
Finding FL-[N]
Phase: [phase name]
Entry contract: [what must be true to enter this phase]
Exit contract: [what must be true to exit this phase and enter the next]
Exception path: [what happens when the entry or exit contract is not met]
Gap in spec: [yes | no] -- if yes, state what the spec does not address in one sentence
Blast radius: [wide | medium | narrow] -- lifecycle gaps affecting shared state are wide;
  name the census component
---

If no gaps are found:
"flow-lifecycle: clean -- all phase contracts verified, no lifecycle gaps detected."

EXIT CRITERIA: All lifecycle phases covered. Entry and exit contracts evaluated for every phase boundary.

---

## PHASE 5 -- flow-trigger

For each automation trigger in scope, write one finding block using this structure exactly:

---
Finding FT-[N]
Trigger: [trigger name]
Activating event: [the event or condition that causes the trigger to fire]
Side effects: [every state change or message produced when this trigger fires]
Fire order: [position in execution sequence; concurrent or sequential with which other triggers]
Race condition: [yes | no] -- if yes, name the shared state surface involved and describe the race
Blast radius: [wide | medium | narrow] -- race conditions on shared state surfaces are wide by default
Spec gap: [yes | no]
---

If no conflicts are found:
"flow-trigger: clean -- all triggers verified, no race conditions or conflicts detected."

EXIT CRITERIA: All triggers and all activating events in scope have been evaluated.

---

## CALIBRATION BLOCK

All five sub-skills have completed. Do not rank findings yet.
Re-ground blast radius in evidence before ranking.

Write the following calibration paragraphs:

**Evidence inventory:**
For every finding code from Phases 1-5, state the census component it names.
Example: "TC-1 names the shared event bus. TS-2 names the order state machine."
If any finding cannot name a census component, revise it now before proceeding.

**Shared state re-assessment:**
For each finding that names a component listed under "shared state surfaces" in the census:
if blast radius was assessed as medium or narrow, upgrade it to wide and explain why.
For findings that do not name a shared state surface, confirm their blast radius is
correctly contained (medium or narrow).

**Cross-phase corroboration:**
Identify every root cause surfaced by two or more phases independently. A contract mismatch
that also manifests as a lifecycle gap and a trigger race represents the same root cause
surviving three simulation angles. For each corroborated root cause, write one sentence
explaining why it appears in multiple phases and mark it SYSTEMIC.

**Clean zones:**
Name every census component that appears in zero findings across Phases 1-5.
These components are cleared for implementation. Absence of findings is positive evidence.

**Calibration summary:**
Write one paragraph (4-6 sentences) summarizing the calibration results.
Which findings moved up in blast radius? Which are SYSTEMIC? What is the highest-blast-radius
finding after calibration, and which census component does it name?

---

## CONSOLIDATE

Write ONE report. Do not concatenate five phase outputs.

**Spec gaps:**
For each spec gap confirmed in calibration: state the finding code, the phase, and what
the spec does not address in one sentence. Write "none detected" if clean.

**Contract violations:**
For each contract mismatch from trace-contract: state the finding code and the promise
broken in one sentence. Write "none detected" if clean.

**Ranked findings (calibrated blast radius order, wide first):**
For each finding, write one labeled block:

---
[Finding code] -- [one sentence: what breaks]
Source: [phase name]
Blast radius: [wide | medium | narrow] -- [census component name]; [is | is not] a shared state surface
Severity at epicenter: [high | med | low]
What must change: [one concrete fix direction]
SYSTEMIC: [yes | no] -- [if yes: name the phases that surfaced the same root cause]
---

Do not merge blast radius and severity. They are separate fields. This is not optional.

**Cross-skill findings:**
Repeat every SYSTEMIC finding here with the full list of phases that corroborated it.

**Clean zones:** [list census components with zero findings from calibration]

**VERDICT:** go / conditional-go / no-go. One sentence naming the finding with the widest
blast radius (by its census component name) and its calibrated rank, or stating that
calibration confirmed no blocking findings across all five sub-skills.

Output file: `simulations/{{topic}}/campaign-behavior-{{date}}.md`
```

---

## V-02 -- Behavior-first role sequence
**Axis:** Role sequence -- run the two "what DOES happen" sub-skills first (lifecycle + trigger), then the three "what CAN happen" sub-skills (contract + state + permissions) to diagnose why the behavior breaks
**Hypothesis:** Observing runtime behavior before running structural diagnostics may surface emergent failure modes that contract-first analysis does not predict. The behavior notes after Phases 1-2 serve as explicit leads for the diagnostic phases -- testing whether directing diagnostic attention toward observed anomalies produces higher-signal findings than running all sub-skills independently.

```
Simulate the technical behavior of: {{topic}}

You will run five sub-skills in behavior-first sequence: observe what the system does before
diagnosing why it breaks. The two behavior phases run first and produce explicit diagnostic
leads. The three diagnostic phases use those leads to explain the failures structurally.

---

## BLAST RADIUS DEFINITION

Blast radius = how broadly a failure propagates through the system.
Wide: corrupts shared state, breaks downstream callers, or blocks multiple user roles simultaneously.
Medium: two or more components affected; no shared state surface reached.
Narrow: failure contained within one component boundary.

Severity = damage depth at the epicenter (high / med / low). Independent of blast radius.
Wide blast radius + low severity is possible. Narrow blast radius + high severity is possible.
Record both as separate fields. Never merge them.

---

## PHASE 0 -- Topology census

Before any sub-skill runs, enumerate from the spec or codebase:

**Components in scope:** [every named service, module, API, schema, queue]
**Shared state surfaces:** [databases, caches, event buses, config objects used by multiple components]
**Downstream callers:** [every component that depends on the system under simulation]
**Role-resource inventory:** [every role and the resources it may access]

All blast radius assessments must name a specific census component.
Generic claims are not valid blast radius assessments.

---

## PHASE 1 -- flow-lifecycle (observe behavior: what does the system do?)

Trace the complete business lifecycle from creation to terminal state.
You are observing what the system does -- not yet diagnosing why.
Record every phase boundary, every exception path, and every place where
the spec is silent about what happens.

| Phase | Entry contract | Exit contract | Exception path | Spec silent? | Blast radius (census component) |
|-------|----------------|---------------|----------------|--------------|--------------------------------|

EXIT CRITERIA: All lifecycle phases covered. Entry and exit contracts evaluated for every phase.
If no gaps: write "flow-lifecycle: no behavioral gaps observed."

**Diagnostic leads from Phase 1:**
Write 2-3 sentences identifying unexpected behaviors or spec silences that the lifecycle
trace revealed. These are the leads for Phases 3-5. Be specific about which components
or phase boundaries raised questions.

---

## PHASE 2 -- flow-trigger (observe behavior: what fires, in what order?)

Simulate each automation trigger: fire order, side effects, and potential firing conflicts.
You are observing what fires -- not yet diagnosing race root causes.

| Trigger | Activating event | Side effects | Fire order | Conflict possible? | Shared state surface involved? | Blast radius (census component) | Spec gap? |
|---------|-----------------|--------------|------------|--------------------|---------------------------------|---------------------------------|-----------|

EXIT CRITERIA: All triggers and activating events in scope covered.
If no conflicts: write "flow-trigger: no behavioral conflicts observed."

**Diagnostic leads from Phase 2:**
Write 2-3 sentences identifying trigger interactions or spec silences that warrant
investigation in Phases 3-5. Name the specific triggers and shared state surfaces involved.

---

## PHASE 3 -- trace-contract (diagnose: contract dimension)

Using the diagnostic leads from Phases 1-2 as your starting frame, verify every
producer/consumer pairing. For each behavioral gap or anomaly from Phases 1-2,
ask: is there a contract mismatch that explains it?

For each finding, record the behavioral lead it addresses (if any).

| Producer | Consumer | Contract term | Expected | Actual | Mismatch? | Behavioral lead addressed | Severity | Blast radius (census component) | Spec gap? |
|----------|----------|---------------|----------|--------|-----------|--------------------------|----------|---------------------------------|-----------|

EXIT CRITERIA: All producer/consumer pairs covered. Behavioral leads from Phases 1-2
mapped to contract findings where applicable.
If no mismatches: write "trace-contract: clean."

---

## PHASE 4 -- trace-state (diagnose: state dimension)

Using the diagnostic leads from Phases 1-2, hand-compile every state transition.
For each behavioral gap or trigger conflict from Phases 1-2, ask: is there a state
transition violation or missing transition that explains it?

| State | Preconditions | Trigger | Postcondition | Invariant | Violated? | Behavioral lead addressed | Blast radius (census component) | Spec gap? |
|-------|---------------|---------|---------------|-----------|-----------|--------------------------|--------------------------------|-----------|

EXIT CRITERIA: All states and transitions covered. Behavioral leads mapped where applicable.
If no violations: write "trace-state: clean."

---

## PHASE 5 -- trace-permissions (diagnose: permission dimension)

Using the diagnostic leads from Phases 1-2, walk every role-resource-action combination.
For each behavioral gap from Phases 1-2, ask: is there a permission model failure that
enables or amplifies the observed behavior?

| Role | Resource | Action | Expected access | Actual access | Privilege escalation? | Behavioral lead addressed | Blast radius (census component) | Spec gap? |
|------|----------|--------|-----------------|---------------|-----------------------|--------------------------|--------------------------------|-----------|

EXIT CRITERIA: All role-resource pairs covered. Behavioral leads mapped where applicable.
If no violations: write "trace-permissions: clean."

---

## CALIBRATION BLOCK

All five sub-skills are complete. Before ranking, re-ground blast radius in evidence.

**Evidence inventory:** List every finding from Phases 1-5 with the census component it names.

**Behavioral root cause resolution:** For each diagnostic lead from Phases 1-2, record
whether it was resolved by a finding in Phases 3-5. If a behavioral lead from Phase 1-2
was not explained by any finding in Phases 3-5, flag it as an unexplained behavioral
anomaly and add it to the findings list at RUNTIME ANOMALY status.

**Shared state re-assessment:** For each finding that names a component from the census
"shared state surfaces" list: upgrade blast radius to wide if not already wide.

**Cross-phase corroboration:** Identify findings that appear in two or more phases
(same root cause, multiple simulation angles). Mark them SYSTEMIC.

**Clean zones:** Census components with zero findings across all phases.

Calibration table:

| Finding | Phases | Census component | Shared state? | Behavioral lead resolved? | Blast radius (calibrated) | SYSTEMIC? |
|---------|--------|-----------------|---------------|--------------------------|--------------------------|-----------|

---

## CONSOLIDATE

Write ONE report.

**Spec gaps:** [all spec gaps from calibration, or "none detected"]
**Contract violations:** [all mismatches from trace-contract, or "none detected"]
**Unexplained behavioral anomalies:** [leads from Phases 1-2 not resolved by Phases 3-5, or "none"]

**Ranked findings (calibrated blast radius order, wide first):**
Per finding:
- Source: [phase]
- What breaks: [one sentence]
- Blast radius: [wide | medium | narrow] -- [census component; shared state surface?]
- Severity at epicenter: [high | med | low]
- What must change: [one concrete fix direction]
- SYSTEMIC: [yes | no]

Do not merge blast radius and severity.

**Cross-skill findings:** SYSTEMIC findings with full phase corroboration list.

**Clean zones:** [census components with zero findings]

**VERDICT:** go / conditional-go / no-go. One sentence naming the highest-blast-radius
finding from the calibration table (census component name), or stating that calibration
confirmed no blocking findings.

Output file: `simulations/{{topic}}/campaign-behavior-{{date}}.md`
```

---

## V-03 -- Inertia framing as recurring phase architecture
**Axis:** Inertia framing -- every phase opens with the specific assumption teams hold without simulation; the phase gate closes by declaring whether the assumption was confirmed or displaced
**Hypothesis:** Framing each phase as assumption-testing (not documentation) activates deeper analysis by making the cost of skipping explicit at each step rather than only in a preamble. The assumption-displacement pattern at each EXIT CRITERIA gate tests whether recurrent inertia framing improves execution quality over a single pre-campaign inertia block.

```
Simulate the technical behavior of: {{topic}}

---

## What this campaign measures

Every phase below names one assumption that teams hold before running simulation.
The phase either confirms the assumption is safe or displaces it with evidence.

The cost of a displaced assumption that ships undisplaced is measured as blast radius:
how broadly a failure propagates if the assumption was wrong.
Wide = shared state, multiple callers, or multiple user roles break simultaneously.
Medium = two or more components affected; no shared state surface reached.
Narrow = one component absorbs the failure alone.

Severity = damage at the epicenter (high / med / low). Independent of blast radius.
Both appear in every finding. Never merge them.

---

## PHASE 0 -- Topology census
**Assumption being tested:** "We know what components are in scope."

Record the system vocabulary explicitly. This census is the reference for every blast radius
claim. A blast radius claim that cannot name a component from this census is itself an
undisplaced assumption -- not a finding.

**Components in scope:** [every named service, module, API, schema, queue]
**Shared state surfaces:** [databases, caches, event buses, config objects used by multiple components]
**Downstream callers:** [every component that depends on the system being simulated]
**Role-resource inventory:** [every role and the resources it may access]

Phase gate: Record the census explicitly. Proceed only when every component that will
appear in a blast radius claim is named here.

---

## PHASE 1 -- trace-contract
**Assumption being tested:** "Producers and consumers agree on what is exchanged."

For each producer/consumer pairing, verify expected vs actual output.
A mismatch displaces the assumption for that pairing.

| Producer | Consumer | Contract term | Expected | Actual | Mismatch? | Severity | Blast radius (census component) | Spec gap? |
|----------|----------|---------------|----------|--------|-----------|----------|---------------------------------|-----------|

EXIT CRITERIA: All producer/consumer pairs evaluated.
If no mismatches: write "Assumption confirmed: all producer/consumer contracts hold."
If mismatches: write "Assumption displaced: [N] contract violation(s) found."

---

## PHASE 2 -- trace-state
**Assumption being tested:** "The state machine transitions correctly under all conditions."

Hand-compile every state transition with preconditions and invariants.
A violation or missing transition displaces the assumption.

| State | Preconditions | Trigger | Postcondition | Invariant | Violated? | Blast radius (census component) | Spec gap? |
|-------|---------------|---------|---------------|-----------|-----------|--------------------------------|-----------|

EXIT CRITERIA: All states and all transitions in scope evaluated.
If no violations: write "Assumption confirmed: all state transitions are valid."
If violations: write "Assumption displaced: [N] invariant violation(s) found."

---

## PHASE 3 -- trace-permissions
**Assumption being tested:** "Each role can access exactly what it needs and nothing more."

Walk every role-resource-action combination through the permission model.
An escalation path displaces the assumption and has wide blast radius by default.

| Role | Resource | Action | Expected access | Actual access | Escalation? | Blast radius (census component) | Spec gap? |
|------|----------|--------|-----------------|---------------|-------------|--------------------------------|-----------|

EXIT CRITERIA: All role-resource pairs in the census evaluated.
If no violations: write "Assumption confirmed: no escalation paths detected."
If violations: write "Assumption displaced: [N] permission violation(s) found."

---

## PHASE 4 -- flow-lifecycle
**Assumption being tested:** "The business lifecycle is fully specified from creation to terminal state."

Trace every phase boundary. Every missing entry or exit contract is a displaced assumption
that will arrive as a runtime surprise in production. Exception paths the spec does not
describe are the most expensive category of displaced assumption.

| Phase | Entry contract | Exit contract | Exception path | Gap in spec? | Blast radius (census component) |
|-------|----------------|---------------|----------------|--------------|--------------------------------|

EXIT CRITERIA: All lifecycle phases covered. All entry and exit contracts evaluated.
If no gaps: write "Assumption confirmed: all lifecycle contracts specified."
If gaps: write "Assumption displaced: [N] lifecycle contract gap(s) found."

---

## PHASE 5 -- flow-trigger
**Assumption being tested:** "Automation triggers fire in a predictable order without competing for shared state."

Simulate every trigger's fire order, side effects, and potential races.
A race condition on a shared state surface displaces this assumption at the highest
cost: it is the most expensive category of displaced assumption because it is
non-deterministic and difficult to reproduce post-ship.

| Trigger | Activating event | Side effects | Fire order | Race possible? | Shared state surface? | Blast radius (census component) | Spec gap? |
|---------|-----------------|--------------|------------|----------------|----------------------|---------------------------------|-----------|

EXIT CRITERIA: All triggers and all activating events in scope covered.
If no conflicts: write "Assumption confirmed: no trigger races detected."
If conflicts: write "Assumption displaced: [N] trigger conflict(s) found."

---

## CALIBRATION BLOCK
**Assumption being tested:** "The blast radius assessments from each phase are accurate."

Before ranking, verify that each displacement is grounded in evidence -- not inference.

**Evidence inventory:** For each finding, name the census component it involves.
Findings that cannot name a census component are themselves displaced assumptions.
Revise them now.

**Shared state amplifier:** For each finding naming a shared state surface from the census:
blast radius is wide. Confirm or upgrade. Shared state propagates to all dependent components --
this is the highest-cost category of displaced assumption in this campaign.

**Cross-phase corroboration:** A displaced assumption surfaced by two or more independent
phases is more credible than one surfaced by a single phase. Mark these SYSTEMIC.
A SYSTEMIC finding is one that survived multiple simulation angles -- it was going to
ship regardless of which sub-skill you ran first.

**Clean zones:** Census components where every assumption was confirmed (zero findings).
These components are safe to implement. Confirmed assumptions are a positive campaign output.

Calibration table:

| Finding | Phases | Census component | Shared state? | Assumption displaced? | Blast radius (calibrated) | SYSTEMIC? |
|---------|--------|-----------------|---------------|----------------------|--------------------------|-----------|

---

## CONSOLIDATE

One report. Every finding is a displaced assumption, ranked by the cost of shipping with
it undisplaced.

**Spec gaps:** [displaced completeness assumptions -- or "none displaced"]
**Contract violations:** [displaced producer/consumer assumptions -- or "none displaced"]

**Ranked findings (calibrated blast radius order, wide first):**
Per finding:
- Source: [phase]
- Assumption displaced: [one sentence: what teams believed before simulation, and what
  displaced it]
- Blast radius: wide / medium / narrow -- [census component; shared state surface?]
- Severity at epicenter: high / med / low
- What restores safety: [one concrete action that grounds this assumption in verified reality]
- SYSTEMIC: yes / no

Do not merge blast radius and severity. They are independent dimensions. Both appear in
every finding.

**Cross-skill findings:** SYSTEMIC displaced assumptions with full phase corroboration list.

**Clean zones:** Census components where all assumptions were confirmed.
Name them explicitly -- confirmed assumptions are a positive output of this campaign.

**VERDICT:** go / conditional-go / no-go. One sentence. If displaced assumptions exist,
name the one with the widest blast radius and state what it would cost to ship with it
undisplaced. If no assumptions were displaced, state that the campaign confirmed all
pre-implementation assumptions across all five sub-skills.

Output file: `simulations/{{topic}}/campaign-behavior-{{date}}.md`
```

---

## V-04 -- R3 V-04 architecture + CONFIRMED distinction (C-15 + C-16 + C-18)
**Axis:** Combination -- complete R3 V-04 architecture (Phase 0 census, EXIT CRITERIA per phase, CALIBRATION BLOCK, anti-conflation) extended with CONFIRMED/RUNTIME ANOMALY classification from R3 V-02
**Hypothesis:** R3 V-04 already passes C-15 (EXIT CRITERIA) and C-18 (census). Adding CONFIRMED classification from R3 V-02 closes C-16 without breaking any existing criteria. The CONFIRMED/RUNTIME ANOMALY distinction integrated into the calibration block (rather than the execution phases) tests whether classification at calibration time produces the same rubric outcome as classification at execution time.

```
Simulate the technical behavior of: {{topic}}

---

## BLAST RADIUS -- Definition (active during all phases)

Blast radius = how broadly a failure propagates.
- **Wide:** corrupts shared state, breaks downstream callers, or blocks multiple roles simultaneously
- **Medium:** two or more components affected, no shared state surface reached
- **Narrow:** contained within a single component boundary

**Severity** = damage depth at the epicenter (high / med / low).
These are independent dimensions. Wide blast radius + low severity is possible. Narrow + high
is possible. Do NOT merge them into a single "impact" field at any point in this report.

---

## PHASE 0 -- Topology census

Before any sub-skill runs, enumerate from the spec or codebase:

**Components in scope:**
[list every named service, module, API, schema, queue]

**Shared state surfaces:**
[shared databases, caches, event buses, config objects touched by multiple components]

**Downstream callers:**
[every component that depends on the system being simulated]

**Role-resource inventory:**
[every role and the resources it is permitted to access]

**Pre-declared contracts:**
[any contracts explicitly stated in the spec: "A delivers X to B before Y". These are
the contract topology baseline. Findings in Phases 4-5 that match violations from
Phases 1-3 are CONFIRMED. Findings with no matching topology violation are RUNTIME ANOMALY.]

This census is the vocabulary for all blast radius assessments.
Every finding must name a specific census entry -- not a generic description.

---

## PHASE 1 -- trace-contract

Verify every producer/consumer pairing against the spec contract.
These findings form the contract topology baseline for CONFIRMED classification in Phases 4-5.

| Producer | Consumer | Contract term | Expected | Actual | Mismatch? | Severity | Blast radius (census component) | Spec gap? |
|----------|----------|---------------|----------|--------|-----------|----------|---------------------------------|-----------|

EXIT CRITERIA: All producer/consumer pairs covered.
Write "trace-contract: clean" if no mismatches.

---

## PHASE 2 -- trace-state

Hand-compile every state transition with preconditions and invariants.
These findings form the state topology baseline for CONFIRMED classification in Phases 4-5.

| State | Preconditions | Trigger | Postcondition | Invariant | Violated? | Blast radius (census component) | Spec gap? |
|-------|---------------|---------|---------------|-----------|-----------|--------------------------------|-----------|

EXIT CRITERIA: All states and transitions covered.
Write "trace-state: clean" if no violations.

---

## PHASE 3 -- trace-permissions

Walk every role-resource-action combination through the permission model.
These findings form the permission topology baseline for CONFIRMED classification in Phases 4-5.

| Role | Resource | Action | Expected access | Actual access | Privilege escalation? | Blast radius (census component) | Spec gap? |
|------|----------|--------|-----------------|---------------|-----------------------|--------------------------------|-----------|

EXIT CRITERIA: All role-resource pairs covered.
Write "trace-permissions: clean" if no violations.

---

## PHASE 4 -- flow-lifecycle

Trace the business lifecycle from creation to terminal state, phase by phase.
At each phase boundary, check against findings from Phases 1-3.

| Phase | Entry contract | Exit contract | Exception path | Spec gap? | Blast radius (census component) |
|-------|----------------|---------------|----------------|-----------|--------------------------------|

EXIT CRITERIA: All lifecycle phases covered. All entry and exit contracts evaluated.
Write "flow-lifecycle: clean" if no contract gaps.

---

## PHASE 5 -- flow-trigger

Simulate each automation trigger: fire order, side effects, and race conditions.
At each trigger finding, note which shared state surface is involved.

| Trigger | Activating event | Side effects | Fire order | Race condition? | Shared state surface? | Blast radius (census component) | Spec gap? |
|---------|-----------------|--------------|------------|-----------------|----------------------|---------------------------------|-----------|

EXIT CRITERIA: All triggers and events covered. All races evaluated.
Write "flow-trigger: clean" if no conflicts.

---

## PHASE 6 -- CALIBRATION BLOCK

All five sub-skills are complete. Do not rank yet. Re-ground blast radius and classify
all findings before ordering.

**Step 6a -- Evidence inventory:**
List every finding from Phases 1-5 with the census component it names.

**Step 6b -- CONFIRMED vs RUNTIME ANOMALY classification:**
For each finding from Phases 4-5:
- If it matches a contract mismatch (Phase 1), state violation (Phase 2), or permission
  violation (Phase 3): mark it CONFIRMED. A CONFIRMED finding has structural evidence
  (contract topology) and runtime evidence (simulation). Upgrade its blast radius if the
  matching topology violation is wider.
- If it has no match in Phases 1-3: mark it RUNTIME ANOMALY. A RUNTIME ANOMALY is an
  emergent behavior the contract topology did not predict -- it requires spec amendment
  before implementation.

CONFIRMED findings rank higher than RUNTIME ANOMALY findings of equivalent blast radius.

Classification summary:

| Finding (Phases 4-5) | Matching finding from Phases 1-3 | Classification | Blast radius adjustment |
|---------------------|----------------------------------|----------------|------------------------|

**Step 6c -- Shared state re-assessment:**
For each finding (all phases) that names a shared state surface from the census:
confirm or upgrade blast radius to wide.

**Step 6d -- Cross-phase corroboration:**
Identify findings that appear in two or more phases (same root cause, multiple angles).
Mark them SYSTEMIC. SYSTEMIC findings rank higher than isolated findings of equivalent
blast radius and CONFIRMED status.

**Step 6e -- Clean zone identification:**
Census components with zero findings across all phases. Record them explicitly.
Clean zones are positive evidence -- these components are safe to implement.

Calibration table:

| Finding (summary) | Phases | Census component | Shared state? | CONFIRMED / RUNTIME ANOMALY | Blast radius (calibrated) | SYSTEMIC? |
|-------------------|--------|-----------------|---------------|----------------------------|--------------------------|-----------|

---

## CONSOLIDATE

Write ONE report. Do not concatenate five phase outputs.

**Spec gaps:**
[all spec gaps from calibration step 6a. Write "none detected" if clean.]

**Contract violations:**
[from trace-contract and CONFIRMED findings from Phases 4-5. Write "none detected" if clean.]

**Ranked findings (calibrated blast radius order, wide first):**
Within equivalent blast radius: CONFIRMED > RUNTIME ANOMALY. SYSTEMIC > isolated.
For each finding:

- **Sub-skill source:** [phase]
- **What breaks:** [one sentence]
- **Blast radius:** wide / medium / narrow -- name the census component and whether it
  is a shared state surface
- **Severity at the epicenter:** high / med / low
- **Classification:** CONFIRMED / RUNTIME ANOMALY
- **What must change:** [one concrete fix direction]
- **SYSTEMIC:** yes / no -- if yes, list the phases that corroborated it

Do not merge blast radius and severity. They are separate fields. Always.

**Cross-skill findings:**
List every SYSTEMIC finding with its full phase corroboration list.

**Clean zones:**
Census components from calibration step 6e.
These components are cleared for implementation.

**VERDICT:** go / conditional-go / no-go. One sentence. Name the highest-blast-radius
CONFIRMED finding from the calibration table (using its census component name), or the
highest-blast-radius RUNTIME ANOMALY if no confirmed violations exist, or state that
calibration found no blocking findings.

Output file: `simulations/{{topic}}/campaign-behavior-{{date}}.md`
```

---

## V-05 -- All four new criteria (C-15 + C-16 + C-17 + C-18)
**Axis:** Combination -- full integration of all four v4 aspirational criteria: Phase 0 census (C-18), EXIT CRITERIA per phase (C-15), CONFIRMED/RUNTIME ANOMALY classification (C-16), and interrogative calibration Q1-Q5 (C-17)
**Hypothesis:** C-15, C-16, C-17, and C-18 are architecturally compatible if sequenced correctly: census establishes vocabulary (C-18), contract-anchor phases build topology baseline for CONFIRMED classification (C-16), EXIT CRITERIA gate each phase (C-15), and interrogative Q-form calibration replaces the formal CALIBRATION BLOCK header while still performing evidence re-grounding (C-17). If compatible, this variation is the first candidate for maximum aspirational credit on the v4 rubric.

```
Simulate the technical behavior of: {{topic}}

You will run five sub-skills in contract-anchor sequence, classify runtime findings against
the contract topology baseline, answer five calibration questions before ranking, and produce
one consolidated findings report.

---

## BLAST RADIUS -- Definition (active throughout)

Blast radius = propagation scope.
Wide: corrupts shared state, breaks downstream callers, or blocks multiple user roles.
Medium: two or more components affected; no shared state surface reached.
Narrow: failure contained within one component boundary.

Severity = damage depth at the epicenter (high / med / low). Independent of blast radius.
Report both as separate labeled fields. Never merge them.

---

## PHASE 0 -- Topology census

Before any sub-skill runs, record the system vocabulary.

**Components in scope:** [every named service, module, API, schema, queue from spec or codebase]
**Shared state surfaces:** [databases, caches, event buses, config objects used by multiple components]
**Downstream callers:** [every component depending on the system under simulation]
**Role-resource inventory:** [every role and the resources it may access]

This census serves two purposes:
1. All blast radius assessments must name a specific census component.
2. Findings in Phases 4-5 that match violations from Phases 1-3 are CONFIRMED.
   Findings in Phases 4-5 with no matching topology violation are RUNTIME ANOMALY.

---

## PHASE 1 -- trace-contract (contract topology baseline)

Verify every producer/consumer pairing. These findings are the contract baseline.
Any lifecycle or trigger finding in Phases 4-5 that reproduces a mismatch from here is CONFIRMED.

| Producer | Consumer | Contract term | Expected | Actual | Mismatch? | Severity | Blast radius (census component) | Spec gap? |
|----------|----------|---------------|----------|--------|-----------|----------|---------------------------------|-----------|

EXIT CRITERIA: All producer/consumer pairs in scope evaluated.
If no mismatches: "trace-contract: clean."

---

## PHASE 2 -- trace-state (state topology baseline)

Hand-compile every state transition with preconditions and invariants.
Any trigger finding in Phase 5 that violates an invariant from here is CONFIRMED.

| State | Preconditions | Trigger | Postcondition | Invariant | Violated? | Blast radius (census component) | Spec gap? |
|-------|---------------|---------|---------------|-----------|-----------|--------------------------------|-----------|

EXIT CRITERIA: All states and all transitions in scope evaluated.
If no violations: "trace-state: clean."

---

## PHASE 3 -- trace-permissions (permission topology baseline)

Walk every role-resource-action combination through the permission model.

| Role | Resource | Action | Expected access | Actual access | Escalation? | Blast radius (census component) | Spec gap? |
|------|----------|--------|-----------------|---------------|-------------|--------------------------------|-----------|

EXIT CRITERIA: All role-resource pairs in scope evaluated.
If no violations: "trace-permissions: clean."

---

## PHASE 4 -- flow-lifecycle (runtime -- CONFIRMED classification)

Trace the business lifecycle phase by phase. At each finding, cross-reference Phases 1-3.
Mark CONFIRMED if the finding matches a contract mismatch (Phase 1), state violation (Phase 2),
or permission violation (Phase 3). Mark RUNTIME ANOMALY if no match exists.

| Phase | Entry contract | Exit contract | Exception path | Spec gap? | Phase 1-3 match? | CONFIRMED / RUNTIME ANOMALY | Blast radius (census component) |
|-------|----------------|---------------|----------------|-----------|-----------------|-----------------------------|---------------------------------|

EXIT CRITERIA: All lifecycle phases covered. All findings classified.
If no gaps: "flow-lifecycle: clean."

---

## PHASE 5 -- flow-trigger (runtime -- CONFIRMED classification)

Simulate each automation trigger. Mark CONFIRMED if the finding matches a state invariant
violation (Phase 2) or contract mismatch (Phase 1). Mark RUNTIME ANOMALY if no match.

| Trigger | Activating event | Side effects | Fire order | Race? | Phase 1-3 match? | CONFIRMED / RUNTIME ANOMALY | Blast radius (census component) | Spec gap? |
|---------|-----------------|--------------|------------|-------|-----------------|-----------------------------|---------------------------------|-----------|

EXIT CRITERIA: All triggers and activating events in scope covered. All findings classified.
If no conflicts: "flow-trigger: clean."

---

## Calibration questions (answer before you rank)

You have completed all five sub-skills. Answer these five questions from the findings above --
not from the spec. The answers govern the ranked findings list.

**Q1. Which specific census components actually showed up in your findings?**
List only the component names that appear in the evidence from Phases 1-5.
You are ranking what you found, not what you expected to find. Components not named
in any finding are clean zones -- list them separately.

**Q2. Which findings name a shared state surface?**
For each finding that names a component from the census "shared state surfaces" list:
confirm or upgrade its blast radius to wide. State each upgrade explicitly.
A finding that touches shared state propagates laterally -- its blast radius cannot be
narrow or medium.

**Q3. Which findings are CONFIRMED?**
List every finding classified CONFIRMED in Phases 4-5 and the Phase 1-3 entry it matches.
CONFIRMED findings have structural evidence (Phases 1-3) and runtime evidence (Phases 4-5).
In the ranked list: CONFIRMED > RUNTIME ANOMALY at equivalent blast radius.

**Q4. Which findings appear in two or more phases?**
A finding that surfaces in two or more phases independently is SYSTEMIC -- the same root
cause survived multiple simulation angles. List every SYSTEMIC finding and the phases that
surfaced it. In the ranked list: SYSTEMIC > non-systemic at equivalent blast radius and
CONFIRMED status.

**Q5. What is the single finding whose failure would propagate furthest in production?**
Name it. Name the census component. State whether it is CONFIRMED or RUNTIME ANOMALY.
State whether it is SYSTEMIC. This finding is the VERDICT anchor.

Calibration summary:
Write one paragraph (4-6 sentences). State the adjusted blast radius understanding after
your answers. Which findings moved up in rank? What is the full tier order: CONFIRMED +
SYSTEMIC at the top, then CONFIRMED, then RUNTIME ANOMALY + SYSTEMIC, then RUNTIME ANOMALY?
What did you find that the spec did not predict?

---

## CONSOLIDATE

Write ONE report. Do not concatenate five sub-skill outputs.

**Spec gaps:** [all spec gaps from Phases 1-5, or "none detected"]

**Contract violations:**
[CONFIRMED violations from trace-contract and Phases 4-5. Write "none detected" if clean.]

**Ranked findings (calibrated blast radius order, wide first):**
Within equal blast radius: CONFIRMED + SYSTEMIC > CONFIRMED > RUNTIME ANOMALY + SYSTEMIC >
RUNTIME ANOMALY.

For each finding:
- **Sub-skill source:** [phase]
- **What breaks:** [one sentence]
- **Blast radius:** wide / medium / narrow -- [census component name; shared state surface?]
- **Severity at epicenter:** high / med / low
- **Classification:** CONFIRMED / RUNTIME ANOMALY
- **What must change:** [one concrete fix direction]
- **SYSTEMIC:** yes / no -- if yes, name the phases that surfaced the same root cause

Do not merge blast radius and severity. They are separate fields.

**Cross-skill findings:** Every SYSTEMIC finding with its full phase corroboration list.

**Clean zones:** Census components from Q1 that appeared in zero findings.
These components are cleared for implementation.

**VERDICT:** go / conditional-go / no-go. One sentence citing the Q5 anchor finding --
name the finding, its census component, its CONFIRMED/RUNTIME status, and its blast radius.
Or state that calibration confirmed no blocking findings across all five sub-skills.

Output file: `simulations/{{topic}}/campaign-behavior-{{date}}.md`
```

---

## Variation Summary

| Variation | Axis | New criteria targeted | Hypothesis summary |
|-----------|------|-----------------------|--------------------|
| V-01 | Output format (prose blocks, no tables) | C-15, C-18 (inherited) | Format-independence test: labeled-field prose blocks satisfy same structural criteria as tables |
| V-02 | Role sequence (behavior-first: lifecycle+trigger then contract+state+permissions) | C-15, C-18 (inherited) | Behavior-first observation produces diagnostic leads that direct structural analysis -- tests emergent vs predicted findings |
| V-03 | Inertia framing (recurrent per phase, not preamble-only) | C-15, C-18 (inherited) | Per-phase assumption displacement framing activates deeper analysis than single pre-campaign inertia block |
| V-04 | Combination: R3 V-04 + CONFIRMED/RUNTIME ANOMALY (at calibration time) | C-15, C-16, C-18 | Minimum addition to R3 V-04 to close C-16; classification at calibration time vs execution time |
| V-05 | Combination: all four new criteria simultaneously | C-15, C-16, C-17, C-18 | First candidate for maximum v4 aspirational credit; tests architectural compatibility of CONFIRMED + interrogative calibration |

**Predicted ranking on v4 rubric:** V-05 >= V-04 > V-03 > V-01 > V-02

V-05 is the first variation explicitly targeting all four new aspirational criteria; if the
architecture is coherent, it scores maximum on C-15 through C-18 while inheriting the
C-01 through C-14 coverage from V-04's structural skeleton. V-04 closes C-16 with the
minimum change to R3 V-04 (proven 90/90 on v3) -- likely the safest high scorer.
V-03 and V-01 are structurally sound but target fewer new criteria. V-02's behavior-first
sequence is the highest-risk variation: the diagnostic lead mechanism is novel and may
produce higher-quality findings, but the sub-skill sequence deviates from established
pattern and may cause C-01 scoring ambiguity if the evaluator expects a fixed order.

**Primary unknown:** Does C-17 (interrogative calibration) require the absence of a named
CALIBRATION BLOCK, or can both coexist? V-05 tests the coexistence path. If C-17 and the
CALIBRATION BLOCK are mutually exclusive, V-05 scores on one but not the other. If they
coexist, V-05 is the maximum-coverage variation.
