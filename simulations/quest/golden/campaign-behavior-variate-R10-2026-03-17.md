# Quest Variations — campaign-behavior (R10)
**Skill:** campaign-behavior
**Rubric:** v8 (C-01–C-29)
**Round:** 10
**Date:** 2026-03-17

---

## Axes explored in R10

Single-axis (unexplored as of R9, targeting new v8 criteria):
- **Chain Terminus Registry (C-27)** — Phase 0 gains a T-NN indexed terminus table. Every
  propagation chain in field 3 must end with a T-NN code. Chains that cannot resolve to a T-NN
  entry are flagged "unresolved chain — registry miss."
- **EXECUTIVE SUMMARY section (C-28)** — A dedicated `## EXECUTIVE SUMMARY` section with exactly
  3 structured bullets (F-NN | blast-radius tier | chain | confirmation) is inserted between the
  CALIBRATION BLOCK and CONSOLIDATE. Top-3 findings are identified by section position (bullet
  order), not by list-order inference from the ranked findings.
- **Inline CONFIRMED evidence citation (C-29)** — Field 6 of every atomic finding block changes
  to embed the evidence citation: `CONFIRMED -- evidence: [phase]: [finding]`. The template also
  propagates into VERDICT and into Q2's audit instruction.

Combinations (V-04, V-05):
- **V-04:** Chain Terminus Registry + EXECUTIVE SUMMARY (C-27 + C-28; C-29 absent)
- **V-05:** Full integration — C-27 + C-28 + C-29 + all R8 axes (DEPTH asymmetry anchor
  headers, Q6 sequence integrity gate, explicit propagation chain in field 3)

---

## V-01 — Chain Terminus Registry
**Axis:** Phase 0 terminus table — each unique propagation chain endpoint is assigned a T-NN
code. Field 3 of every atomic finding block must cite its terminal as `[terminal: T-NN]`.
Chains that cannot name a census terminus are flagged "unresolved chain — registry miss."
**Hypothesis:** R8 V-05 introduced explicit propagation chains in field 3 but left terminus
validation as prose. C-27 converts terminus validation into a table lookup: if the chain's
terminal is not in the T-NN table, the finding is incomplete. This should force completeness
at Phase 0 and make Q1 chain-to-terminus tracing mechanically auditable. All other structure
is R8 V-05 unchanged. If C-27 adds signal without disrupting existing structure, V-01 should
hold the R8 V-05 score on v6 criteria while passing C-27 on v8.

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
The terminal must resolve to an entry in the Phase 0 terminus registry (T-NN code).
Chains that cannot be named using census components and a valid T-NN terminus must be flagged:
"unresolved chain — registry miss."

T-NN = terminus registry code. Assigned in Phase 0 to every unique propagation chain endpoint
(shared state surface, downstream caller boundary, or role-boundary that terminates blast).
Referenced in field 3 of every finding.

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

Q1: Does any finding's blast radius change when the propagation chain is traced to its T-NN terminus?
For each finding: trace the full propagation chain ([origin] → ... → [terminal: T-NN]). Does the
chain reach a Phase 0 shared state surface (T-NN flagged as shared-state)? If yes, upgrade to wide.
List every revision and show the full T-NN-terminated chain for each reclassified finding.
Flag any finding whose chain cannot resolve to a T-NN entry as "unresolved chain — registry miss."

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
State the propagation chain from origin to terminal blast surface, including the T-NN terminus code.
State CONFIRMED or RUNTIME ANOMALY. If SYSTEMIC, list the corroborating phases.
State the assumption the team would have carried into implementation had this simulation not run.
Conclude: proceed, proceed with conditions, or halt.
```

---

## V-02 — EXECUTIVE SUMMARY section
**Axis:** A dedicated `## EXECUTIVE SUMMARY` section with exactly 3 structured bullets is inserted
between the CALIBRATION BLOCK and CONSOLIDATE. Each bullet names the finding (F-NN), its blast-radius
tier, its propagation chain, and its classification. Top-3 are identified by bullet order in this
section — not by inference from the ranked list below.
**Hypothesis:** C-28 requires the EXECUTIVE SUMMARY to precede the ranked findings so that top-3
identification is positional (the first 3 bullets = the top-3), not a list-order inference. Without
a dedicated section, scorers must infer the top-3 from the ranked findings list — ambiguous when
ties exist. A separate EXECUTIVE SUMMARY section resolves the ambiguity structurally. All other
structure is R8 V-05 unchanged. If C-28 adds signal independently, V-02 should score identically
to R8 V-05 on v6/v7 criteria while passing C-28.

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

## EXECUTIVE SUMMARY

Write exactly 3 bullets. These are your top-3 findings by blast-radius tier, identified by position
in this section. The first bullet is the highest-blast-radius finding; the third is the third.
If fewer than 3 findings exist, write the available count and note the shortfall.

Use this format for each bullet exactly:
- F-[N]: [finding name] | blast-radius: [wide|medium|narrow] | chain: [origin] -> [component] -> [terminal] | [CONFIRMED | RUNTIME ANOMALY]

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

## V-03 — Inline CONFIRMED evidence citation
**Axis:** Field 6 of every atomic finding block is restructured to embed the evidence citation
inline: `CONFIRMED -- evidence: [source-phase]: [matching-finding-name]`. The VERDICT template
is updated to require the same inline format. Q2 in the CALIBRATION BLOCK is updated to audit
for the citation's presence and reject any CONFIRMED classification that omits it.
**Hypothesis:** Prior rounds classified findings as CONFIRMED but left the evidence as implicit
("matches Phase 1 violation") or required inference from adjacent text. C-29 requires the
citation to be embedded in the field itself, making CONFIRMED auditable at four checkpoints:
field 6 template, VERDICT, EXECUTIVE SUMMARY bullets (if present), and Q2. All other structure
is R8 V-05 unchanged. If the inline citation format adds auditable signal, V-03 should score
identically on v6/v7 criteria while passing C-29.

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
CONFIRMED = matches a Phase 1–3 violation. Use format: CONFIRMED -- evidence: [phase]: [finding].
RUNTIME ANOMALY = no matching topology violation.

If clean: "flow-lifecycle: clean — all lifecycle transitions verified."

EXIT CRITERIA: All lifecycle phases evaluated.
State: "flow-lifecycle complete: [N] phases, [N] failures, [N] CONFIRMED, [N] RUNTIME ANOMALY."

---

## PHASE 5 — flow-trigger

| Trigger | Expected fire order | Actual fire order | Race condition? | Phase 2 escalation role? | Phase tag | CONFIRMED / RUNTIME ANOMALY |
|---------|---------------------|-------------------|-----------------|--------------------------|-----------|------------------------------|

Phase 2 escalation role = yes if trigger involves a Phase 2 escalation role: blast radius = wide.
CONFIRMED = matches a Phase 1–3 violation. Use format: CONFIRMED -- evidence: [phase]: [finding].

If clean: "flow-trigger: clean — all triggers verified."

EXIT CRITERIA: All triggers and activating events evaluated.
State: "flow-trigger complete: [N] triggers, [N] failures, [N] CONFIRMED, [N] RUNTIME ANOMALY."

---

## CALIBRATION BLOCK

Q1: Does any finding's blast radius change when the propagation chain is traced to terminus?
For each finding: trace the full propagation chain ([origin] → ... → [terminal]). Does the
chain reach a Phase 0 shared state surface? If yes, upgrade to wide. List every revision.

Q2: Do any Phase 4–5 findings match topology violations from Phases 1–3?
For each Phase 4–5 finding classified as CONFIRMED: verify the inline citation is present in
field 6 using format "CONFIRMED -- evidence: [source-phase]: [matching-finding-name]."
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
State the propagation chain from origin to terminal blast surface.
State CONFIRMED -- evidence: [source-phase]: [matching-finding-name], or RUNTIME ANOMALY.
If SYSTEMIC, list the corroborating phases.
State the assumption the team would have carried into implementation had this simulation not run.
Conclude: proceed, proceed with conditions, or halt.
```

---

## V-04 — Chain Terminus Registry + EXECUTIVE SUMMARY (C-27 + C-28)
**Axis:** Combines V-01 (T-NN terminus registry in Phase 0, T-NN codes in field 3) with V-02
(dedicated `## EXECUTIVE SUMMARY` section with 3 structured bullets before CONSOLIDATE).
C-29 inline evidence citation is deliberately absent — testing whether C-27 and C-28 compose
cleanly without interference before adding the third new axis.
**Hypothesis:** V-01 and V-02 target orthogonal checkpoints — Phase 0 completeness and
pre-ranking summary position respectively. They should compose without conflict. The T-NN
terminus codes in field 3 also give the EXECUTIVE SUMMARY bullets a more precise chain
notation (`[origin] -> [component] -> [terminal: T-NN]`). If both pass independently, the
combination should score 90/90 on v6/v7 criteria while passing both C-27 and C-28 on v8.

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

T-NN = terminus registry code. Assigned in Phase 0 to every unique propagation chain endpoint.
Referenced in field 3 of every finding and in EXECUTIVE SUMMARY bullets.

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

**Terminus registry:**

| T-NN | Terminus component | Type |
|------|--------------------|------|
| T-01 | [component name]   | [shared-state \| downstream-caller \| role-boundary] |
| ...  | ...                | ... |

Assign a T-NN code to every unique blast-surface endpoint. Propagation chains must terminate
at a T-NN entry. Chains that cannot resolve = "unresolved chain — registry miss."

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

Q1: Does any finding's blast radius change when the propagation chain is traced to its T-NN terminus?
For each finding: trace the full chain ([origin] → ... → [terminal: T-NN]). Does the chain reach
a shared-state T-NN entry? If yes, upgrade to wide. List every revision and the full chain.
Flag any finding whose chain cannot resolve to a T-NN entry: "unresolved chain — registry miss."

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

## EXECUTIVE SUMMARY

Write exactly 3 bullets. These are your top-3 findings by blast-radius tier, identified by position
in this section. The first bullet is the highest-blast-radius finding; the third is the third.
If fewer than 3 findings exist, write the available count and note the shortfall.

Use this format for each bullet exactly:
- F-[N]: [finding name] | blast-radius: [wide|medium|narrow] | chain: [origin] -> [component] -> [terminal: T-NN] | [CONFIRMED | RUNTIME ANOMALY]

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
State the propagation chain from origin to terminal blast surface, including the T-NN terminus code.
State CONFIRMED or RUNTIME ANOMALY. If SYSTEMIC, list the corroborating phases.
State the assumption the team would have carried into implementation had this simulation not run.
Conclude: proceed, proceed with conditions, or halt.
```

---

## V-05 — Full integration (C-27 + C-28 + C-29 + DEPTH asymmetry + Q6 + propagation chain)
**Axis:** All three v8 new criteria combined with all three R8 excellence axes. C-27: terminus
registry with T-NN codes. C-28: dedicated EXECUTIVE SUMMARY section with 3 structured bullets
before CONSOLIDATE. C-29: inline CONFIRMED evidence citation in field 6, VERDICT, EXECUTIVE
SUMMARY bullets, and Q2. R8 axes retained: DEPTH asymmetry anchor headers on Ph1/Ph2, Q6
sequence integrity gate, explicit propagation chain in field 3.
**Hypothesis:** V-01, V-02, V-03 test each v8 axis in isolation against the R8 V-05 base.
V-05 tests whether all three v8 criteria compose with each other and with the three R8 axes
without structural interference. The T-NN terminus codes in field 3, the EXECUTIVE SUMMARY
bullets citing T-NN chains, and the inline CONFIRMED citations in field 6 and VERDICT should
all reinforce each other: the EXECUTIVE SUMMARY bullet for a CONFIRMED finding cites both
the T-NN terminus and the evidence phase, creating a fully traceable top-3 summary. If all
six axes compose cleanly, V-05 is the R10 golden candidate.

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
