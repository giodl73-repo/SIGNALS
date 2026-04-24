# Quest Variations — campaign-behavior (R11)
**Skill:** campaign-behavior
**Rubric:** v9 (C-01–C-31)
**Round:** 11
**Date:** 2026-03-17

---

## Axes explored in R11

**Context:** R10 V-05 scored 90/90 under v8. Under v9 (denominator 23), two new criteria
target the EXECUTIVE SUMMARY section specifically:

- **C-30** — EXECUTIVE SUMMARY bullet chains must reference T-NN terminus codes, not
  free-form component names. V-05 uses `[terminal: T-NN]` in the bullet format, which is
  structurally correct — but does not explicitly forbid free-form names or require
  verification against the Phase 0 registry before writing each bullet.
- **C-31** — EXECUTIVE SUMMARY bullet confirmation slots must carry inline evidence
  citations (`CONFIRMED -- evidence: [source-phase]: [finding-name]`), not plain
  `[CONFIRMED]` tokens. V-05 uses the correct citation format in the template — but does
  not explicitly reject the plain-token form or audit EXECUTIVE SUMMARY bullets in Q2.

**Gap hypothesis:** V-05 R10 has the right formats embedded. The risk is format drift at
execution time when no explicit rejection rule and no dedicated calibration gate exist for
the EXECUTIVE SUMMARY section specifically. C-30 and C-31 may be PARTIAL rather than
PASS if a model executing the template substitutes free-form names or plain tokens in
the summary without triggering a structural failure.

Single-axis (three independent axes):
- **C-30 explicit enforcement** — Add a rejection rule in EXECUTIVE SUMMARY that flags
  free-form terminal names as invalid and requires T-NN registry verification per bullet.
- **C-31 explicit enforcement** — Add a rejection rule in EXECUTIVE SUMMARY that forbids
  plain `[CONFIRMED]` tokens and requires inline citation format in every confirmation slot.
- **Phrasing register shift** — Convert imperative instructions to descriptive/explanatory
  register throughout DEFINITIONS and phase headers. Tests whether WHY framing improves
  structural compliance without disrupting the template format.

Combinations (V-04, V-05):
- **V-04:** C-30 enforcement + C-31 enforcement (both single-axis structural rules combined)
- **V-05:** Full integration — V-04 axes + Q7 EXECUTIVE SUMMARY audit gate + Q2 extended
  to cover EXECUTIVE SUMMARY bullets explicitly.

---

## V-01 — C-30 Explicit Enforcement
**Axis:** EXECUTIVE SUMMARY T-NN rejection rule — adds an explicit validity gate requiring
every EXECUTIVE SUMMARY bullet chain to resolve to a T-NN code from the Phase 0 registry
before the bullet is written. Free-form terminal names are flagged as invalid.
**Hypothesis:** R10 V-05 uses `[terminal: T-NN]` in the bullet format, which is the correct
structural instruction. However, the EXECUTIVE SUMMARY section has no explicit rejection
language for free-form names and no instruction to verify each chain terminus against the
Phase 0 registry before committing the bullet. Adding a pre-write validation step closes
C-30's "chains use free-form names without T-NN notation = PARTIAL" failure path.

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
List all reclassifications and all citations verified or added.

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

BEFORE writing each bullet, verify:
1. The chain terminus for this finding resolves to a T-NN entry in the Phase 0 registry.
   A free-form terminal name (e.g., "DataLayer") is INVALID here — use the T-NN code (e.g., T-04).
   If the chain cannot resolve to a T-NN entry, write "unresolved chain — registry miss: [component name]"
   and exclude this finding from the top-3 ranking until the chain is resolved.

Write exactly 3 bullets. These are your top-3 findings by blast-radius tier, identified by position
in this section. The first bullet is the highest-blast-radius finding; the third is the third.
If fewer than 3 findings exist, write the available count and note the shortfall.

Use this format for each bullet exactly:
- F-[N]: [finding name] | blast-radius: [wide|medium|narrow] | chain: [origin] -> [component] -> [terminal: T-NN] | [CONFIRMED -- evidence: [phase]: [finding] | RUNTIME ANOMALY]

Do not summarize. Do not add prose. Three structured bullets, then stop.

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

## V-02 — C-31 Explicit Enforcement
**Axis:** EXECUTIVE SUMMARY inline evidence rejection rule — adds an explicit validity rule
that forbids plain `[CONFIRMED]` tokens in EXECUTIVE SUMMARY bullet confirmation slots.
The confirmation slot must carry the full inline citation format, and the EXECUTIVE SUMMARY
section states what happens when it is absent.
**Hypothesis:** R10 V-05 uses the correct citation format in the EXECUTIVE SUMMARY bullet
template. However, the section does not explicitly state that plain `[CONFIRMED]` tokens are
invalid there. An explicit rejection rule is necessary because the EXECUTIVE SUMMARY is written
AFTER all calibration questions (where Q2 has already verified field 6 inline citations) —
a model may reason that Q2 compliance is sufficient and use a shorter form in the summary.
Making the rejection explicit at the EXECUTIVE SUMMARY writing point prevents this inference.

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
List all reclassifications and all citations verified or added.

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

IMPORTANT: The confirmation slot in each bullet MUST use the inline evidence citation format above.
The plain token [CONFIRMED] is NOT valid in EXECUTIVE SUMMARY bullets — it omits the evidence
link that makes the top-3 summary independently auditable. Any bullet using plain [CONFIRMED]
without "-- evidence: [source-phase]: [finding-name]" is structurally incomplete.

Do not summarize. Do not add prose. Three structured bullets, then stop.

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

## V-03 — Phrasing Register Shift
**Axis:** Descriptive/explanatory register — converts the imperative instruction style of
R10 V-05 into an explanatory register that states WHY each structural requirement exists,
not just WHAT to do. DEFINITIONS explain the reasoning behind each term. Phase headers
explain the purpose of each anchor. EXECUTIVE SUMMARY section explains why T-NN codes
and inline citations are required in that specific context.
**Hypothesis:** Imperative style ("Write exactly 3 bullets") is compact but gives no
scaffolding for edge-case reasoning. When a model encounters an edge case (fewer than 3
findings, a finding whose chain doesn't resolve, a CONFIRMED finding from a non-standard
phase), explanatory framing gives it the intent to reason from. The risk is verbosity
increasing prompt length without adding structural compliance. If phrasing register is
neutral for scoring criteria, this variation should score identically to R10 V-05 on
structural criteria while potentially improving edge-case output quality.

```
Simulate the technical behavior of: {{topic}}

---

## DEFINITIONS

**Blast radius** measures how broadly a failure propagates through the system — not how bad
the failure is at the source (that is severity), but how far it reaches.
- Wide: the failure corrupts shared state, breaks downstream callers, or blocks multiple user
  roles simultaneously. Wide findings are dangerous because fixing them requires coordinating
  multiple teams or reverting shared resources.
- Medium: two or more components are affected, but no shared state surface is reached. The
  damage is bounded to a subsystem.
- Narrow: the failure is contained within one component boundary. A narrow finding can be fixed
  by one team without cross-system coordination.
Blast radius and severity are independent dimensions. Report them as separate labeled fields
in every finding — merging them obscures the difference between a localized but catastrophic
failure (narrow/high) and a diffuse but recoverable one (wide/low).

**Propagation chain** is the ordered path a failure travels from its origin through intermediate
components to the terminal blast surface. Chains make blast radius claims auditable: a reviewer
can follow each hop and verify the tier assignment rather than accepting an asserted label.
Format: [origin] → [component-B] → [terminal: T-NN]
The terminal must resolve to a T-NN entry in the Phase 0 terminus registry. Chains that cannot
name a registry terminus are flagged "unresolved chain — registry miss" and excluded from
ranking until resolved.

**T-NN** is a terminus registry code assigned in Phase 0 to every unique propagation chain
endpoint. Using T-NN codes instead of component names prevents naming divergence: two chains
that describe the same terminal surface using different names can appear distinct. T-NN codes
appear in field 3 of every finding, in EXECUTIVE SUMMARY bullets, and in Q1 chain-to-terminus
tracing. The registry is the single source of truth for valid blast surfaces.

**SYSTEMIC** means a finding is corroborated across three or more phases — it is not an artifact
of one sub-skill's analysis but a cross-cutting structural violation.
Required format: "SYSTEMIC: yes — phases: [phase-name-1], [phase-name-2], [phase-name-3]"
Binary "SYSTEMIC: yes" without a phase list is not valid. The phase list is what distinguishes
a genuine SYSTEMIC classification from an inflated one — it must be verifiable.

**CONFIRMED** means a Phase 4 or Phase 5 finding matches a topology violation already
identified in Phases 1–3. The match must be structural: same component, access pattern,
contract term, or state surface. A CONFIRMED finding is more actionable than a RUNTIME
ANOMALY because its root cause is already located in the topology analysis.
Required format: "CONFIRMED -- evidence: [source-phase]: [matching-finding-name]"
Omitting the evidence citation means the CONFIRMED classification cannot be verified.

**RUNTIME ANOMALY** means a Phase 4 or Phase 5 finding has no matching topology violation
in Phases 1–3. It may indicate a gap in the topology analysis or a genuinely emergent
runtime behavior not predictable from static structure.

**Tiebreaker protocol** determines ranking order when two findings have equal blast radius.
Apply in order: (1) blast radius descending (wide > medium > narrow), (2) CONFIRMED before
RUNTIME ANOMALY, (3) SYSTEMIC before isolated. State whether any ties occurred and how the
protocol resolved them. If no ties: state that explicitly.

---

## PHASE 0 — Topology census

Before running any sub-skill, establish the system vocabulary that all subsequent phases
will reference. Without a shared census, each phase may name components differently, making
cross-phase comparison unreliable.

**Components in scope:** [every named service, module, API, schema, queue from the spec]

**Shared state surfaces:** [databases, caches, event buses, config objects read or written by
multiple components — blast-radius amplifiers; any propagation chain reaching these = wide]

**Downstream callers:** [every component that depends on outputs from this system]

**Role-resource inventory:** [every role and the resources it may access]

**Pre-declared contracts:** [every producer/consumer contract term the spec commits to —
the CONFIRMED classification baseline for Phases 4–5]

**Terminus registry:**

The terminus registry assigns a T-NN code to every unique blast-surface endpoint. Phases 1–5
must resolve their propagation chains to a T-NN entry. This prevents free-form naming from
obscuring whether two findings share the same terminal surface.

| T-NN | Terminus component | Type |
|------|--------------------|------|
| T-01 | [component name]   | [shared-state \| downstream-caller \| role-boundary] |
| ...  | ...                | ... |

---

## PHASE 1 — trace-state [ANCHOR: state topology pre-classifies blast radius candidates for all downstream phases]

trace-state runs first because shared-state topology determines which findings can reach wide
blast radius. By classifying state surfaces before any other analysis begins, Phases 2–5
inherit a consistent blast radius map rather than each independently assessing whether a
given component is a blast amplifier.

| From state | To state | Trigger | Invariant | Invariant holds? | Shared state surface? | Blast radius candidate |
|------------|----------|---------|-----------|------------------|-----------------------|------------------------|

For each shared state surface = yes: record blast radius candidate as wide. This classification
is locked for downstream phases — a Phase 4 or Phase 5 finding involving this surface inherits
the wide classification without re-derivation.

If no violations: "trace-state: clean — all invariants verified."

EXIT CRITERIA: All state transitions and invariants evaluated. No transitions deferred.
State: "trace-state complete: [N] transitions evaluated, [N] violations found, [N] pre-classified wide."

---

## PHASE 2 — trace-permissions [ANCHOR: privilege boundary classification anchors flow blast radius assessment]

trace-permissions runs second, before all flow sub-skills, because privilege boundary violations
are SYSTEMIC by definition — a flow that crosses a privilege boundary cannot be analyzed in
isolation. Without knowing where privilege boundaries sit before flow analysis begins, flow
sub-skills may understate propagation scope for violations that touch access control.

| Role | Resource | Action | Permitted? | Escalation path? | Phase 1 state surface involved? | Blast radius ceiling |
|------|----------|--------|------------|------------------|---------------------------------|----------------------|

When Phase 1 state surface involved = yes AND escalation path = yes: record a compound anchor
hit. The blast radius ceiling for this finding is wide, enforced by both anchors.

If clean: "trace-permissions: clean — all role-resource pairs verified, no escalation paths detected."

EXIT CRITERIA: All role-resource pairs evaluated. No pairs deferred.
State: "trace-permissions complete: [N] pairs evaluated, [N] escalation paths found, [N] compound anchor hits."

---

## PHASE 3 — trace-contract

| Producer | Consumer | Contract term | Expected | Actual | Mismatch? | Phase 1/2 topology match? |
|----------|----------|---------------|----------|--------|-----------|--------------------------|

Phase 1/2 topology match = yes if the contract involves a Phase 1 state violation surface or
a Phase 2 escalation role. When match = yes, the contract mismatch is not a standalone finding
but a structural consequence of a topology violation already identified. Classify:
  CONFIRMED -- evidence: [phase-1|phase-2]: [matching-finding-name]
Name the specific matching finding from Phase 1 or Phase 2.

If clean: "trace-contract: clean — all contracts verified."

EXIT CRITERIA: All producer/consumer pairs evaluated.
State: "trace-contract complete: [N] pairs evaluated, [N] mismatches found, [N] CONFIRMED."

---

## PHASE 4 — flow-lifecycle

| Phase | Entry contract | Exit contract | Exception path | Exception handled? | Phase tag | CONFIRMED / RUNTIME ANOMALY |
|-------|----------------|---------------|----------------|--------------------|-----------|-----------------------------|

Phase tag records the lifecycle phase of the violation (INIT, ACTIVE, SUSPENDED, TERMINAL, etc.)
so that phase-specific blast radius comparisons are possible after consolidation.

CONFIRMED means this lifecycle failure matches a topology violation from Phases 1–3.
Use format: CONFIRMED -- evidence: [source-phase]: [matching-finding-name]
RUNTIME ANOMALY means no matching topology violation was found.

If clean: "flow-lifecycle: clean — all lifecycle transitions verified."

EXIT CRITERIA: All lifecycle phases evaluated — including exception paths.
State: "flow-lifecycle complete: [N] phases, [N] failures, [N] CONFIRMED, [N] RUNTIME ANOMALY."

---

## PHASE 5 — flow-trigger

| Trigger | Expected fire order | Actual fire order | Race condition? | Phase 2 escalation role? | Phase tag | CONFIRMED / RUNTIME ANOMALY |
|---------|---------------------|-------------------|-----------------|--------------------------|-----------|------------------------------|

Phase 2 escalation role = yes if the trigger involves a Phase 2 escalation role. When yes,
the blast radius is wide regardless of the trigger's apparent isolation.
CONFIRMED = matches a Phase 1–3 violation. Use format:
  CONFIRMED -- evidence: [source-phase]: [matching-finding-name]

If clean: "flow-trigger: clean — all triggers verified."

EXIT CRITERIA: All triggers and activating events evaluated.
State: "flow-trigger complete: [N] triggers, [N] failures, [N] CONFIRMED, [N] RUNTIME ANOMALY."

---

## CALIBRATION BLOCK

Q1: Does any finding's blast radius change when the propagation chain is traced to its T-NN terminus?
Tracing to the terminus catches cases where the initial blast radius was assessed from the
origin component without following the full propagation path.
For each finding: trace the full chain ([origin] → ... → [terminal: T-NN]). Does the chain reach
a Phase 0 shared-state T-NN entry? If yes, upgrade to wide. List every revision and the full chain.
Flag any finding whose chain cannot resolve to a T-NN entry: "unresolved chain — registry miss."

Q2: Do any Phase 4–5 findings match topology violations from Phases 1–3?
CONFIRMED classification requires structural match, not superficial resemblance.
For each Phase 4–5 finding classified as CONFIRMED: verify the inline citation is present using
format "CONFIRMED -- evidence: [source-phase]: [matching-finding-name]."
Any CONFIRMED classification missing this citation must be revised before consolidation.
List all reclassifications and all citations verified or added.

Q3: Which findings appear in three or more phases?
SYSTEMIC findings are the highest-priority for remediation because they cannot be fixed by
addressing one phase's output in isolation.
For every SYSTEMIC finding: "SYSTEMIC: yes — phases: [phase-name-1], [phase-name-2], [phase-name-3]"
Binary SYSTEMIC flags are not valid.

Q4: Does the blast radius pre-classification map from Phases 1–2 hold throughout?
Pre-classification is only valuable if downstream phases respect it.
For every finding involving a Phase 2 escalation role or Phase 1 state surface: verify wide.
Revise and explain any finding below wide for a pre-classified component.

Q5: Would any finding below have shipped without this simulation?
This question surfaces the value of the campaign — findings that static analysis or code review
would have missed. For each wide-blast-radius finding: name the assumption it would have bypassed.

Q6: Did the execution sequence deliver its pre-classification guarantee?
The anchor ordering (Ph1 → Ph2 → Ph3–Ph5) is only valuable if it produced consistent
blast radius values across phases. Review every blast radius value in the consolidated findings.
Were any revised post-hoc because a finding touched a state surface or escalation role that
Phase 1 or Phase 2 had not yet classified at the time the downstream phase ran?
- Zero revisions: "Anchor guarantee delivered — Phase 1 and Phase 2 pre-classified all blast radius
  values before downstream phases consumed them."
- Any revision: log each as an anchor violation — name the finding, the downstream phase, and the
  Phase 1/2 classification that arrived too late.

---

## EXECUTIVE SUMMARY

The EXECUTIVE SUMMARY gives a reader assessing campaign risk a three-line view without requiring
them to read the full ranked findings list. For this section to be independently auditable, each
bullet must carry: the finding's ID (for cross-reference), blast-radius tier (for risk triage),
propagation chain including T-NN terminus code (so the blast surface is named, not inferred),
and confirmation status with evidence citation (so the reader knows whether the finding is
structural or emergent). Using T-NN codes here, rather than free-form component names, ensures
the summary bullets are consistent with the Phase 0 registry without requiring a manual re-read
of the registry to verify.

Write exactly 3 bullets. These are your top-3 findings by blast-radius tier, identified by position
in this section. The first bullet is the highest-blast-radius finding; the third is the third.
If fewer than 3 findings exist, write the available count and note the shortfall.

Use this format for each bullet exactly:
- F-[N]: [finding name] | blast-radius: [wide|medium|narrow] | chain: [origin] -> [component] -> [terminal: T-NN] | [CONFIRMED -- evidence: [phase]: [finding] | RUNTIME ANOMALY]

Do not summarize. Do not add prose. Three structured bullets, then stop.

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

## V-04 — C-30 + C-31 Explicit Enforcement (combination)
**Axis:** Combines V-01 (T-NN rejection rule in EXECUTIVE SUMMARY) and V-02 (inline evidence
rejection rule in EXECUTIVE SUMMARY). Both explicit validity gates added to the EXECUTIVE
SUMMARY section. No other changes from R10 V-05.
**Hypothesis:** V-01 and V-02 address orthogonal failure modes in EXECUTIVE SUMMARY output:
free-form terminal names (C-30) and plain CONFIRMED tokens (C-31). The two rejection rules
operate on different fields of the bullet format — the chain field (C-30) and the confirmation
slot (C-31) — so they should compose without structural interference. If both rules add
signal independently, V-04 should pass C-30 and C-31 while holding all R10 V-05 baseline
criteria. V-04 is the direct R11 candidate for the 90/90 ceiling under v9.

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
List all reclassifications and all citations verified or added.

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
   free-form component name (e.g., "DataLayer"). A bullet with a free-form terminus is
   INVALID and must be rewritten using the T-NN code before this section is complete.
   If no T-NN code resolves for a terminus, write "unresolved chain — registry miss: [name]"
   and exclude the finding from this section until the chain is resolved in Q1.
2. The confirmation slot must carry the inline evidence citation format:
   CONFIRMED -- evidence: [source-phase]: [matching-finding-name]
   The plain token [CONFIRMED] is NOT valid in EXECUTIVE SUMMARY bullets. A bullet that
   uses [CONFIRMED] without "-- evidence: [source-phase]: [finding-name]" is structurally
   incomplete and must be revised before this section is complete.

Do not summarize. Do not add prose. Three structured bullets, then stop.

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

## V-05 — Full Integration (C-30 + C-31 enforcement + Q7 EXECUTIVE SUMMARY audit gate + Q2 extension)
**Axis:** All R11 structural axes combined: V-04 explicit rejection rules for C-30 and C-31 in
EXECUTIVE SUMMARY, Q2 extended to explicitly audit EXECUTIVE SUMMARY bullet citations, and a
new Q7 dedicated EXECUTIVE SUMMARY structural audit gate (T-NN codes + inline evidence citations).
**Hypothesis:** V-04 adds the rejection rules at the point of writing, which closes the primary
failure path. V-05 adds two additional enforcement layers: Q2 is extended to audit EXECUTIVE
SUMMARY bullets in the same pass where it audits field 6 citations (C-29 coherence), and Q7
adds a dedicated post-EXECUTIVE SUMMARY gate that explicitly audits both C-30 and C-31
compliance per bullet before CONSOLIDATE begins. Three-layer enforcement — rejection rule at
write time, Q2 extended audit, Q7 dedicated gate — makes C-30 and C-31 as structurally locked
as C-29. If V-04 already achieves 90/90, V-05 adds structural depth beyond the scoring threshold
that may prove valuable in production execution. If V-04 has gaps, V-05 closes them.

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

## VERDICT

One paragraph. Name the finding with the widest blast radius by its Phase 0 census component name.
State the propagation chain from origin to terminal blast surface, including the T-NN terminus code.
State CONFIRMED -- evidence: [source-phase]: [matching-finding-name], or RUNTIME ANOMALY.
If SYSTEMIC, list the corroborating phases.
State the assumption the team would have carried into implementation had this simulation not run.
Conclude: proceed, proceed with conditions, or halt.
```
