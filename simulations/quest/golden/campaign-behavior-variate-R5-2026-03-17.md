# Quest Variations -- campaign-behavior (R5)
**Skill:** campaign-behavior
**Rubric:** v4 (C-01--C-18)
**Round:** 5
**Date:** 2026-03-17

---

## Axes explored in R5

Single-axis (unexplored as of R4):
- **Permissions-anchor sequence** -- permissions first establishes access surface before contract/state/flow phases
- **Phrasing register** -- descriptive/interrogative throughout (no imperative instructions)
- **Asymmetric lifecycle emphasis** -- explicit DEPTH labels per phase based on expected blast-radius yield

Combinations (V-04, V-05):
- **V-04:** Phrasing register + scorecard output format
- **V-05:** Permissions-anchor + asymmetric depth + inertia at VERDICT only + CONFIRMED/RUNTIME ANOMALY

---

## V-01 -- Permissions-anchor role sequence
**Axis:** Role sequence -- run trace-permissions first to establish the access surface, then trace-state to map what state is reachable through that surface, then trace-contract to verify what crosses role boundaries, then flow-lifecycle and flow-trigger to observe runtime behavior within the permission/state/contract envelope
**Hypothesis:** Permissions define the blast radius amplifier: a role that can write to a shared state surface determines how widely any single failure propagates. Starting from permissions and working inward may pre-classify blast radius before any lifecycle or trigger findings exist, improving calibration accuracy and surface high-privilege escalation paths that contract-first analysis underweights.

```
Simulate the technical behavior of: {{topic}}

You will run five sub-skills in permissions-anchor sequence: establish the access surface
(trace-permissions), map state reachability through that surface (trace-state), verify
contracts that cross role boundaries (trace-contract), then observe runtime behavior within
the permission/state/contract envelope (flow-lifecycle, flow-trigger).

---

## BLAST RADIUS DEFINITION

Blast radius = how broadly a failure propagates through the system.
Wide: corrupts shared state, breaks downstream callers, or blocks multiple user roles simultaneously.
Medium: two or more components affected; no shared state surface reached.
Narrow: failure contained within one component boundary.

Severity = damage depth at the epicenter (high / med / low). Independent of blast radius.
A wide blast radius with low severity is possible. A narrow blast radius with high severity is possible.
Report both as separate labeled fields in every finding. Never merge them.

---

## PHASE 0 -- Topology census

Before any sub-skill runs, record the system vocabulary explicitly.
This census is the reference for all blast radius assessments.

**Components in scope:** [every named service, module, API, schema, queue from the spec or codebase]

**Shared state surfaces:** [databases, caches, event buses, config objects touched by multiple components --
these are the blast radius amplifiers; any role that can write here determines maximum blast radius]

**Downstream callers:** [every component whose behavior depends on the system under simulation]

**Role-resource inventory:** [every role and the resources it is permitted to access --
organize by role: list each role, then the resources it can read/write/execute]

Every blast radius assessment below must name a specific item from this census.
A finding that cannot name a census item is not a finding -- return to the spec and
identify the component before recording it.

---

## PHASE 1 -- trace-permissions (access surface anchor)

Run trace-permissions first. The goal: identify which roles can reach shared state surfaces.
Any role with write access to a shared state surface is the highest blast radius amplifier
in the system -- it sets the upper bound for all subsequent findings.

For each role-resource-action combination in the census:

| Role | Resource | Action | Expected access | Actual access | Privilege escalation? | Shared state surface? | Blast radius (census component) | Spec gap? |
|------|----------|--------|-----------------|---------------|-----------------------|-----------------------|--------------------------------|-----------|

If escalation is found: blast radius is wide by default.
If the escalated resource is a shared state surface: blast radius is wide and systemic by default.

EXIT CRITERIA: All role-resource pairs in the census have been evaluated.
Write "trace-permissions: clean -- no escalation paths detected." if no violations.
Write "trace-permissions: [N] escalation path(s) found, [N] involving shared state surfaces." if violations.

---

## PHASE 2 -- trace-state (state reachability through permission surface)

Run trace-state second. Use the permission surface from Phase 1 as your frame:
for each state transition, note which role can trigger it and whether that role's
access (from Phase 1) is appropriate for the resulting state change.

For each state transition in the system:

| State | Preconditions | Trigger | Triggering role (from Phase 1) | Postcondition | Invariant | Violated? | Role access appropriate? | Blast radius (census component) | Spec gap? |
|-------|---------------|---------|-------------------------------|---------------|-----------|-----------|--------------------------|--------------------------------|-----------|

A state transition that can be triggered by a role whose Phase 1 access was flagged
as an escalation path is automatically CONFIRMED (structural evidence + runtime evidence).
Mark it CONFIRMED in the table.

EXIT CRITERIA: All states and all transitions in scope have been evaluated.
Write "trace-state: clean -- all transitions verified." if no violations.

---

## PHASE 3 -- trace-contract (contracts that cross role boundaries)

Run trace-contract third. Focus on producer/consumer pairs where the producer and consumer
operate under different roles or permission sets (identified in Phase 1).
Cross-role contracts are the contracts most likely to produce blast radius wider than
a single component.

For each producer/consumer pairing:

| Producer | Producer role | Consumer | Consumer role | Contract term | Expected | Actual | Mismatch? | Roles same? | Severity | Blast radius (census component) | Spec gap? |
|----------|--------------|----------|--------------|---------------|----------|--------|-----------|-------------|----------|---------------------------------|-----------|

If the producer and consumer operate under different roles AND a mismatch exists:
this finding inherits the blast radius of the widest Phase 1 violation for either role.
Mark it CONFIRMED if it connects to a Phase 1 or Phase 2 finding.

EXIT CRITERIA: All producer/consumer pairs covered.
Write "trace-contract: clean -- all contracts verified." if no mismatches.

---

## PHASE 4 -- flow-lifecycle (runtime behavior within permission/state/contract envelope)

Run flow-lifecycle fourth. For each lifecycle phase, note which role drives entry or exit.
Check: does the role driving this phase boundary have the expected permissions from Phase 1?
Does the resulting state transition comply with Phase 2 invariants?

For each lifecycle phase from creation to terminal state:

| Phase | Driving role | Entry contract | Exit contract | Exception path | Phase 1 permission compliant? | Phase 2 invariant compliant? | Gap in spec? | Blast radius (census component) |
|-------|-------------|----------------|---------------|----------------|-------------------------------|------------------------------|--------------|--------------------------------|

EXIT CRITERIA: All lifecycle phases covered. All entry and exit contracts evaluated.
Write "flow-lifecycle: clean -- all phase contracts verified." if no gaps.

---

## PHASE 5 -- flow-trigger (runtime behavior: race conditions on access surface)

Run flow-trigger last. For each automation trigger, identify: which role's action activates it?
Does the trigger write to a shared state surface? Can two triggers write to the same shared
state surface without coordination -- creating a race?

A trigger race on a shared state surface from Phase 0 is wide blast radius.
A trigger that can be activated by a role whose access was flagged in Phase 1 is CONFIRMED.

For each automation trigger:

| Trigger | Activating event | Activating role | Side effects | Fire order | Writes to shared state? | Shared state surface (Phase 0) | Race condition? | Phase 1 escalation involved? | Blast radius (census component) | Spec gap? |
|---------|-----------------|-----------------|--------------|------------|-------------------------|-------------------------------|-----------------|------------------------------|---------------------------------|-----------|

EXIT CRITERIA: All triggers and all activating events in scope have been evaluated.
Write "flow-trigger: clean -- no race conditions or conflicts detected." if clean.

---

## CALIBRATION BLOCK

All five sub-skills have completed. Do not rank findings yet.
Re-ground blast radius in evidence and promote confirmed cross-phase findings.

**Access surface inventory:**
Revisit the Phase 1 permission findings. List every role that has write access to a shared
state surface. These are the blast radius ceiling: any finding involving these roles is at
minimum medium blast radius; any finding involving the shared state surface directly is wide.

**CONFIRMED classification:**
A finding is CONFIRMED if it appears in two or more phases (same root cause from different
simulation angles). List each CONFIRMED finding with its phase evidence.
Mark it SYSTEMIC if it appears in three or more phases.

**Shared state re-assessment:**
For each finding that names a component listed as a shared state surface in the census:
if blast radius was assessed as medium or narrow, upgrade it to wide and explain why.

**Clean zones:**
Census components that appear in zero findings across all five phases.
These are cleared for implementation -- absence of findings is positive evidence.

**Calibration table:**

| Finding | Phases | Census component | Shared state? | CONFIRMED? | Blast radius (calibrated) | SYSTEMIC? |
|---------|--------|-----------------|---------------|------------|--------------------------|-----------|

---

## CONSOLIDATE

Write ONE report. Do not concatenate five phase outputs.

**Spec gaps:**
All spec gaps from calibration. Write "none detected" if clean.

**Contract violations:**
All mismatches from trace-contract (Phase 3). Write "none detected" if clean.

**Privilege escalation paths:**
All escalation findings from trace-permissions (Phase 1). Write "none detected" if clean.
Note: this section exists because permissions-anchor sequence may surface escalation paths
that contract-first campaigns do not detect.

**Ranked findings (calibrated blast radius order, wide first):**
Within equivalent blast radius: CONFIRMED > unconfirmed. SYSTEMIC > isolated.
For each finding:

- **Source:** [phase]
- **What breaks:** [one sentence]
- **Blast radius:** wide / medium / narrow -- [census component]; [is / is not] a shared state surface
- **Severity at epicenter:** high / med / low
- **CONFIRMED:** yes / no -- if yes, name the phases that corroborated it
- **SYSTEMIC:** yes / no
- **What must change:** [one concrete fix direction]

Do not merge blast radius and severity. They are separate fields. Always.

**Cross-skill findings:** All SYSTEMIC findings with full phase corroboration.

**Clean zones:** Census components with zero findings.

**VERDICT:** go / conditional-go / no-go. One sentence naming the finding with the widest
blast radius (by census component name) and noting whether it was CONFIRMED by a permission
surface anchor, or stating that the access surface audit confirmed no escalation paths and
calibration found no blocking findings.

Output file: `simulations/{{topic}}/campaign-behavior-{{date}}.md`
```

---

## V-02 -- Phrasing register: descriptive/interrogative throughout
**Axis:** Phrasing register -- all instructions are replaced with descriptive interrogatives; the prompt describes what a complete, well-executed output looks like rather than commanding actions; no imperative verbs ("run", "write", "record", "list") in phase headers
**Hypothesis:** Descriptive register activates self-evaluation: the model compares its output against a described standard rather than executing a command. If the rubric criteria are output-pattern-dependent (not instruction-dependent), descriptive framing should pass the same criteria. If imperative framing is load-bearing for structural compliance, the descriptive register will reveal which criteria are instruction-sensitive versus output-sensitive.

```
Simulating the technical behavior of: {{topic}}

---

## What this report is

A campaign-behavior simulation produces five independent sub-skill outputs -- trace-contract,
trace-state, trace-permissions, flow-lifecycle, flow-trigger -- consolidated into one findings
report ranked by blast radius. It surfaces spec gaps and contract violations before
implementation so that the blast radius of each finding is known before code is written.

Blast radius measures how broadly a failure propagates: wide if shared state is corrupted,
multiple roles are blocked, or downstream callers are affected; medium if two or more
components are involved without a shared state surface; narrow if one component absorbs
the failure alone. Severity measures damage at the epicenter: high, medium, or low.
These are independent dimensions. A finding always carries both. They are never merged.

---

## What a topology census looks like

Before any sub-skill output is produced, there is a census of the system vocabulary.
A complete census names every component in scope: services, modules, APIs, schemas,
queues. It separately identifies shared state surfaces -- components that multiple other
components read or write -- because these are the blast radius amplifiers. It names every
downstream caller: components whose behavior depends on the system being simulated. And
it carries a role-resource inventory: every role and the resources accessible to it.

Every blast radius claim in the sub-skill outputs references a specific census component.
A blast radius claim that cannot name a census component has no evidence basis.

**Components in scope:** [every named service, module, API, schema, queue]
**Shared state surfaces:** [databases, caches, event buses, config objects -- blast radius amplifiers]
**Downstream callers:** [components that depend on the system under simulation]
**Role-resource inventory:** [every role and the resources it may access]

---

## What a complete trace-contract output looks like

A trace-contract output names each producer/consumer pairing in the system and compares
what the producer promises to deliver against what the consumer actually receives when the
system runs. Where promised and received diverge, there is a contract mismatch. A complete
trace-contract output covers every producer/consumer pair in scope -- it does not stop when
it finds one mismatch. If no mismatches exist, it states: "trace-contract: clean -- all
contracts verified, no violations detected."

Each mismatch carries: the producer name (from the census), the consumer name (from the census),
the contract term that was violated, the expected behavior, the actual behavior, a severity
assessment at the epicenter, a blast radius assessment naming a specific census component and
explaining the propagation path, and a spec gap assessment stating whether the spec addresses
this condition.

For each pairing in scope:

| Producer | Consumer | Contract term | Expected | Actual | Mismatch? | Severity | Blast radius (census component) | Spec gap? |
|----------|----------|---------------|----------|--------|-----------|----------|---------------------------------|-----------|

A complete trace-contract output names every pairing. Pairings are not deferred.

---

## What a complete trace-state output looks like

A trace-state output hand-compiles every state transition in the system with its
preconditions, triggering event, postcondition, and invariant. Where an invariant is
violated or a transition is missing, there is a state finding. A complete trace-state
output covers every state and every transition in scope. If no violations exist, it states:
"trace-state: clean -- all transitions verified, no invariant violations detected."

Each violation carries: the from-state and to-state (named from the census), the triggering
event, the preconditions that must hold, the postcondition that should result, the invariant
that was violated or the transition that is missing, a blast radius assessment naming a
specific census component, and a spec gap assessment.

For each transition in scope:

| State | Preconditions | Trigger | Postcondition | Invariant | Violated? | Blast radius (census component) | Spec gap? |
|-------|---------------|---------|---------------|-----------|-----------|--------------------------------|-----------|

Invariant violations on shared state surfaces carry wide blast radius. Every other violation
carries the blast radius of the narrowest census component that contains it.

---

## What a complete trace-permissions output looks like

A trace-permissions output walks every role-resource-action combination through the
permission model and identifies where a role can perform an action that the spec does not
intend. Where a role can escalate privileges -- accessing a resource or performing an action
beyond what the spec assigns -- there is a permission finding. A complete trace-permissions
output covers every role-resource pair in the census. If no violations exist, it states:
"trace-permissions: clean -- all role-resource pairs verified, no escalation paths detected."

Each escalation carries: the role name, the resource name (from the census), the action,
the expected access per spec, the actual access the permission model delivers, a blast radius
assessment (privilege escalation is wide by default; name the census component), and a spec
gap assessment.

For each role-resource pair in the census:

| Role | Resource | Action | Expected access | Actual access | Privilege escalation? | Blast radius (census component) | Spec gap? |
|------|----------|--------|-----------------|---------------|-----------------------|--------------------------------|-----------|

---

## What a complete flow-lifecycle output looks like

A flow-lifecycle output traces the business lifecycle from creation to terminal state,
phase by phase. For each phase boundary, it states what must be true to enter the phase
and what must be true to exit it. Where the spec is silent about what happens when an
entry or exit condition is not met, there is a lifecycle gap. A complete flow-lifecycle
output covers every phase from creation to every terminal state. If no gaps exist, it states:
"flow-lifecycle: clean -- all phase contracts verified, no lifecycle gaps detected."

Each gap carries: the phase name, the entry contract (what must hold to enter), the exit
contract (what must hold to exit), what the spec says happens when the entry or exit contract
fails (or a note that the spec is silent), a blast radius assessment naming a specific census
component, and a spec gap assessment.

For each lifecycle phase from creation to terminal state:

| Phase | Entry contract | Exit contract | Exception path | Gap in spec? | Blast radius (census component) |
|-------|----------------|---------------|----------------|--------------|--------------------------------|

Lifecycle gaps on shared state surfaces carry wide blast radius.

---

## What a complete flow-trigger output looks like

A flow-trigger output simulates every automation trigger in the system: what fires it,
what it produces when it fires, its position in the execution sequence, and whether it
competes with other triggers for access to a shared state surface. Where two triggers can
reach the same shared state surface without coordination, there is a race condition.
A complete flow-trigger output covers every trigger and every activating event in scope.
If no conflicts exist, it states: "flow-trigger: clean -- all triggers verified, no race
conditions or conflicts detected."

Each race carries: the trigger name, the activating event, the side effects of firing,
the fire order relative to other triggers, the shared state surface involved (from the
census), a blast radius assessment (race conditions on shared state surfaces are wide by
default), and a spec gap assessment.

For each trigger in scope:

| Trigger | Activating event | Side effects | Fire order | Race condition? | Shared state surface (census) | Blast radius (census component) | Spec gap? |
|---------|-----------------|--------------|------------|-----------------|-------------------------------|---------------------------------|-----------|

---

## What a complete calibration block looks like

After all five sub-skill outputs are produced, calibration re-grounds blast radius in
evidence before ranking. A complete calibration block does four things:

First, it inventories the evidence: for each finding from all five phases, it names the
census component the finding involves. A finding that cannot name a census component is
not evidenced -- it is revised before proceeding.

Second, it re-assesses shared state: for each finding that names a component on the shared
state surfaces list, it confirms or upgrades blast radius to wide. Shared state propagates
to all dependent components; this is the highest-cost category.

Third, it identifies corroboration: where two or more phases surface the same root cause
from independent simulation angles, the finding is SYSTEMIC. A SYSTEMIC finding was going
to ship regardless of which sub-skill ran first.

Fourth, it identifies clean zones: census components that appear in zero findings across
all five phases. These components are cleared for implementation.

**Evidence inventory:** [finding code] names [census component].

**Shared state re-assessment:** [upgrades and confirmations]

**Cross-phase corroboration:** [SYSTEMIC findings with phase evidence]

**Clean zones:** [census components with zero findings]

Calibration table:

| Finding | Phases | Census component | Shared state? | Blast radius (calibrated) | SYSTEMIC? |
|---------|--------|-----------------|---------------|--------------------------|-----------|

---

## What a complete consolidated report looks like

The consolidated report is one document -- not five phase outputs concatenated. It contains:

**Spec gaps:** Each spec gap from calibration named by finding code, phase, and what the
spec does not address. Write "none detected" if clean.

**Contract violations:** Each contract mismatch from trace-contract. Write "none detected" if clean.

**Ranked findings (calibrated blast radius order, wide first):**
Per finding: source phase, what breaks in one sentence, blast radius with census component
name and whether it is a shared state surface, severity at epicenter, what must change as
one concrete fix direction, SYSTEMIC status.

Do not merge blast radius and severity. They are independent dimensions. Both appear in
every finding.

**Cross-skill findings:** SYSTEMIC findings with full phase corroboration lists.

**Clean zones:** Census components with zero findings.

**VERDICT:** go / conditional-go / no-go. One sentence naming the finding with the widest
blast radius (by census component name) and its calibrated rank, or stating that calibration
confirmed no blocking findings across all five sub-skills.

Output file: `simulations/{{topic}}/campaign-behavior-{{date}}.md`
```

---

## V-03 -- Asymmetric lifecycle emphasis (DEPTH labels per phase)
**Axis:** Lifecycle emphasis -- each phase carries an explicit DEPTH label (HIGH / MEDIUM / AS-NEEDED) based on expected blast-radius yield; phases with DEPTH: HIGH receive a minimum finding count requirement and an extended instruction set; phases with DEPTH: AS-NEEDED run with a minimal instruction footprint
**Hypothesis:** Phases are not equal contributors to blast radius findings historically. trace-contract and flow-trigger tend to yield the widest-blast-radius findings; trace-permissions yields escalation findings with wide blast radius by definition; trace-state and flow-lifecycle tend to yield medium/narrow findings or to confirm root causes from the other three. Explicit depth asymmetry may improve finding quality in high-yield phases while satisfying C-01 (all five sub-skills still execute). If depth weighting improves consolidation signal-to-noise, it may surface a new rubric criterion around per-phase finding quality rather than just phase completion.

```
Simulate the technical behavior of: {{topic}}

---

## BLAST RADIUS DEFINITION

Blast radius = how broadly a failure propagates through the system.
Wide: corrupts shared state, breaks downstream callers, or blocks multiple user roles simultaneously.
Medium: two or more components affected; no shared state surface reached.
Narrow: failure contained within one component boundary.

Severity = damage depth at the epicenter (high / med / low). Independent of blast radius.
Both fields appear in every finding. Never merge them.

---

## PHASE 0 -- Topology census

Before any sub-skill runs, record the system vocabulary explicitly.

**Components in scope:** [every named service, module, API, schema, queue from the spec or codebase]
**Shared state surfaces:** [databases, caches, event buses, config objects used by multiple components]
**Downstream callers:** [every component that depends on the system under simulation]
**Role-resource inventory:** [every role and the resources it may access]

Every blast radius assessment below must name a specific item from this census.
A finding that cannot name a census item is not a finding.

---

## PHASE 1 -- trace-contract [DEPTH: HIGH]

Contract mismatches are the highest-yield finding category. Producer/consumer divergence
on shared state surfaces produces wide blast radius by default. Do not stop at the first
mismatch -- every pairing must be evaluated.

Minimum: evaluate every producer/consumer pair in scope. If fewer than three pairings
exist, document all of them. If no pairings exist, state why.

For each pairing, record all of the following:

| Producer | Consumer | Contract term | Expected | Actual | Mismatch? | Severity | Blast radius (census component) | Propagation path (one sentence) | Spec gap? |
|----------|----------|---------------|----------|--------|-----------|----------|---------------------------------|---------------------------------|-----------|

For each mismatch, additionally record:
- **Root cause hypothesis:** [one sentence -- why does the producer deliver something other than what the consumer expects?]
- **Fix direction:** [one concrete action that would close the mismatch]
- **Downstream caller impact:** [list every census downstream caller affected if this contract is violated at runtime]

EXIT CRITERIA: All producer/consumer pairs in scope evaluated. No pairings deferred.
Write the following when complete:
"trace-contract complete: [N] pairs evaluated, [N] mismatches found, [N] involving shared
state surfaces."

---

## PHASE 2 -- trace-state [DEPTH: AS-NEEDED]

Hand-compile every state transition. Focus on invariant violations -- especially on shared
state surfaces. If state violations are found, note whether they connect to a contract
mismatch from Phase 1 (a connected finding is CONFIRMED).

| State | Preconditions | Trigger | Postcondition | Invariant | Violated? | Connected to Phase 1? | Blast radius (census component) | Spec gap? |
|-------|---------------|---------|---------------|-----------|-----------|----------------------|--------------------------------|-----------|

EXIT CRITERIA: All states and all transitions in scope evaluated.
Write "trace-state: clean" if no violations, or a one-line summary of violations found.

---

## PHASE 3 -- trace-permissions [DEPTH: MEDIUM]

Walk every role-resource-action combination through the permission model.
Escalation paths are wide blast radius by default.
Note which escalation paths involve shared state surfaces -- these are highest priority.

| Role | Resource | Action | Expected access | Actual access | Privilege escalation? | Shared state surface involved? | Blast radius (census component) | Spec gap? |
|------|----------|--------|-----------------|---------------|-----------------------|-------------------------------|--------------------------------|-----------|

For each escalation path, additionally record:
- **Escalation mechanism:** [how does the role reach the forbidden resource?]
- **Blast radius justification:** [why is this wide -- which downstream callers or roles are affected?]

EXIT CRITERIA: All role-resource pairs in the census evaluated.
Write "trace-permissions complete: [N] pairs evaluated, [N] escalation paths found."

---

## PHASE 4 -- flow-lifecycle [DEPTH: MEDIUM]

Trace every lifecycle phase from creation to terminal state.
Focus on missing exception paths -- these are the most expensive spec gap category.
Note whether lifecycle gaps connect to Phase 1 contract mismatches or Phase 2 state violations.

| Phase | Entry contract | Exit contract | Exception path | Spec silent on exception? | Connected to Phase 1 or 2? | Gap in spec? | Blast radius (census component) |
|-------|----------------|---------------|----------------|--------------------------|---------------------------|--------------|--------------------------------|

EXIT CRITERIA: All lifecycle phases covered. All entry and exit contracts evaluated.
Write "flow-lifecycle: clean" if no gaps, or a one-line summary of gaps found.

---

## PHASE 5 -- flow-trigger [DEPTH: HIGH]

Trigger races on shared state surfaces are the highest-risk category in this campaign:
they are non-deterministic, difficult to reproduce post-ship, and produce wide blast radius
by default. Do not stop at the first race -- every trigger and every activating event must
be evaluated.

Minimum: evaluate every trigger in scope. If fewer than three triggers exist, document all
of them. If no triggers exist, state why.

For each trigger, record all of the following:

| Trigger | Activating event | Side effects | Fire order | Concurrent with? | Shared state surface? | Race condition? | Phase 1 contract affected? | Blast radius (census component) | Spec gap? |
|---------|-----------------|--------------|------------|------------------|-----------------------|-----------------|---------------------------|--------------------------------|-----------|

For each race condition, additionally record:
- **Race window:** [what must happen for the race to manifest -- which two triggers must fire within what time window?]
- **Worst-case outcome:** [one sentence -- what does the system look like if the race resolves in the worst order?]
- **Fix direction:** [one concrete action that would eliminate the race]

EXIT CRITERIA: All triggers and all activating events in scope evaluated. No triggers deferred.
Write the following when complete:
"flow-trigger complete: [N] triggers evaluated, [N] race conditions found, [N] involving
shared state surfaces."

---

## CALIBRATION BLOCK

All five sub-skills have completed. Do not rank findings yet.
Re-ground blast radius in evidence before ranking.

**Depth yield review:**
For DEPTH: HIGH phases (trace-contract, flow-trigger): confirm that each produced at least
one finding or an explicit "clean" statement with evidence. A DEPTH: HIGH phase with zero
findings and no explanation is an incomplete execution.

**Evidence inventory:**
For each finding from all five phases, name the census component it involves.
Findings that cannot name a census component are revised before proceeding.

**Shared state re-assessment:**
For each finding naming a shared state surface from the census: confirm or upgrade blast
radius to wide.

**Cross-phase corroboration:**
Identify findings that appear in two or more phases (same root cause, multiple angles).
Mark SYSTEMIC. A DEPTH: HIGH finding corroborated by a DEPTH: AS-NEEDED phase carries
stronger evidence than an isolated DEPTH: HIGH finding.

**Clean zones:** Census components with zero findings across all phases.

Calibration table:

| Finding | Source phase | Depth label | Census component | Shared state? | Blast radius (calibrated) | SYSTEMIC? |
|---------|-------------|-------------|-----------------|---------------|--------------------------|-----------|

---

## CONSOLIDATE

Write ONE report. Do not concatenate five phase outputs.

**Spec gaps:** All spec gaps from calibration. Write "none detected" if clean.

**Contract violations:** All mismatches from trace-contract (Phase 1). Write "none detected" if clean.

**Ranked findings (calibrated blast radius order, wide first):**
Within equivalent blast radius: SYSTEMIC > isolated. DEPTH: HIGH source > DEPTH: MEDIUM > DEPTH: AS-NEEDED.
Per finding:

- **Source:** [phase] [DEPTH label]
- **What breaks:** [one sentence]
- **Blast radius:** wide / medium / narrow -- [census component; shared state surface?]
- **Severity at epicenter:** high / med / low
- **SYSTEMIC:** yes / no -- if yes, name the phases that corroborated it
- **What must change:** [one concrete fix direction]

Do not merge blast radius and severity.

**Cross-skill findings:** All SYSTEMIC findings with full phase corroboration.

**Clean zones:** Census components with zero findings.

**VERDICT:** go / conditional-go / no-go. One sentence naming the finding with the widest
blast radius (by census component name), its source phase DEPTH label, and whether it is
SYSTEMIC -- or stating that all DEPTH: HIGH phases confirmed clean and calibration found
no blocking findings.

Output file: `simulations/{{topic}}/campaign-behavior-{{date}}.md`
```

---

## V-04 -- Phrasing register + scorecard output format (combination)
**Axis:** Combination -- descriptive/interrogative register (V-02) + numbered scorecard per finding instead of tables; the prompt describes what each finding looks like as a 6-field scorecard; no tables, no prose blocks, no imperative instructions
**Hypothesis:** Descriptive register + scorecard format may produce the highest per-finding completeness: the descriptive framing activates self-evaluation (does this finding look like what was described?), and the numbered scorecard enforces mandatory field presence in a format that cannot suppress fields via column truncation (unlike tables) or field omission (unlike prose). The combination tests whether format and register are complementary or competing levers for structural compliance.

```
Simulating the technical behavior of: {{topic}}

---

## What blast radius means in this campaign

A finding in this campaign carries two independent measurements.

The first is blast radius: how broadly a failure propagates if this finding is not addressed
before implementation. Wide blast radius means the failure corrupts shared state, breaks
downstream callers, or blocks multiple user roles at once. Medium means two or more
components are affected but no shared state surface is reached. Narrow means one component
absorbs the failure alone.

The second is severity: how deep the damage goes at the epicenter. High severity means the
failure makes the system unusable for its primary purpose. Medium means partial degradation.
Low means cosmetic or edge-case impact.

These two measurements are independent. A finding can have wide blast radius and low severity
(failure propagates broadly but is recoverable), or narrow blast radius and high severity
(one component is destroyed but the rest of the system continues). Every finding in this
report carries both measurements in separate labeled fields.

---

## What the topology census contains

Before any sub-skill output is produced, there is a census that names every component the
blast radius claims will reference. A census that does not name a component is incomplete;
a blast radius claim that references a component not in the census is unsupported.

A complete census has four sections:

Components in scope -- the named services, modules, APIs, schemas, and queues that are
part of the system under simulation. These are the entities that appear in finding fields.

**Components in scope:**

Shared state surfaces -- the databases, caches, event buses, and configuration objects
that multiple components read or write. Any finding that involves a shared state surface
has wide blast radius by definition, because corruption here reaches all dependent components.

**Shared state surfaces:**

Downstream callers -- the components whose behavior depends on the output of the system
under simulation. A wide blast radius finding names at least one downstream caller.

**Downstream callers:**

Role-resource inventory -- every role and the resources it is permitted to access, organized
as a list of (role, resource, permitted actions) triples.

**Role-resource inventory:**

---

## What a trace-contract finding looks like

A trace-contract output names every producer/consumer pairing in the system and verifies
whether the producer delivers what the consumer expects. A complete trace-contract output
evaluates every pairing -- not just the ones where a mismatch is suspected.

Each finding in the trace-contract output is a numbered scorecard:

```
FINDING TC-[N]:
1. Producer: [component name from census]
2. Consumer: [component name from census]
3. Contract term: [what the producer promises to deliver]
4. Mismatch: [yes -- describe the divergence in one sentence | no -- contract holds]
5. Blast radius: [wide | medium | narrow] -- [census component name]; [explain propagation in one sentence]
6. Severity at epicenter: [high | med | low]
7. Spec gap: [yes -- what the spec does not address | no]
```

If no mismatches exist across all pairings: write "trace-contract: clean -- all contracts
verified, no violations detected." This is a positive finding.

---

## What a trace-state finding looks like

A trace-state output hand-compiles every state transition with preconditions and invariants.
It identifies transitions that cannot complete (missing preconditions), invariants that
are violated under reachable conditions, and states that the spec names but does not
connect to any transition.

Each finding in the trace-state output is a numbered scorecard:

```
FINDING TS-[N]:
1. From state: [state name]
2. Trigger: [the event or action that initiates this transition]
3. To state: [state name]
4. Invariant: [what must hold throughout this state -- or "not specified"]
5. Violated: [yes -- describe the violation in one sentence | no -- invariant holds]
6. Blast radius: [wide | medium | narrow] -- [census component name; invariant violations on shared state are wide]
7. Spec gap: [yes -- what the spec does not address | no]
```

If no violations exist: write "trace-state: clean -- all transitions verified, no invariant
violations detected."

---

## What a trace-permissions finding looks like

A trace-permissions output walks every role-resource-action combination through the
permission model and identifies where a role can perform an action the spec does not intend.
Privilege escalation -- reaching a resource or action beyond what the spec assigns -- is
a wide blast radius finding by default.

Each finding in the trace-permissions output is a numbered scorecard:

```
FINDING TP-[N]:
1. Role: [role name from census]
2. Resource: [resource name from census]
3. Action: [read | write | delete | execute | escalate | other]
4. Expected access: [what the spec says]
5. Actual access: [what the permission model delivers]
6. Privilege escalation: [yes -- describe the escalation path in one sentence | no]
7. Blast radius: [wide by default if escalation; otherwise wide | medium | narrow] -- [census component]
8. Spec gap: [yes | no]
```

If no violations exist: write "trace-permissions: clean -- all role-resource pairs verified,
no escalation paths detected."

---

## What a flow-lifecycle finding looks like

A flow-lifecycle output traces the business lifecycle from creation to every terminal state,
phase by phase. For each phase boundary, it asks: what must be true to enter this phase,
and what must be true to exit it? Where the spec is silent about what happens when an
entry or exit condition is not met, there is a lifecycle gap.

Each finding in the flow-lifecycle output is a numbered scorecard:

```
FINDING FL-[N]:
1. Phase: [phase name]
2. Entry contract: [what must hold to enter this phase]
3. Exit contract: [what must hold to exit this phase and advance to the next]
4. Exception path: [what the spec says happens when entry or exit contract fails -- or "spec is silent"]
5. Spec gap: [yes -- what the spec does not address | no]
6. Blast radius: [wide | medium | narrow] -- [census component; lifecycle gaps on shared state are wide]
7. Severity at epicenter: [high | med | low]
```

If no gaps exist: write "flow-lifecycle: clean -- all phase contracts verified, no gaps detected."

---

## What a flow-trigger finding looks like

A flow-trigger output simulates every automation trigger: what fires it, what it produces,
and whether it can race with another trigger for access to a shared state surface. Race
conditions on shared state surfaces are wide blast radius by default -- they are
non-deterministic and the most expensive category of post-ship finding.

Each finding in the flow-trigger output is a numbered scorecard:

```
FINDING FT-[N]:
1. Trigger: [trigger name]
2. Activating event: [the event or condition that causes the trigger to fire]
3. Side effects: [every state change or message produced when this trigger fires]
4. Fire order: [position in execution sequence; concurrent or sequential with which other triggers]
5. Race condition: [yes -- name the shared state surface and describe the race | no]
6. Blast radius: [wide if race on shared state; otherwise wide | medium | narrow] -- [census component]
7. Spec gap: [yes | no]
```

If no conflicts exist: write "flow-trigger: clean -- all triggers verified, no race conditions
or conflicts detected."

---

## What a complete calibration block looks like

After all five sub-skill outputs are produced, calibration re-grounds blast radius in
evidence. A complete calibration block does not rank findings -- it prepares them for ranking.

The evidence inventory checks: does each finding scorecard name a census component in its
blast radius field? If any finding uses a generic description instead of a census component
name, it is revised before calibration proceeds.

The shared state re-assessment checks: does any finding name a shared state surface in its
blast radius field but carry medium or narrow blast radius? If so, it is upgraded to wide.
Shared state propagates to all dependent components -- this upgrade is not optional.

The cross-phase corroboration check identifies: are there findings across multiple phases
that share the same root cause? A contract mismatch that also produces a lifecycle gap and
a trigger race is the same failure surviving three independent simulation angles. These are
SYSTEMIC findings -- mark them before ranking.

The clean zone identification names census components that appear in zero findings. These
are cleared for implementation.

**Evidence inventory:** [for each finding, census component named in blast radius field]

**Shared state re-assessment:** [upgrades and confirmations]

**Cross-phase corroboration:**

```
SYSTEMIC FINDING S-[N]:
1. Root cause: [one sentence describing the shared root cause]
2. Phases: [list of phases that surfaced it independently]
3. Finding codes: [list of TC/TS/TP/FL/FT codes involved]
4. Blast radius (calibrated): [wide | medium | narrow] -- [census component]
5. Why it would have shipped: [one sentence -- which phase would have been skipped in a typical review?]
```

**Clean zones:** [census components with zero findings]

---

## What a complete consolidated report looks like

The consolidated report contains exactly these sections:

**Spec gaps:** Each spec gap from calibration: finding code, phase, and one sentence on
what the spec does not address. Write "none detected" if clean.

**Contract violations:** Each trace-contract mismatch: finding code, producer/consumer pair,
and one sentence on the promise broken. Write "none detected" if clean.

**Ranked findings (calibrated blast radius order, wide first):**
Within equivalent blast radius: SYSTEMIC > isolated.
Each finding uses this scorecard:

```
RANKED FINDING [rank]:
1. Finding code: [TC/TS/TP/FL/FT-N]
2. Source phase: [phase name]
3. What breaks: [one sentence]
4. Blast radius: [wide | medium | narrow] -- [census component]; [is | is not] a shared state surface
5. Severity at epicenter: [high | med | low]
6. SYSTEMIC: [yes -- phases: [list] | no]
7. What must change: [one concrete fix direction]
```

Do not merge blast radius and severity. They are separate scorecard fields.

**Cross-skill findings:** All SYSTEMIC findings with their S-N codes and full phase corroboration.

**Clean zones:** Census components with zero findings.

**VERDICT:** go / conditional-go / no-go. One sentence. Names the finding with the widest
blast radius by its census component name and its calibrated rank, or states that calibration
confirmed no blocking findings across all five sub-skills.

Output file: `simulations/{{topic}}/campaign-behavior-{{date}}.md`
```

---

## V-05 -- Permissions-anchor + asymmetric depth + inertia at VERDICT only (combination)
**Axis:** Combination -- permissions-anchor role sequence (V-01: permissions first to establish blast radius ceiling) + asymmetric depth weighting (V-03: DEPTH: HIGH for trace-permissions and flow-trigger, DEPTH: MEDIUM for trace-contract and flow-lifecycle, DEPTH: AS-NEEDED for trace-state) + CONFIRMED/RUNTIME ANOMALY classification (v4 rubric C-16) + inertia framing concentrated entirely in the VERDICT section rather than distributed per-phase
**Hypothesis:** Permissions-first establishes the access surface ceiling before any contract or lifecycle finding is made, which should improve blast radius pre-classification accuracy. Asymmetric depth concentrates token budget where blast radius yield is highest. Inertia at VERDICT only (vs. per-phase as in R4 V-03) tests whether assumption-displacement language is more effective as a capstone judgment than as a recurring phase frame. CONFIRMED/RUNTIME ANOMALY adds the evidence-tier distinction that R4 V-05 scored highest on. If compatible, this variation is the candidate for maximum rubric credit across C-01 through C-18.

```
Simulate the technical behavior of: {{topic}}

You will run five sub-skills in permissions-anchor sequence with asymmetric depth weighting.
The sequence establishes the access surface first, then maps what is reachable through it,
then verifies contracts, then observes runtime behavior within the verified envelope.
Each finding is classified as CONFIRMED (structural + runtime evidence) or RUNTIME ANOMALY
(emergent behavior the topology did not predict).

---

## BLAST RADIUS DEFINITION (active throughout)

Blast radius = how broadly a failure propagates.
- **Wide:** corrupts shared state, breaks downstream callers, or blocks multiple user roles simultaneously
- **Medium:** two or more components affected; no shared state surface reached
- **Narrow:** contained within one component boundary

**Severity** = damage depth at the epicenter (high / med / low). Independent of blast radius.
Wide blast radius + low severity is possible. Narrow blast radius + high severity is possible.
Report both as separate labeled fields in every finding. Never merge them.

---

## PHASE 0 -- Topology census

Before any sub-skill runs, enumerate from the spec or codebase:

**Components in scope:**
[every named service, module, API, schema, queue]

**Shared state surfaces:**
[shared databases, caches, event buses, configuration objects touched by multiple components;
these are the blast radius amplifiers -- any role that can write here sets the blast radius ceiling]

**Downstream callers:**
[every component that depends on the system being simulated]

**Role-resource inventory:**
[every role and the resources it may access; this is the permission topology baseline]

**Pre-declared contracts:**
[any contracts explicitly stated in the spec: "A delivers X to B". These form the contract
topology baseline. Findings in Phases 4-5 that match violations from Phases 1-3 are CONFIRMED.
Findings in Phases 4-5 with no matching topology violation are RUNTIME ANOMALY.]

Every blast radius claim below names a specific census entry. Generic claims are not valid.

---

## PHASE 1 -- trace-permissions [DEPTH: HIGH] (access surface anchor)

Run trace-permissions first. The goal: establish which roles can reach shared state surfaces.
This sets the blast radius ceiling for all subsequent findings.
A role with write access to a shared state surface produces wide blast radius by default
for any finding involving that role.

Minimum expectation: every role-resource pair in the census is evaluated.

| Role | Resource | Action | Expected access | Actual access | Privilege escalation? | Shared state surface? | Blast radius (census component) | Spec gap? |
|------|----------|--------|-----------------|---------------|-----------------------|-----------------------|--------------------------------|-----------|

For each escalation path, additionally record:
- **Escalation mechanism:** [how does the role reach the resource?]
- **Blast radius justification:** [which downstream callers or shared state surfaces are at risk?]

EXIT CRITERIA: All role-resource pairs in the census evaluated. No pairs deferred.
Write: "trace-permissions complete: [N] pairs evaluated, [N] escalation paths found,
[N] involving shared state surfaces."

These findings form the permission topology baseline.
Findings from Phases 4-5 that involve roles flagged here will be classified CONFIRMED.

---

## PHASE 2 -- trace-state [DEPTH: AS-NEEDED] (state reachability through access surface)

Hand-compile every state transition. Use the permission surface from Phase 1 as context:
for each transition, note which role triggers it and whether that role's Phase 1 access
is appropriate for the resulting state change.

| State | Preconditions | Trigger | Triggering role | Phase 1 escalation involved? | Postcondition | Invariant | Violated? | Blast radius (census component) | Spec gap? |
|-------|---------------|---------|-----------------|------------------------------|---------------|-----------|-----------|--------------------------------|-----------|

Transitions involving roles with Phase 1 escalations: mark CONFIRMED if Phase 1 match exists.

EXIT CRITERIA: All states and all transitions in scope evaluated.
Write "trace-state: clean" if no violations, or a brief summary of findings.

These findings form the state topology baseline.

---

## PHASE 3 -- trace-contract [DEPTH: MEDIUM] (contracts across permission/state envelope)

Verify every producer/consumer pairing. Focus on cross-role contracts: where the producer
and consumer operate under different permission sets from Phase 1.
A cross-role mismatch is more likely to produce wide blast radius than a same-role mismatch.

| Producer | Producer role | Consumer | Consumer role | Contract term | Expected | Actual | Mismatch? | Cross-role? | Severity | Blast radius (census component) | Spec gap? |
|----------|--------------|----------|--------------|---------------|----------|--------|-----------|-------------|----------|---------------------------------|-----------|

Mark CONFIRMED if the mismatch connects to a Phase 1 or Phase 2 finding.

EXIT CRITERIA: All producer/consumer pairs covered.
Write "trace-contract: clean" if no mismatches.

These findings form the contract topology baseline.

---

## PHASE 4 -- flow-lifecycle [DEPTH: MEDIUM] (runtime behavior -- lifecycle dimension)

Trace the business lifecycle from creation to terminal state. For each phase boundary,
ask: does the driving role have appropriate permissions (Phase 1)? Does the phase
transition respect state invariants (Phase 2)? Does it cross a contract boundary (Phase 3)?

| Phase | Driving role | Entry contract | Exit contract | Exception path | Spec gap? | Phase 1 compliant? | Phase 2/3 match? | CONFIRMED / RUNTIME ANOMALY | Blast radius (census component) |
|-------|-------------|----------------|---------------|----------------|-----------|-------------------|-----------------|-----------------------------|---------------------------------|

EXIT CRITERIA: All lifecycle phases covered. All entry and exit contracts evaluated.
All findings classified as CONFIRMED or RUNTIME ANOMALY.
Write "flow-lifecycle: clean" if no gaps.

---

## PHASE 5 -- flow-trigger [DEPTH: HIGH] (runtime behavior -- trigger dimension)

Trigger races on shared state surfaces are the highest-risk category.
Non-deterministic, expensive to reproduce post-ship, wide blast radius by default.
A trigger race involving a role with Phase 1 escalation: mark CONFIRMED.
A trigger race on a shared state surface not predicted by Phases 1-3: mark RUNTIME ANOMALY.

Minimum expectation: every trigger and every activating event is evaluated.

| Trigger | Activating event | Activating role | Side effects | Fire order | Concurrent with? | Shared state surface? | Race condition? | Phase 1 escalation involved? | CONFIRMED / RUNTIME ANOMALY | Blast radius (census component) | Spec gap? |
|---------|-----------------|-----------------|--------------|------------|------------------|-----------------------|-----------------|------------------------------|-----------------------------|---------------------------------|-----------|

For each race condition, additionally record:
- **Race window:** [what must happen for this race to manifest?]
- **Worst-case outcome:** [one sentence -- what does the system look like if the race resolves worst-case?]
- **Fix direction:** [one concrete action that eliminates the race]

EXIT CRITERIA: All triggers and all activating events evaluated. All findings classified.
Write: "flow-trigger complete: [N] triggers evaluated, [N] races found, [N] CONFIRMED,
[N] RUNTIME ANOMALY."

---

## CALIBRATION BLOCK

All five sub-skills are complete. Do not rank yet. Re-ground blast radius and verify
classifications before ordering.

**Step 1 -- Evidence inventory:**
List every finding from all phases with the census component it names.
Findings that cannot name a census component are revised before proceeding.

**Step 2 -- Blast radius ceiling check:**
For every finding involving a role flagged in Phase 1 as having write access to a shared
state surface: confirm blast radius is wide. If not, upgrade now.

**Step 3 -- CONFIRMED vs RUNTIME ANOMALY review:**
- CONFIRMED requires: structural evidence (matching Phase 1, 2, or 3 topology violation)
  AND runtime evidence (Phase 4 or 5 observation)
- RUNTIME ANOMALY: Phase 4 or 5 finding with no matching topology violation
Review each Phase 4-5 finding and confirm classification is accurate.

CONFIRMED findings rank higher than RUNTIME ANOMALY findings of equivalent blast radius.

**Step 4 -- Cross-phase corroboration (SYSTEMIC):**
A finding surfaced by three or more phases is SYSTEMIC. Mark it now.
SYSTEMIC findings rank above CONFIRMED within the same blast radius tier.

**Step 5 -- Clean zones:**
Census components with zero findings across all five phases.

Calibration table:

| Finding | Source phase | Depth label | Census component | Shared state? | CONFIRMED / RUNTIME ANOMALY | Blast radius (calibrated) | SYSTEMIC? |
|---------|-------------|-------------|-----------------|---------------|----------------------------|--------------------------|-----------|

---

## CONSOLIDATE

Write ONE report. Do not concatenate five phase outputs.

**Spec gaps:** [all spec gaps from calibration, or "none detected"]

**Contract violations:** [all mismatches from trace-contract, or "none detected"]

**Privilege escalation paths:** [all Phase 1 escalation findings, or "none detected"]

**Ranked findings (calibrated blast radius order, wide first):**
Within equivalent blast radius: SYSTEMIC > CONFIRMED > RUNTIME ANOMALY.
Per finding:

- **Source:** [phase] [DEPTH label]
- **What breaks:** [one sentence]
- **Blast radius:** wide / medium / narrow -- [census component]; [is / is not] a shared state surface
- **Severity at epicenter:** high / med / low
- **Classification:** CONFIRMED / RUNTIME ANOMALY
- **SYSTEMIC:** yes / no -- if yes, list the phases
- **What must change:** [one concrete fix direction]

Do not merge blast radius and severity. They are separate fields. Always.

**Cross-skill findings:** All SYSTEMIC findings with full phase corroboration lists.

**Clean zones:** Census components with zero findings.

**VERDICT:** go / conditional-go / no-go.

Before stating the verdict, state what teams assumed before this campaign ran:
- What the access surface was assumed to be (vs. what Phase 1 found)
- What trigger ordering was assumed to be predictable (vs. what Phase 5 found)
- What lifecycle contracts were assumed to be fully specified (vs. what Phase 4 found)

Then state the verdict: one sentence naming the highest-blast-radius finding (SYSTEMIC
CONFIRMED finding preferred over isolated findings), its census component, and its
classification. Or state that the access surface audit, state analysis, contract verification,
lifecycle trace, and trigger simulation all completed cleanly and no pre-implementation
assumptions were displaced.

Output file: `simulations/{{topic}}/campaign-behavior-{{date}}.md`
```
