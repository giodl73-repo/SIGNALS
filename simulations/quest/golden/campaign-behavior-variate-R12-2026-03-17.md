# Quest Variations — campaign-behavior (R12)
**Skill:** campaign-behavior
**Rubric:** v10 (C-01–C-34)
**Round:** 12
**Date:** 2026-03-17

---

## Axes explored in R12

**Context:** R11 V-05 scored 90/90 under v10. V-05 introduced the three-layer enforcement
architecture for EXECUTIVE SUMMARY (C-32 write-time rejection gate + C-33 Q7 post-write audit
+ C-34 Q2 pre-write preview). All three layers target the EXECUTIVE SUMMARY section
specifically — 26/26 aspirational satisfied, ceiling achieved.

R12 asks: do equivalent enforcement gaps exist in other output sections that could become
v11 criteria?

- **CONSOLIDATE finding blocks** — Q1–Q6 validate chain resolution and classification
  *before* CONSOLIDATE is written, but no post-write structural gate verifies that the
  written blocks preserve T-NN notation and 7-field completeness. Q7 covers EXECUTIVE
  SUMMARY; CONSOLIDATE has no equivalent post-write gate.
- **Phase 0 registry commitment** — Phase 0 produces the terminus registry table but
  includes no explicit lock declaration. A model could add terminus components during
  Phases 1–5 without triggering a structural failure, undermining the canonical authority
  of the Phase 0 registry.
- **Per-phase chain drift** — T-NN resolution is verified in Q1 (post-hoc chain tracing)
  but not at the point of each phase's EXIT CRITERIA. Free-form terminus names introduced
  in phase bodies could propagate to CONSOLIDATE and EXECUTIVE SUMMARY undetected until Q1.

Single-axis (three independent axes):
- **Per-phase T-NN exit gate** — Each phase's EXIT CRITERIA gains a chain-resolution check:
  all chains produced in this phase must resolve to T-NN entries or be flagged before the
  phase exits.
- **Registry-lock declaration** — Phase 0 closes with an explicit lock statement:
  registry is authoritative, no terminus may be added after Phase 0 exits.
- **Q8 CONSOLIDATE completeness gate** — A new calibration gate fires after CONSOLIDATE
  is written and before VERDICT: audits each finding block for 7-field completeness and
  T-NN chain resolution, analogous to Q7 for EXECUTIVE SUMMARY.

Combinations:
- **V-04:** Registry-lock + per-phase T-NN exit gates (upstream enforcement — prevent drift
  before it reaches CONSOLIDATE or EXECUTIVE SUMMARY)
- **V-05:** Full integration — V-04 + Q8 CONSOLIDATE gate (three-layer enforcement for
  CONSOLIDATE finding blocks, mirroring the three-layer architecture V-05 R11 introduced
  for EXECUTIVE SUMMARY)

---

## V-01 — Per-Phase T-NN Exit Gate
**Axis:** Each phase's EXIT CRITERIA gains a mandatory T-NN chain resolution statement.
After the standard completion line, the phase states whether all chains produced in the phase
resolve to T-NN entries from the Phase 0 registry, or flags unresolved chains by name before
the phase can be considered complete.
**Hypothesis:** V-05 R11 verifies T-NN chain resolution in Q1 (post-hoc) and Q7 (EXECUTIVE
SUMMARY post-write audit). But chains in phase body tables could use free-form terminal names
that reach CONSOLIDATE without triggering a structural failure until Q1 catches them.
Moving verification to each phase's EXIT CRITERIA intercepts drift at the source — a phase
cannot exit in a valid state if any chain is unresolved. This mirrors the per-phase completion
accountability already present in the exit status lines (N violations found) and extends it to
chain integrity. If V-05 R11 holds 90/90 under v10, this variation adds structural depth beyond
the existing ceiling and may expose a v11 criterion pattern.

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
Format: [origin] → [component-B] → [terminal: T-NN]
The terminal must resolve to a T-NN entry in the Phase 0 terminus registry.
Chains that cannot resolve to a T-NN entry must be flagged:
"unresolved chain — registry miss."

T-NN = terminus registry code. Assigned in Phase 0 to every unique propagation chain endpoint
(shared state surface, downstream caller boundary, or role-boundary that terminates blast).
Referenced in field 3 of every finding, in EXECUTIVE SUMMARY bullets, and in chain-to-terminus
tracing during Q1.

SYSTEMIC = a finding corroborated across three or more phases.
Required format: "SYSTEMIC: yes — phases: [phase-name-1], [phase-name-2], [phase-name-3]"
Binary "SYSTEMIC: yes" without a phase list is not valid and will be rejected.

CONFIRMED = a Phase 4 or Phase 5 finding that matches a topology violation from Phases 1–3.
Match is structural: same component, access pattern, contract term, or state surface.
Required format when classifying CONFIRMED:
  "CONFIRMED -- evidence: [source-phase]: [matching-finding-name]"
Omitting the evidence citation invalidates the CONFIRMED classification.

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

**Terminus registry:**

| T-NN | Terminus component | Type |
|------|--------------------|------|
| T-01 | [component name]   | [shared-state \| downstream-caller \| role-boundary] |
| ...  | ...                | ... |

Assign a T-NN code to every unique blast-surface endpoint in the system. Propagation chains
in findings below must terminate at a T-NN entry. Chains that cannot resolve = registry miss.

Every blast radius claim must name a specific census entry.
Every propagation chain must terminate at a T-NN registry code.

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
T-NN resolution check: All propagation chains produced in this phase resolve to T-NN registry entries.
State: "[N] chains produced, [N] resolved to T-NN, [N] registry miss."
If any registry miss: flag "unresolved chain — registry miss: [component name]" and carry forward to Q1.

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
T-NN resolution check: All propagation chains produced in this phase resolve to T-NN registry entries.
State: "[N] chains produced, [N] resolved to T-NN, [N] registry miss."
If any registry miss: flag "unresolved chain — registry miss: [component name]" and carry forward to Q1.

---

## PHASE 3 — trace-contract

| Producer | Consumer | Contract term | Expected | Actual | Mismatch? | Phase 1/2 topology match? |
|----------|----------|---------------|----------|--------|-----------|--------------------------|

Phase 1/2 topology match = yes if contract involves a Phase 1 state violation surface or Phase 2
escalation role. If match = yes: classify CONFIRMED -- evidence: [phase-1|phase-2]: [matching-finding-name].
Name the matching finding from Phase 1 or Phase 2.

If clean: "trace-contract: clean — all contracts verified."

EXIT CRITERIA: All producer/consumer pairs evaluated.
State: "trace-contract complete: [N] pairs evaluated, [N] mismatches found, [N] CONFIRMED."
T-NN resolution check: All propagation chains produced in this phase resolve to T-NN registry entries.
State: "[N] chains produced, [N] resolved to T-NN, [N] registry miss."
If any registry miss: flag "unresolved chain — registry miss: [component name]" and carry forward to Q1.

---

## PHASE 4 — flow-lifecycle

| Phase | Entry contract | Exit contract | Exception path | Exception handled? | Phase tag | CONFIRMED / RUNTIME ANOMALY |
|-------|----------------|---------------|----------------|--------------------|-----------|-----------------------------|

Phase tag = lifecycle phase of violation (INIT, ACTIVE, SUSPENDED, TERMINAL, etc.).
CONFIRMED = matches a Phase 1–3 violation. Use format:
  CONFIRMED -- evidence: [source-phase]: [matching-finding-name]
RUNTIME ANOMALY = no matching topology violation.

If clean: "flow-lifecycle: clean — all lifecycle transitions verified."

EXIT CRITERIA: All lifecycle phases evaluated.
State: "flow-lifecycle complete: [N] phases, [N] failures, [N] CONFIRMED, [N] RUNTIME ANOMALY."
T-NN resolution check: All propagation chains produced in this phase resolve to T-NN registry entries.
State: "[N] chains produced, [N] resolved to T-NN, [N] registry miss."
If any registry miss: flag "unresolved chain — registry miss: [component name]" and carry forward to Q1.

---

## PHASE 5 — flow-trigger

| Trigger | Expected fire order | Actual fire order | Race condition? | Phase 2 escalation role? | Phase tag | CONFIRMED / RUNTIME ANOMALY |
|---------|---------------------|-------------------|-----------------|--------------------------|-----------|------------------------------|

Phase 2 escalation role = yes if trigger involves a Phase 2 escalation role: blast radius = wide.
CONFIRMED = matches a Phase 1–3 violation. Use format:
  CONFIRMED -- evidence: [source-phase]: [matching-finding-name]

If clean: "flow-trigger: clean — all triggers verified."

EXIT CRITERIA: All triggers and activating events evaluated.
State: "flow-trigger complete: [N] triggers, [N] failures, [N] CONFIRMED, [N] RUNTIME ANOMALY."
T-NN resolution check: All propagation chains produced in this phase resolve to T-NN registry entries.
State: "[N] chains produced, [N] resolved to T-NN, [N] registry miss."
If any registry miss: flag "unresolved chain — registry miss: [component name]" and carry forward to Q1.

---

## CALIBRATION BLOCK

Q1: Does any finding's blast radius change when the propagation chain is traced to its T-NN terminus?
For each finding: trace the full chain ([origin] → ... → [terminal: T-NN]). Does the chain reach
a Phase 0 shared-state T-NN entry? If yes, upgrade to wide. List every revision and the full chain.
Flag any finding whose chain cannot resolve to a T-NN entry: "unresolved chain — registry miss."

Q2: Do any Phase 4–5 findings match topology violations from Phases 1–3?
For each Phase 4–5 finding classified as CONFIRMED: verify the inline citation is present using
format "CONFIRMED -- evidence: [source-phase]: [matching-finding-name]."
Any CONFIRMED classification missing this citation must be revised before consolidation.
Also verify: for any finding that will appear in the EXECUTIVE SUMMARY as CONFIRMED, confirm
that the same inline citation format will be used in the summary bullet (not a plain [CONFIRMED]
token). Note any summary slots that would use plain tokens — revise those bullets after Q7.
List all reclassifications and citations verified or added.

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

## EXECUTIVE SUMMARY

Write exactly 3 bullets. These are your top-3 findings by blast-radius tier, identified by position
in this section. The first bullet is the highest-blast-radius finding; the third is the third.
If fewer than 3 findings exist, write the available count and note the shortfall.

Use this format for each bullet exactly:
- F-[N]: [finding name] | blast-radius: [wide|medium|narrow] | chain: [origin] -> [component] -> [terminal: T-NN] | [CONFIRMED -- evidence: [phase]: [finding] | RUNTIME ANOMALY]

VALIDITY RULES for this section:
1. Chain terminus must use a T-NN code from the Phase 0 registry (e.g., T-04), not a
   free-form component name. A bullet with a free-form terminus is INVALID.
   If a chain cannot resolve to a T-NN code, write "unresolved chain — registry miss: [name]"
   and exclude until resolved via Q1.
2. Confirmation slot must carry the inline evidence citation format:
   CONFIRMED -- evidence: [source-phase]: [matching-finding-name]
   Plain [CONFIRMED] token is NOT valid in EXECUTIVE SUMMARY bullets.

Do not summarize. Do not add prose. Three structured bullets, then stop.

---

## Q7 — EXECUTIVE SUMMARY structural audit

Before writing CONSOLIDATE, audit the EXECUTIVE SUMMARY bullets you just wrote.

For each bullet:
- C-30 check: Does the chain field terminate at a T-NN code (e.g., `-> T-04`), not a free-form
  component name? If free-form name found: identify the matching T-NN entry from the Phase 0
  registry and rewrite the bullet with the T-NN code. If no T-NN entry resolves: flag
  "unresolved chain — registry miss" and exclude from ranking.
- C-31 check: Does the confirmation slot use `CONFIRMED -- evidence: [source-phase]: [finding-name]`
  format? If plain [CONFIRMED] found without inline citation: rewrite using the citation verified
  in Q2. If no Q2 citation exists for this finding: reclassify as RUNTIME ANOMALY.

State the result of each check:
- "Bullet F-[N]: C-30 PASS (terminal: T-NN), C-31 PASS (inline citation present)"
- OR list the revision made and the corrected bullet text.

If all three bullets pass both checks: "EXECUTIVE SUMMARY audit complete — C-30 and C-31 satisfied
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
3. Blast radius: [wide | medium | narrow] — propagation chain: [origin] → [component] → [terminal: T-NN]
4. Severity at epicenter: [high | med | low]
5. SYSTEMIC: [yes — phases: [comma-separated phase list] | no]
6. Classification: [CONFIRMED -- evidence: [source-phase]: [matching-finding-name] | RUNTIME ANOMALY | isolated]
7. What must change: [one concrete fix direction in spec, contract, or implementation]
---

**Spec gaps:** [list each gap with missing-clause citation, or "none detected"]

**Contract violations:** [list each with producer and consumer named, or "none detected"]

**Privilege escalation paths:** [list each, or "none detected"]

**Clean zones:** [Phase 0 census components with no findings across all five phases]

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

## V-02 — Registry-Lock Declaration
**Axis:** Phase 0 closes with an explicit registry-lock statement before any analysis phase begins.
The lock declares the terminus registry authoritative: no T-NN entry may be added, removed, or
renamed after Phase 0 exits. Phases 1–5 must resolve all chains to the locked registry or flag
"registry miss."
**Hypothesis:** V-05 R11 treats Phase 0 as the authority for terminus codes but does not explicitly
close the registry. A model executing the template could introduce new terminus components in phase
bodies (e.g., "new service X discovered in Phase 3") without triggering a structural failure.
An explicit lock statement makes Phase 0 commitment irreversible: post-Phase-0 terminus additions
fail validation. This is the production-time gate for registry integrity — analogous to C-32's
write-time gate for EXECUTIVE SUMMARY. If the registry can grow after Phase 0, T-NN codes assigned
during Phase 0 may not represent the full blast surface landscape, undermining chain tracing.

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
Format: [origin] → [component-B] → [terminal: T-NN]
The terminal must resolve to a T-NN entry in the Phase 0 terminus registry.
Chains that cannot resolve to a T-NN entry must be flagged:
"unresolved chain — registry miss."

T-NN = terminus registry code. Assigned in Phase 0 to every unique propagation chain endpoint
(shared state surface, downstream caller boundary, or role-boundary that terminates blast).
The Phase 0 registry is the single source of truth. No T-NN entry may be added, removed, or
renamed after Phase 0 is locked. Referenced in field 3 of every finding, in EXECUTIVE SUMMARY
bullets, and in chain-to-terminus tracing during Q1.

SYSTEMIC = a finding corroborated across three or more phases.
Required format: "SYSTEMIC: yes — phases: [phase-name-1], [phase-name-2], [phase-name-3]"
Binary "SYSTEMIC: yes" without a phase list is not valid and will be rejected.

CONFIRMED = a Phase 4 or Phase 5 finding that matches a topology violation from Phases 1–3.
Match is structural: same component, access pattern, contract term, or state surface.
Required format when classifying CONFIRMED:
  "CONFIRMED -- evidence: [source-phase]: [matching-finding-name]"
Omitting the evidence citation invalidates the CONFIRMED classification.

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

**Terminus registry:**

| T-NN | Terminus component | Type |
|------|--------------------|------|
| T-01 | [component name]   | [shared-state \| downstream-caller \| role-boundary] |
| ...  | ...                | ... |

Assign a T-NN code to every unique blast-surface endpoint in the system. Propagation chains
in findings below must terminate at a T-NN entry. Chains that cannot resolve = registry miss.

Every blast radius claim must name a specific census entry.
Every propagation chain must terminate at a T-NN registry code.

**Registry lock:** The terminus registry is now complete.
No terminus component may be added, removed, or renamed after this point.
All propagation chains in Phases 1–5 must resolve to a T-NN entry from this registry or be
flagged "unresolved chain — registry miss: [component name]."
Any component encountered in Phases 1–5 that is not in this registry must be recorded as a
spec gap (undeclared blast surface) — it may not be silently added to the registry.
State: "Registry locked: [N] terminus entries. Phase execution may begin."

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
escalation role. If match = yes: classify CONFIRMED -- evidence: [phase-1|phase-2]: [matching-finding-name].
Name the matching finding from Phase 1 or Phase 2.

If clean: "trace-contract: clean — all contracts verified."

EXIT CRITERIA: All producer/consumer pairs evaluated.
State: "trace-contract complete: [N] pairs evaluated, [N] mismatches found, [N] CONFIRMED."

---

## PHASE 4 — flow-lifecycle

| Phase | Entry contract | Exit contract | Exception path | Exception handled? | Phase tag | CONFIRMED / RUNTIME ANOMALY |
|-------|----------------|---------------|----------------|--------------------|-----------|-----------------------------|

Phase tag = lifecycle phase of violation (INIT, ACTIVE, SUSPENDED, TERMINAL, etc.).
CONFIRMED = matches a Phase 1–3 violation. Use format:
  CONFIRMED -- evidence: [source-phase]: [matching-finding-name]
RUNTIME ANOMALY = no matching topology violation.

If clean: "flow-lifecycle: clean — all lifecycle transitions verified."

EXIT CRITERIA: All lifecycle phases evaluated.
State: "flow-lifecycle complete: [N] phases, [N] failures, [N] CONFIRMED, [N] RUNTIME ANOMALY."

---

## PHASE 5 — flow-trigger

| Trigger | Expected fire order | Actual fire order | Race condition? | Phase 2 escalation role? | Phase tag | CONFIRMED / RUNTIME ANOMALY |
|---------|---------------------|-------------------|-----------------|--------------------------|-----------|------------------------------|

Phase 2 escalation role = yes if trigger involves a Phase 2 escalation role: blast radius = wide.
CONFIRMED = matches a Phase 1–3 violation. Use format:
  CONFIRMED -- evidence: [source-phase]: [matching-finding-name]

If clean: "flow-trigger: clean — all triggers verified."

EXIT CRITERIA: All triggers and activating events evaluated.
State: "flow-trigger complete: [N] triggers, [N] failures, [N] CONFIRMED, [N] RUNTIME ANOMALY."

---

## CALIBRATION BLOCK

Q1: Does any finding's blast radius change when the propagation chain is traced to its T-NN terminus?
For each finding: trace the full chain ([origin] → ... → [terminal: T-NN]). Does the chain reach
a Phase 0 shared-state T-NN entry? If yes, upgrade to wide. List every revision and the full chain.
Flag any finding whose chain cannot resolve to a T-NN entry: "unresolved chain — registry miss."

Q2: Do any Phase 4–5 findings match topology violations from Phases 1–3?
For each Phase 4–5 finding classified as CONFIRMED: verify the inline citation is present using
format "CONFIRMED -- evidence: [source-phase]: [matching-finding-name]."
Any CONFIRMED classification missing this citation must be revised before consolidation.
Also verify: for any finding that will appear in the EXECUTIVE SUMMARY as CONFIRMED, confirm
that the same inline citation format will be used in the summary bullet (not a plain [CONFIRMED]
token). Note any summary slots that would use plain tokens — revise those bullets after Q7.
List all reclassifications and citations verified or added.

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

## EXECUTIVE SUMMARY

Write exactly 3 bullets. These are your top-3 findings by blast-radius tier, identified by position
in this section. The first bullet is the highest-blast-radius finding; the third is the third.
If fewer than 3 findings exist, write the available count and note the shortfall.

Use this format for each bullet exactly:
- F-[N]: [finding name] | blast-radius: [wide|medium|narrow] | chain: [origin] -> [component] -> [terminal: T-NN] | [CONFIRMED -- evidence: [phase]: [finding] | RUNTIME ANOMALY]

VALIDITY RULES for this section:
1. Chain terminus must use a T-NN code from the Phase 0 registry (e.g., T-04), not a
   free-form component name. A bullet with a free-form terminus is INVALID.
   If a chain cannot resolve to a T-NN code, write "unresolved chain — registry miss: [name]"
   and exclude until resolved via Q1.
2. Confirmation slot must carry the inline evidence citation format:
   CONFIRMED -- evidence: [source-phase]: [matching-finding-name]
   Plain [CONFIRMED] token is NOT valid in EXECUTIVE SUMMARY bullets.

Do not summarize. Do not add prose. Three structured bullets, then stop.

---

## Q7 — EXECUTIVE SUMMARY structural audit

Before writing CONSOLIDATE, audit the EXECUTIVE SUMMARY bullets you just wrote.

For each bullet:
- C-30 check: Does the chain field terminate at a T-NN code (e.g., `-> T-04`), not a free-form
  component name? If free-form name found: identify the matching T-NN entry from the Phase 0
  registry and rewrite the bullet with the T-NN code. If no T-NN entry resolves: flag
  "unresolved chain — registry miss" and exclude from ranking.
- C-31 check: Does the confirmation slot use `CONFIRMED -- evidence: [source-phase]: [finding-name]`
  format? If plain [CONFIRMED] found without inline citation: rewrite using the citation verified
  in Q2. If no Q2 citation exists for this finding: reclassify as RUNTIME ANOMALY.

State the result of each check:
- "Bullet F-[N]: C-30 PASS (terminal: T-NN), C-31 PASS (inline citation present)"
- OR list the revision made and the corrected bullet text.

If all three bullets pass both checks: "EXECUTIVE SUMMARY audit complete — C-30 and C-31 satisfied
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
3. Blast radius: [wide | medium | narrow] — propagation chain: [origin] → [component] → [terminal: T-NN]
4. Severity at epicenter: [high | med | low]
5. SYSTEMIC: [yes — phases: [comma-separated phase list] | no]
6. Classification: [CONFIRMED -- evidence: [source-phase]: [matching-finding-name] | RUNTIME ANOMALY | isolated]
7. What must change: [one concrete fix direction in spec, contract, or implementation]
---

**Spec gaps:** [list each gap with missing-clause citation, or "none detected"]

**Contract violations:** [list each with producer and consumer named, or "none detected"]

**Privilege escalation paths:** [list each, or "none detected"]

**Clean zones:** [Phase 0 census components with no findings across all five phases]

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

## V-03 — Q8 CONSOLIDATE Completeness Gate
**Axis:** A new Q8 gate fires after CONSOLIDATE is written and before VERDICT. Q8 audits every
finding block for 7-field completeness and T-NN chain resolution — analogous to Q7 for EXECUTIVE
SUMMARY. If any field is missing or any chain uses a free-form terminus name, Q8 flags the
finding and states the required revision before VERDICT proceeds.
**Hypothesis:** EXECUTIVE SUMMARY gets Q7 (C-33) — a post-write structural audit before
CONSOLIDATE. But CONSOLIDATE finding blocks themselves have no equivalent post-write gate. Q1–Q6
validate inputs and calibration before CONSOLIDATE is written, but if a model writes CONSOLIDATE
with a free-form chain terminus or a missing field, no structural gate catches it before VERDICT.
Q8 closes this gap: it is to CONSOLIDATE what Q7 is to EXECUTIVE SUMMARY. If this pattern scores
well, it may inform a v11 criterion (C-35) requiring a dedicated post-CONSOLIDATE audit gate.
The three-layer enforcement architecture introduced in V-05 R11 for EXECUTIVE SUMMARY
(write-time gate + pre-write Q2 + post-write Q7) has no counterpart for CONSOLIDATE blocks;
Q8 is the post-write layer for CONSOLIDATE.

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
Format: [origin] → [component-B] → [terminal: T-NN]
The terminal must resolve to a T-NN entry in the Phase 0 terminus registry.
Chains that cannot resolve to a T-NN entry must be flagged:
"unresolved chain — registry miss."

T-NN = terminus registry code. Assigned in Phase 0 to every unique propagation chain endpoint
(shared state surface, downstream caller boundary, or role-boundary that terminates blast).
Referenced in field 3 of every finding, in EXECUTIVE SUMMARY bullets, and in chain-to-terminus
tracing during Q1.

SYSTEMIC = a finding corroborated across three or more phases.
Required format: "SYSTEMIC: yes — phases: [phase-name-1], [phase-name-2], [phase-name-3]"
Binary "SYSTEMIC: yes" without a phase list is not valid and will be rejected.

CONFIRMED = a Phase 4 or Phase 5 finding that matches a topology violation from Phases 1–3.
Match is structural: same component, access pattern, contract term, or state surface.
Required format when classifying CONFIRMED:
  "CONFIRMED -- evidence: [source-phase]: [matching-finding-name]"
Omitting the evidence citation invalidates the CONFIRMED classification.

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

**Terminus registry:**

| T-NN | Terminus component | Type |
|------|--------------------|------|
| T-01 | [component name]   | [shared-state \| downstream-caller \| role-boundary] |
| ...  | ...                | ... |

Assign a T-NN code to every unique blast-surface endpoint in the system. Propagation chains
in findings below must terminate at a T-NN entry. Chains that cannot resolve = registry miss.

Every blast radius claim must name a specific census entry.
Every propagation chain must terminate at a T-NN registry code.

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
escalation role. If match = yes: classify CONFIRMED -- evidence: [phase-1|phase-2]: [matching-finding-name].
Name the matching finding from Phase 1 or Phase 2.

If clean: "trace-contract: clean — all contracts verified."

EXIT CRITERIA: All producer/consumer pairs evaluated.
State: "trace-contract complete: [N] pairs evaluated, [N] mismatches found, [N] CONFIRMED."

---

## PHASE 4 — flow-lifecycle

| Phase | Entry contract | Exit contract | Exception path | Exception handled? | Phase tag | CONFIRMED / RUNTIME ANOMALY |
|-------|----------------|---------------|----------------|--------------------|-----------|-----------------------------|

Phase tag = lifecycle phase of violation (INIT, ACTIVE, SUSPENDED, TERMINAL, etc.).
CONFIRMED = matches a Phase 1–3 violation. Use format:
  CONFIRMED -- evidence: [source-phase]: [matching-finding-name]
RUNTIME ANOMALY = no matching topology violation.

If clean: "flow-lifecycle: clean — all lifecycle transitions verified."

EXIT CRITERIA: All lifecycle phases evaluated.
State: "flow-lifecycle complete: [N] phases, [N] failures, [N] CONFIRMED, [N] RUNTIME ANOMALY."

---

## PHASE 5 — flow-trigger

| Trigger | Expected fire order | Actual fire order | Race condition? | Phase 2 escalation role? | Phase tag | CONFIRMED / RUNTIME ANOMALY |
|---------|---------------------|-------------------|-----------------|--------------------------|-----------|------------------------------|

Phase 2 escalation role = yes if trigger involves a Phase 2 escalation role: blast radius = wide.
CONFIRMED = matches a Phase 1–3 violation. Use format:
  CONFIRMED -- evidence: [source-phase]: [matching-finding-name]

If clean: "flow-trigger: clean — all triggers verified."

EXIT CRITERIA: All triggers and activating events evaluated.
State: "flow-trigger complete: [N] triggers, [N] failures, [N] CONFIRMED, [N] RUNTIME ANOMALY."

---

## CALIBRATION BLOCK

Q1: Does any finding's blast radius change when the propagation chain is traced to its T-NN terminus?
For each finding: trace the full chain ([origin] → ... → [terminal: T-NN]). Does the chain reach
a Phase 0 shared-state T-NN entry? If yes, upgrade to wide. List every revision and the full chain.
Flag any finding whose chain cannot resolve to a T-NN entry: "unresolved chain — registry miss."

Q2: Do any Phase 4–5 findings match topology violations from Phases 1–3?
For each Phase 4–5 finding classified as CONFIRMED: verify the inline citation is present using
format "CONFIRMED -- evidence: [source-phase]: [matching-finding-name]."
Any CONFIRMED classification missing this citation must be revised before consolidation.
Also verify: for any finding that will appear in the EXECUTIVE SUMMARY as CONFIRMED, confirm
that the same inline citation format will be used in the summary bullet (not a plain [CONFIRMED]
token). Note any summary slots that would use plain tokens — revise those bullets after Q7.
List all reclassifications and citations verified or added.

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

## EXECUTIVE SUMMARY

Write exactly 3 bullets. These are your top-3 findings by blast-radius tier, identified by position
in this section. The first bullet is the highest-blast-radius finding; the third is the third.
If fewer than 3 findings exist, write the available count and note the shortfall.

Use this format for each bullet exactly:
- F-[N]: [finding name] | blast-radius: [wide|medium|narrow] | chain: [origin] -> [component] -> [terminal: T-NN] | [CONFIRMED -- evidence: [phase]: [finding] | RUNTIME ANOMALY]

VALIDITY RULES for this section:
1. Chain terminus must use a T-NN code from the Phase 0 registry (e.g., T-04), not a
   free-form component name. A bullet with a free-form terminus is INVALID.
   If a chain cannot resolve to a T-NN code, write "unresolved chain — registry miss: [name]"
   and exclude until resolved via Q1.
2. Confirmation slot must carry the inline evidence citation format:
   CONFIRMED -- evidence: [source-phase]: [matching-finding-name]
   Plain [CONFIRMED] token is NOT valid in EXECUTIVE SUMMARY bullets.

Do not summarize. Do not add prose. Three structured bullets, then stop.

---

## Q7 — EXECUTIVE SUMMARY structural audit

Before writing CONSOLIDATE, audit the EXECUTIVE SUMMARY bullets you just wrote.

For each bullet:
- C-30 check: Does the chain field terminate at a T-NN code (e.g., `-> T-04`), not a free-form
  component name? If free-form name found: identify the matching T-NN entry from the Phase 0
  registry and rewrite the bullet with the T-NN code. If no T-NN entry resolves: flag
  "unresolved chain — registry miss" and exclude from ranking.
- C-31 check: Does the confirmation slot use `CONFIRMED -- evidence: [source-phase]: [finding-name]`
  format? If plain [CONFIRMED] found without inline citation: rewrite using the citation verified
  in Q2. If no Q2 citation exists for this finding: reclassify as RUNTIME ANOMALY.

State the result of each check:
- "Bullet F-[N]: C-30 PASS (terminal: T-NN), C-31 PASS (inline citation present)"
- OR list the revision made and the corrected bullet text.

If all three bullets pass both checks: "EXECUTIVE SUMMARY audit complete — C-30 and C-31 satisfied
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
3. Blast radius: [wide | medium | narrow] — propagation chain: [origin] → [component] → [terminal: T-NN]
4. Severity at epicenter: [high | med | low]
5. SYSTEMIC: [yes — phases: [comma-separated phase list] | no]
6. Classification: [CONFIRMED -- evidence: [source-phase]: [matching-finding-name] | RUNTIME ANOMALY | isolated]
7. What must change: [one concrete fix direction in spec, contract, or implementation]
---

**Spec gaps:** [list each gap with missing-clause citation, or "none detected"]

**Contract violations:** [list each with producer and consumer named, or "none detected"]

**Privilege escalation paths:** [list each, or "none detected"]

**Clean zones:** [Phase 0 census components with no findings across all five phases]

---

## Q8 — CONSOLIDATE finding block completeness gate

Before writing VERDICT, audit every finding block written in CONSOLIDATE.

For each finding block [N]:
- 7-field check: All seven fields (Name, Source phase, Blast radius, Severity, SYSTEMIC,
  Classification, What must change) are present and non-empty.
  If any field is missing or blank: identify the field and state the required content.
- T-NN chain check: Field 3 blast radius chain terminates at a T-NN code from the Phase 0
  registry (e.g., `[terminal: T-04]`), not a free-form component name.
  If free-form terminus found: identify the matching T-NN entry and rewrite field 3.
  If no T-NN entry resolves: flag "unresolved chain — registry miss: [component name]."
- Classification format check: Field 6 uses `CONFIRMED -- evidence: [source-phase]: [finding-name]`
  format, or RUNTIME ANOMALY, or isolated.
  Plain [CONFIRMED] without inline citation is NOT valid. Rewrite using Q2-verified citation,
  or reclassify as RUNTIME ANOMALY if no Q2 citation exists.

State the result for each block:
- "Finding [N]: 7-field PASS, T-NN PASS (terminal: T-NN), classification PASS"
- OR list the revision made and the corrected field content.

If all blocks pass all checks: "CONSOLIDATE audit complete — all [N] finding blocks satisfy
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

## V-04 — Registry-Lock + Per-Phase T-NN Exit Gates (V-02 + V-01)
**Axis:** Combines registry-lock declaration (V-02) with per-phase T-NN exit gates (V-01).
Tests whether upstream enforcement — locking the registry before phases run and verifying chain
resolution at each phase exit — compose without structural interference and eliminate the main
paths to free-form terminus drift before they can reach CONSOLIDATE or EXECUTIVE SUMMARY.
**Hypothesis:** V-01 and V-02 address orthogonal enforcement points. V-02 prevents new terminus
components from entering the registry post-Phase-0 (declaration-time integrity). V-01 verifies
that each phase's findings resolve to the locked registry before the phase exits (production-time
integrity per phase). The two rules operate at different execution moments — V-02 at Phase 0 exit,
V-01 at each subsequent phase exit — so they should compose without structural interference. If
both add signal independently, V-04 should produce a template where free-form terminus names
cannot survive past any individual phase's exit gate, and the Phase 0 registry is the immutable
authority. V-04 is the upstream enforcement candidate; V-05 adds the post-CONSOLIDATE gate.

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
Format: [origin] → [component-B] → [terminal: T-NN]
The terminal must resolve to a T-NN entry in the Phase 0 terminus registry.
Chains that cannot resolve to a T-NN entry must be flagged:
"unresolved chain — registry miss."

T-NN = terminus registry code. Assigned in Phase 0 to every unique propagation chain endpoint
(shared state surface, downstream caller boundary, or role-boundary that terminates blast).
The Phase 0 registry is the single source of truth. No T-NN entry may be added, removed, or
renamed after Phase 0 is locked. Referenced in field 3 of every finding, in EXECUTIVE SUMMARY
bullets, and in chain-to-terminus tracing during Q1.

SYSTEMIC = a finding corroborated across three or more phases.
Required format: "SYSTEMIC: yes — phases: [phase-name-1], [phase-name-2], [phase-name-3]"
Binary "SYSTEMIC: yes" without a phase list is not valid and will be rejected.

CONFIRMED = a Phase 4 or Phase 5 finding that matches a topology violation from Phases 1–3.
Match is structural: same component, access pattern, contract term, or state surface.
Required format when classifying CONFIRMED:
  "CONFIRMED -- evidence: [source-phase]: [matching-finding-name]"
Omitting the evidence citation invalidates the CONFIRMED classification.

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

**Terminus registry:**

| T-NN | Terminus component | Type |
|------|--------------------|------|
| T-01 | [component name]   | [shared-state \| downstream-caller \| role-boundary] |
| ...  | ...                | ... |

Assign a T-NN code to every unique blast-surface endpoint in the system. Propagation chains
in findings below must terminate at a T-NN entry. Chains that cannot resolve = registry miss.

Every blast radius claim must name a specific census entry.
Every propagation chain must terminate at a T-NN registry code.

**Registry lock:** The terminus registry is now complete.
No terminus component may be added, removed, or renamed after this point.
All propagation chains in Phases 1–5 must resolve to a T-NN entry from this registry or be
flagged "unresolved chain — registry miss: [component name]."
Any component encountered in Phases 1–5 that is not in this registry must be recorded as a
spec gap (undeclared blast surface) — it may not be silently added to the registry.
State: "Registry locked: [N] terminus entries. Phase execution may begin."

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
T-NN resolution check: All propagation chains produced in this phase resolve to T-NN registry entries.
State: "[N] chains produced, [N] resolved to T-NN, [N] registry miss."
If any registry miss: flag "unresolved chain — registry miss: [component name]" and carry forward to Q1.

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
T-NN resolution check: All propagation chains produced in this phase resolve to T-NN registry entries.
State: "[N] chains produced, [N] resolved to T-NN, [N] registry miss."
If any registry miss: flag "unresolved chain — registry miss: [component name]" and carry forward to Q1.

---

## PHASE 3 — trace-contract

| Producer | Consumer | Contract term | Expected | Actual | Mismatch? | Phase 1/2 topology match? |
|----------|----------|---------------|----------|--------|-----------|--------------------------|

Phase 1/2 topology match = yes if contract involves a Phase 1 state violation surface or Phase 2
escalation role. If match = yes: classify CONFIRMED -- evidence: [phase-1|phase-2]: [matching-finding-name].
Name the matching finding from Phase 1 or Phase 2.

If clean: "trace-contract: clean — all contracts verified."

EXIT CRITERIA: All producer/consumer pairs evaluated.
State: "trace-contract complete: [N] pairs evaluated, [N] mismatches found, [N] CONFIRMED."
T-NN resolution check: All propagation chains produced in this phase resolve to T-NN registry entries.
State: "[N] chains produced, [N] resolved to T-NN, [N] registry miss."
If any registry miss: flag "unresolved chain — registry miss: [component name]" and carry forward to Q1.

---

## PHASE 4 — flow-lifecycle

| Phase | Entry contract | Exit contract | Exception path | Exception handled? | Phase tag | CONFIRMED / RUNTIME ANOMALY |
|-------|----------------|---------------|----------------|--------------------|-----------|-----------------------------|

Phase tag = lifecycle phase of violation (INIT, ACTIVE, SUSPENDED, TERMINAL, etc.).
CONFIRMED = matches a Phase 1–3 violation. Use format:
  CONFIRMED -- evidence: [source-phase]: [matching-finding-name]
RUNTIME ANOMALY = no matching topology violation.

If clean: "flow-lifecycle: clean — all lifecycle transitions verified."

EXIT CRITERIA: All lifecycle phases evaluated.
State: "flow-lifecycle complete: [N] phases, [N] failures, [N] CONFIRMED, [N] RUNTIME ANOMALY."
T-NN resolution check: All propagation chains produced in this phase resolve to T-NN registry entries.
State: "[N] chains produced, [N] resolved to T-NN, [N] registry miss."
If any registry miss: flag "unresolved chain — registry miss: [component name]" and carry forward to Q1.

---

## PHASE 5 — flow-trigger

| Trigger | Expected fire order | Actual fire order | Race condition? | Phase 2 escalation role? | Phase tag | CONFIRMED / RUNTIME ANOMALY |
|---------|---------------------|-------------------|-----------------|--------------------------|-----------|------------------------------|

Phase 2 escalation role = yes if trigger involves a Phase 2 escalation role: blast radius = wide.
CONFIRMED = matches a Phase 1–3 violation. Use format:
  CONFIRMED -- evidence: [source-phase]: [matching-finding-name]

If clean: "flow-trigger: clean — all triggers verified."

EXIT CRITERIA: All triggers and activating events evaluated.
State: "flow-trigger complete: [N] triggers, [N] failures, [N] CONFIRMED, [N] RUNTIME ANOMALY."
T-NN resolution check: All propagation chains produced in this phase resolve to T-NN registry entries.
State: "[N] chains produced, [N] resolved to T-NN, [N] registry miss."
If any registry miss: flag "unresolved chain — registry miss: [component name]" and carry forward to Q1.

---

## CALIBRATION BLOCK

Q1: Does any finding's blast radius change when the propagation chain is traced to its T-NN terminus?
For each finding: trace the full chain ([origin] → ... → [terminal: T-NN]). Does the chain reach
a Phase 0 shared-state T-NN entry? If yes, upgrade to wide. List every revision and the full chain.
Flag any finding whose chain cannot resolve to a T-NN entry: "unresolved chain — registry miss."

Q2: Do any Phase 4–5 findings match topology violations from Phases 1–3?
For each Phase 4–5 finding classified as CONFIRMED: verify the inline citation is present using
format "CONFIRMED -- evidence: [source-phase]: [matching-finding-name]."
Any CONFIRMED classification missing this citation must be revised before consolidation.
Also verify: for any finding that will appear in the EXECUTIVE SUMMARY as CONFIRMED, confirm
that the same inline citation format will be used in the summary bullet (not a plain [CONFIRMED]
token). Note any summary slots that would use plain tokens — revise those bullets after Q7.
List all reclassifications and citations verified or added.

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

## EXECUTIVE SUMMARY

Write exactly 3 bullets. These are your top-3 findings by blast-radius tier, identified by position
in this section. The first bullet is the highest-blast-radius finding; the third is the third.
If fewer than 3 findings exist, write the available count and note the shortfall.

Use this format for each bullet exactly:
- F-[N]: [finding name] | blast-radius: [wide|medium|narrow] | chain: [origin] -> [component] -> [terminal: T-NN] | [CONFIRMED -- evidence: [phase]: [finding] | RUNTIME ANOMALY]

VALIDITY RULES for this section:
1. Chain terminus must use a T-NN code from the Phase 0 registry (e.g., T-04), not a
   free-form component name. A bullet with a free-form terminus is INVALID.
   If a chain cannot resolve to a T-NN code, write "unresolved chain — registry miss: [name]"
   and exclude until resolved via Q1.
2. Confirmation slot must carry the inline evidence citation format:
   CONFIRMED -- evidence: [source-phase]: [matching-finding-name]
   Plain [CONFIRMED] token is NOT valid in EXECUTIVE SUMMARY bullets.

Do not summarize. Do not add prose. Three structured bullets, then stop.

---

## Q7 — EXECUTIVE SUMMARY structural audit

Before writing CONSOLIDATE, audit the EXECUTIVE SUMMARY bullets you just wrote.

For each bullet:
- C-30 check: Does the chain field terminate at a T-NN code (e.g., `-> T-04`), not a free-form
  component name? If free-form name found: identify the matching T-NN entry from the Phase 0
  registry and rewrite the bullet with the T-NN code. If no T-NN entry resolves: flag
  "unresolved chain — registry miss" and exclude from ranking.
- C-31 check: Does the confirmation slot use `CONFIRMED -- evidence: [source-phase]: [finding-name]`
  format? If plain [CONFIRMED] found without inline citation: rewrite using the citation verified
  in Q2. If no Q2 citation exists for this finding: reclassify as RUNTIME ANOMALY.

State the result of each check:
- "Bullet F-[N]: C-30 PASS (terminal: T-NN), C-31 PASS (inline citation present)"
- OR list the revision made and the corrected bullet text.

If all three bullets pass both checks: "EXECUTIVE SUMMARY audit complete — C-30 and C-31 satisfied
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
3. Blast radius: [wide | medium | narrow] — propagation chain: [origin] → [component] → [terminal: T-NN]
4. Severity at epicenter: [high | med | low]
5. SYSTEMIC: [yes — phases: [comma-separated phase list] | no]
6. Classification: [CONFIRMED -- evidence: [source-phase]: [matching-finding-name] | RUNTIME ANOMALY | isolated]
7. What must change: [one concrete fix direction in spec, contract, or implementation]
---

**Spec gaps:** [list each gap with missing-clause citation, or "none detected"]

**Contract violations:** [list each with producer and consumer named, or "none detected"]

**Privilege escalation paths:** [list each, or "none detected"]

**Clean zones:** [Phase 0 census components with no findings across all five phases]

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

## V-05 — Full Pipeline Enforcement (Registry-Lock + Per-Phase Exit Gates + Q8 CONSOLIDATE Gate)
**Axis:** All R12 structural axes combined: V-02 registry-lock declaration, V-01 per-phase T-NN
exit gates, and V-03 Q8 post-CONSOLIDATE completeness gate. This is the full three-layer
enforcement architecture for the CONSOLIDATE pipeline, mirroring the three-layer architecture
V-05 R11 introduced for EXECUTIVE SUMMARY. The three independent layers: registry-lock (prevents
unauthorized terminus additions before phases run), per-phase exit gates (catches drift at each
phase before it propagates), Q8 CONSOLIDATE gate (verifies the written output after CONSOLIDATE).
**Hypothesis:** V-05 R11 achieved three-layer enforcement for EXECUTIVE SUMMARY (C-32 write-time
rejection gate + C-34 Q2 pre-write preview + C-33 Q7 post-write audit). Each layer catches
failures the other two miss: C-32 rejects invalid formats before they are written, C-34 flags
gaps before the section is drafted, C-33 confirms the produced output is correct. No analogous
three-layer stack exists for CONSOLIDATE finding blocks under v10. V-05 R12 closes this gap by
applying the same logic: registry-lock prevents invalid terminus additions before any phase runs
(write-time gate), per-phase exit gates catch drift as each phase produces findings (production-time
gate per phase), Q8 confirms the CONSOLIDATE output is structurally sound after writing (post-write
gate). If this pattern scores well under evaluation, it may inform three new v11 criteria
(C-35 registry-lock, C-36 per-phase exit gates, C-37 Q8 CONSOLIDATE gate) that mirror C-32/C-33/C-34
for the CONSOLIDATE output section.

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
Format: [origin] → [component-B] → [terminal: T-NN]
The terminal must resolve to a T-NN entry in the Phase 0 terminus registry.
Chains that cannot resolve to a T-NN entry must be flagged:
"unresolved chain — registry miss."

T-NN = terminus registry code. Assigned in Phase 0 to every unique propagation chain endpoint
(shared state surface, downstream caller boundary, or role-boundary that terminates blast).
The Phase 0 registry is the single source of truth. No T-NN entry may be added, removed, or
renamed after Phase 0 is locked. Referenced in field 3 of every finding, in EXECUTIVE SUMMARY
bullets, and in chain-to-terminus tracing during Q1.

SYSTEMIC = a finding corroborated across three or more phases.
Required format: "SYSTEMIC: yes — phases: [phase-name-1], [phase-name-2], [phase-name-3]"
Binary "SYSTEMIC: yes" without a phase list is not valid and will be rejected.

CONFIRMED = a Phase 4 or Phase 5 finding that matches a topology violation from Phases 1–3.
Match is structural: same component, access pattern, contract term, or state surface.
Required format when classifying CONFIRMED:
  "CONFIRMED -- evidence: [source-phase]: [matching-finding-name]"
Omitting the evidence citation invalidates the CONFIRMED classification.

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

**Terminus registry:**

| T-NN | Terminus component | Type |
|------|--------------------|------|
| T-01 | [component name]   | [shared-state \| downstream-caller \| role-boundary] |
| ...  | ...                | ... |

Assign a T-NN code to every unique blast-surface endpoint in the system. Propagation chains
in findings below must terminate at a T-NN entry. Chains that cannot resolve = registry miss.

Every blast radius claim must name a specific census entry.
Every propagation chain must terminate at a T-NN registry code.

**Registry lock:** The terminus registry is now complete.
No terminus component may be added, removed, or renamed after this point.
All propagation chains in Phases 1–5 must resolve to a T-NN entry from this registry or be
flagged "unresolved chain — registry miss: [component name]."
Any component encountered in Phases 1–5 that is not in this registry must be recorded as a
spec gap (undeclared blast surface) — it may not be silently added to the registry.
State: "Registry locked: [N] terminus entries. Phase execution may begin."

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
T-NN resolution check: All propagation chains produced in this phase resolve to T-NN registry entries.
State: "[N] chains produced, [N] resolved to T-NN, [N] registry miss."
If any registry miss: flag "unresolved chain — registry miss: [component name]" and carry forward to Q1.

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
T-NN resolution check: All propagation chains produced in this phase resolve to T-NN registry entries.
State: "[N] chains produced, [N] resolved to T-NN, [N] registry miss."
If any registry miss: flag "unresolved chain — registry miss: [component name]" and carry forward to Q1.

---

## PHASE 3 — trace-contract

| Producer | Consumer | Contract term | Expected | Actual | Mismatch? | Phase 1/2 topology match? |
|----------|----------|---------------|----------|--------|-----------|--------------------------|

Phase 1/2 topology match = yes if contract involves a Phase 1 state violation surface or Phase 2
escalation role. If match = yes: classify CONFIRMED -- evidence: [phase-1|phase-2]: [matching-finding-name].
Name the matching finding from Phase 1 or Phase 2.

If clean: "trace-contract: clean — all contracts verified."

EXIT CRITERIA: All producer/consumer pairs evaluated.
State: "trace-contract complete: [N] pairs evaluated, [N] mismatches found, [N] CONFIRMED."
T-NN resolution check: All propagation chains produced in this phase resolve to T-NN registry entries.
State: "[N] chains produced, [N] resolved to T-NN, [N] registry miss."
If any registry miss: flag "unresolved chain — registry miss: [component name]" and carry forward to Q1.

---

## PHASE 4 — flow-lifecycle

| Phase | Entry contract | Exit contract | Exception path | Exception handled? | Phase tag | CONFIRMED / RUNTIME ANOMALY |
|-------|----------------|---------------|----------------|--------------------|-----------|-----------------------------|

Phase tag = lifecycle phase of violation (INIT, ACTIVE, SUSPENDED, TERMINAL, etc.).
CONFIRMED = matches a Phase 1–3 violation. Use format:
  CONFIRMED -- evidence: [source-phase]: [matching-finding-name]
RUNTIME ANOMALY = no matching topology violation.

If clean: "flow-lifecycle: clean — all lifecycle transitions verified."

EXIT CRITERIA: All lifecycle phases evaluated.
State: "flow-lifecycle complete: [N] phases, [N] failures, [N] CONFIRMED, [N] RUNTIME ANOMALY."
T-NN resolution check: All propagation chains produced in this phase resolve to T-NN registry entries.
State: "[N] chains produced, [N] resolved to T-NN, [N] registry miss."
If any registry miss: flag "unresolved chain — registry miss: [component name]" and carry forward to Q1.

---

## PHASE 5 — flow-trigger

| Trigger | Expected fire order | Actual fire order | Race condition? | Phase 2 escalation role? | Phase tag | CONFIRMED / RUNTIME ANOMALY |
|---------|---------------------|-------------------|-----------------|--------------------------|-----------|------------------------------|

Phase 2 escalation role = yes if trigger involves a Phase 2 escalation role: blast radius = wide.
CONFIRMED = matches a Phase 1–3 violation. Use format:
  CONFIRMED -- evidence: [source-phase]: [matching-finding-name]

If clean: "flow-trigger: clean — all triggers verified."

EXIT CRITERIA: All triggers and activating events evaluated.
State: "flow-trigger complete: [N] triggers, [N] failures, [N] CONFIRMED, [N] RUNTIME ANOMALY."
T-NN resolution check: All propagation chains produced in this phase resolve to T-NN registry entries.
State: "[N] chains produced, [N] resolved to T-NN, [N] registry miss."
If any registry miss: flag "unresolved chain — registry miss: [component name]" and carry forward to Q1.

---

## CALIBRATION BLOCK

Q1: Does any finding's blast radius change when the propagation chain is traced to its T-NN terminus?
For each finding: trace the full chain ([origin] → ... → [terminal: T-NN]). Does the chain reach
a Phase 0 shared-state T-NN entry? If yes, upgrade to wide. List every revision and the full chain.
Flag any finding whose chain cannot resolve to a T-NN entry: "unresolved chain — registry miss."

Q2: Do any Phase 4–5 findings match topology violations from Phases 1–3?
For each Phase 4–5 finding classified as CONFIRMED: verify the inline citation is present using
format "CONFIRMED -- evidence: [source-phase]: [matching-finding-name]."
Any CONFIRMED classification missing this citation must be revised before consolidation.
Also verify: for any finding that will appear in the EXECUTIVE SUMMARY as CONFIRMED, confirm
that the same inline citation format will be used in the summary bullet (not a plain [CONFIRMED]
token). Note any summary slots that would use plain tokens — revise those bullets after Q7.
List all reclassifications and citations verified or added.

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

## EXECUTIVE SUMMARY

Write exactly 3 bullets. These are your top-3 findings by blast-radius tier, identified by position
in this section. The first bullet is the highest-blast-radius finding; the third is the third.
If fewer than 3 findings exist, write the available count and note the shortfall.

Use this format for each bullet exactly:
- F-[N]: [finding name] | blast-radius: [wide|medium|narrow] | chain: [origin] -> [component] -> [terminal: T-NN] | [CONFIRMED -- evidence: [phase]: [finding] | RUNTIME ANOMALY]

VALIDITY RULES for this section:
1. Chain terminus must use a T-NN code from the Phase 0 registry (e.g., T-04), not a
   free-form component name. A bullet with a free-form terminus is INVALID.
   If a chain cannot resolve to a T-NN code, write "unresolved chain — registry miss: [name]"
   and exclude until resolved via Q1.
2. Confirmation slot must carry the inline evidence citation format:
   CONFIRMED -- evidence: [source-phase]: [matching-finding-name]
   Plain [CONFIRMED] token is NOT valid in EXECUTIVE SUMMARY bullets.

Do not summarize. Do not add prose. Three structured bullets, then stop.

---

## Q7 — EXECUTIVE SUMMARY structural audit

Before writing CONSOLIDATE, audit the EXECUTIVE SUMMARY bullets you just wrote.

For each bullet:
- C-30 check: Does the chain field terminate at a T-NN code (e.g., `-> T-04`), not a free-form
  component name? If free-form name found: identify the matching T-NN entry from the Phase 0
  registry and rewrite the bullet with the T-NN code. If no T-NN entry resolves: flag
  "unresolved chain — registry miss" and exclude from ranking.
- C-31 check: Does the confirmation slot use `CONFIRMED -- evidence: [source-phase]: [finding-name]`
  format? If plain [CONFIRMED] found without inline citation: rewrite using the citation verified
  in Q2. If no Q2 citation exists for this finding: reclassify as RUNTIME ANOMALY.

State the result of each check:
- "Bullet F-[N]: C-30 PASS (terminal: T-NN), C-31 PASS (inline citation present)"
- OR list the revision made and the corrected bullet text.

If all three bullets pass both checks: "EXECUTIVE SUMMARY audit complete — C-30 and C-31 satisfied
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
3. Blast radius: [wide | medium | narrow] — propagation chain: [origin] → [component] → [terminal: T-NN]
4. Severity at epicenter: [high | med | low]
5. SYSTEMIC: [yes — phases: [comma-separated phase list] | no]
6. Classification: [CONFIRMED -- evidence: [source-phase]: [matching-finding-name] | RUNTIME ANOMALY | isolated]
7. What must change: [one concrete fix direction in spec, contract, or implementation]
---

**Spec gaps:** [list each gap with missing-clause citation, or "none detected"]

**Contract violations:** [list each with producer and consumer named, or "none detected"]

**Privilege escalation paths:** [list each, or "none detected"]

**Clean zones:** [Phase 0 census components with no findings across all five phases]

---

## Q8 — CONSOLIDATE finding block completeness gate

Before writing VERDICT, audit every finding block written in CONSOLIDATE.

For each finding block [N]:
- 7-field check: All seven fields (Name, Source phase, Blast radius, Severity, SYSTEMIC,
  Classification, What must change) are present and non-empty.
  If any field is missing or blank: identify the field and state the required content.
- T-NN chain check: Field 3 blast radius chain terminates at a T-NN code from the Phase 0
  registry (e.g., `[terminal: T-04]`), not a free-form component name.
  If free-form terminus found: identify the matching T-NN entry and rewrite field 3.
  If no T-NN entry resolves: flag "unresolved chain — registry miss: [component name]."
- Classification format check: Field 6 uses `CONFIRMED -- evidence: [source-phase]: [finding-name]`
  format, or RUNTIME ANOMALY, or isolated.
  Plain [CONFIRMED] without inline citation is NOT valid. Rewrite using Q2-verified citation,
  or reclassify as RUNTIME ANOMALY if no Q2 citation exists.

State the result for each block:
- "Finding [N]: 7-field PASS, T-NN PASS (terminal: T-NN), classification PASS"
- OR list the revision made and the corrected field content.

If all blocks pass all checks: "CONSOLIDATE audit complete — all [N] finding blocks satisfy
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
