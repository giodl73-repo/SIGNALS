# Quest Variations — campaign-behavior (R3)
**Skill:** campaign-behavior
**Rubric:** v3 (C-01–C-14, adds CALIBRATION BLOCK as C-14)
**Round:** 3
**Date:** 2026-03-17

---

## V-01 — Calibration block injected into R2 V-05 base
**Axis:** Lifecycle emphasis — CALIBRATION BLOCK added as Phase 6 between sub-skill execution and consolidation
**Hypothesis:** A single named CALIBRATION BLOCK inserted after all five sub-skills and before CONSOLIDATE closes C-14 without disturbing the 90/90 pattern from R2 V-05.

```
Simulate the technical behavior of: {{topic}}

---

## BLAST RADIUS DEFINITION (read before any sub-skill runs)

Blast radius = how broadly a failure propagates across the system.
Wide blast radius: corrupts shared state, breaks downstream callers, or
  blocks multiple user roles simultaneously.
Narrow blast radius: isolated to one operation or one component boundary.
Do NOT substitute severity, priority, or frequency for blast radius.

---

## PHASE 0 — Pre-execution topology census

Before running any sub-skill, enumerate from the spec or codebase:

- **Components:** List every named component in scope (services, modules, APIs, schemas, queues)
- **Shared state surfaces:** Identify shared databases, caches, event buses, or configuration objects that multiple components read or write
- **Downstream callers:** List every component that depends on the system under simulation
- **Permission boundaries:** List every role and resource pairing in scope

Record this census as a block at the top of your report.
All blast radius assessments must name a specific artifact from this census.

---

## PHASE 1 — trace-contract

For each producer/consumer pairing in the spec, verify expected vs actual output:

| Producer | Consumer | Contract term | Expected | Actual | Mismatch? | Severity | Blast radius | Spec gap? |
|----------|----------|---------------|----------|--------|-----------|----------|--------------|-----------|

EXIT CRITERIA: Record all mismatches. If no mismatches, write "trace-contract: clean."

---

## PHASE 2 — trace-state

Hand-compile every state transition in the system:

| State | Preconditions | Trigger | Postcondition | Invariant | Violated? | Blast radius | Spec gap? |
|-------|---------------|---------|---------------|-----------|-----------|--------------|-----------|

EXIT CRITERIA: Record all violations. If no violations, write "trace-state: clean."

---

## PHASE 3 — trace-permissions

Walk every role-resource-action combination through the permission model:

| Role | Resource | Action | Expected access | Actual access | Escalation? | Blast radius | Spec gap? |
|------|----------|--------|-----------------|---------------|-------------|--------------|-----------|

EXIT CRITERIA: Record all violations. If no violations, write "trace-permissions: clean."

---

## PHASE 4 — flow-lifecycle

Trace the complete business lifecycle from creation to terminal state:

| Phase | Entry contract | Exit contract | Exception path | Gap in spec? | Blast radius |
|-------|----------------|---------------|----------------|--------------|--------------|

EXIT CRITERIA: Record all phase contract gaps. If none, write "flow-lifecycle: clean."

---

## PHASE 5 — flow-trigger

Simulate each automation trigger: for each triggering event, show fire order, side effects, and races:

| Trigger | Event | Side effects | Fire order | Race condition? | Blast radius | Spec gap? |
|---------|-------|--------------|------------|-----------------|--------------|-----------|

EXIT CRITERIA: Record all trigger conflicts. If none, write "flow-trigger: clean."

---

## PHASE 6 — CALIBRATION BLOCK

Before ranking, calibrate blast radius against actual findings — not against pre-declared topology.

1. **Evidence inventory:** List every finding from Phases 1-5 with the component name from the census that it touches.
2. **Re-assess propagation:** For each finding, ask: does this finding affect a shared state surface from the census? If yes, upgrade blast radius. If no, confirm it is contained to a single component.
3. **Topology correction:** Identify any component listed in the census that was not touched by any finding. These are clean zones. Remove them from blast radius calculations.
4. **Cross-phase corroboration:** Identify findings that appear in two or more phases. Mark them SYSTEMIC. Systemic findings rank higher than isolated findings of equivalent blast radius.

Record calibration results as a table:

| Finding | Phases that surfaced it | Census component(s) affected | Shared state? | Blast radius (calibrated) | SYSTEMIC? |
|---------|------------------------|------------------------------|---------------|--------------------------|-----------|

---

## CONSOLIDATE — One report

Write ONE report. Not five.

**Spec gaps:** List all spec gaps from the census. Write "none detected" if clean.

**Contract violations:** List all producer/consumer mismatches. Write "none detected" if clean.

**Ranked findings (blast radius order, calibrated):** Use the calibration table. Wide blast radius first.
For each finding:
- **Sub-skill source:** [phase that found it]
- **What breaks:** [one clear sentence]
- **Blast radius:** wide / medium / narrow — and why (name the census component affected)
- **Severity at the epicenter:** high / med / low
- **What must change:** [one clear direction]
- **SYSTEMIC:** yes / no

Do not merge severity and blast radius into a single "impact" field. They measure different things.

**Cross-skill findings:** Repeat SYSTEMIC findings here with their phase list.

**VERDICT:** go / conditional-go / no-go. One sentence rationale. Name the highest-blast-radius
finding from the calibration table, or state that no blocking findings were detected.

Output file: `simulations/{{topic}}/campaign-behavior-{{date}}.md`
```

---

## V-02 — Contract-anchor sequence with calibration phased-in
**Axis:** Role sequence — permissions + state + contract run first (what CAN happen), lifecycle + trigger second (what DOES happen); calibration reconciles the two sets
**Hypothesis:** Running the three "what CAN happen" sub-skills before the two "what DOES happen" sub-skills gives the calibration block a contract baseline to re-ground against — distinguishing topology violations from runtime violations.

```
Simulate the technical behavior of: {{topic}}

You will run five sub-skills in contract-anchor sequence, then calibrate, then consolidate.
The sequence is deliberate: establish what is supposed to happen before simulating what does happen.

---

## BLAST RADIUS DEFINITION

Blast radius measures propagation scope, not damage severity.
Wide: a failure propagates to shared state, multiple roles, or downstream callers.
Narrow: a failure is contained within a single component boundary.
Severity measures damage depth at the epicenter (high/med/low). These are distinct dimensions.
Record both. Never merge them.

---

## STEP 1 — trace-permissions (establish access topology)

Walk every role-resource-action pairing through the permission model.
These findings define the access topology all other sub-skills run against.

| Role | Resource | Action | Expected | Actual | Privilege escalation? | Blast radius | Spec gap? |
|------|----------|--------|----------|--------|-----------------------|--------------|-----------|

Checkpoint: confirm permission topology is recorded before proceeding.

---

## STEP 2 — trace-state (establish state topology)

Hand-compile every state transition. Preconditions and invariants define the legal state space.
These findings are the baseline for lifecycle simulation.

| State | Preconditions | Trigger | Postcondition | Invariant | Violated? | Blast radius | Spec gap? |
|-------|---------------|---------|---------------|-----------|-----------|--------------|-----------|

Checkpoint: confirm state topology is recorded before proceeding.

---

## STEP 3 — trace-contract (establish contract topology)

Verify every producer/consumer pairing. Contract violations here are the gold standard for
mismatches -- they represent promises the system is breaking, not just runtime anomalies.

| Producer | Consumer | Contract term | Expected | Actual | Mismatch? | Severity | Blast radius | Spec gap? |
|----------|----------|---------------|----------|--------|-----------|----------|--------------|-----------|

Checkpoint: confirm contract topology is recorded before proceeding.

---

## STEP 4 — flow-lifecycle (simulate against contract baseline)

Now simulate the business lifecycle. At each phase boundary, check the contracts from Step 3.
Any lifecycle violation that also matches a contract mismatch from Step 3 is a confirmed
violation -- mark CONFIRMED.

| Phase | Entry contract | Exit contract | Exception path | Contract match from Step 3? | Blast radius | Spec gap? |
|-------|----------------|---------------|----------------|------------------------------|--------------|-----------|

---

## STEP 5 — flow-trigger (simulate trigger dynamics against state baseline)

Simulate each automation trigger. At each trigger, check state preconditions from Step 2.
Any trigger race that also violates a state invariant from Step 2 is a confirmed violation
-- mark CONFIRMED.

| Trigger | Event | Side effects | Fire order | Race? | State invariant violated (Step 2)? | Blast radius | Spec gap? |
|---------|-------|--------------|------------|-------|------------------------------------|--------------|-----------|

---

## CALIBRATION BLOCK

You have now run all five sub-skills. The contract topology from Steps 1-3 is your baseline.
Re-ground blast radius in what you actually found, not in what you expected to find.

**Calibration steps:**

1. **Contract-baseline reconciliation:** For each finding from Steps 4-5, check whether a
   matching entry exists in the contract topology (Steps 1-3). If yes: this is a CONFIRMED
   violation. Upgrade its blast radius -- contract violations propagate by definition. If no
   match: the finding is a RUNTIME anomaly with no contract precedent.

2. **Cross-step corroboration:** Any finding that appears in two or more steps is SYSTEMIC.
   List them. Systemic findings rank higher than isolated findings of equivalent blast radius.

3. **Spec gap audit:** Collect all "Spec gap? = yes" entries from all five steps.

Calibrated finding summary:

| Finding | Steps that surfaced it | CONFIRMED contract violation? | SYSTEMIC? | Blast radius (calibrated) | Severity |
|---------|----------------------|-------------------------------|-----------|--------------------------|---------|

---

## CONSOLIDATE

Write ONE report synthesizing all steps and calibration.

**Spec gaps:** [from calibration audit -- or "none detected"]
**Contract violations:** [CONFIRMED violations from calibration -- or "none detected"]

**Ranked findings (by calibrated blast radius, wide first):**
Per finding: sub-skill source | what breaks | blast radius (wide/med/narrow) | severity
(high/med/low) | what must change | CONFIRMED? | SYSTEMIC?

Do not merge blast radius and severity.

**VERDICT:** go / conditional-go / no-go. One sentence naming the highest-blast-radius
CONFIRMED finding, or stating that no confirmed violations were detected.

Output file: `simulations/{{topic}}/campaign-behavior-{{date}}.md`
```

---

## V-03 — Interrogative calibration (evidence-first phrasing register)
**Axis:** Phrasing register — conversational interrogative calibration replaces formal CALIBRATION BLOCK; five questions force evidence-grounding through natural language rather than phase architecture
**Hypothesis:** An interrogative calibration pattern achieves C-14's evidence-grounding intent through questions rather than a named phase -- testing whether the mechanism or the label matters more for rubric passage.

```
Simulate the technical behavior of: {{topic}}

Run all five sub-skills, then answer five calibration questions before ranking.

---

## What you are doing and why

You are running a behavioral simulation campaign. You will find things the spec doesn't say.
You will find promises components are making that other components are not keeping.
You will find state machines with missing transitions and triggers that race each other.

The output is a ranked findings report. The ranking criterion is blast radius:
how broadly does this failure propagate if it happens? Wide = shared state, multiple roles,
downstream callers all break. Narrow = one component absorbs the failure alone.

This is not the same as severity. A narrow bug that corrupts a shared cache has
wide blast radius. A critical bug that crashes one optional component has narrow blast radius.
Both dimensions matter. Neither subsumes the other.

---

## Sub-skill execution

Run each sub-skill against {{topic}}. For each, produce a findings section.
If a sub-skill finds nothing, write "[sub-skill]: no findings -- clean."

**trace-contract** -- For each producer/consumer pair in scope, compare expected vs actual output.
Report: producer, consumer, expected, actual, mismatch type, severity, blast radius, spec gap?

**trace-state** -- Hand-compile every state transition.
Report: from-state, trigger, to-state, preconditions, postcondition, invariant, violated?, blast radius, spec gap?

**trace-permissions** -- Walk every role-resource-action combination through the permission model.
Report: role, resource, action, expected access, actual access, privilege escalation?, blast radius, spec gap?

**flow-lifecycle** -- Trace the complete business process lifecycle phase by phase.
Report: phase, entry contract, exit contract, exception path, violation?, blast radius, spec gap?

**flow-trigger** -- Simulate each automation trigger for fire order and side effects.
Report: trigger, event, side effects, fire order, race condition?, blast radius, spec gap?

---

## Calibration questions (answer before you rank)

You have now run all five sub-skills. Before you rank the findings, answer these five questions.
The answers will change how you rank. Answer from the findings above -- not from the spec.

**Q1. Which specific components actually showed up in your findings?**
List the component names that appear in the evidence above. You are ranking what you found,
not what you feared you might find.

**Q2. Which findings touch shared state or shared infrastructure?**
Name every finding where the affected component is something multiple other components depend on
(a shared database table, a cache layer, an event bus, a shared schema type). These have wide
blast radius by definition -- flag them.

**Q3. Which findings appeared in more than one sub-skill?**
A finding corroborated by two or more sub-skills is SYSTEMIC. It means the same root cause is
propagating across simulation boundaries. List these.

**Q4. Which spec gaps, if left unfixed, would make a finding worse?**
Label those findings "spec-gap-amplified."

**Q5. What is the single finding that, if it went wrong in production, would wake up the most people?**
This is your blast-radius anchor. Name the component from your findings that it touches.

Calibration summary (one paragraph): Based on your answers, state the adjusted blast radius
understanding. Which findings moved up in rank? Which moved down? What did you find that you
did not expect based on the spec alone?

---

## Consolidate

Write ONE report.

**Spec gaps:** [list from Q4 evidence -- or "none detected"]
**Contract violations:** [from trace-contract findings -- or "none detected"]

**Ranked findings (calibrated blast radius, wide first):**
For each finding:
- Source: [sub-skill]
- What breaks: [one sentence]
- Blast radius: wide / medium / narrow (from calibration -- cite the component from Q1)
- Severity at epicenter: high / med / low
- Fix direction: [one clear action]
- SYSTEMIC: yes / no (from Q3)

**VERDICT:** go / conditional-go / no-go. One sentence citing the Q5 anchor finding, or
stating that calibration found no blocking findings.

Output file: `simulations/{{topic}}/campaign-behavior-{{date}}.md`
```

---

## V-04 — R2 V-05 base + CALIBRATION BLOCK (structural completion)
**Axis:** Combination — complete R2 V-05 architecture (census + typed schemas + phase gates + anti-conflation + systemic elevation) with CALIBRATION BLOCK injected as Phase 6
**Hypothesis:** R2 V-05 already passes C-01 through C-13. Adding a structurally-positioned CALIBRATION BLOCK closes C-14 without breaking any existing criteria -- first candidate for 90/90 on v3 rubric.

```
Simulate the technical behavior of: {{topic}}

---

## BLAST RADIUS -- Definition (active during all phases)

Blast radius = how broadly a failure propagates.
- **Wide:** corrupts shared state, breaks downstream callers, or blocks multiple roles simultaneously
- **Medium:** two or more components affected, no shared state surface reached
- **Narrow:** contained within a single component boundary

**Severity** = damage depth at the epicenter (high / med / low).
These are independent dimensions. Wide blast radius + low severity is possible. Narrow + high is possible.
Do NOT merge them into a single "impact" field at any point in this report.

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

This census is the vocabulary for all blast radius assessments.
Every finding must name a specific entry from this census -- not a generic description.

---

## PHASE 1 -- trace-contract

Verify every producer/consumer pairing against the spec contract.

| Producer | Consumer | Contract term | Expected | Actual | Mismatch? | Severity | Blast radius (census component) | Spec gap? |
|----------|----------|---------------|----------|--------|-----------|----------|---------------------------------|-----------|

EXIT CRITERIA: All producer/consumer pairs covered. Write "trace-contract: clean" if no mismatches.

---

## PHASE 2 -- trace-state

Hand-compile every state transition with preconditions and invariants.

| State | Preconditions | Trigger | Postcondition | Invariant | Violated? | Blast radius (census component) | Spec gap? |
|-------|---------------|---------|---------------|-----------|-----------|----------------------------------|-----------|

EXIT CRITERIA: All states and transitions covered. Write "trace-state: clean" if no violations.

---

## PHASE 3 -- trace-permissions

Walk every role-resource-action combination through the permission model.

| Role | Resource | Action | Expected access | Actual access | Privilege escalation? | Blast radius (census component) | Spec gap? |
|------|----------|--------|-----------------|---------------|-----------------------|---------------------------------|-----------|

EXIT CRITERIA: All role-resource pairs covered. Write "trace-permissions: clean" if no violations.

---

## PHASE 4 -- flow-lifecycle

Trace the business lifecycle from creation to terminal state, phase by phase.

| Phase | Entry contract | Exit contract | Exception path | Spec gap? | Blast radius (census component) |
|-------|----------------|---------------|----------------|-----------|----------------------------------|

EXIT CRITERIA: All lifecycle phases covered. Write "flow-lifecycle: clean" if no contract gaps.

---

## PHASE 5 -- flow-trigger

Simulate each automation trigger: fire order, side effects, and race conditions.

| Trigger | Event | Side effects | Fire order | Race condition? | Blast radius (census component) | Spec gap? |
|---------|-------|--------------|------------|-----------------|---------------------------------|-----------|

EXIT CRITERIA: All triggers and events covered. Write "flow-trigger: clean" if no conflicts.

---

## PHASE 6 -- CALIBRATION BLOCK

All five sub-skills have completed. Before ranking, re-ground blast radius in what you actually found.

**Step 6a -- Evidence inventory:**
List every finding from Phases 1-5 with the census component it names.

**Step 6b -- Shared state check:**
For each finding, does it touch a shared state surface from the census?
If yes: the blast radius is wide by definition -- update if it was assessed as medium or narrow.
If no: confirm the finding is contained to the named component.

**Step 6c -- Topology correction:**
Identify census components that appear in zero findings. These are clean zones.
Note them explicitly -- absence of evidence is evidence of absence for those components.

**Step 6d -- Cross-phase corroboration:**
Identify findings that appear in two or more phases. Mark them SYSTEMIC.
Systemic findings rank HIGHER than isolated findings of equivalent blast radius.

Calibration table:

| Finding (summary) | Phases that surfaced it | Census component(s) | Shared state surface? | Blast radius (calibrated) | SYSTEMIC? |
|-------------------|------------------------|---------------------|-----------------------|--------------------------|-----------|

---

## CONSOLIDATE

Write ONE report. Do not concatenate five separate outputs.

**Spec gaps:**
[from calibration step 6c -- all spec gaps collected across all phases]
Write "none detected" if every case was covered.

**Contract violations:**
[from trace-contract findings and any corroborating evidence from other phases]
Write "none detected" if clean.

**Ranked findings (calibrated blast radius, wide first):**
Use the calibration table from Phase 6. For each finding:

- **Sub-skill source:** [phase]
- **What breaks:** [one sentence]
- **Blast radius:** wide / medium / narrow -- name the census component affected and whether
  it is a shared state surface
- **Severity at the epicenter:** high / med / low
- **What must change:** [one clear fix direction]
- **SYSTEMIC:** yes / no

Do not merge blast radius and severity. They are separate labeled fields. Always.

**Cross-skill findings:**
List every SYSTEMIC finding from calibration step 6d, with the phases that corroborated it.

**VERDICT:** go / conditional-go / no-go. One sentence. Name the highest-blast-radius finding
from the calibration table (using its census component name), or state that calibration found
no blocking findings.

Output file: `simulations/{{topic}}/campaign-behavior-{{date}}.md`
```

---

## V-05 -- Full integration: census + schemas + calibration + phase gates + anti-conflation + inertia framing
**Axis:** Combination -- all R2 V-05 patterns + CALIBRATION BLOCK + inertia framing positioning the campaign against "just reading the spec" as the status-quo baseline
**Hypothesis:** Inertia framing activates thoroughness across all phases by naming the cost of skipping each step; combined with full structural architecture, produces higher fidelity on every aspirational criterion including C-14 -- while specifically reducing partial execution failure modes.

```
Simulate the technical behavior of: {{topic}}

---

## Why this campaign exists

Without this campaign, teams read the spec and assume they understand system behavior.
The spec describes the happy path. It is silent about state races, permission gaps,
trigger conflicts, and producer/consumer mismatches. Every finding in this campaign
is something you would have shipped without it.

The output replaces three categories of expensive post-ship work:
1. Bug triage that reveals "the spec didn't say" -- surfaced here as spec gaps
2. Integration failures between components -- surfaced here as contract violations
3. Production incidents with wide propagation -- surfaced here by blast radius ranking

This campaign runs before implementation. Run it now or debug it in production.

---

## BLAST RADIUS -- Active definition

Blast radius = how broadly a failure propagates through the system.
- **Wide:** affects shared state, multiple downstream callers, or multiple user roles
- **Medium:** two or more components affected; no shared state surface reached
- **Narrow:** contained within one component boundary

**Severity** = damage at the epicenter (high / med / low). Independent dimension.
A narrow bug with high severity affects one component deeply.
A wide bug with low severity ripples broadly but shallowly.
Both dimensions appear as named fields in every finding. Never merge them.

---

## PHASE 0 -- Topology census

Record this before any sub-skill runs. These names are the vocabulary for all blast radius claims.

**Components in scope:**
[list every named service, module, API, schema, queue -- from the spec or codebase]

**Shared state surfaces:**
[shared databases, caches, event buses, config objects read/written by multiple components]

**Downstream callers:**
[every component that depends on the system under simulation]

**Role-resource inventory:**
[every role + the resources it may access -- the permission perimeter]

If a blast radius claim cannot name a component from this census, it is a generic claim.
Return to the spec and name the component before proceeding.

---

## PHASE 1 -- trace-contract

Verify every producer/consumer pairing. Contract violations are promises the system is already breaking.

| Producer | Consumer | Contract term | Expected | Actual | Mismatch type | Severity | Blast radius (census component) | Spec gap? |
|----------|----------|---------------|----------|--------|---------------|----------|---------------------------------|-----------|

EXIT CRITERIA: All producer/consumer pairs evaluated.
If no mismatches: write "trace-contract: clean -- no contract violations detected."

---

## PHASE 2 -- trace-state

Hand-compile every state transition. Missing transitions are silent failure modes.

| State | Preconditions | Trigger | Postcondition | Invariant checked | Violated? | Blast radius (census component) | Spec gap? |
|-------|---------------|---------|---------------|-------------------|-----------|---------------------------------|-----------|

EXIT CRITERIA: All states and all transitions covered.
If no violations: write "trace-state: clean -- no invariant violations detected."

---

## PHASE 3 -- trace-permissions

Walk every role-resource-action combination. Privilege escalation = wide blast radius by default.

| Role | Resource | Action | Expected access | Actual access | Escalation? | Blast radius (census component) | Spec gap? |
|------|----------|--------|-----------------|---------------|-------------|----------------------------------|-----------|

EXIT CRITERIA: All role-resource pairs covered.
If no violations: write "trace-permissions: clean -- no escalation paths detected."

---

## PHASE 4 -- flow-lifecycle

Trace the business process lifecycle from creation to terminal state.
Phase boundaries are contract boundaries -- every phase entry and exit is a testable claim.

| Phase | Entry contract | Exit contract | Exception path | Gap in spec? | Blast radius (census component) |
|-------|----------------|---------------|----------------|--------------|----------------------------------|

EXIT CRITERIA: All lifecycle phases covered, entry and exit contracts evaluated.
If no gaps: write "flow-lifecycle: clean -- no lifecycle contract gaps detected."

---

## PHASE 5 -- flow-trigger

Simulate every automation trigger. Triggers that share preconditions can race. Races that
touch shared state surfaces are wide blast radius.

| Trigger | Activating event | Side effects | Fire order | Race possible? | Shared state hit? | Blast radius (census component) | Spec gap? |
|---------|-----------------|--------------|------------|----------------|-------------------|---------------------------------|-----------|

EXIT CRITERIA: All triggers and events covered, races evaluated.
If no conflicts: write "flow-trigger: clean -- no trigger conflicts detected."

---

## PHASE 6 -- CALIBRATION BLOCK

All five sub-skills are complete. Do not rank yet. Re-ground blast radius in evidence.

The census described what you expected to find. The findings describe what you actually found.
Calibration reconciles the two. Findings that were not anticipated by the topology deserve
re-assessment. Findings that were anticipated but did not materialize reduce blast radius estimates.

**6a -- Evidence inventory:**
List every finding from Phases 1-5. For each, record the census component it names.

**6b -- Shared state re-assessment:**
For each finding, check: does the named component appear under "shared state surfaces" in the census?
- If yes and blast radius was not already "wide": upgrade to wide. Shared state propagates laterally.
- If no: confirm blast radius is contained. Narrow or medium confirmed.

**6c -- Clean zone identification:**
Which census components appear in zero findings? Record them as clean zones.
These are meaningful -- they mean the spec is coherent for those components.
Knowing what is safe is as valuable as knowing what is not.

**6d -- Cross-phase corroboration:**
Which findings appear in two or more phases?
Mark them SYSTEMIC. Systemic findings rank higher than isolated findings of equivalent blast radius.
A finding corroborated by multiple independent simulation methods is more credible, not just
better labeled.

Calibration output table:

| Finding (one line) | Phases | Census component | Shared state surface? | Blast radius (calibrated) | Severity | SYSTEMIC? |
|--------------------|--------|------------------|-----------------------|--------------------------|---------|-----------|

---

## CONSOLIDATE

One report. Do not concatenate five sub-skill outputs.

**Spec gaps:**
Compile all spec gaps from the calibration inventory. Write "none detected" if the spec covered
every case.

**Contract violations:**
Compile all mismatches from trace-contract and any corroborating evidence from other phases.
Write "none detected" if clean.

**Ranked findings (calibrated blast radius order, wide first):**
Use the calibration table from Phase 6. Sort by calibrated blast radius, then SYSTEMIC status for ties.
For each finding:

- **Sub-skill source:** [phase name]
- **What breaks:** [one sentence]
- **Blast radius:** wide / medium / narrow -- name the census component and whether it is a
  shared state surface
- **Severity at the epicenter:** high / med / low
- **What must change:** [one concrete fix direction]
- **SYSTEMIC:** yes / no -- if yes, list the phases that corroborated it

Do not merge blast radius and severity. They are separate fields. This is not optional.

**Cross-skill findings:**
Repeat every SYSTEMIC finding here with its full phase corroboration list.

**Clean zones:**
List census components with zero findings from calibration step 6c.
These components are cleared for implementation.

**VERDICT:** go / conditional-go / no-go. One sentence. Name the finding from the calibration
table with the widest blast radius and highest corroboration, or state that calibration
confirmed no blocking findings across all five sub-skills.

Output file: `simulations/{{topic}}/campaign-behavior-{{date}}.md`
```

---

## Variation Summary

| Variation | Axis | Hypothesis summary |
|-----------|------|--------------------|
| V-01 | Lifecycle emphasis | Injects CALIBRATION BLOCK as Phase 6 into R2 V-05 base -- minimal change, tests C-14 closure alone |
| V-02 | Role sequence | Contract-anchor order (permissions->state->contract->lifecycle->trigger) feeds calibration block with baseline evidence |
| V-03 | Phrasing register | Interrogative calibration (5 questions) replaces formal CALIBRATION BLOCK -- tests mechanism vs label |
| V-04 | Combination (C-14 + R2 V-05) | Full R2 V-05 skeleton (census + typed schemas + gates + anti-conflation) + CALIBRATION BLOCK -- first structural 90/90 candidate |
| V-05 | Combination (all + inertia) | V-04 + inertia framing + clean zone reporting -- positions against "just reading the spec" as status-quo competitor |

**Predicted ranking:** V-04 >= V-05 > V-01 > V-02 > V-03

V-04 and V-05 are structurally complete against the rubric. V-01 inherits R2 V-05 base so
is likely 88+ before calibration is scored. V-02's contract-anchor sequence adds semantic
sophistication but may dilute direct criterion targeting. V-03 is highest-risk: interrogative
calibration may pass C-14 (evidence-grounding intent satisfied) or fail it (no named
CALIBRATION BLOCK = no named synthesis phase as specified by criterion).
